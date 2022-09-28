# linear search
def linear(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return-1
array=[8,6,2,5]
x=2
n=len(array)
result=linear(array,n,x)

if (result==-1):
    print("Element not found")
else:
    print("Element found at index :- ",result)
    