from distutils import command
from tkinter import *

def yaz(x):
    s = len(giris.get())
    giris.insert(s,str(x))
    #print(x)

hesap = 5
s1 = 0

def işaretler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0,'end')

s2 = 0
def hesapla():
    global s2
    s2 = float(giris.get())
    print(s2)
    global hesap
    sonuç = 0
    if (hesap == 0): sonuç = s1 + s2 
    elif (hesap == 1): sonuç = s1 - s2
    elif (hesap == 2): sonuç = s1 * s2
    elif (hesap == 3): sonuç = s1 / s2
    giris.delete(0, 'end')
    giris.insert(0, str(sonuç))

pencere = Tk()
pencere.geometry("250x300")

giris = Entry(font="Verdana 14 bold", width=15 , justify=RIGHT)
giris.place(x=20 , y=20)

b = []
for i in range(1,10):
    b.append(Button(text=str(i), font="Verdana 14 bold", command=lambda x=i:yaz(x)))

sayaç = 0

for i in range(0,3):
    for j in range(0,3):
        b[sayaç].place(x=20+j*50, y=50+i*50)
        sayaç += 1

işlem = []
for i in range(0,4):
    işlem.append(Button(font="Verdana 14 bold", width=2, command=lambda x=i:işaretler(x)))

işlem[0]['text'] = "+"
işlem[1]['text'] = "-"
işlem[2]['text'] = "*"
işlem[3]['text'] = "/"


for i in range(0,4):
    işlem[i].place(x=170, y=50+50*i)

sb = Button(text="0", font="Verdana 14 bold", command=lambda x=0:yaz(x))
sb.place(x=20, y=200)

nb = Button(text=".", font="Verdana 14 bold", width=2, command=lambda x=".":yaz(x))
nb.place(x=70, y=200)

eb = Button(text="=", fg= "Blue" ,font="Verdana 14 bold", command=hesapla)
eb.place(x=120, y=200)


pencere.mainloop()