class BankRules:
    """
    Basel III Standardised Approach
    Bank Exposure Rule
    """

    # 장기 외부등급별 Risk Weight
    RISK_WEIGHT_TABLE = {

        "AAA": 0.20,
        "AA+": 0.20,
        "AA": 0.20,
        "AA-": 0.20,

        "A+": 0.30,
        "A": 0.30,
        "A-": 0.30,

        "BBB+": 0.50,
        "BBB": 0.50,
        "BBB-": 0.50,

        "BB+": 1.00,
        "BB": 1.00,
        "BB-": 1.00,

        "B+": 1.00,
        "B": 1.00,
        "B-": 1.00,

        "CCC": 1.50,
        "CC": 1.50,
        "C": 1.50,
        "D": 1.50,

        "UNRATED": 1.50
    }

    @classmethod
    def get_risk_weight(cls, row):

        rating = row["장기 외부등급"]

        if rating is None:
            rating = "UNRATED"

        rating = str(rating).strip().upper()

        return cls.RISK_WEIGHT_TABLE.get(
            rating,
            cls.RISK_WEIGHT_TABLE["UNRATED"]
        )

    @staticmethod
    def calculate_ead(row):

        balance = float(row["잔액"])
        undrawn = float(row["미사용한도"])
        ccf = float(row["CCF"])

        return balance + (undrawn * ccf)

    @staticmethod
    def calculate_rwa(ead, risk_weight):

        return ead * risk_weight