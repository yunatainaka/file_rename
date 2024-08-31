import glob
import os


import os, sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


# def file_rename():
#     files = glob.glob("./B版/*")
#     for file in files:
#         rename = (
#             file.replace("_(", "_")
#             .replace(")", "_")
#             .replace(".01", "")
#             .replace("step2.0", "step2.0)")
#             .replace("__", "_")
#         )
#         print(rename)
#         # os.rename(file, rename)


# def file_version_update():
#     files = glob.glob("./B版/*")
#     for file in files:
#         rename = file.replace("_A_", "_C_").replace("_B_", "_C_")
#         print(rename)
#         os.rename(file, rename)


class FileRename:
    def __init__(self):
        self.test = ""
        self.input_folder = ""
        self.output_folder = ""

    def main(self):
        print("AAAAAA")
        self._create_GUI()

    def _create_GUI(self):
        root = tk.Tk()
        root.title("File Rename Tool")
        root.geometry("400x600")
        root.resizable(False, False)

        tk.Message(
            root,
            width=400,
            text="""～使い方～
        １．フォルダを選択する。
        　　選択したフォルダ内の全てのファイルを対象としてファイル名の置換を行う。
        ２．置換対象のファイル名を入力する
        ３．前方一致検索、部分一致検索、後方一致検索を選択する。
            """,
        ).place(x=0, y=0)

        # 入力フォルダフレーム
        frame1 = ttk.Frame(root, width=360, height=60, padding=10, relief="groove")
        frame1.place(x=20, y=100)
        tk.Label(frame1, text="入力フォルダを選択してください").place(x=0, y=0)
        input_path = tk.StringVar()
        IDirEntry = ttk.Entry(
            frame1, textvariable=input_path, width=48, state="readonly"
        )
        IDirEntry.place(x=0, y=20)
        tk.Button(
            frame1,
            text=("選択"),
            command=lambda: self._push_input_folder_bottun(input_path),
        ).place(x=300, y=18)

        # 置換文言フレーム
        frame2 = ttk.Frame(root, width=360, height=60, padding=10, relief="groove")
        frame2.place(x=20, y=160)

        tk.Label(frame2, text="置換する文言を入力してください").place(x=0, y=0)
        self.before = tk.StringVar()
        IDirEntry = ttk.Entry(frame2, textvariable=self.before, width=20)
        IDirEntry.place(x=0, y=20)
        tk.Label(frame2, text="→").place(x=130, y=20)
        self.after = tk.StringVar()
        IDirEntry = ttk.Entry(frame2, textvariable=self.after, width=20)
        IDirEntry.place(x=150, y=20)

        # ラジオボタンフレーム
        frame3 = ttk.Frame(root, width=360, height=100, padding=10, relief="groove")
        frame3.place(x=20, y=220)
        tk.Label(frame3, text="検索種別を選択してください").place(x=0, y=0)
        self.selected_option = tk.StringVar(value=1)
        tk.Radiobutton(
            frame3, text="前方一致", variable=self.selected_option, value="1"
        ).place(x=0, y=20)
        tk.Radiobutton(
            frame3, text="部分一致", variable=self.selected_option, value="2"
        ).place(x=0, y=40)
        tk.Radiobutton(
            frame3, text="後方一致", variable=self.selected_option, value="3"
        ).place(x=0, y=60)
        # tk.Button(text=("終了"), command=quit).place(x=150, y=150)

        # 出力フォルダフレーム
        frame4 = ttk.Frame(root, width=360, height=60, padding=10, relief="groove")
        frame4.place(x=20, y=320)
        tk.Label(frame4, text="出力フォルダを選択してください").place(x=0, y=0)
        output_path = tk.StringVar()
        IDirEntry = ttk.Entry(
            frame4, textvariable=output_path, width=48, state="readonly"
        )
        IDirEntry.place(x=0, y=20)
        tk.Button(
            frame4,
            text=("選択"),
            command=lambda: self._push_output_folder_bottun(output_path),
        ).place(x=300, y=18)

        tk.Button(
            root,
            text=("置換開始"),
            command=lambda: self._file_rename(),
        ).place(x=200, y=400)

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
        if self.after.get() == "":
            error_list.append("置換後文言を入力してください")

        return error_list

    def _file_rename(self):
        error_list = self._check()
        if len(error_list) != 0:
            print(error_list)
            return
        print("input_folder: ", self.input_folder)
        print("output_folder: ", self.output_folder)
        print("before: ", self.before.get())
        print("after: ", self.after.get())
        print("selected_option:", self.selected_option.get())
        files = glob.glob(f"{self.input_folder}/*")
        for file in files:
            rename = file.replace(self.before.get(), self.after.get())
            print(file)
            os.rename(file, rename)


if __name__ == "__main__":
    fr = FileRename()
    fr.main()
