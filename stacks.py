class stack():
    def __init__(self,l=[0 for i in range(10)]):
        self.l=l;self.top=-1
        self.choice()
    def choice(self):
        while 1:
            u=input('1=continue 2=exit')
            if u==1:
                
                n=input('push=1 pop=2')
                if n==1:
                    data=input('data to be inseeted')
                    self.push(data)
                elif n==2:
                    self.pop()
                else:
                    print 'invalid input'
            else:
                break
    def push(self,data=0):
            try:
                self.top=self.top+1
                self.l[self.top]=data
                print self.l
            except:
                print 'overflow'
    def pop(self):
        if self.top==-1:
            print 'underflow'
        else:
            del self.l[self.top]
            self.top=self.top-1
        print self.l


