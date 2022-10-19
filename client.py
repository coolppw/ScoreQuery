import grpc
import query_pb2_grpc
import query_pb2
import tkinter as tk
from tkinter import messagebox

_HOST = 'localhost'
_PORT = '6060'

def run(idIn, nameIn, lessonIn):
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = query_pb2_grpc.queryScoreStub(channel=conn)
    response = client.query(query_pb2.queryRequest(id = idIn, name = nameIn, lesson = lessonIn))
    print("received: " + response.score)
    return response.score


if __name__ == '__main__':
    #主框架
    window = tk.Tk()
    window.title('Score Query')
    window.geometry('400x200')
    window.resizable(0, 0)
    #说明
    label1 = tk.Label(window, text="学号")
    label2 = tk.Label(window, text="姓名")
    label3 = tk.Label(window, text="课程")
    label1.grid(row=0, padx=10, pady=5)
    label2.grid(row=1, padx=10, pady=5)
    label3.grid(row=2, padx=10, pady=5)
    #输入框
    entry1 = tk.Entry(window)
    entry2 = tk.Entry(window)
    entry3 = tk.Entry(window)
    entry1.grid(row=0, column=4, padx=10, pady=5)
    entry2.grid(row=1, column=4, padx=10, pady=5)
    entry3.grid(row=2, column=4, padx=10, pady=5)
    #按钮函数
    def callback():
        idIn = entry1.get()
        nameIn = entry2.get()
        lessonIn = entry3.get()
        print(idIn)
        print(nameIn)
        print(lessonIn)
        getScore = run(idIn, nameIn, lessonIn)
        messagebox.showinfo(title = '成绩', message = '这门课的成绩为：' + getScore)
    #按钮
    button = tk.Button(window, text='查询', command=callback, bd=3).grid(row=3, column=4, padx=10, pady=5)
    window.mainloop()