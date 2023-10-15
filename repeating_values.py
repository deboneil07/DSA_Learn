def repeating_values(arr, n):
    s = set()  # a set which stores normal non-repeating values
    duplicate = set() # a set which stores duplicate values
    

    for num in arr: # starting a loop for each and every values in the array
        if num in s:   # checking if that value in array is in the 's' named set
            duplicate.add(num) # if that value is already there then we add it to 'duplicate' set
        else:
            s.add(num) # or else we add that value in array to set 's'

    result = sorted(list(duplicate)) # storing those duplicate values of the set in a list and sorting them

    if not result: # if theres no values in duplicate list 
        result = [-1] # we return -1 in a list
    return result  # or else we return the duplicate values in a list

if __name__ == "__main__":
    arr = [1,2,3]
    n = len(arr)


    x = repeating_values(arr, n)
    print(x)

    

  
