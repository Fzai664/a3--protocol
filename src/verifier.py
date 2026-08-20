"""
A3 Protocol - SLA Verification Layer

Deterministically checks whether an autonomous financial
agent violated its predefined SLA.
"""

class Verifier:

    def __init__(self, sla):
        self.sla = sla
        self.status = "ready"

    def validate(self, action):
        violations = []

        # 1. Check maximum transaction amount
        if action["amount"] > self.sla["max_trade_amount"]:
            violations.append({
                "rule": "MAX_TRADE_AMOUNT",
                "expected": self.sla["max_trade_amount"],
                "actual": action["amount"]
            })

        # 2. Check allowed protocols
        if action["protocol"] not in self.sla["allowed_protocols"]:
            violations.append({
                "rule": "UNAUTHORIZED_PROTOCOL",
                "expected": self.sla["allowed_protocols"],
                "actual": action["protocol"]
            })

        # 3. Check maximum slippage
        if action["slippage"] > self.sla["max_slippage"]:
            violations.append({
                "rule": "MAX_SLIPPAGE",
                "expected": self.sla["max_slippage"],
                "actual": action["slippage"]
            })

        # 4. Check leverage
        if action["leverage"] > self.sla["max_leverage"]:
            violations.append({
                "rule": "MAX_LEVERAGE",
                "expected": self.sla["max_leverage"],
                "actual": action["leverage"]
            })

        result = {
            "agent": action["agent"],
            "action": action,
            "valid": len(violations) == 0,
            "violations": violations
        }

        self.status = "verified"

        return result

    def check_integrity(self, record):
        """
        Verify that an accountability record contains
        the information required for later auditing.
        """

        required_fields = [
            "agent",
            "action",
            "valid",
            "violations"
        ]

        missing = [
            field for field in required_fields
            if field not in record
        ]

        return {
            "integrity": len(missing) == 0,
            "missing_fields": missing
        }