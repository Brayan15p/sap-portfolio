CRITICAL = {"bank_account", "tax_id"}
class ChangeRequest:
    def __init__(self, cr_id, requester, changes):
        self.id, self.requester, self.changes = cr_id, requester, changes
        self.state, self.approvals, self.log = "DRAFT", [], [("create", requester)]
    def submit(self):
        if self.state != "DRAFT": raise ValueError("Only drafts can be submitted")
        self.state = "VALIDATION"; self.log.append(("submit", self.requester))
    def validate(self, steward, errors=()):
        if self.state != "VALIDATION": raise ValueError("Not in validation")
        self.state = "REJECTED" if errors else "APPROVAL"; self.log.append(("validate", steward, list(errors)))
    def approve(self, user):
        if self.state != "APPROVAL": raise ValueError("Not in approval")
        if user == self.requester or user in self.approvals: raise PermissionError("Four-eyes: approver must be a different person")
        self.approvals.append(user); self.log.append(("approve", user))
        needed = 2 if CRITICAL & set(self.changes) else 1
        if len(self.approvals) >= needed: self.state = "ACTIVATED"
