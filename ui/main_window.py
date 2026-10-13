import customtkinter as ctk
from tkinter import filedialog

from core.excel_reader import ExcelReader
from core.validator_engine import ValidatorEngine
from core.report_generator import ReportGenerator


class MainWindow:

    def __init__(self):

        # Theme
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        # Window
        self.window = ctk.CTk()
        self.window.title("SA-RWA Validator")
        self.window.geometry("1024x650")

        self.df = None

        self.create_header()
        self.create_file_section()
        self.create_action_section()
        self.create_status_section()
        self.create_summary_section()
        self.create_log_section()
        self.create_footer()

        self.write_log("INFO", "프로그램 시작")

    ####################################################
    # Header
    ####################################################

    def create_header(self):

        title = ctk.CTkLabel(
            self.window,
            text="SA-RWA Validator",
            font=("Arial", 28, "bold")
        )

        title.pack(pady=(20, 0))

        subtitle = ctk.CTkLabel(
            self.window,
            text="Basel III Standardised Approach Validation Tool",
            font=("Arial", 14)
        )

        subtitle.pack(pady=(0, 15))

    ####################################################
    # File Section
    ####################################################

    def create_file_section(self):

        frame = ctk.CTkFrame(self.window)

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        title = ctk.CTkLabel(
            frame,
            text="Input Excel",
            font=("Arial", 14, "bold")
        )

        title.pack(anchor="w", padx=10, pady=(10, 0))

        self.file_label = ctk.CTkLabel(
            frame,
            text="선택된 파일 : 없음",
            anchor="w"
        )

        self.file_label.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10,
            pady=15
        )

        button = ctk.CTkButton(
            frame,
            text="Excel 선택",
            width=120,
            command=self.select_file
        )

        button.pack(
            side="right",
            padx=10,
            pady=10
        )

    ####################################################
    # Action
    ####################################################

    def create_action_section(self):

        self.validate_button = ctk.CTkButton(
            self.window,
            text="검증 실행",
            width=200,
            height=40,
            state="disabled",
            command=self.validate
        )

        self.validate_button.pack(
            pady=15
        )

    ####################################################
    # Status
    ####################################################

    def create_status_section(self):

        frame = ctk.CTkFrame(self.window)

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.status_label = ctk.CTkLabel(
            frame,
            text="상태 : 대기중",
            font=("Arial", 13, "bold")
        )

        self.status_label.pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        self.progress = ctk.CTkProgressBar(frame)

        self.progress.pack(
            fill="x",
            padx=10,
            pady=(0, 10)
        )

        self.progress.set(0)

    ####################################################
    # Summary
    ####################################################

    def create_summary_section(self):

        frame = ctk.CTkFrame(self.window)

        frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.total_value = self.create_card(
            frame,
            "Total"
        )

        self.pass_value = self.create_card(
            frame,
            "PASS"
        )

        self.fail_value = self.create_card(
            frame,
            "FAIL"
        )

    def create_card(self, parent, title):

        card = ctk.CTkFrame(parent)

        card.pack(
            side="left",
            expand=True,
            fill="x",
            padx=8,
            pady=10
        )

        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=("Arial", 14, "bold")
        )

        title_label.pack(
            pady=(10, 5)
        )

        value = ctk.CTkLabel(
            card,
            text="0",
            font=("Arial", 28, "bold")
        )

        value.pack(
            pady=(0, 10)
        )

        return value

    ####################################################
    # Log
    ####################################################

    def create_log_section(self):

        frame = ctk.CTkFrame(self.window)

        frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        label = ctk.CTkLabel(
            frame,
            text="Log",
            font=("Arial", 14, "bold")
        )

        label.pack(
            anchor="w",
            padx=10,
            pady=(10, 5)
        )

        self.log_box = ctk.CTkTextbox(
            frame,
            height=250
        )

        self.log_box.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=(0, 10)
        )

    ####################################################
    # Footer
    ####################################################

    def create_footer(self):

        footer = ctk.CTkLabel(
            self.window,
            text="Version 1.0",
            font=("Arial", 11)
        )

        footer.pack(
            pady=(0, 10)
        )

    ####################################################
    # Select File
    ####################################################

    def select_file(self):

        file_path = filedialog.askopenfilename(
            title="Excel 선택",
            filetypes=[
                ("Excel Files", "*.xlsx")
            ]
        )

        if not file_path:
            return

        try:

            reader = ExcelReader()

            self.df = reader.read(file_path)

            self.file_label.configure(
                text=file_path
            )

            self.validate_button.configure(
                state="normal"
            )

            self.write_log(
                "SUCCESS",
                f"Excel 읽기 완료 ({len(self.df):,}건)"
            )

        except Exception as e:

            self.write_log(
                "ERROR",
                str(e)
            )

    ####################################################
    # Validate
    ####################################################

    def validate(self):

        if self.df is None:
            return

        try:

            self.status_label.configure(
                text="상태 : 검증중..."
            )

            self.progress.set(0.2)

            self.write_log(
                "INFO",
                "Validator 실행"
            )

            engine = ValidatorEngine()

            result_df = engine.validate(
                self.df
            )

            self.progress.set(0.7)

            save_path = filedialog.asksaveasfilename(
                title="검증 결과 저장",
                defaultextension=".xlsx",
                initialfile="validation_result.xlsx",
                filetypes=[
                    ("Excel Files", "*.xlsx")
                ]
            )

            if not save_path:

                self.status_label.configure(
                    text="상태 : 대기중"
                )

                self.progress.set(0)

                self.write_log(
                    "INFO",
                    "저장을 취소했습니다."
                )

                return

            report = ReportGenerator()

            report.generate(
                result_df,
                save_path
            )

            total = len(result_df)

            passed = (
                result_df["검증결과"] == "PASS"
            ).sum()

            failed = total - passed

            self.total_value.configure(
                text=f"{total:,}"
            )

            self.pass_value.configure(
                text=f"{passed:,}"
            )

            self.fail_value.configure(
                text=f"{failed:,}"
            )

            self.progress.set(1)

            self.status_label.configure(
                text="상태 : 완료"
            )

            self.write_log(
                "SUCCESS",
                "검증 완료"
            )

            self.write_log(
                "INFO",
                f"저장 위치 : {save_path}"
            )

        except Exception as e:

            self.progress.set(0)

            self.status_label.configure(
                text="상태 : 오류"
            )

            self.write_log(
                "ERROR",
                str(e)
            )

    ####################################################
    # Log
    ####################################################

    def write_log(self, level, message):

        self.log_box.insert(
            "end",
            f"[{level}] {message}\n"
        )

        self.log_box.see("end")

    ####################################################
    # Run
    ####################################################

    def run(self):

        self.window.mainloop()