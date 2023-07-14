def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if arr[midpoint] == target:
            print(f"found at {target} !!")
            break
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

arr = [1,2,3,4,5,6,7,8,9,10]   


if __name__ == "__main__":
    binary_search(arr, 9)    