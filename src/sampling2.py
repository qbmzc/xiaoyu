import tkinter as tk
from tkinter import filedialog
import pandas as pd
from pandas.core.frame import DataFrame
import random


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    entry_file.delete(0, tk.END)
    entry_file.insert(0, file_path)


def split_csv():
    input_file = entry_file.get()
    samples_per_file = int(entry_samples.get())

    if not input_file:
        print("请选择一个CSV文件")
        return

    if samples_per_file <= 0:
        print("请输入一个正整数作为每个文件的样本个数")
        return

    df = pd.read_csv(input_file)
    # dfs = df.values.tolist()
    # random.shuffle(dfs)
    # df =  DataFrame(dfs)
    # print(dfs)
    df = df.sample(frac=1).reset_index(drop=True)

    for i in range(0, len(df), samples_per_file):
        output_file = f"split_{i // samples_per_file + 1}.csv"
        df[i:i + samples_per_file].to_csv(output_file, index=False)
        print(f"已生成拆分文件：{output_file}")


root = tk.Tk()
root.title("CSV文件拆分工具")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label_file = tk.Label(frame, text="选择CSV文件：")
label_file.grid(row=0, column=0, sticky="w")

entry_file = tk.Entry(frame, width=50)
entry_file.grid(row=0, column=1)

button_browse = tk.Button(frame, text="浏览", command=browse_file)
button_browse.grid(row=0, column=2, padx=5)

label_samples = tk.Label(frame, text="每个文件的样本个数：")
label_samples.grid(row=1, column=0, sticky="w")

entry_samples = tk.Entry(frame, width=50)
entry_samples.grid(row=1, column=1)

button_split = tk.Button(frame, text="拆分", command=split_csv)
button_split.grid(row=1, column=2, padx=5)

root.mainloop()
