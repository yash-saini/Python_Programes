''' An array havig n integers,find the sum of the
 contiguous sub array having the smallest sum'''

#Kadane's Theorem
def sma_sum():
    l=input("Enter the list:")
    current_sum=l[0]
    min_sum=l[0]
    for i in xrange(1,len(l)):
        current_sum=min([current_sum+l[i],l[i]])
        if current_sum<min_sum:
            min_sum=current_sum
    print min_sum
sma_sum()

