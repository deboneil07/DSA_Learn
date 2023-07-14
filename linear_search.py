def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            print(f"found!! at {list[i]} ")
            break

list = [1,2,3,4,5,6]
target = 3
linear_search(list, target)
print('nice')