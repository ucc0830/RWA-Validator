from pathlib import Path

import pandas as pd


class ReportGenerator:
    """
    검증 결과를 Excel 파일로 저장한다.
    """


    def generate(
        self,
        result_df: pd.DataFrame,
        output_path: str
    ) -> str:

        result_df.to_excel(
            output_path,
            index=False
        )

        return output_path
    
    # def generate(
    #     self,
    #     result_df: pd.DataFrame,
    #     output_file: str = "validation_result.xlsx"
    # ) -> str:

    #     # output 폴더 생성 (없으면 생성)
    #     output_dir = Path("output")
    #     output_dir.mkdir(exist_ok=True)

    #     # 저장 경로
    #     output_path = output_dir / output_file

    #     # Excel 저장
    #     result_df.to_excel(
    #         output_path,
    #         index=False
    #     )

    #     return str(output_path)