
import math
import pandas as pd


class SovereignRules:
    """
    Basel Framework - Sovereign Exposure Rules

    적용 범위:
    - Sovereign (정부 익스포져)
    - Central Bank (중앙은행 익스포져)

    1차 구현 범위:
    - 장기 외부등급 기준 Risk Weight
    - EAD 재계산
    - RWA 재계산

    주의:
    - 기본 Basel 위험가중치 기준
    - 국내 통화 우대 및 ECA 기준은 미포함
    - 외부등급은 S&P 방식의 표준 등급 코드 사용
    """

    # Basel CRE20.7
    # Risk Weight는 20%가 아니라 0.20 형태로 저장
    RATING_RISK_WEIGHT_TABLE = {
        # AAA ~ AA-
        "AAA": 0.00,
        "AA+": 0.00,
        "AA": 0.00,
        "AA-": 0.00,

        # A+ ~ A-
        "A+": 0.20,
        "A": 0.20,
        "A-": 0.20,

        # BBB+ ~ BBB-
        "BBB+": 0.50,
        "BBB": 0.50,
        "BBB-": 0.50,

        # BB+ ~ B-
        "BB+": 1.00,
        "BB": 1.00,
        "BB-": 1.00,
        "B+": 1.00,
        "B": 1.00,
        "B-": 1.00,

        # Below B-
        "CCC+": 1.50,
        "CCC": 1.50,
        "CCC-": 1.50,
        "CC": 1.50,
        "C": 1.50,
        "D": 1.50,
        "SD": 1.50,
        "RD": 1.50,

        # Unrated
        "UNRATED": 1.00,
    }

    # 등급이 없는 경우 Unrated로 처리할 입력값
    UNRATED_LABELS = {
        "",
        "UNRATED",
        "NR",
        "N/R",
        "NOTRATED",
        "N/A",
        "NA",
        "NONE",
        "NAN",
        "-",
    }

    @classmethod
    def normalize_rating(cls, rating):
        """
        외부등급 문자열 정규화.

        None, NaN, 공백 등은 UNRATED로 처리한다.
        """

        if rating is None or pd.isna(rating):
            return "UNRATED"

        normalized = "".join(str(rating).upper().split())

        if normalized in cls.UNRATED_LABELS:
            return "UNRATED"

        return normalized

    @classmethod
    def get_risk_weight(cls, row):
        """
        장기 외부등급에 해당하는 Risk Weight 반환.

        지원하지 않는 등급 코드는 Unrated로 간주하지 않고
        오류를 발생시켜 검증 결과에서 확인할 수 있게 한다.
        """

        try:
            raw_rating = row["장기 외부등급"]
        except (KeyError, TypeError) as exc:
            raise ValueError(
                "필수 컬럼 '장기 외부등급'이 없습니다."
            ) from exc

        rating = cls.normalize_rating(raw_rating)

        if rating not in cls.RATING_RISK_WEIGHT_TABLE:
            raise ValueError(
                f"지원하지 않는 장기 외부등급: {rating}"
            )

        return cls.RATING_RISK_WEIGHT_TABLE[rating]

    @staticmethod
    def _to_finite_float(value, column_name):
        """숫자 입력값 검증."""

        try:
            number = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(
                f"'{column_name}' 숫자값을 확인하세요."
            ) from exc

        if not math.isfinite(number):
            raise ValueError(
                f"'{column_name}' 값이 비어 있거나 유효하지 않습니다."
            )

        return number

    @classmethod
    def calculate_ead(cls, row):
        """
        EAD = 잔액 + (미사용한도 * CCF)

        기존 BankRules와 동일한 산식 및 컬럼을 사용한다.
        CCF는 20%라면 0.20 형태로 입력한다.
        """

        try:
            balance = cls._to_finite_float(
                row["잔액"], "잔액"
            )
            undrawn = cls._to_finite_float(
                row["미사용한도"], "미사용한도"
            )
            ccf = cls._to_finite_float(
                row["CCF"], "CCF"
            )
        except KeyError as exc:
            raise ValueError(
                f"필수 컬럼이 없습니다: {exc.args[0]}"
            ) from exc

        return balance + (undrawn * ccf)

    @staticmethod
    def calculate_rwa(ead, risk_weight):
        """RWA = EAD * Risk Weight"""

        return ead * risk_weight
