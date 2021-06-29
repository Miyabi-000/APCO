import os
import csv
import tkinter
from tkinter import messagebox, filedialog, Label, Button


# UI ------------------------------


root = tkinter.Tk()
root.title('AutoCaptionTool')
root.geometry('600x150')

ReadedPath = tkinter.StringVar()


def load_path_button():
    fTyp = [("", "*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filePath = filedialog.askopenfilename(
        initialdir=iDir,
        filetypes=fTyp
    )

    if len(filePath) == 0:
        ReadedPath.set('Not loaded')
    else:
        ReadedPath.set(filePath)


def submit_button():
    if ReadedPath.get() != 'Not loaded':
        input_value = ReadedPath.get()
        ja_list_from_csv = csv_get_ja_row(input_value)
        tc_list_from_csv = csv_get_time_row(input_value)

        fixed_ja_list = formatter(ja_list_from_csv)

        export_xlsx(tc_list_from_csv, fixed_ja_list,)

        messagebox.showinfo('Warning', input_value)

    else:
        messagebox.showinfo('Warning', 'File is not loaded.')

# ------------------------------

# import CSV


def csv_get_ja_row(csv_path):
    print('ja to list')
    ja_list = []

    with open(csv_path, encoding='utf-8') as f:
        for row in csv.reader(f):
            ja_list.append(row[2])
        del ja_list[0]

    print(ja_list)
    return ja_list


def csv_get_time_row(csv_path):
    print('timecode to list')
    time_list = []

    with open(csv_path, encoding='utf-8') as f:
        for row in csv.reader(f):
            time_list.append(row[0])

        del time_list[0]

    return time_list

# setup "。"

# 複数回答
    # あります系統　（英字ひとつ）
    ja_list = ja_list.replace("ありますが", "A、")
    ja_list = ja_list.replace("ありますか", "B、")
    ja_list = ja_list.replace("ありますので", "C、")
    ja_list = ja_list.replace("ありますでしょうか", "D、")
    ja_list = ja_list.replace("あります", "あります。\n")
    ja_list = ja_list.replace("A、", "ありますが、")
    ja_list = ja_list.replace("B、", "ありますか。")
    ja_list = ja_list.replace("C、", "ありますので、")
    ja_list = ja_list.replace("D、", "ありますでしょうか。\n")

    # こと系統　（英字２つ、A＊）
    ja_list = ja_list.replace("ことでしょうか", "AA、")
    ja_list = ja_list.replace("ことですか", "AB、")
    ja_list = ja_list.replace("ことで", "ことで、")
    ja_list = ja_list.replace("AA、", "ことでしょうか。")
    ja_list = ja_list.replace("AB、", "ことですか。")

    # です系統　（英字２つ、B＊）
    ja_list = ja_list.replace("ですけれども", "BA、")
    ja_list = ja_list.replace("ですけども", "BB、")
    ja_list = ja_list.replace("ですけど", "BC、")
    ja_list = ja_list.replace("ですが", "BD、")
    ja_list = ja_list.replace("です", "です。\n")
    ja_list = ja_list.replace("けれども", "けれども、")
    ja_list = ja_list.replace("BA、", "ですけれども、")
    ja_list = ja_list.replace("BB、", "ですけども、")
    ja_list = ja_list.replace("BC、", "ですけど、")
    ja_list = ja_list.replace("BD、", "ですが、")

    # まして系統　（英字２つ、C＊）
    ja_list = ja_list.replace("つきましては", "CA、")
    ja_list = ja_list.replace("つきまして", "CB、")
    ja_list = ja_list.replace("ましては", "CC、")
    ja_list = ja_list.replace("まして", "まして、")
    ja_list = ja_list.replace("CA、", "つきましては、")
    ja_list = ja_list.replace("CB、", "つきまして、")
    ja_list = ja_list.replace("CC、", "ましては、")
    
# 読点
    ja_list = ja_list.replace("ついては", "ついては、")
    ja_list = ja_list.replace("また", "また、")

# 句点
    ja_list = ja_list.replace("いいでしょうか", "いいでしょうか。")
    ja_list = ja_list.replace("おきます", "おきます。")
    ja_list = ja_list.replace("行いました", "行いました。")
    ja_list = ja_list.replace("思います", "思います。")
    ja_list = ja_list.replace("お願いいたします", "お願いいたします。")
    ja_list = ja_list.replace("お願いします", "お願いします。\n")
    ja_list = ja_list.replace("おりました", "おりました。")
    ja_list = ja_list.replace("ございました", "ございました。\n")
    ja_list = ja_list.replace("ございます", "ございます。\n")
    ja_list = ja_list.replace("すみません", "すみません。\n")
    ja_list = ja_list.replace("参りました", "参りました。")
    ja_list = ja_list.replace("申し上げました", "申し上げました。")


def formatter(ja_list):
    print('add ., N / to list')
    fixed_ja_list = []

    ###

    return fixed_ja_list

# export xlsx


def export_xlsx():
    print('inline_xlsx')

# build


def main():

    ReadedPath.set('Not loaded')

    button = Button(text="load", command=load_path_button)
    button.place(x=10, y=20)

    input_box = Label(width=120, textvariable=ReadedPath)
    input_box.place(x=10, y=50)

    button = Button(text="Submit", command=submit_button)
    button.place(x=10, y=80)

    root.mainloop()


if __name__ == "__main__":
    main()
