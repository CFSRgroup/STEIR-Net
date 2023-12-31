# coding:utf-8
# author : Ganster
# date   : 09/11/2022 16:33
# file   : emo_label_gui.py
# IDE    : PyCharm
import tkinter as tk
from tkinter import filedialog, messagebox
from matplotlib import pyplot as plt

from os import startfile
from scipy.io import savemat
import time
import numpy as np

# time_list保存点击时间点，record_list保存时间-点击数组，all_record保存三个信息
time_list = []
record_list = []
all_record = {}

# 窗口设置
window = tk.Tk()
window.title("实验记录 SEED-IV 数据集 session3")
# window.geometry('1060x670')

canvas = tk.Canvas(master=window, width=1060,height=670)
scroy = tk.Scrollbar(master=window)
scroy.pack(side='right',fill='y')
scrox = tk.Scrollbar(master=window, orient=tk.HORIZONTAL)
scrox.pack(side='bottom',fill='x')

canvas.pack(side='right')

# Frame作为容器放置组件
frame = tk.Frame(canvas, width=1060,height=670)
frame.pack()
# 将Frame添加至Canvas上
canvas.create_window((0,0),window=frame,anchor="nw")

# 介绍性文本
intro1_1 = tk.Label(frame, text="使用说明：", font=('Times', 12, 'bold'))
intro1_1.grid(row=1, column=1)
intro1_2 = tk.Label(frame, text="点击视频列表中视频，", font=('Times', 12, 'bold'))
intro1_2.grid(row=1, column=2)
intro1_3 = tk.Label(frame, text="自动开始计时", font=('Times', 12, 'bold'))
intro1_3.grid(row=1, column=3)
intro21 = tk.Label(frame, text="观看视频时", font=('Times', 12, 'bold'))
intro21.grid(row=3, column=1)
intro22 = tk.Label(frame, text="若有情绪诱发请点击", font=('Times', 12, 'bold'))
intro22.grid(row=3, column=2)
intro23 = tk.Label(frame, text="emo键进行记录", font=('Times', 12, 'bold'))
intro23.grid(row=3, column=3)
intro31 = tk.Label(frame, text="视频结束的同时", font=('Times', 12, 'bold'))
intro31.grid(row=5, column=1)
intro32 = tk.Label(frame, text="请及时点击", font=('Times', 12, 'bold'))
intro32.grid(row=5, column=2)
intro33 = tk.Label(frame, text="end键完成记录", font=('Times', 12, 'bold'))
intro33.grid(row=5, column=3)

intro41 = tk.Label(frame, text="最后查看图示后并关闭", font=('Times', 12, 'bold'))
intro41.grid(row=7, column=1)
intro42 = tk.Label(frame, text="点击save键选择路径", font=('Times', 12, 'bold'))
intro42.grid(row=7, column=2)
intro43 = tk.Label(frame, text="命名文件并保存", font=('Times', 12, 'bold'))
intro43.grid(row=7, column=3)

intro51 = tk.Label(frame, text="提示：每个视频结束时", font=('Times', 12, 'bold'))
intro51.grid(row=9, column=1)
intro52 = tk.Label(frame, text="都需要点击end按钮", font=('Times', 12, 'bold'))
intro52.grid(row=9, column=2)
intro53 = tk.Label(frame, text="来记录当前视频产生的标签", font=('Times', 12, 'bold'))
intro53.grid(row=9, column=3)

# 介绍性文本
intro61 = tk.Label(frame, text="Instructions: Click the video", font=('Times', 12, 'bold'))
intro61.grid(row=2, column=1)
intro62 = tk.Label(frame, text="in the video list ", font=('Times', 12, 'bold'))
intro62.grid(row=2, column=2)
intro63 = tk.Label(frame, text="in order to automatically start timing.", font=('Times', 12, 'bold'))
intro63.grid(row=2, column=3)

intro71 = tk.Label(frame, text="Please click the emo button", font=('Times', 12, 'bold'))
intro71.grid(row=4, column=1)
intro72 = tk.Label(frame, text="to record if there is any", font=('Times', 12, 'bold'))
intro72.grid(row=4, column=2)
intro73 = tk.Label(frame, text="emotion induced while watching the video.", font=('Times', 12, 'bold'))
intro73.grid(row=4, column=3)

intro81 = tk.Label(frame, text="When the video ends", font=('Times', 12, 'bold'))
intro81.grid(row=6, column=1)
intro82 = tk.Label(frame, text="click the end button", font=('Times', 12, 'bold'))
intro82.grid(row=6, column=2)
intro83 = tk.Label(frame, text="in time to complete the recording.", font=('Times', 12, 'bold'))
intro83.grid(row=6, column=3)

intro91 = tk.Label(frame, text="Finally, look at the diagram and close it.", font=('Times', 12, 'bold'))
intro91.grid(row=8, column=1)
intro92 = tk.Label(frame, text="Click save to select a path,", font=('Times', 12, 'bold'))
intro92.grid(row=8, column=2)
intro93 = tk.Label(frame, text="name the file and save it.", font=('Times', 12, 'bold'))
intro93.grid(row=8, column=3)

intro101 = tk.Label(frame, text="Hint: The end button needs to be clicked", font=('Times', 12, 'bold'))
intro101.grid(row=10, column=1)
intro102 = tk.Label(frame, text="at the end of each video to record", font=('Times', 12, 'bold'))
intro102.grid(row=10, column=2)
intro103 = tk.Label(frame, text="the labels generated by the current video.", font=('Times', 12, 'bold'))
intro103.grid(row=10, column=3)

tips11 = tk.Label(frame, text="特别提示：情绪激烈时", bg="white", fg="purple", font=('Times', 14, 'bold'))
tips11.grid(row=40, column=1)
tips12 = tk.Label(frame, text="可以在同一时间内", bg="white", fg="purple", font=('Times', 14, 'bold'))
tips12.grid(row=40, column=2)
tips13 = tk.Label(frame, text="多次点击emo按钮", bg="white", fg="purple", font=('Times', 14, 'bold'))
tips13.grid(row=40, column=3)

tips21 = tk.Label(frame, text="Special note: You can click the", bg="white", fg="purple", font=('Times', 14, 'bold'))
tips21.grid(row=41, column=1)
tips22 = tk.Label(frame, text="emo button multiple times at the same time", bg="white", fg="purple", font=('Times', 14, 'bold'))
tips22.grid(row=41, column=2)
tips23 = tk.Label(frame, text="when you are in a strong mood.", bg="white", fg="purple", font=('Times', 14, 'bold'))
tips23.grid(row=41, column=3)
# positive = tk.Label(window, text="积极情绪：兴奋、愉快、开心、欢乐、激动等", bg="yellow", fg="red",
#                     font=('Times', 15, 'bold italic underline'))
# positive.grid(row=6, column=2)
#
# negative = tk.Label(window, text="消极情绪：紧张、慌张、伤感、痛苦、生气等", bg="#7CCD7C", fg="blue",
#                     font=('Times', 15, 'bold italic underline'))
# negative.grid(row=7, column=2)
#
# neutral = tk.Label(window, text="在观看中立情绪视频时若有情绪产生，请点击emo按钮", bg="green", fg="white",
#                    font=('Times', 15, 'bold italic underline'))
# neutral.grid(row=8, column=2)


# 点击start开始监听
def start_listen():
    time_list.clear()
    record_list.clear()
    all_record.clear()
    s = time.time()
    time_list.append(s)
    print("开始！")


# 点击emo表示获取有情绪的点
def get_emo():
    g = time.time()
    time_list.append(g)
    print("emo!")


# # 点击emo表示获取有情绪的点
# def get_emo2(event):
#     g = time.time()
#     time_list.append(g)
#     print("emo!")


# 计算实际时间点
def calculate(point, start):
    elap = point - start  # 获取时间差
    minutes = int(elap / 60)
    seconds = int(elap - minutes * 60.0)
    hseconds = int((elap - minutes * 60.0 - seconds) * 1000)
    print('%02d:%02d:%03d' % (minutes, seconds, hseconds))
    record = '%02d:%02d:%03d' % (minutes, seconds, hseconds)
    record_list.append(record)


# 找到数组内每秒的点击次数
def findTime(item):
    minute = int(item[1])
    second1 = int(item[3])
    second2 = int(item[4])
    total_second = minute * 60 + second1 * 10 + second2
    return total_second


# 结束点击监听
def end_listen():
    e = time.time()
    time_list.append(e)
    print("结束！")
    # 获取记录时间长度
    length = len(time_list)
    # 计算出按键时间点
    for i in time_list:
        calculate(i, time_list[0])
    print(record_list)
    print("---------------")

    length = len(record_list)
    trial_size = findTime(record_list[length - 1])

    count_list = np.zeros([trial_size + 1], dtype=int)
    # 计算出每秒按击的次数
    for i in record_list:
        total_second = findTime(i)
        count_list[total_second] += 1
    print(trial_size)
    print("---------------")
    print(count_list)
    # 将结果记录到字典
    all_record['press_time'] = record_list
    all_record['length'] = trial_size
    all_record['count'] = count_list

    plt.plot(count_list)
    plt.title('count-time figure')
    plt.xlabel("time")
    plt.ylabel("count")
    plt.show()


# 三个按钮
emo = tk.Button(frame, text='emo', font=('Times', 16, 'bold'), bd=20, bg="red", command=get_emo)
emo.grid(row=12, column=2)

# start = tk.Button(window, text='start', font=('Times', 12, 'bold'), bd=20, bg="white", command=start_listen)
# start.grid(row=12, column=1)
introxx = tk.Label(frame, text="(๑•̀ㅂ•́)و✧", font=('Times', 16, 'bold'))
introxx.grid(row=12, column=1)

end = tk.Button(frame, text='end', font=('Times', 16, 'bold'), bd=20, bg="white", command=end_listen)
end.grid(row=12, column=3)


# plt.plot(all_record.get('count'))
# plt.title('count-time figure')
# plt.xlabel("time")
# plt.ylabel("count")
# show_count = tk.Label(window, image=plt.show())
# show_count.grid(row=10, column=2)


# 保存为mat格式文件
def save_mat():
    try:
        filetypes = [("MAT", "*.mat"), ('All files', '*')]
        # 返回一个 pathname 文件路径字符串，如果取消或者关闭则返回空字符，返回文件如何操作是后续代码的事情，
        # 该函数知识返回选择文件的文件名字，不具备保存文件的能力
        filenewpath = filedialog.asksaveasfilename(title='保存文件',
                                                   filetypes=filetypes,
                                                   defaultextension='.mat',
                                                   initialdir='C:/Users/Administrator/Desktop')
        path_var.set(filenewpath)
        # 保存文件
        savemat(str(path_var.get()), all_record)
        # all_record.save()
        messagebox.showinfo(title="保存信息", message="保存成功！")
    except Exception as e:
        messagebox.showinfo(title="保存信息", message="保存失败！")
        print(e)


path_var = tk.StringVar()

tk.Label(frame, text='savepath:', font=('Times', 12, 'bold')).grid(row=13, column=1)
path = tk.Entry(frame, textvariable=path_var)
path.grid(row=13, column=2)

save = tk.Button(frame, text='save', font=('Times', 12, 'bold'), bd=10, bg="white", command=save_mat)
save.grid(row=13, column=3)

# 视频列表
tag = tk.Label(frame, text="视频列表", font=('Times', 12))
tag.grid(row=14, column=1)


# def v1(name):
#     path1 = "../session3\\" + name + ".mp4"
#     # path1 = "F:\\生理信号数据库\\SEED-IV\\seed-iv-video\\session3\\" + name + ".mp4"
#     startfile(path1)
#     start_listen()
#
#
# text1 = "1"
# video1 = tk.Button(frame, text="1 Fleet of Time/匆匆那年 sad", font=('Times', 10), command=lambda: v1(text1))
# video1.grid(row=15, column=1)
# text2 = "2"
# video2 = tk.Button(frame, text="2 The House That Never Dies/京城81号 fear", font=('Times', 10), command=lambda: v1(text2))
# video2.grid(row=16, column=1)
# text3 = "3"
# video3 = tk.Button(frame, text="3 The Child's Eye/童眼 fear", font=('Times', 10), command=lambda: v1(text3))
# video3.grid(row=17, column=1)
# text4 = "4"
# video4 = tk.Button(frame, text="4 Dearest/亲爱的 sad", font=('Times', 10), command=lambda: v1(text4))
# video4.grid(row=18, column=1)
# text5 = "5"
# video5 = tk.Button(frame, text="5 The Stolen Years/被偷走的那五年 happy", font=('Times', 10), command=lambda: v1(text5))
# video5.grid(row=19, column=1)
# text6 = "6"
# video6 = tk.Button(frame, text="6 Very Happy/我家有喜 EP47 happy", font=('Times', 10), command=lambda: v1(text6))
# video6.grid(row=20, column=1)
# text7 = "7"
# video7 = tk.Button(frame, text="7 You are my life more complete /你是我的生命 EP8 happy", font=('Times', 10), command=lambda: v1(text7))
# video7.grid(row=21, column=1)
# text8 = "8"
# video8 = tk.Button(frame, text="8 Dearest/亲爱的 sad", font=('Times', 10), command=lambda: v1(text8))
# video8.grid(row=22, column=1)
#
#
# text9 = "9"
# video9 = tk.Button(frame, text="9 Aftershock/唐山大地震 sad", font=('Times', 10), command=lambda: v1(text9))
# video9.grid(row=15, column=2)
# text10 = "10"
# video10 = tk.Button(frame, text="10 The Great Hypnotist/催眠大师 fear", font=('Times', 10), command=lambda: v1(text10))
# video10.grid(row=16, column=2)
# text11 = "11"
# video11 = tk.Button(frame, text="11 Foster Father/养父 EP3 sad", font=('Times', 10), command=lambda: v1(text11))
# video11.grid(row=17, column=2)
# text12 = "12"
# video12 = tk.Button(frame, text="12 A Bite of China/舌尖上的中国 S1EP1 neutral", font=('Times', 10), command=lambda: v1(text12))
# video12.grid(row=18, column=2)
# text13 = "13"
# video13 = tk.Button(frame, text="13 Bunshinsaba III/笔仙 S3 fear", font=('Times', 10), command=lambda: v1(text13))
# video13.grid(row=19, column=2)
# text14 = "14"
# video14 = tk.Button(frame, text="14 Under the Hawthorn Tree/山楂树之恋 happy", font=('Times', 10), command=lambda: v1(text14))
# video14.grid(row=20, column=2)
# text15 = "15"
# video15 = tk.Button(frame, text="15 Very Happy/我家有喜 EP1 happy", font=('Times', 10), command=lambda: v1(text15))
# video15.grid(row=21, column=2)
# text16 = "16"
# video16 = tk.Button(frame, text="16 A Bite of China/舌尖上的中国 S1EP2 neutral", font=('Times', 10), command=lambda: v1(text16))
# video16.grid(row=22, column=2)
#
# text17 = "17"
# video17 = tk.Button(frame, text="17 Hungry Ghost Ritual/盂兰神功 fear", font=('Times', 10), command=lambda: v1(text17))
# video17.grid(row=15, column=3)
# text18 = "18"
# video18 = tk.Button(frame, text="18 20 Once Again/重返20岁 happy", font=('Times', 10), command=lambda: v1(text18))
# video18.grid(row=16, column=3)
# text19 = "19"
# video19 = tk.Button(frame, text="19 A Bite of China/舌尖上的中国S1EP2 neutral", font=('Times', 10), command=lambda: v1(text19))
# video19.grid(row=17, column=3)
# text20 = "20"
# video20 = tk.Button(frame, text="20 A Bite of China/舌尖上的中国S1EP4 neutral", font=('Times', 10), command=lambda: v1(text20))
# video20.grid(row=18, column=3)
# text21 = "21"
# video21 = tk.Button(frame, text="21 Hungry Ghost Ritual/盂兰神功 fear", font=('Times', 10), command=lambda: v1(text21))
# video21.grid(row=19, column=3)
# text22 = "22"
# video22 = tk.Button(frame, text="22 A Bite of China/舌尖上的中国S1EP2 neutral", font=('Times', 10), command=lambda: v1(text22))
# video22.grid(row=20, column=3)
# text23 = "23"
# video23 = tk.Button(frame, text="23 So Young/致我们终将逝去的青春 sad", font=('Times', 10), command=lambda: v1(text23))
# video23.grid(row=21, column=3)
# text24 = "24"
# video24 = tk.Button(frame, text="24 A Bite of China/舌尖上的中国S1EP4 neutral", font=('Times', 10), command=lambda: v1(text24))
# video24.grid(row=22, column=3)

def v1(name):
    path1 = "../session2\\" + name + ".mp4"
    # path1 = "F:\\生理信号数据库\\SEED-IV\\seed-iv-video\\session3\\" + name + ".mp4"
    startfile(path1)
    start_listen()


text1 = "1"
video1 = tk.Button(frame, text="1 Annabelle/安娜贝尔 fear", font=('Times', 10), command=lambda: v1(text1))
video1.grid(row=15, column=1)
text2 = "2"
video2 = tk.Button(frame, text="2 Secret/不能说的秘密 sad", font=('Times', 10), command=lambda: v1(text2))
video2.grid(row=16, column=1)
text3 = "3"
video3 = tk.Button(frame, text="3 Rob-B-Hood/宝贝计划 happy", font=('Times', 10), command=lambda: v1(text3))
video3.grid(row=17, column=1)
text4 = "4"
video4 = tk.Button(frame, text="4 A Bite of China/舌尖上的中国 S1EP3 neutral", font=('Times', 10), command=lambda: v1(text4))
video4.grid(row=18, column=1)
text5 = "5"
video5 = tk.Button(frame, text="5 A Bite of China/舌尖上的中国 S1EP2 neutral", font=('Times', 10), command=lambda: v1(text5))
video5.grid(row=19, column=1)
text6 = "6"
video6 = tk.Button(frame, text="6 Re-Cycle/鬼域 fear", font=('Times', 10), command=lambda: v1(text6))
video6.grid(row=20, column=1)
text7 = "7"
video7 = tk.Button(frame, text="7 A Bite of China/舌尖上的中国 S1EP2 neutral", font=('Times', 10), command=lambda: v1(text7))
video7.grid(row=21, column=1)
text8 = "8"
video8 = tk.Button(frame, text="8 The Child's Eye/童眼 fear", font=('Times', 10), command=lambda: v1(text8))
video8.grid(row=22, column=1)


text9 = "9"
video9 = tk.Button(frame, text="9 Very Happy/我家有喜 EP47 happy", font=('Times', 10), command=lambda: v1(text9))
video9.grid(row=15, column=2)
text10 = "10"
video10 = tk.Button(frame, text="10 You Are the Apple of My Eye/那些年，我们一起追的女孩 happy", font=('Times', 10), command=lambda: v1(text10))
video10.grid(row=16, column=2)
text11 = "11"
video11 = tk.Button(frame, text="11 Bunshinsaba III/笔仙 S3 fear", font=('Times', 10), command=lambda: v1(text11))
video11.grid(row=17, column=2)
text12 = "12"
video12 = tk.Button(frame, text="12 Hsue-shen Tsien/钱学森 happy", font=('Times', 10), command=lambda: v1(text12))
video12.grid(row=18, column=2)
text13 = "13"
video13 = tk.Button(frame, text="13 1408 phontom horror/1408幻影凶间 fear", font=('Times', 10), command=lambda: v1(text13))
video13.grid(row=19, column=2)
text14 = "14"
video14 = tk.Button(frame, text="14 A Bite of China/舌尖上的中国 S1EP2 neutral", font=('Times', 10), command=lambda: v1(text14))
video14.grid(row=20, column=2)
text15 = "15"
video15 = tk.Button(frame, text="15 You are my life more complete/你是我的生命 sad", font=('Times', 10), command=lambda: v1(text15))
video15.grid(row=21, column=2)
text16 = "16"
video16 = tk.Button(frame, text="16 Dearest/亲爱的 sad", font=('Times', 10), command=lambda: v1(text16))
video16.grid(row=22, column=2)

text17 = "17"
video17 = tk.Button(frame, text="17 Hungry Ghost Ritual/盂兰神功 fear", font=('Times', 10), command=lambda: v1(text17))
video17.grid(row=15, column=3)
text18 = "18"
video18 = tk.Button(frame, text="18 Under the Hawthorn Tree/山楂树之恋 sad", font=('Times', 10), command=lambda: v1(text18))
video18.grid(row=16, column=3)
text19 = "19"
video19 = tk.Button(frame, text="19 A Bite of China/舌尖上的中国S1EP2 neutral", font=('Times', 10), command=lambda: v1(text19))
video19.grid(row=17, column=3)
text20 = "20"
video20 = tk.Button(frame, text="20 Meet Miss Anxiety/我的早更女友 happy", font=('Times', 10), command=lambda: v1(text20))
video20.grid(row=18, column=3)
text21 = "21"
video21 = tk.Button(frame, text="21 A Bite of China/舌尖上的中国 S1EP2 neutral", font=('Times', 10), command=lambda: v1(text21))
video21.grid(row=19, column=3)
text22 = "22"
video22 = tk.Button(frame, text="22 Little Daddy/小爸爸 EP30 sad", font=('Times', 10), command=lambda: v1(text22))
video22.grid(row=20, column=3)
text23 = "23"
video23 = tk.Button(frame, text="23 Goodbye Jinhua Station/再见金华站 happy", font=('Times', 10), command=lambda: v1(text23))
video23.grid(row=21, column=3)
text24 = "24"
video24 = tk.Button(frame, text="24 Foster Father/养父 EP40 sad", font=('Times', 10), command=lambda: v1(text24))
video24.grid(row=22, column=3)

# entry = tk.Frame()
# tk.bind()
# window.focus_get()
# window.bind('<Key-e>', get_emo2)
# 更新Frame大小，不然没有滚动效果
frame.update()
# 将滚动按钮绑定只Canvas上
canvas.configure(yscrollcommand=scroy.set, xscrollcommand=scrox.set, scrollregion=canvas.bbox("all"))
scroy.config(command=canvas.yview)
scrox.config(command=canvas.xview)

tk.mainloop()
