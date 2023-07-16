def binary_search(arr, target):
    arr.sort()
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if arr[midpoint] == target:
            print(f"found the target at: {arr.index(target)}")
            break
        elif arr[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

if __name__ == "__main__":
    arr = [5,2,1,3,7]
    binary_search(arr, 5)
