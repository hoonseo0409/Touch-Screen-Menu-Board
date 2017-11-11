#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from PIL import ImageTk
from PIL import Image
import Pmw
import time
import webbrowser


root = Tk()
root.resizable(0, 0)
root.geometry("800x478+0+0")

cur_time = time.ctime()
# print (cur_time[-13:-5])



Label(root, text=u"MENU", background="seashell3", font=("Helvetica", 20)).place(x=170, y=20)


def pop_pasta():
    bigpasta = Toplevel(root)
    b5 = Button(bigpasta)
    bigpasta.title("확대보기")
    bigpasta.geometry("300x210+30+80")
    img5 = Image.open("big_pasta.png")
    this_image5 = ImageTk.PhotoImage(img5)
    b5.config(image=this_image5)
    b5.image = this_image5
    b5.command = lambda: bigpasta.quit
    b5.pack()
    # bigpasta.overrideredirect(1)


def pop_steak():
    bigsteak = Toplevel(root)
    b6 = Button(bigsteak)
    bigsteak.title("확대보기")
    bigsteak.geometry("300x210+30+80")
    img6 = Image.open("big_steak.png")
    this_image6 = ImageTk.PhotoImage(img6)
    b6.config(image=this_image6)
    b6.image = this_image6
    b6.command = lambda: bigsteak.quit
    b6.pack()


def pop_pizza():
    bigpizza = Toplevel(root)
    b7 = Button(bigpizza)
    bigpizza.title("확대보기")
    bigpizza.geometry("300x210+30+80")
    img7 = Image.open("big_pizza.png")
    this_image7 = ImageTk.PhotoImage(img7)
    b7.config(image=this_image7)
    b7.image = this_image7
    b7.command = lambda: bigpizza.quit
    b7.pack()


def pop_salad():
    bigsalad = Toplevel(root)
    b8 = Button(bigsalad)
    bigsalad.title("확대보기")
    bigsalad.geometry("300x210+30+80")
    img8 = Image.open("big_salad.png")
    this_image8 = ImageTk.PhotoImage(img8)
    b8.config(image=this_image8)
    b8.image = this_image8
    b8.command = lambda: bigsalad.quit
    b8.pack()


item = []
cost = 0


def order():
    box = None
    global cost
    global cur_pasta
    if (cur_pasta != 0):
        cur_time = time.ctime()
        item.append('Pasta*' + str(cur_pasta) + ' = ' + str(7000 * cur_pasta) + '               ' + cur_time[-13:-5])
        cost = cost + 7000 * cur_pasta
    cur_pasta = 0
    for i in range(99):
        pasta_counter.decrement()
    global cur_steak
    if (cur_steak != 0):
        cur_time = time.ctime()
        item.append('steak*' + str(cur_steak) + ' = ' + str(19000 * cur_steak) + '               ' + cur_time[-13:-5])
        cost = cost + 19000 * cur_steak
    cur_steak = 0
    for i in range(99):
        steak_counter.decrement()
    global cur_pizza
    if (cur_pizza != 0):
        cur_time = time.ctime()
        item.append('pizza*' + str(cur_pizza) + ' = ' + str(25000 * cur_pizza) + '               ' + cur_time[-13:-5])
        cost = cost + 25000 * cur_pizza
    cur_pizza = 0
    for i in range(99):
        pizza_counter.decrement()
    global cur_salad
    if (cur_salad != 0):
        cur_time = time.ctime()
        item.append('salad*' + str(cur_salad) + ' = ' + str(5000 * cur_salad) + '               ' + cur_time[-13:-5])
        cost = cost + 5000 * cur_salad
    cur_salad = 0
    for i in range(99):
        salad_counter.decrement()
    box = Pmw.ScrolledListBox(root, listbox_selectmode=SINGLE, items=item, labelpos=NW, label_text='ORDER LIST',
                              listbox_height=5, vscrollmode='static', usehullsize=1, hull_width=250, hull_height=350, )
    Label(root, text='Total amount:' + str(cost) + 'KRW').place(x=550, y=400)
    box.place(x=550, y=50)


def view():
    url = 'http://afree.ca/blindpainter'
    webbrowser.open(url)


Button(root, text=u"주문하기", command=order, relief=GROOVE, borderwidth=8).place(x=300, y=400)
Button(root, text=u"주방 구경하기", command=view, relief=GROOVE, borderwidth=8).place(x=550, y=420)

###ORDER LIST scrolled list box

box = None
item = []
box = Pmw.ScrolledListBox(root, listbox_selectmode=SINGLE, items=item, labelpos=NW, label_text='ORDER LIST',
                          listbox_height=5, vscrollmode='static', usehullsize=1, hull_width=250, hull_height=350, )
box.place(x=550, y=50)

###pasta ctrl func
global cur_pasta
cur_pasta = 0


def numup_pasta():
    global cur_pasta
    cur_pasta = cur_pasta + 1
    pasta_counter.increment()
    print
    cur_pasta


def numdown_pasta():
    global cur_pasta
    if (cur_pasta > 0):
        cur_pasta = cur_pasta - 1
        pasta_counter.decrement()
        print
        cur_pasta


pasta_counter = Pmw.Counter(root, labelpos=W, label_text=' ', orient=HORIZONTAL, autorepeat=0, increment=1,
                            entry_width=2, entryfield_value=0,
                            entryfield_validate={'validator': 'integer', 'min': 0, 'max': 99})
# pasta_counter.component('uparrow').bind("<Button 1>", up_curpasta(), add="+")
# pasta_counter.component('downarrow').bind("<Button 1>", down_curpasta(), add="+")
# pasta_counter.pack(padx=5, pady=5)
pasta_counter.place(x=180, y=90)
Label(root, text='Pasta: 7,000 KRW').place(x=170, y=120)
Button(root, text='+', command=lambda: numup_pasta()).place(x=175, y=90)
Button(root, text='-', command=lambda: numdown_pasta()).place(x=230, y=90)

###steak ctrl func
global cur_steak
cur_steak = 0


def numup_steak():
    global cur_steak
    cur_steak = cur_steak + 1
    steak_counter.increment()
    print
    cur_steak


def numdown_steak():
    global cur_steak
    if (cur_steak > 0):
        cur_steak = cur_steak - 1
        steak_counter.decrement()
        print
        cur_steak


steak_counter = Pmw.Counter(root, labelpos=W, label_text=' ', orient=HORIZONTAL, autorepeat=0, increment=1,
                            entry_width=2, entryfield_value=0,
                            entryfield_validate={'validator': 'integer', 'min': 0, 'max': 99})

steak_counter.place(x=180, y=190)
Label(root, text='Steak: 19,000 KRW').place(x=170, y=220)
Button(root, text='+', command=lambda: numup_steak()).place(x=175, y=190)
Button(root, text='-', command=lambda: numdown_steak()).place(x=230, y=190)

###pizza ctrl func
global cur_pizza
cur_pizza = 0


def numup_pizza():
    global cur_pizza
    cur_pizza = cur_pizza + 1
    pizza_counter.increment()
    print
    cur_pizza


def numdown_pizza():
    global cur_pizza
    if (cur_pizza > 0):
        cur_pizza = cur_pizza - 1
        pizza_counter.decrement()
        print
        cur_pizza


pizza_counter = Pmw.Counter(root, labelpos=W, label_text=' ', orient=HORIZONTAL, autorepeat=0, increment=1,
                            entry_width=2, entryfield_value=0,
                            entryfield_validate={'validator': 'integer', 'min': 0, 'max': 99})

pizza_counter.place(x=180, y=290)
Label(root, text='Pizza: 25,000 KRW').place(x=170, y=320)
Button(root, text='+', command=lambda: numup_pizza()).place(x=175, y=290)
Button(root, text='-', command=lambda: numdown_pizza()).place(x=230, y=290)

###salad ctrl func
global cur_salad
cur_salad = 0


def numup_salad():
    global cur_salad
    cur_salad = cur_salad + 1
    salad_counter.increment()
    print
    cur_salad


def numdown_salad():
    global cur_salad
    if (cur_salad > 0):
        cur_salad = cur_salad - 1
        salad_counter.decrement()
        print
        cur_salad


salad_counter = Pmw.Counter(root, labelpos=W, label_text=' ', orient=HORIZONTAL, autorepeat=0, increment=1,
                            entry_width=2, entryfield_value=0,
                            entryfield_validate={'validator': 'integer', 'min': 0, 'max': 99})

salad_counter.place(x=180, y=390)
Label(root, text='Salad: 5,000 KRW').place(x=170, y=420)

###small picutre insert

Button(root, text='+', command=lambda: numup_salad()).place(x=175, y=390)
Button(root, text='-', command=lambda: numdown_salad()).place(x=230, y=390)

img = Image.open("small_pasta.png")
this_image1 = ImageTk.PhotoImage(img)
Button(root, image=this_image1, command=lambda: pop_pasta()).place(x=30, y=70)

img = Image.open("small_steak.png")
this_image2 = ImageTk.PhotoImage(img)
Button(root, image=this_image2, command=lambda: pop_steak()).place(x=30, y=170)

img = Image.open("small_pizza.png")
this_image3 = ImageTk.PhotoImage(img)
Button(root, image=this_image3, command=lambda: pop_pizza()).place(x=30, y=270)

img = Image.open("small_salad.png")
this_image4 = ImageTk.PhotoImage(img)
Button(root, image=this_image4, command=lambda: pop_salad()).place(x=30, y=370)

root.config(width=600, height=800, background="seashell3")

root.title(u"라즈베리 스테이크 하우스 메뉴판")
root.mainloop()