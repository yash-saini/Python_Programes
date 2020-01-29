def compare(a,b):
    #comparator function
    if a['value']<b['value']:
        return -1
    return 1
def buy_max_stock(n,k,a=[]):
    v=[]
    d={}
    for i in xrange(len(a)):
        d={}
        d['index']=i+1
        d['value']=a[i]
        v.append(d)
    v.sort(cmp=compare)
    ans=0
    for i in xrange(len(v)):
        if k>=v[i]['value']*v[i]['index']:
            k-=v[i]['value']*v[i]['index']
            ans+=v[i]['index']
        else:
            break
    if i<len(a):
        j=k/v[i]['value']
        ans+=j
    return ans
    
    
        
