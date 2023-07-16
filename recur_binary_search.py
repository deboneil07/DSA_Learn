def binary_search(arr, target):  # sourcery skip: remove-unnecessary-else
    if len(arr) == 0:
        return False
    else:
        midpoint = (len(arr))//2

        if arr[midpoint] == target:
            print(f"found at {target} !!")
        elif arr[midpoint] < target:
            binary_search(arr[midpoint:], target)
        else:
            binary_search(arr[:midpoint], target)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,3]
    binary_search(arr, 7)
            
