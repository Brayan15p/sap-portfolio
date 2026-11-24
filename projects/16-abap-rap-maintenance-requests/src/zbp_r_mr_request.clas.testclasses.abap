" ABAP Unit with EML: business rules of the approval flow.
CLASS ltc_request DEFINITION FINAL FOR TESTING DURATION SHORT RISK LEVEL HARMLESS.
  PRIVATE SECTION.
    CLASS-DATA env TYPE REF TO if_cds_test_environment.
    CLASS-METHODS class_setup.
    CLASS-METHODS class_teardown.
    METHODS setup.
    METHODS create_submitted RETURNING VALUE(tky) TYPE sysuuid_x16.
    METHODS invalid_priority_rejected FOR TESTING.
    METHODS approve_only_once        FOR TESTING.
ENDCLASS.

CLASS ltc_request IMPLEMENTATION.
  METHOD class_setup.
    env = cl_cds_test_environment=>create( i_for_entity = 'ZR_MR_REQUEST' ).
  ENDMETHOD.
  METHOD class_teardown.
    env->destroy( ).
  ENDMETHOD.
  METHOD setup.
    env->clear_doubles( ).
    ROLLBACK ENTITIES.
  ENDMETHOD.

  METHOD create_submitted.
    MODIFY ENTITIES OF zr_mr_request
      ENTITY Request CREATE FIELDS ( EquipmentId Plant Description Priority )
      WITH VALUE #( ( %cid = 'c1' EquipmentId = 'CHILLER-01' Plant = 'BOG1'
                      Description = 'Compressor noise' Priority = '1' ) )
      MAPPED DATA(mapped).
    tky = mapped-request[ 1 ]-RequestUuid.
    MODIFY ENTITIES OF zr_mr_request ENTITY Request
      EXECUTE submit FROM VALUE #( ( RequestUuid = tky ) ).
  ENDMETHOD.

  METHOD invalid_priority_rejected.
    MODIFY ENTITIES OF zr_mr_request
      ENTITY Request CREATE FIELDS ( EquipmentId Plant Description Priority )
      WITH VALUE #( ( %cid = 'c1' EquipmentId = 'X' Plant = 'BOG1' Description = 'Y' Priority = '9' ) ).
    COMMIT ENTITIES RESPONSE OF zr_mr_request FAILED DATA(failed).
    cl_abap_unit_assert=>assert_not_initial( act = failed-request msg = 'Priority 9 must fail' ).
  ENDMETHOD.

  METHOD approve_only_once.
    DATA(id) = create_submitted( ).
    MODIFY ENTITIES OF zr_mr_request ENTITY Request
      EXECUTE approve FROM VALUE #( ( RequestUuid = id ) ).
    GET ENTITIES OF zr_mr_request ENTITY Request FEATURES
      FROM VALUE #( ( RequestUuid = id ) ) REQUEST VALUE #( %action-approve = if_abap_behv=>mk-on )
      RESULT DATA(features).
    cl_abap_unit_assert=>assert_equals(
      act = features[ 1 ]-%action-approve exp = if_abap_behv=>fc-o-disabled
      msg = 'An approved request cannot be approved again' ).
  ENDMETHOD.
ENDCLASS.
