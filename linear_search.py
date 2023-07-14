def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            print(f"found!! at {list[i]} ")
            break

list = [1,2,3,4,5,6]


if __name__ == "__main__":
    linear_search(list, 5)

