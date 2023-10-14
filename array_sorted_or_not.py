#RECURSIVE METHOD

#def arraysortedornot(arr):
#    n = len(arr) 

#    if n == 1 or n == 0 :
#        return True
#    
#    return arr[0] <= arr[1] and arraysortedornot(arr[1:])
#
#if __name__ == "__main__":
#    arr = [1,2,3,4,5,6,7]

#    if arraysortedornot(arr):
#        print('yes')
#    else:
#        print('nope')


#Another Recursive Method

#def sortedornot(arr, n):
#    if (n == 0 or n==1):
#        return True
#    return (arr[n-1] >= arr[n-2] and sortedornot(arr, n-1))
#
#
#if __name__ == "__main__":
#    arr = [1,2,3,4,5,6]
#    n = len(arr)
#    if sortedornot(arr, n):
#        print('yes')
#    else:
#        print('nope')

#Iterative Approach

def sortedornot(arr, n):
    if (n==1 or n==0):
        return True
    for i in range(1,n):
        if (arr[i-1] > arr[i]):
            return False
    return True


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]   
    n = len(arr)

    if sortedornot(arr, n):
        print('yes')
    else:
        print('nope')
