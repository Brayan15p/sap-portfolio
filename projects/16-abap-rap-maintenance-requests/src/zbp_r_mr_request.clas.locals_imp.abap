CLASS lhc_request DEFINITION INHERITING FROM cl_abap_behavior_handler.
  PRIVATE SECTION.
    CONSTANTS:
      BEGIN OF status,
        new       TYPE c LENGTH 1 VALUE 'N',
        submitted TYPE c LENGTH 1 VALUE 'S',
        approved  TYPE c LENGTH 1 VALUE 'A',
        rejected  TYPE c LENGTH 1 VALUE 'R',
      END OF status.

    METHODS get_instance_features FOR INSTANCE FEATURES
      IMPORTING keys REQUEST requested_features FOR Request RESULT result.
    METHODS get_instance_authorizations FOR INSTANCE AUTHORIZATION
      IMPORTING keys REQUEST requested_authorizations FOR Request RESULT result.
    METHODS setInitialValues FOR DETERMINE ON MODIFY
      IMPORTING keys FOR Request~setInitialValues.
    METHODS validatePriority FOR VALIDATE ON SAVE
      IMPORTING keys FOR Request~validatePriority.
    METHODS validateCost FOR VALIDATE ON SAVE
      IMPORTING keys FOR Request~validateCost.
    METHODS submit FOR MODIFY
      IMPORTING keys FOR ACTION Request~submit RESULT result.
    METHODS approve FOR MODIFY
      IMPORTING keys FOR ACTION Request~approve RESULT result.
    METHODS reject FOR MODIFY
      IMPORTING keys FOR ACTION Request~reject RESULT result.
    METHODS decide
      IMPORTING keys       TYPE ANY TABLE
                new_status TYPE c.
ENDCLASS.

CLASS lhc_request IMPLEMENTATION.

  " Only a submitted request can be approved or rejected; this is what blocks a second approval.
  METHOD get_instance_features.
    READ ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request FIELDS ( Status ) WITH CORRESPONDING #( keys )
      RESULT DATA(requests).
    result = VALUE #( FOR r IN requests (
      %tky           = r-%tky
      %action-submit  = COND #( WHEN r-Status = status-new       THEN if_abap_behv=>fc-o-enabled ELSE if_abap_behv=>fc-o-disabled )
      %action-approve = COND #( WHEN r-Status = status-submitted THEN if_abap_behv=>fc-o-enabled ELSE if_abap_behv=>fc-o-disabled )
      %action-reject  = COND #( WHEN r-Status = status-submitted THEN if_abap_behv=>fc-o-enabled ELSE if_abap_behv=>fc-o-disabled ) ) ).
  ENDMETHOD.

  " Segregation of duties: the creator cannot approve their own request.
  METHOD get_instance_authorizations.
    READ ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request FIELDS ( CreatedBy ) WITH CORRESPONDING #( keys )
      RESULT DATA(requests).
    LOOP AT requests INTO DATA(r).
      DATA(own) = xsdbool( r-CreatedBy = cl_abap_context_info=>get_user_technical_name( ) ).
      APPEND VALUE #( %tky = r-%tky
        %action-approve = COND #( WHEN own = abap_true THEN if_abap_behv=>auth-unauthorized ELSE if_abap_behv=>auth-allowed )
        %action-reject  = COND #( WHEN own = abap_true THEN if_abap_behv=>auth-unauthorized ELSE if_abap_behv=>auth-allowed ) ) TO result.
    ENDLOOP.
  ENDMETHOD.

  METHOD setInitialValues.
    READ ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request FIELDS ( Status RequestId ) WITH CORRESPONDING #( keys )
      RESULT DATA(requests).
    DELETE requests WHERE Status IS NOT INITIAL.
    CHECK requests IS NOT INITIAL.
    SELECT MAX( request_id ) FROM zmr_request INTO @DATA(max_id).
    MODIFY ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request UPDATE FIELDS ( Status RequestId )
      WITH VALUE #( FOR r IN requests INDEX INTO i (
        %tky = r-%tky  Status = status-new  RequestId = max_id + i ) ).
  ENDMETHOD.

  METHOD validatePriority.
    READ ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request FIELDS ( Priority ) WITH CORRESPONDING #( keys )
      RESULT DATA(requests).
    LOOP AT requests INTO DATA(r) WHERE Priority NA '123'.
      APPEND VALUE #( %tky = r-%tky ) TO failed-request.
      APPEND VALUE #( %tky = r-%tky
        %msg = new_message_with_text( severity = if_abap_behv_message=>severity-error
                                      text     = |Priority must be 1, 2 or 3| )
        %element-Priority = if_abap_behv=>mk-on ) TO reported-request.
    ENDLOOP.
  ENDMETHOD.

  METHOD validateCost.
    READ ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request FIELDS ( EstimatedCost Currency ) WITH CORRESPONDING #( keys )
      RESULT DATA(requests).
    LOOP AT requests INTO DATA(r) WHERE EstimatedCost < 0 OR ( EstimatedCost > 0 AND Currency IS INITIAL ).
      APPEND VALUE #( %tky = r-%tky ) TO failed-request.
      APPEND VALUE #( %tky = r-%tky
        %msg = new_message_with_text( severity = if_abap_behv_message=>severity-error
                                      text     = |Cost must be >= 0 and needs a currency| )
        %element-EstimatedCost = if_abap_behv=>mk-on ) TO reported-request.
    ENDLOOP.
  ENDMETHOD.

  METHOD submit.
    MODIFY ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request UPDATE FIELDS ( Status )
      WITH VALUE #( FOR k IN keys ( %tky = k-%tky  Status = status-submitted ) ).
    READ ENTITIES OF zr_mr_request IN LOCAL MODE ENTITY Request
      ALL FIELDS WITH CORRESPONDING #( keys ) RESULT DATA(r).
    result = VALUE #( FOR x IN r ( %tky = x-%tky %param = x ) ).
  ENDMETHOD.

  METHOD approve.
    decide( keys = keys new_status = status-approved ).
    READ ENTITIES OF zr_mr_request IN LOCAL MODE ENTITY Request
      ALL FIELDS WITH CORRESPONDING #( keys ) RESULT DATA(r).
    result = VALUE #( FOR x IN r ( %tky = x-%tky %param = x ) ).
  ENDMETHOD.

  METHOD reject.
    decide( keys = keys new_status = status-rejected ).
    READ ENTITIES OF zr_mr_request IN LOCAL MODE ENTITY Request
      ALL FIELDS WITH CORRESPONDING #( keys ) RESULT DATA(r).
    result = VALUE #( FOR x IN r ( %tky = x-%tky %param = x ) ).
  ENDMETHOD.

  " Records who decided and when, so the decision is auditable.
  METHOD decide.
    DATA upd TYPE TABLE FOR UPDATE zr_mr_request.
    GET TIME STAMP FIELD DATA(now).
    LOOP AT keys ASSIGNING FIELD-SYMBOL(<k>).
      ASSIGN COMPONENT '%TKY' OF STRUCTURE <k> TO FIELD-SYMBOL(<tky>).
      APPEND INITIAL LINE TO upd ASSIGNING FIELD-SYMBOL(<u>).
      <u>-%tky      = <tky>.
      <u>-Status    = new_status.
      <u>-DecidedBy = cl_abap_context_info=>get_user_technical_name( ).
      <u>-DecidedAt = now.
    ENDLOOP.
    MODIFY ENTITIES OF zr_mr_request IN LOCAL MODE
      ENTITY Request UPDATE FIELDS ( Status DecidedBy DecidedAt ) WITH upd.
  ENDMETHOD.

ENDCLASS.
