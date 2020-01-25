class queues():
    def __init__(self):
        self.f=-1;self.r=-1;self.l=[0 for i in range(10)]
        self.choice()
    def choice(self):
        while 1:
            n=input('1=continue 2= exit')
            if n==1:
                x=input('1=insertion 2=deletion')
                if x==1:
                    data=input('enter the data')
                    
                    self.insertion(data)
                elif x==2:
                    self.deletion()
            else:
                break
    def insertion(self,data):
    
            if self.f==self.r==-1:
                self.f+=1;self.r+=1
            else:
                self.r+=1
            self.l[self.r]=data
            print self.l
    def deletion(self):
        if self.f==-1:
            print 'underflow'
        else:
            del self.l[self.f]
            self.f+=1
        print self.l
def main():
    c=queues()
    
        
        
    
