import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import lxml.html
from janome.analyzer import Analyzer
from janome.tokenfilter import *
import openpyxl
import pickle
import os
import time

url_input = "https://pet-stay.net/blog/"

def pickle_load(path):
    with open(path, mode='rb') as f:
        data = pickle.load(f)
        return data

def function():
    title_list = pickle_load('./title.pickle')
    url_list = pickle_load('./url.pickle')
    """
    f = open('title.txt', 'r', encoding='UTF-8')
    data1 = f.read()
    f.close()
    title_list = data1

    f = open('url.txt', 'r', encoding='UTF-8')
    data = f.read()
    f.close()
    url_list=data
    """

    """
    title_list = []
    df1 = pd.read_csv('title.csv')
    title_list = df1

    url_list = []
    df2 = pd.read_csv('url.csv')
    url_list = df2
    """


    if v1.get()=="A":
        url = 'https://pet-stay.net/blog/'
    elif v1.get()=="B":
        url = 'https://orange-kid.com/'
    a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])
    book = openpyxl.Workbook()
    sheet = book['Sheet']
    sheet.column_dimensions['A'].width = '50'
    n = 1#記事数
    m = 1#ページ数


    while True:
        #petstay
        if v1.get()=="A":
            if m==1:
                url = "https://pet-stay.net/blog/"
            else:
                url = "https://pet-stay.net/blog/page/" + str(m) + "/"

            res = requests.get(url)
            soup = BeautifulSoup(res.content, "lxml")
            title_elements = soup.find_all(class_='article')
            if m!=33:
                print(title_elements[0].text)
            else:

                k = 1
                while True:
                    if os.path.isfile('出力//pet-stay' + str(k) + '.xlsx'):
                        k = k + 1
                    else:

                        #これなければ正常
                        #追加の記事
                        #time.sleep(10)
                        l = 382
                        b = 0
                        for (title2, url) in zip(title_list, url_list):

                            

                            g_count = a.analyze(title2)
                            words = list(g_count)
                            for word in words:
                                word = word[0]
                            #url = url_list[b]
                            content = title2 + '\n' + url + '\n\n'

                            for word in words:
                                word = word[0]
                                content = content + '#' + word + ' '

                            # 赤文字追加（追加のタグ）
                            additional_tags = entry3.get("1.0", "end").split()
                            for additional_tag in additional_tags:
                                content = content + '#' + additional_tag + ' '

                            sheet['A' + str(l)].value = content
                            sheet['A' + str(l)].alignment = openpyxl.styles.Alignment(wrapText=True)
                            l = l + 1
                            b = b + 1

                        time.sleep(12)
                        book.save('出力//pet-stay' + str(k) + '.xlsx')
                        save_name.set("保存完了" + 'pet-stay' + str(k) + '.xlsx')
                        break

                break
            for title_element in title_elements:

                title = title_element.find("a").get("title")
                url = title_element.find("a").get("href")
                g_count = a.analyze(title)
                words = list(g_count)
                for word in words:
                    word = word[0]
                content = title + '\n' + url + '\n\n'
                for word in words:
                    word = word[0]
                    content = content + '#' + word + ' '

                # 赤文字追加（追加のタグ）
                additional_tags = entry3.get("1.0", "end").split()
                for additional_tag in additional_tags:
                    content = content + '#' + additional_tag + ' '

                sheet['A' + str(n)].value = content
                sheet['A'+ str(n)].alignment = openpyxl.styles.Alignment(wrapText=True)
                #print("記事" + str(n))
                #save_name.set("記事" + str(n))
                n = n + 1
                #print(content)
            print(str(m) + "ページ")
                #save_name.set(str(m) + "ページ")
            m = m + 1

            """
            k = 1
            while True:
                if os.path.isfile('出力//pet-stay' + str(k) + '.xlsx'):
                    k = k + 1
                else:
                    book.save('出力//pet-stay' + str(k) + '.xlsx')
                    break
            """

        elif v1.get() == "B":
            if m == 1:
                url = "https://orange-kid.com/"
            else:
                url = "https://orange-kid.com/page/" + str(m) + "/"
            res = requests.get(url)
            soup = BeautifulSoup(res.content, "lxml")
            title_elements = soup.find_all(class_='post-list animated fadeInUp')
            if m==53:
                k = 1
                while True:
                    if os.path.isfile('出力//orange-kid' + str(k) + '.xlsx'):
                        k = k + 1
                    else:
                        print(m)
                        book.save('出力//orange-kid' + str(k) + '.xlsx')
                        save_name.set("保存完了" + 'orange-kid' + str(k) + '.xlsx')
                        break

                break
            for title_element in title_elements:

                title = title_element.find("a").get("title")
                url = title_element.find("a").get("href")
                g_count = a.analyze(title)
                words = list(g_count)
                for word in words:
                    word = word[0]
                content = title + '\n' + url + '\n\n'
                for word in words:
                    word = word[0]
                    content = content + '#' + word + ' '

                # 赤文字追加（追加のタグ）
                additional_tags = entry3.get("1.0", "end").split()
                for additional_tag in additional_tags:
                    content = content + '#' + additional_tag + ' '

                sheet['A' + str(n)].value = content
                sheet['A' + str(n)].alignment = openpyxl.styles.Alignment(wrapText=True)
                n = n + 1
            # print(content)
            #print(str(m) + "ページ")
            #save_name.set(str(m) + "ページ")
            m = m + 1

            """
            k = 1
            while True:
                if os.path.isfile('出力//orange-kid' + str(k) + '.xlsx'):
                    k = k + 1
                else:
                    book.save('出力//orange-kid' + str(k) + '.xlsx')
                    break
            """

        elif v1.get()=="":
            save_name.set('どちらか選択してください')

#UI作成
root = tk.Tk()
root.title('タグ付けソフト')
frame1 = ttk.Frame(root, padding=16)
v1 = tk.StringVar()
v1.set("A")
radio_0=tk.Radiobutton(frame1,value="A",variable=v1,text="ペットと泊まれる宿  ")
radio_0.configure(font=("", 14, ""))
radio_0.pack(fill=tk.BOTH)
radio_1=tk.Radiobutton(frame1,value="B",variable=v1,text="ワンコとHappy life！")
radio_1.configure(font=("", 14, ""))
radio_1.pack(fill=tk.BOTH)

frame3= ttk.Frame(root, padding=16)
label3 = ttk.Label(frame3, text='追加タグ（改行またはスペースで区切り）')
#tag_str_var = StringVar()
entry3 = tk.Text(frame3, height=10,width = 80)
entry3.configure(font=("", 14, ""))
frame2 = ttk.Frame(root, padding=16)
button1 = ttk.Button(
    frame2,
    text='OK',
    command=function)
frame4= ttk.Frame(root, padding=16)
save_name = tk.StringVar()
entry4 = ttk.Entry(frame4, textvariable=save_name, width = 30)

frame1.pack(side=tk.TOP, anchor=tk.NW)
frame3.pack(side=tk.TOP, anchor=tk.NW)
frame2.pack(side=tk.TOP, anchor=tk.NW)
frame4.pack(side=tk.TOP, anchor=tk.NW)

label3.pack(fill=tk.X)
entry3.pack(fill=tk.X)
button1.pack(fill=tk.X)
frame4.pack(side=tk.TOP, anchor=tk.NW)

# ウィンドウの表示開始
root.mainloop()