@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Maintenance request - root'
define root view entity ZR_MR_REQUEST
  as select from zmr_request
{
  key request_uuid          as RequestUuid,
      request_id            as RequestId,
      equipment_id          as EquipmentId,
      plant                 as Plant,
      description           as Description,
      priority              as Priority,
      @Semantics.amount.currencyCode: 'Currency'
      estimated_cost        as EstimatedCost,
      currency              as Currency,
      status                as Status,
      decided_by            as DecidedBy,
      decided_at            as DecidedAt,
      @Semantics.user.createdBy: true
      created_by            as CreatedBy,
      @Semantics.systemDateTime.createdAt: true
      created_at            as CreatedAt,
      @Semantics.systemDateTime.localInstanceLastChangedAt: true
      local_last_changed_at as LocalLastChangedAt,
      @Semantics.systemDateTime.lastChangedAt: true
      last_changed_at       as LastChangedAt
}
