def mergesort_iterative(nums):
    length = len(nums)
    if length < 2:
        print "array is already in sorted order"
        return
    step = 1
    while step < length:
        i = 0
        j = step
        while j + step <= length:
            merge(nums,i,i+step,j,j+step)
            i = j + step
            j = i + step
        if j < length:
            merge(nums,i,i+step,j,length)
        step = step*2
    print "sorted array: "
    print nums

def merge(nums,l,m,r,q):
    temp1 = []
    temp2 = []
    i,k =0,r
    while(i<len(temp2)-1):
        temp2.append(nums[k])
        k+=1
    j,p = 0,1
    while(j<len(temp1)-1):
        temp1.append(nums[p])
        p+=1
    s,x,y= l,0,0
    while(s<q):
        nums.append(min(temp2[x],temp2[y])
            
def get_input():
    a=[]
    while(1):
      x = int(raw_input())
      if(x==-1):
         break
      a.append(x)
    return a

if __name__ == '__main__':
	#get input from user
	nums = get_input()
	#sort the list
        mergesort_iterative(nums)
    

