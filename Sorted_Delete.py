def delete(arr, n, key):
    position = binarysearch(arr, n-1, 0,  key)

    if (position == -1):
        print("Error")
        return n
    
    for i in range(position, n-1):
        arr[i] = arr[i + 1]

    return n-1

def binarysearch(arr, high, low, key):
    if (high < low):
        return -1
    mid = (high + low) // 2
    if (key == arr[mid]):
        return mid
    if (key < arr[mid]):
        return binarysearch(arr, mid-1, low, key)
    else:
        return binarysearch(arr, high, mid+1, key)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    n = len(arr)
    key = 4

    print("Before deletion:  ")
    for i in range(n):
        print(arr[i], end=' ')

    n = delete(arr, n, key)

    print("\nAfter deletion:  ")
    for i in range(n):
        print(arr[i], end=' ')