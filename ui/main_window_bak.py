import customtkinter as ctk
from tkinter import filedialog
from core.excel_reader import ExcelReader
from core.validator_engine import ValidatorEngine
from core.report_generator import ReportGenerator


class MainWindow:

    def __init__(self):
        # 테마 설정
        ctk.set_appearance_mode("System")      # Light / Dark / System
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()

        self.window.title("SA-RWA Validator")
        self.window.geometry("900x400")

        self.create_widgets()
        self.df = None  # DataFrame 초기화

    def create_widgets(self):

        # 제목
        title = ctk.CTkLabel(
            self.window,
            text="SA-RWA Validator",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=20)

        # 파일 선택 버튼
        self.select_button = ctk.CTkButton(
            self.window,
            text="Excel 파일 선택",
            command=self.select_file
        )

        self.select_button.pack(pady=10)

        # 선택된 파일 표시
        self.file_label = ctk.CTkLabel(
            self.window,
            text="선택된 파일 : 없음"
        )

        self.file_label.pack(pady=10)

        # 검증 버튼 (처음에는 비활성)
        self.validate_button = ctk.CTkButton(
            self.window,
            text="검증 실행",
            state="disabled",    
            command=self.validate
        )

        self.validate_button.pack(pady=10)

        # 로그창
        self.log_box = ctk.CTkTextbox(
            self.window,
            width=800,
            height=250
        )

        self.log_box.pack(pady=20)

        self.write_log("프로그램 시작")

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Excel 선택",
            filetypes=[("Excel Files", "*.xlsx")]
        )
        if not file_path:
            return

        try:
            reader = ExcelReader()
            self.df = reader.read(file_path)
            self.file_label.configure(
                text=f"선택된 파일 : {file_path}"
            )
            self.validate_button.configure(
                state="normal"
            )
            self.write_log(f"파일 읽기 성공 ({len(self.df):,}건)")

        except Exception as e:
            self.write_log(str(e))

    def write_log(self, message):

        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")

    def run(self):
        self.window.mainloop()

    def validate(self):
        # try:

        #     self.write_log("검증 시작...")

        #     engine = ValidatorEngine()

        #     result_df = engine.validate(self.df)

        #     report = ReportGenerator()

        #     output_path = report.generate(result_df)

        #     self.write_log("검증 완료")

        #     self.write_log(f"저장 위치 : {output_path}")

        # except Exception as e:

        #     self.write_log(str(e))
        try:

            self.write_log("검증 시작...")

            engine = ValidatorEngine()

            result_df = engine.validate(self.df)

            save_path = filedialog.asksaveasfilename(
                title="검증 결과 저장",
                defaultextension=".xlsx",
                initialfile="validation_result.xlsx",
                filetypes=[("Excel Files", "*.xlsx")]
            )

            if not save_path:

                self.write_log("저장이 취소되었습니다.")
                return

            report = ReportGenerator()

            report.generate(
                result_df,
                save_path
            )

            self.write_log("검증 완료")

            self.write_log(f"저장 위치 : {save_path}")

        except Exception as e:

            self.write_log(str(e))