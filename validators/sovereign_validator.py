
import math
import pandas as pd

from rules.sovereign_rules import SovereignRules


class SovereignValidator:
    """
    Sovereign Exposure Validator

    수행 업무:
    1. 외부등급 기반 Risk Weight 재산출
    2. EAD 재산출
    3. RWA 재산출
    4. 원장 값과 비교
    5. 검증결과 및 오류원인 반환
    """

    RISK_WEIGHT_TOLERANCE = 0.0001
    AMOUNT_TOLERANCE = 10.0

    @staticmethod
    def _matches(reported_value, calculated_value, tolerance):
        """원장 값과 계산값의 차이를 비교한다."""

        if calculated_value is None:
            return False

        try:
            reported = float(reported_value)
        except (TypeError, ValueError):
            return False

        if not math.isfinite(reported):
            return False

        return abs(reported - calculated_value) < tolerance

    def validate(self, row: pd.Series):
        """단일 Sovereign Exposure 행 검증."""

        reasons = []

        # 1. Risk Weight 재산출
        try:
            calculated_rw = SovereignRules.get_risk_weight(row)
        except ValueError as exc:
            calculated_rw = None
            reasons.append(str(exc))

        # 2. EAD 재산출
        try:
            calculated_ead = SovereignRules.calculate_ead(row)
        except ValueError as exc:
            calculated_ead = None
            reasons.append(f"EAD 산출 불가: {exc}")

        # 3. RWA 재산출
        calculated_rwa = None

        if calculated_rw is not None and calculated_ead is not None:
            calculated_rwa = SovereignRules.calculate_rwa(
                calculated_ead,
                calculated_rw,
            )

        # 4. 원장 Risk Weight 비교
        if calculated_rw is not None:
            rw_match = self._matches(
                row.get("Risk Weight"),
                calculated_rw,
                self.RISK_WEIGHT_TOLERANCE,
            )

            if not rw_match:
                reasons.append("Risk Weight 불일치")

        # 5. 원장 EAD 비교
        if calculated_ead is not None:
            ead_match = self._matches(
                row.get("EAD"),
                calculated_ead,
                self.AMOUNT_TOLERANCE,
            )

            if not ead_match:
                reasons.append("EAD 계산 오류")

        # 6. 원장 RWA 비교
        if calculated_rwa is not None:
            rwa_match = self._matches(
                row.get("RWA"),
                calculated_rwa,
                self.AMOUNT_TOLERANCE,
            )

            if not rwa_match:
                reasons.append("RWA 계산 오류")

        # 7. 검증 결과 반환
        result = {
            "계좌번호": row.get("계좌번호", ""),
            "검증결과": "PASS" if not reasons else "FAIL",

            "원장 Risk Weight": row.get("Risk Weight"),
            "계산 Risk Weight": calculated_rw,

            "원장 EAD": row.get("EAD"),
            "계산 EAD": calculated_ead,

            "원장 RWA": row.get("RWA"),
            "계산 RWA": calculated_rwa,

            "오류원인": ", ".join(reasons),
        }

        return result
