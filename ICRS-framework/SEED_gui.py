# coding:utf-8
# author : Ganster
# date   : 16/09/2022 16:17
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
window.title("Experimental record")
window.minsize(500, 500)

# 介绍性文本
intro1 = tk.Label(window, text="使用说明：点击视频列表中视频，视频开始时点击start键开始记录", font=('Times', 12, 'bold'))
# intro1 = tk.Label(window, text="Instructions: Click the video in the video list,\n and click the start button to start recording when the video starts", font=('Times', 12, 'bold'))
intro1.grid(row=0, column=2)
intro2 = tk.Label(window, text="观看视频时若有情绪诱发请点击emo键进行记录", font=('Times', 12, 'bold'))
# intro2 = tk.Label(window, text="Please click the emo button to record if there is any emotion induced while watching the video", font=('Times', 12, 'bold'))
intro2.grid(row=1, column=2)
intro3 = tk.Label(window, text="视频结束的同时及时点击end键完成记录", font=('Times', 12, 'bold'))
# intro3 = tk.Label(window, text="When the video ends, click the end button in time to complete the recording", font=('Times', 12, 'bold'))
intro3.grid(row=2, column=2)
intro4 = tk.Label(window, text="最后点击save键选择路径，命名文件并保存", font=('Times', 12, 'bold'))
# intro4 = tk.Label(window, text="Finally, click save to select a path, name the file, and save it", font=('Times', 12, 'bold'))
intro4.grid(row=3, column=2)

tips = tk.Label(window, text="特别提示：有情绪时点击emo按钮，可以同时点击多次", bg="white",fg="purple",font=('Times', 18, 'bold'))
# tips = tk.Label(window, text="Special note: If an emotion arises, click the emo button,\n you can click multiple times at the same time", bg="white",fg="purple",font=('Times', 14, 'bold'))
tips.grid(row=5, column=2)

positive = tk.Label(window,text="积极情绪：兴奋、愉快、开心、欢乐、激动等", bg="yellow",fg="red",font=('Times', 15, 'bold italic underline'))
# positive = tk.Label(window,text="Positive emotions: excitement, pleasure, happiness, joy, excitement, etc", bg="yellow",fg="red",font=('Times', 15, 'bold italic underline'))
positive.grid(row=6, column=2)

negative = tk.Label(window,text="消极情绪：紧张、慌张、伤感、痛苦、生气等", bg="#7CCD7C",fg="blue",font=('Times', 15, 'bold italic underline'))
# negative = tk.Label(window,text="Negative emotions: nervousness, panic, sadness, pain, anger, etc", bg="#7CCD7C",fg="blue",font=('Times', 15, 'bold italic underline'))
negative.grid(row=7, column=2)

neutral = tk.Label(window,text="在观看中立情绪视频时若有情绪产生，请点击emo按钮", bg="green",fg="white",font=('Times', 15, 'bold italic underline'))
# neutral = tk.Label(window,text="If an emotion arises while watching a neutral emotion video,\nclick the emo button", bg="green",fg="white",font=('Times', 15, 'bold italic underline'))
neutral.grid(row=8, column=2)


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
emo = tk.Button(window, text='emo', font=('Times', 16, 'bold'), bd=20,  bg="red", command=get_emo)
emo.grid(row=9, column=2)

start = tk.Button(window, text='start',font=('Times', 16, 'bold'), bd=20,  bg="white", command=start_listen)
start.grid(row=9, column=1)

end = tk.Button(window, text='end', font=('Times', 16, 'bold'),bd=20,   bg="white", command=end_listen)
end.grid(row=9, column=3)


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
        filenewpath= filedialog.asksaveasfilename(title='保存文件',
                                                filetypes=filetypes,
                                                defaultextension='.mat',
                                                initialdir='C:/Users/Administrator/Desktop' )
        path_var.set(filenewpath)
        # 保存文件
        savemat(str(path_var.get()), all_record)
        # all_record.save()
        messagebox.showinfo(title="保存信息", message="保存成功！")
    except Exception as e:
        messagebox.showinfo(title="保存信息", message="保存失败！")
        print(e)


path_var = tk.StringVar()

tk.Label(window, text='savepath:').grid(row=13, column=1)
path = tk.Entry(window, textvariable=path_var)
path.grid(row=11, column=2)


save = tk.Button(window, text='save', font=('Times', 14, 'bold'), bd=10,   bg="white", command=save_mat)
save.grid(row=11, column=3)

# 视频列表
tag = tk.Label(window, text="Video list", font=('Times', 14))
tag.grid(row=12, column=1)


def v1(name):
    # path1 = "H:\\学习资料备份\\情感计算数据集\\SEED\\seed-video\\" + name + ".mp4"
    path1 = "../seed-video\\" + name + ".mp4"
    startfile(path1)


text1 = "1人再囧途之泰囧part1"
video1 = tk.Button(window, text="1 Lost in Thailand part1", font=('Times', 10), command=lambda :v1(text1))
video1.grid(row=13, column=1)
text2 = "2世界遗产在中国-黄山part1"
video2 = tk.Button(window, text="2 World Heritage in China-Mount Huang part1", font=('Times', 10), command=lambda :v1(text2))
video2.grid(row=13, column=2)
text3 = "3唐山大地震part1"
video3 = tk.Button(window, text="3 Aftershock part1", font=('Times', 10), command=lambda :v1(text3))
video3.grid(row=13, column=3)
text4 = "4一九四二part1"
video4 = tk.Button(window, text="4 Back to 1942 part1", font=('Times', 10), command=lambda :v1(text4))
video4.grid(row=14, column=1)
text5 = "5世界遗产在中国-黄山part2"
video5 = tk.Button(window, text="5 World Heritage in China-Mount Huang  part2", font=('Times', 10), command=lambda :v1(text5))
video5.grid(row=14, column=2)
text6 = "6人再囧途之泰囧part2"
video6 = tk.Button(window, text="6 Lost in Thailand part2", font=('Times', 10), command=lambda :v1(text6))
video6.grid(row=14, column=3)
text7 = "7一九四二part2"
video7 = tk.Button(window, text="7 Back to 1942 part2", font=('Times', 10), command=lambda :v1(text7))
video7.grid(row=15, column=1)
text8 = "8世界遗产在中国-苏州古典园林part1"
video8 = tk.Button(window, text="8 World Heritage in China-Classical Gardens of Suzhou part1", font=('Times', 10), command=lambda :v1(text8))
video8.grid(row=15, column=2)
text9 = "9唐伯虎点秋香"
video9 = tk.Button(window, text="9 Flirting Scholar", font=('Times', 10), command=lambda :v1(text9))
video9.grid(row=15, column=3)
text10 = "10越光宝盒part1"
video10 = tk.Button(window, text="10 Just Another Pandora's Box part1", font=('Times', 10), command=lambda :v1(text10))
video10.grid(row=16, column=1)
text11 = "11世界遗产在中国-苏州古典园林part2"
video11 = tk.Button(window, text="11 World Heritage in China-Classical Gardens of Suzhou part2", font=('Times', 10), command=lambda :v1(text11))
video11.grid(row=16, column=2)
text12 = "12一九四二part3"
video12 = tk.Button(window, text="12 Back to 1942 part3", font=('Times', 10), command=lambda :v1(text12))
video12.grid(row=16, column=3)
text13 = "13世界遗产在中国-丽江古城"
video13 = tk.Button(window, text="13 World Heritage in China-Old Town of Lijiang", font=('Times', 10), command=lambda :v1(text13))
video13.grid(row=17, column=1)
text14 = "14越光宝盒part2"
video14 = tk.Button(window, text="14 Just Another Pandora's Box part2", font=('Times', 10), command=lambda :v1(text14))
video14.grid(row=17, column=2)
text15 = "15唐山大地震part2"
video15 = tk.Button(window, text="15 Aftershock part2", font=('Times', 10), command=lambda :v1(text15))
video15.grid(row=17, column=3)

tk.mainloop()