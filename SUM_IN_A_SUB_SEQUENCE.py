T=int(raw_input())
s=map(int,raw_input().split())
n=s[0];sum_given=s[1]
l=map(int,raw_input().split())
sum1=0;f=2;l1=[]
for i in xrange(len(l)):
    while sum(l1)>sum_given:
            l1.pop(0)
    if sum1==sum_given:
        f=1
        print l1
        break
    
    elif sum1<sum_given:
        l1.append(l[i])
        sum1+=l[i]
    
    else:
        pass
        
            
        
        
    
        
        
    
        

