from tkinter import *       #tkinter 라이브러리에 모든 함수를 사용하겠다.
from tkinter import simpledialog
import tkinter.ttk
import tkinter.font
import os

def btnpress():
    all_day = all(chkvar_day[i].get() == 1 for i in range(len(list_day)))
    all_week = all(chkvar_week[i].get() == 1 for i in range(len(list_week)))

    if all_day:
        result_text = "(메할일 끝!!)"
    else:
        result_text = "(아직 할 일 남았어요 ㅠ_ㅠ)"
    if all_week:
        result2_text = "(메할일 끝!!)"
    else:
        result2_text = "(아직 할 일 남았어요 ㅠ_ㅠ)"


    lb.config(text=result_text)       #레이블에 값 입력
    lb2.config(text=result2_text)

def save_status(event):
    file = open(t_path,'w')
    for i in range(len(list_day)):
        file.write("{}\n" .format(chkvar_day[i].get()))
    for i in range(len(list_week)):
        file.write("{}\n" .format(chkvar_week[i].get()))
    file.close()
    lb3.config(text="저장 완료")

def file_open (event):
    os.system("notepad {}".format(t_path))

def choose_computer():
    global num
    num = 1
    dialog_window.destroy()

def choose_laptop():
    global num
    num = 2
    dialog_window.destroy()

# 초기값 설정
num = None

# 대화 상자 생성
dialog_window = Tk()
dialog_window.withdraw()  # 창을 숨김

# 사용자로부터 값을 입력 받기
dialog_window.title("현재 이용중인 기기")
dialog_window.geometry("250x100")
Label(dialog_window, text="컴퓨터 또는 노트북을 선택하세요").pack(pady=10)
Button(dialog_window, text="컴퓨터", command=choose_computer).pack(side=LEFT, padx=30)
Button(dialog_window, text="노트북", command=choose_laptop).pack(side=RIGHT, padx=30)

# 대화 상자 실행
dialog_window.deiconify()
dialog_window.mainloop()

if num == 1:
    maple_ico = "C:/Users/rlarb/Desktop/portfolio/maple/maple.ico"
    t_path = "C:/Users/rlarb/Desktop/portfolio/maple/status.txt"
elif num == 2:
    maple_ico = "C:/Users/hobaragi/Desktop/portfolio/maple/maple.ico"
    t_path = "C:/Users/hobaragi/Desktop/portfolio/maple/status.txt"

root = Tk()                 #root 라는 창을 생성
root.iconbitmap(maple_ico)
root.geometry("300x600")    #창 크기설정
root.title("Maple To Do List") #창 제목설정
root.option_add("*Font", "맑은고딕 16") #폰트설정
root.resizable(False, False) #x,y 창 크기 변경 불가

list_day = ["심볼", "몬파", "메M", "황금마차", "할로윈_출석", "우루스", "데일리기프트"]
list_week = ["심볼", "주간보스", "수로&플래그"]

stat_list = []
with open(t_path) as f:
    for line in f:
        stat_list.append(int(line.strip()))
print ('stat is', stat_list)

enter = Label(root, text="")

chkvar_day = [IntVar() for _ in range(len(list_day))]
chkbox_day = [None] * len(list_day)

chkvar_week = [IntVar() for _ in range(len(list_week))]
chkbox_week = [None] * len(list_week)

daliy = Label(root, text="<일간>")
daliy.pack()
enter.pack()

for i in range(len(list_day)):
    chkbox_day[i] = Checkbutton(root, variable=chkvar_day[i])
    chkbox_day[i].config(text=list_day[i])
    chkbox_day[i].pack()

lb = Label(root)        #root라는 창에 레이블 생성
lb.pack()               #레이블 배치

weekly = Label(root, text="\n<주간>\n")
enter.pack()
weekly.pack()
enter.pack()

for i in range(len(list_week)):
    chkbox_week[i] = Checkbutton(root, variable=chkvar_week[i])
    chkbox_week[i].config(text=list_week[i])
    chkbox_week[i].pack()

lb2 = Label(root)        #root라는 창에 레이블 생성
lb2.pack()               #레이블 배치

btn = Button(root)      #root라는 창에 버튼 생성
btn.config(text="확인") #버튼 내용
btn.config(width=5)    #버튼 크기
btn.config(command=btnpress)    #버튼 기능(btnpree() 함수 호출)
btn.pack()              #버튼 배치

for i in range(len(list_day)):
    if stat_list[i] == 1:
        chkvar_day[i].set(1)
    else:
        chkvar_day[i].set(0)

for i in range(len(list_week)):
    if stat_list[len(list_day) + i] == 1:
        chkvar_week[i].set(1)
    else:
        chkvar_week[i].set(0)

lb3 = Label(root)
lb3.pack()

save_btn = tkinter.Label(root, text="저장", bg='grey19', fg = 'snow')
save_btn.bind('<Button-1>', save_status)
save_btn.bind('<Button-3>', file_open)
save_btn.pack()

root.mainloop()         #창 실행