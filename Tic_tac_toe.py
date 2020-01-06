from  tkinter import *
from tkinter import messagebox
def quit():
    global root
    root.quit()
def congo():
    window= Tk()
    window.title("Congratulations!")
    window.mainloop()
    quit()
def callback(r,c):
    global player
    if player=="X" and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text='X',fg='blue',bg='white')
        states[r][c]="X"
        player="O"
    if player=="O" and states[r][c]==0 and stop_game==False:
        b[r][c].configure(text="O",fg="orange",bg="black")
        states[r][c]="O"
        player="X"
    check_for_winner()   

def check_for_winner():
    global stop_game
    for i in range(0,3):
        if states[i][0] ==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg="grey")
            b[i][1].configure(bg="grey")
            b[i][2].configure(bg="grey")
            stop_game=True
            congo()
            quit()
    for i in range(0,3):
        if states[0][i] ==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg="grey")
            b[1][i].configure(bg="grey")
            b[2][i].configure(bg="grey")
            stop_game=True
            congo()
            quit()

    if states[0][0]==states[1][1]==states[2][2]!=0:
            b[0][0].configure(bg="grey")
            b[1][1].configure(bg="grey")
            b[2][2].configure(bg="grey")
            stop_game=True
            congo()
            quit()

    if states[2][0]==states[1][1]==states[0][2]!=0:
            b[2][0].configure(bg="grey")
            b[1][1].configure(bg="grey")
            b[0][2].configure(bg="grey")
            stop_game=True
            congo()
            quit()
    flag=0
    for k in range(0,3):
        for m in range(0,3):
            if(states[k][m]==0):
                flag=1
                break
    if(flag==0):
        quit()



root =Tk()
root.title("tic tac toc *cid")
player="X"
stop_game=False

states=[[0,0,0],[0,0,0],[0,0,0]]
b=[[0,0,0],[0,0,0,],[0,0,0]]
for i in range(0,3):
        for j in range(0,3):
            b[i][j]=Button(font=("Arial",60),width=4,bg='powder blue',command=lambda r=i,c=j:  callback(r,c))
            b[i][j].grid(row=i,column=j)

mainloop()
