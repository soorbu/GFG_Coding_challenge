class Solution:
    """
    Rotate array function first checks whether d > len(arr). this situtaion is handled by using d%N since array is circular.
    In following example 9 % 4 = 1. Therefore only one rotation happened.

    If d = 0 then no need of rotation, return the array as it is.


    Logic : Rotating d number of times means shifting first d element to the back of the array without changing their order. Therefore, we
    Reverse first d elements of array. Then reverse N-d elements of array. And finally reverse entire array. 

    Why this works? Say arr is divided into [A.B] where A is first d elements and B is set of N-d elements 
    then step 1: reverse A. -> arr = [A'.B]
    step 2: reverse B -> arr = [A'.B']
    step 3: reverse arr -> arr = [A'.B']' = [B".A"] = [B.A]

    Reversing the segements of array can be achieved by using swapping technique. this is handled by reverseArraySegment function. 
    """
    def reverseArraySegment(self, arr,start,end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start = start+1
            end = end -1
            
    def rotateArr(self, arr, d):
        d = d % len(arr)
        if d != 0:
            self.reverseArraySegment(arr,0,d-1)
            self.reverseArraySegment(arr,d,len(arr)-1)
            self.reverseArraySegment(arr,0,len(arr)-1)
        return arr
    
test = Solution()
d = 9
arr = [1,2,3,4]
result = test.rotateArr(arr,d)
print(result)