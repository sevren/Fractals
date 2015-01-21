from Tkinter import Tk, Canvas, PhotoImage, mainloop
from math import sqrt

root=Tk()
root.protocol("WM_DELETE_WINDOW", root.quit())
canvas=Canvas(root,width=640,height=480)
canvas.pack()

WIDTH=640;
HEIGHT=480;

class TComplex:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;

        
z = TComplex(0.0,0.0);
oldz=TComplex(0.0,0.0); 
C =TComplex(-2,-1.1);
square=TComplex(0.0,0.0);
counter=0;
magnitude=0.0;


for x in range (WIDTH):
    C.a=-2+(x*0.00625);
    for y in range (HEIGHT):
       oldz.a = 0 
       oldz.b = 0 
       C.b = -1.5 + (y * 0.00625) 
       counter = 0 
       while True:
            square.a = (oldz.a * oldz.a) - oldz.b * oldz.b 
            square.b = (2 * oldz.a * oldz.b) 

            z.a = square.a + C.a 
            z.b = square.b + C.b 

            oldz.a = z.a 
            oldz.b = z.b 

            magnitude = sqrt ((z.a * z.a) + (z.b * z.b)) 

            counter +=1;
            if( counter >= 255 or magnitude >= 2):
                break
	  
       if (counter >= 255):
            canvas.create_line(x, y, x+1, y, fill='black')
       else:
            canvas.create_line(x, y, x+1, y, fill='blue')
       
root.mainloop()