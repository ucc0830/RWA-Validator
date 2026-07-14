import pandas as pd

from validators.bank_validator import BankValidator


class ValidatorEngine:
    """
    검증 엔진

    입력 DataFrame을 받아 각 행을 검증한 후
    결과 DataFrame을 반환한다.
    """

    def __init__(self):
        self.validator = BankValidator()

    def validate(self, df: pd.DataFrame) -> pd.DataFrame:

        results = []

        # 계좌 단위 검증
        for _, row in df.iterrows():

            result = self.validator.validate(row)

            results.append(result)

        # 결과 DataFrame 생성
        result_df = pd.DataFrame(results)

        return result_df