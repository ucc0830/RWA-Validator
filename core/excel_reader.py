from pathlib import Path

import pandas as pd

from config.required_columns import REQUIRED_COLUMNS


class ExcelReader:
    """
    Excel 파일을 읽고 필수 컬럼을 검증한다.
    """

    def read(self, file_path: str) -> pd.DataFrame:
        """
        Excel 파일을 읽어 DataFrame으로 반환한다.

        Parameters
        ----------
        file_path : str
            Excel 파일 경로

        Returns
        -------
        pd.DataFrame
            읽은 데이터
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"파일이 존재하지 않습니다.\n{file_path}"
            )

        try:
            df = pd.read_excel(path)
            df.columns = df.columns.str.strip()

        except Exception as e:
            raise Exception(
                f"Excel 파일을 읽는 중 오류가 발생했습니다.\n{e}"
            )

        self._validate_required_columns(df)

        return df

    def _validate_required_columns(self, df: pd.DataFrame):
        """
        필수 컬럼 존재 여부를 확인한다.
        """

        missing_columns = [
            column
            for column in REQUIRED_COLUMNS
            if column not in df.columns
        ]

        if missing_columns:

            missing = "\n".join(missing_columns)

            raise ValueError(
                "필수 컬럼이 누락되었습니다.\n\n"
                f"{missing}"
            )