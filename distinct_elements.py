def distinct_values(arr, n):

    s = dict() #creating a hashtable

    for i in range(n):
        if (arr[i] not in s.keys()): #checking if its in the hashtable or not
            s[arr[i]]= arr[i]        # if its not there then we add the value to hashtable named 'n'
            print(arr[i], end=' ')

if __name__ == "__main__":

    arr = [1,2,3,4,5,6,6,6,7]
    n = len(arr)

    distinct_values(arr, n)    