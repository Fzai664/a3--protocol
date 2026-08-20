"""
A3 Protocol - Accountability Engine

Turns verified SLA violations into:
1. Collateral slashing
2. User compensation
3. Accountability records
"""


class AccountabilityEngine:

    def __init__(self, collateral, compensation_rate=1.0):
        self.collateral = collateral
        self.compensation_rate = compensation_rate
        self.records = []

    def enforce(self, verification_result):

        # No violation
        if verification_result["valid"]:
            record = {
                "agent": verification_result["agent"],
                "status": "COMPLIANT",
                "slashed": 0,
                "compensation": 0,
                "remaining_collateral": self.collateral
            }

            self.records.append(record)

            return record

        # Calculate penalty
        violation_count = len(
            verification_result["violations"]
        )

        penalty = min(
            self.collateral,
            self.collateral * 0.10 * violation_count
        )

        compensation = penalty * self.compensation_rate

        self.collateral -= penalty

        record = {
            "agent": verification_result["agent"],
            "status": "SLA_BREACHED",
            "violations": verification_result["violations"],
            "slashed": penalty,
            "compensation": compensation,
            "remaining_collateral": self.collateral
        }

        self.records.append(record)

        return record