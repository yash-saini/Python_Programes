def func(adm_no):
    l={};count=0;k=False
    import pickle
    file=open('C:\Users\Yash\Desktop\student12.dat','rb')
    try:
        while 1:
            d=pickle.load(file)
            if d.has_key(adm_no)==True:
                print d[adm_no],'-is t be deleted'
                del d[adm_no]
                k=True
            l[count]=d
            count+=1
       
    except:
        if k==False:
            print 'not found'
        else:
            print 'DONE'
        file.close()
    file=open('C:\Users\Yash\Desktop\student12.dat','wb')
    for i in l:
        pickle.dump(l[i],file)
    file.close()
    x=input('enter 1 for viewing written file 2=exit')
    if x==1:
        file=open('C:\Users\Yash\Desktop\student12.dat','rb')
        while 1:
            try:
                d=pickle.load(file)
                print d
            except:
                print '****'
                break
def main():
    adm_no=input('enter the adm no. of the student:-')
    func(adm_no)
    
            
