class List(object):
    def __init__(self,l=[],size=0):
        self.l=l;self.size=size
        self.choice()
    def choice(self):
        while 1:
            n=input('1=continue 2=exit')
            if n==1:
                x=input('1=insetion 2=deletion 3=linear 4= binary search:-')
                if x==1:
                    ele=input('enter teh element to be inserted')
                    self.pos_not_given(ele)
                elif x==2:
                    ele=input('enter teh element to be deletedd')
                    self.deletion(ele)
                elif x==3:
                    ele=input('element to be searched')
                    self.linear(ele)
                elif x==4:
                    ele=input('element to be searched')
                    self.binary(ele)
                else:
                    print 'invalid choice'
            else:
                break
                
    def pos_not_given(self,ele):
        if self.size==len(self.l):
            return -1
        else:
            i=self.size
            while self.l[i-1]>=ele or self.l[i]<=ele:
                self.l[i+1]=self.l[i]
                i=i-1
            self.l[i+1]=self.l[i]
            self.l[i]=ele
        print self.l
    def deletion(self,ele):
        for i in range(len(self.l)):
            if self.l[i]==ele:
                break
        if i==len(self.l)-1:
            self.l[-1]=0
        else:
            for  k in range(i,len(self.l)-1):
                self.l[k]=self.l[k+1]
            self.l[-1]=0

        print self.l
    def binary(self,ele):
        if self.size==len(self.l):
            print 'not'
        else:
            start=0;end=self.size
            while start<=end:
                mid=(start+end)/2
                if self.l[mid]==ele:
                    print mid
                    break
                elif self.l[mid]>ele:
                    end=mid-1
                elif self.l[mid]<ele:
                    start=mid+1
            if self.l[mid]!=ele:
                print 'not found'
    def linear(self,ele):
        found=True;i=0
        while i<=self.size and found==True:
            if self.l[i]==ele:
                found=False
                print i
            i=i+1
        if found==True:
            print 'not found'
def main():
    l=input('enter the list')
    size=input('enter the size')
    s=List(l,size)
    

                
            

            

    
        

                    
