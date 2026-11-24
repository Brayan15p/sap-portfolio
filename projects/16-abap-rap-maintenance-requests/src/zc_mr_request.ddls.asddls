@AccessControl.authorizationCheck: #NOT_REQUIRED
@EndUserText.label: 'Maintenance request - projection'
@Metadata.allowExtensions: true
define root view entity ZC_MR_REQUEST
  provider contract transactional_query
  as projection on ZR_MR_REQUEST
{
  key RequestUuid,
      RequestId, EquipmentId, Plant, Description, Priority,
      EstimatedCost, Currency, Status, DecidedBy, DecidedAt,
      CreatedBy, CreatedAt, LocalLastChangedAt, LastChangedAt
}
