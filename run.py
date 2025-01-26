import os

import pathlib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import shutil


class FileRename:
    def __init__(self):
        self.input_folder = ""
        self.output_folder = ""

    def main(self):
        self._create_GUI()

    def _create_GUI(self):
        root = tk.Tk()
        root.title("File Rename Tool")
        root.resizable(False, False)

        tk.Message(
            root,
            width=400,
            text="""※注意
        ・置換後文字列が空白の場合は、置換前文字列を削除する
        ・出力フォルダが未選択の場合は入力フォルダ内のファイルを上書きする
        """,
        ).pack()

        # 入力フォルダフレーム
        frame1 = ttk.Frame(root, width=360, height=60, padding=10, relief="groove")
        frame1.pack()
        tk.Label(frame1, text="入力フォルダを選択してください").place(x=0, y=0)
        input_path = tk.StringVar()
        input_folder = ttk.Entry(
            frame1, textvariable=input_path, width=48, state="readonly"
        )
        input_folder.place(x=0, y=20)
        tk.Button(
            frame1,
            text=("選択"),
            command=lambda: self._push_input_folder_bottun(input_path),
        ).place(x=300, y=18)

        # 置換文言フレーム
        frame2 = ttk.Frame(root, width=360, height=60, padding=10, relief="groove")
        frame2.pack()
        tk.Label(frame2, text="置換する文言を入力してください").place(x=0, y=0)
        self.before = tk.StringVar()
        before_word = ttk.Entry(frame2, textvariable=self.before, width=20)
        before_word.place(x=0, y=20)
        tk.Label(frame2, text="→").place(x=130, y=20)
        self.after = tk.StringVar()
        after_word = ttk.Entry(frame2, textvariable=self.after, width=20)
        after_word.place(x=150, y=20)

        # 出力フォルダフレーム
        frame3 = ttk.Frame(root, width=360, height=60, padding=10, relief="groove")
        frame3.pack()
        tk.Label(frame3, text="出力フォルダを選択してください").place(x=0, y=0)
        output_path = tk.StringVar()
        output_folder = ttk.Entry(
            frame3, textvariable=output_path, width=48, state="readonly"
        )
        output_folder.place(x=0, y=20)
        tk.Button(
            frame3,
            text=("選択"),
            command=lambda: self._push_output_folder_bottun(output_path),
        ).place(x=300, y=18)

        tk.Button(
            root,
            text=("置換開始"),
            command=lambda: self._file_rename(),
        ).pack(pady=10)

        root.mainloop()

    def _push_input_folder_bottun(self, entry):
        iDir = os.path.abspath(os.path.dirname(__file__))
        self.input_folder = tk.filedialog.askdirectory(initialdir=iDir)
        entry.set(self.input_folder)

    def _push_output_folder_bottun(self, entry):
        iDir = os.path.abspath(os.path.dirname(__file__))
        self.output_folder = tk.filedialog.askdirectory(initialdir=iDir)
        entry.set(self.output_folder)

    def _check(self):
        error_list = []
        if self.input_folder == "":
            error_list.append("入力フォルダを選択してください")
        if self.before.get() == "":
            error_list.append("置換前文言を入力してください")

        return error_list

    def _error_dialog(self, error_list):
        error_message = "\n".join(error_list)
        messagebox.showerror("エラー", error_message)

    def _file_rename(self):
        error_list = self._check()
        if len(error_list) != 0:
            self._error_dialog(error_list)
            return

        p_temp = pathlib.Path(self.input_folder).glob("*.*")

        cnt = 0
        for p in p_temp:
            if self.before.get() not in p.name:
                continue

            rename = p.name.replace(self.before.get(), self.after.get())
            if self.output_folder == "":
                if self._check_renamed_file(f"{self.input_folder}/{rename}"):
                    cnt += 1
                    try:
                        os.rename(
                            f"{self.input_folder}/{p.name}",
                            f"{self.input_folder}/{rename}",
                        )
                    except:
                        os.remove(f"{self.input_folder}/{rename}")
                        os.rename(
                            f"{self.input_folder}/{p.name}",
                            f"{self.input_folder}/{rename}",
                        )
            else:
                if self._check_renamed_file(f"{self.output_folder}/{rename}"):
                    cnt += 1
                    shutil.copy2(
                        f"{self.input_folder}/{p.name}",
                        f"{self.output_folder}/{rename}",
                    )

        messagebox.showinfo("置換ファイル数", f"{cnt}件のファイルを置換しました")

    def _check_renamed_file(self, output_path):
        if os.path.isfile(output_path):
            res = messagebox.askokcancel(
                "上書き確認",
                f"{output_path}は存在します。\nファイルの上書きをしますか？",
            )
            return res
        else:
            return True


if __name__ == "__main__":
    fr = FileRename()
    fr.main()
