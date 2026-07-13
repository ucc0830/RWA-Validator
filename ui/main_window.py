import customtkinter as ctk
from tkinter import filedialog


class MainWindow:

    def __init__(self):
        # 테마 설정
        ctk.set_appearance_mode("System")      # Light / Dark / System
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()

        self.window.title("SA-RWA Validator")
        self.window.geometry("1024x768")

        self.create_widgets()

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
            state="disabled"
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

        self.file_label.configure(
            text=f"선택된 파일 : {file_path}"
        )

        self.validate_button.configure(state="normal")

        self.write_log(f"파일 선택 완료 : {file_path}")

    def write_log(self, message):

        self.log_box.insert("end", message + "\n")
        self.log_box.see("end")

    def run(self):
        self.window.mainloop()