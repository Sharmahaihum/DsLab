def merge(list):
    if len(list)>1:
        mid=len(list)//2
        left=list[:mid]
        right=list[mid:]
        merge(left)
        merge(right)
        i=0
        j=0
        k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            list[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            list[k]=right[j]
            j=j+1
            k=k+1

list=[]
limit=int(input("Enter size of list"))
for i in range (limit):
        a=input()
        list.append(a)
print("before sorting:",list)
merge(list)
print("After sorting ",list)



# This Code is Made by Shashwat Sharma
