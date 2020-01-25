def func():
    l=[]
    x=raw_input('enter the string')
    try:
        for i in x:
            if i=='(':
                l.append('(')
            elif i==')':
                l.pop()
        if l!=[]:
            print 'parenthesis not matched'
        else:
            print 'match successful'

    except:
        print 'parenthesis not matched'
    
def main():
    func()
