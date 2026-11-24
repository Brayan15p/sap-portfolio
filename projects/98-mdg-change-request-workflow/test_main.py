import pytest
from main import ChangeRequest
def test_critical_change_needs_two_distinct_approvers():
    cr = ChangeRequest("CR1", "ana", {"bank_account": "123"}); cr.submit(); cr.validate("steward")
    with pytest.raises(PermissionError): cr.approve("ana")
    cr.approve("luis"); assert cr.state == "APPROVAL"
    with pytest.raises(PermissionError): cr.approve("luis")
    cr.approve("eva"); assert cr.state == "ACTIVATED" and len(cr.log) == 5
def test_validation_errors_reject():
    cr = ChangeRequest("CR2", "ana", {"name": "X"}); cr.submit(); cr.validate("steward", ["name too short"])
    assert cr.state == "REJECTED"
