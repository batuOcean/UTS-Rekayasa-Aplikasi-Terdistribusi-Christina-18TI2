import socket
import threading

from tkinter import *
from tkinter import messagebox

window=Tk()

cell = ''
turn = True

host = '127.0.0.1' #host address
port = 52170 #port number

conn , addr = None,None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)

def create_thread (targett):
    thread = threading.Thread(target=targett)
    thread.daemon = True #daemon threads are killed automaticly when the programs exits
    thread.start()

def recieveData ():
    global cell
    global turn
    while True:
        data, addr = conn.recvfrom(1024)
        data2 = data.decode()
        dataa = data2.split('-')
        cell = dataa[0]
        update()
        if dataa[1]=='Your Turn':
            turn = True
            print("server turn = " + str (turn))

def update ():
    if cell == 'A':
        clicked1()
    elif cell == 'B':
        clicked2()
    elif cell == 'C':
        clicked3()
    elif cell == 'D':
        clicked4()
    elif cell == 'E':
        clicked5()
    elif cell == 'F':
        clicked6()
    elif cell == 'G':
        clicked7()
    elif cell == 'H':
        clicked8()
    elif cell == 'I':
        clicked9()
    else:
        print("no matching chat detected")

def waiting4connection():
    print("thread Created")
    global conn ,addr
    conn ,addr = sock.accept() #blocking method untill a connection is extabilished
    print("Client is connected")
    recieveData()

create_thread(waiting4connection)

window.title("Welcome player 1 to the game Tic-Tac-Toe")

window.geometry("400x300")

lb1 = Label(window,text="Tic-Tac-Toe Game", font=("Helvetica", "15"))
lb1.grid(row=0,column=0)
lb1 = Label(window,text="Player 1 is X", font=("Helvetica", "10"))
lb1.grid(row=1,column=0)
lb1 = Label(window,text="Player 2 is O", font=("Helvetica", "10"))
lb1.grid(row=2,column=0)

def clicked1():
    global turn
    global cell
    if turn == True and btn1["text"]==" ":
        btn1["text"]="X"
        send_data = '{}-{}'.format('A', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn1["text"]==" " and cell == 'A':
        btn1["text"]="O"
        turn = True
        check()

def clicked2():
    global turn
    global cell
    if turn == True and btn2["text"]=='':
        btn2["text"]="X"
        send_data = '{}-{}'.format('B', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn2["text"]==" " and cell == 'B':
        btn2["text"]="O"
        turn = True
        check()

def clicked3():
    global turn
    global cell
    if turn == True and btn3["text"]=='':
        btn3["text"]="X"
        send_data = '{}-{}'.format('C', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn3["text"]==" " and cell == 'C':
        btn3["text"]="O"
        turn = True
        check()

def clicked4():
    global turn
    global cell
    if turn == True and btn1["text"]=='':
        btn4["text"]="X"
        send_data = '{}-{}'.format('D', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn4["text"]==" " and cell == 'D':
        btn4["text"]="O"
        turn = True
        check()

def clicked5():
    global turn
    global cell
    if turn == True and btn1["text"]=='':
        btn5["text"]="X"
        send_data = '{}-{}'.format('E', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn5["text"]==" " and cell == 'E':
        btn5["text"]="O"
        turn = True
        check()

def clicked6():
    global turn
    global cell
    if turn == True and btn1["text"]=='':
        btn6["text"]="X"
        send_data = '{}-{}'.format('F', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn6["text"]==" " and cell == 'F':
        btn6["text"]="O"
        turn = True
        check()

def clicked7():
    global turn
    global cell
    if turn == True and btn1["text"]=='':
        btn7["text"]="X"
        send_data = '{}-{}'.format('G', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn7["text"]==" " and cell == 'G':
        btn7["text"]="O"
        turn = True
        check()

def clicked8():
    global turn
    global cell
    if turn == True and btn1["text"]=='':
        btn8["text"]="X"
        send_data = '{}-{}'.format('H', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        check()
    elif turn == False and btn8["text"]==" " and cell == 'H':
        btn8["text"]="O"
        turn = True
        check()

def clicked9():
    global turn
    global cell
    if turn == True and btn1["text"]=='':
        btn9["text"]="X"
        send_data = '{}-{}'.format('I', 'Your Turn').encode()
        conn.send(send_data)
        print(send_data)
        turn = False
        print("server turn = " + str(turn))
        check()
    elif turn == False and btn9["text"]==" " and cell == 'I':
        btn9["text"]="O"
        turn = True
        check()

flag=1
def check():
    global flag
    b1 = btn1["text"]
    b2 = btn2["text"]
    b3 = btn3["text"]
    b4 = btn4["text"]
    b5 = btn5["text"]
    b6 = btn6["text"]
    b7 = btn7["text"]
    b8 = btn8["text"]
    b9 = btn9["text"]
    flag=flag+1
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(btn1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(btn4["text"])
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(btn7["text"])
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(btn1["text"])
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(btn2["text"])
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(btn3["text"])
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(btn1["text"])
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(btn7["text"])
    if flag ==10:
        messagebox.showinfo("Tie", "Match Tied! Try Again")
        window.destroy() #is used to close program

def win(player):
    ans = "Game complete" + player + "wins";
    messagebox.showinfo("Congrats", ans)
    window.destroy() #is used to close program

#create the button for the game
btn1 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked1)
btn1.grid(column=1, row=1)
btn2 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked2)
btn2.grid(column=2, row=1)
btn3 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked3)
btn3.grid(column=3, row=1)
btn4 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked4)
btn4.grid(column=1, row=2)
btn5 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked5)
btn5.grid(column=2, row=2)
btn6 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked6)
btn6.grid(column=3, row=2)
btn7 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked7)
btn7.grid(column=1, row=3)
btn8 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked8)
btn8.grid(column=2, row=3)
btn9 = Button(window, text= " ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'),command=clicked9)
btn9.grid(column=3, row=3)


window.mainloop()