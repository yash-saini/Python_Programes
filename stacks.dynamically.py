class stacks():
    def __init__(self,l=[]):
        self.l=l
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
        self.l.append(data)
        print self.l
    def pop(self):
        self.l.pop()
        print self.l
def main():
    c=input('enter the list')
    s=stacks(c)
    


        
