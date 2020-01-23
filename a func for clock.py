import Tkinter
class clock:
    '''Class calculates the time 

    requires 3 numeric values
    displays the ticking clock'''
    def __init__(self,root):
        self.l=Tkinter.Label(root,fg='blue',bg='white',font='ravi 24 bold')
        self.l.pack()
        self.hr=0
        self.m=0
        self.sec=0
        self.t=''
        self.func()
    def func(self):
        self.hr=input('enter the no. of hrs')
        self.m=input('enter the no. of minutes')
        self.sec=input('enter the no. of second')
        self.proceed()
    def proceed(self):
        if self.sec==60:
            self.m=self.m+1
            self.sec=1
        elif self.m==60:
            self.hr=self.hr+1
            self.m=1
        self.sec=self.sec+1
        self.t='%s: %s: %s'%(self.hr,self.m,self.sec)
        self.l.config(text=self.t)
        self.l.after(1000,self.proceed)
root=Tkinter.Tk()
c=clock(root)
root.mainloop()
