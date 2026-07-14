import pandas as pd

from rules.bank_rules import BankRules

class BankValidator:

    def validate(self, row: pd.Series):

        calculated_rw = BankRules.get_risk_weight(row)

        calculated_ead = BankRules.calculate_ead(row)

        calculated_rwa = BankRules.calculate_rwa(
            calculated_ead,
            calculated_rw
        )

        rw_match = abs(
            float(row["Risk Weight"]) - calculated_rw
        ) < 0.0001

        ead_match = abs(
            float(row["EAD"]) - calculated_ead
        ) < 10

        rwa_match = abs(
            float(row["RWA"]) - calculated_rwa
        ) < 10

        reasons = []

        if not rw_match:
            reasons.append("Risk Weight 불일치")

        if not ead_match:
            reasons.append("EAD 계산 오류")

        if not rwa_match:
            reasons.append("RWA 계산 오류")

        result = {
            "계좌번호": row["계좌번호"],
            "검증결과": "PASS" if len(reasons) == 0 else "FAIL",

            "원장 Risk Weight": row["Risk Weight"],
            "계산 Risk Weight": calculated_rw,

            "원장 EAD": row["EAD"],
            "계산 EAD": calculated_ead,

            "원장 RWA": row["RWA"],
            "계산 RWA": calculated_rwa,

            "오류원인": ", ".join(reasons)
        }

        return result