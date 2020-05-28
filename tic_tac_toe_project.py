from graphics import *
from tkinter import messagebox
import math
w=0

while True:
    p1=input("Player 1 , Naughts or Crosses (n/c)").lower()
    if p1=="n":
        p1,p2="O ","* "
        sym={1:"O ",2:"* "}
        
        playno=0
        break
    elif p1=="c":
        p1,p2="* ","O "
        sym={2:"O ",1:"* "}
        
        playno=1
        break
    else:
        print("Please enter a valid argument")
        
cs=0
row1=["|00|","|01|","|02|"]
row2=["|10|","|11|","|12|"]
row3=["|20|","|21|","|22|"]

var={0:row1,1:row2,2:row3}

win=GraphWin("Tic Tac Toe",300,350)
for i in range(100,400,100):
    l=Line(Point(i,0),Point(i,300))
    l.draw(win)
for i in range(100,400,100):
    l=Line(Point(0,i),Point(300,i))
    l.draw(win)
tex=Text(Point(150,325),"Player 1 your chance")
tex.draw(win)
while True and cs<9 :
	
    if cs%2==0:
        play=1
    else:
        play=2
    
    tex.setText("Player "+str(play)+" your chance")
    tex.setStyle('bold')
    
    p1=win.getMouse()
    x,y=p1.getX(),p1.getY()
    
    x,y=int(math.floor(x/100))*100,int(math.floor(y/100))*100

    list_index,list_no=int(x/100),int(y/100)
    if list_no>2 or list_index>2:
        print("Click a valid square")
    elif list_no<=2 and list_index<=2:
        if var[list_no][list_index]!="|O |" and var[list_no][list_index]!="|* |":
            var[list_no][list_index]=("|"+sym[play]+"|")
            
            cs+=1
            
            if playno%2==1:
                l1=Line(Point(x+10,y+10),Point(x+90,y+90))
                l1.draw(win)
                l2=Line(Point(x+90,y+10),Point(x+10,y+90))
                l2.draw(win)
            if playno%2==0:
                cir=Circle(Point(x+50,y+50),40)
                cir.draw(win)
            playno+=1
        else:
            messagebox.showerror("Error", "Please click on a valid square")
    
    ##to check whether any lines horizontally
        
    if (row1[0]==row1[1]==row1[2]) or (row2[0]==row2[1]==row2[2]) or (row3[0]==row3[1]==row3[2]):
        messagebox.showinfo("Information","Game Over! Player "+str(play)+" won")
        w=1
        break
    ## check lines vertically
    elif (row1[0]==row2[0]==row3[0]) or (row1[1]==row2[1]==row3[1]) or (row1[2]==row2[2]==row3[2]):
        messagebox.showinfo("Information","Game Over! Player "+str(play)+" won")
        w=1
        break
    ## check lines diagonally
    elif (row1[0]==row2[1]==row3[2]) or (row1[2]==row2[1]==row3[0]):
        messagebox.showinfo("Information","Game Over! Player "+str(play)+" won")
        w=1
        break
    if cs>=9 or w==1:
        break
if cs==9 and w!=1:
    messagebox.showinfo("Information","Game Over! It's a tie!")



