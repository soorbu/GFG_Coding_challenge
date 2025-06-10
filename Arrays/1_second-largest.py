def getSecondLargest(arr):
    largest, second_largest = -1, -1
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif (arr[i] > second_largest and arr[i] != largest):
            second_largest = arr[i]
            
    return second_largest
    
arr = [10,5,10]
print(getSecondLargest(arr))