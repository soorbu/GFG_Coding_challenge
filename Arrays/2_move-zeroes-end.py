def pushZerosToEnd(arr):
    """
    The first for loop keeps the track of all non-zero elements through count variable.
    On zero the loop proceeds with no change. But for every non-zero element the value of count is used as an index to 
    mark it to that non-zero element.
    
    In following example the first element is 10, there the if condition runs and:
    arr[count = 0] = 10; count = 1 -> arr = [10,0,20,0...]. 
    
    On first zero the if condition won't be executed. On 20 the if condition runs again:
    arr[count = 1] = 20; count = 2 -> arr = [10,20,20,0,...]
    After the for loop is executed all the zeroes of array will be converted to their correct non-zero element. 

    The second for loop will handle the zeroes at the end of array. Count variable contains the number of all non-zero elements.
    Therefore we start a loop from count (index at which first zero should come) and make all the elements after it 0. 
    """
    count = 0
    for i in range (0, len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    for j in range(count, len(arr)):
        arr[j] = 0
        
    return arr

arr = [10, 0, 20, 0, 30, 40 , 0, 50, 0]
print(pushZerosToEnd(arr))