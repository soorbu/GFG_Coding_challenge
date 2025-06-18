def reverseArray(arr):
    """
    Find the mid of the array. 
    Run a for loop from index 0 to mid of the array.
    For every index swap the corresponding element from left index. 

    In the following example: 
    mid = 7-1/2 = 3
    loop runs from 0 to 3 (3 included)
    at 0 swap element at position 0 with element at index len(arr)-1-0 = 7-1-0 = 6 -> [50,20,0,30,40,20,10]
    at 1 swap arr[1] with arr[7-1-1] = arr[5] -> [50, 20, 0, 30, 40, 20, 10] 
    at 2 swap arr[2] with arr[7-1-2] = arr[4] -> [50, 20, 40, 30, 0, 20, 10] 
    at 3 swap arr[3] with arr[7-1-3] = arr[3] -> [50, 20, 40, 30, 0, 20, 10] 
    """
    mid = (len(arr)-1)//2
    for i in range(0, mid+1):
        temp = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = arr[i]
        arr[i] = temp
    return arr

arr = [10, 20, 0, 30, 40, 20, 50]
print(reverseArray(arr))


