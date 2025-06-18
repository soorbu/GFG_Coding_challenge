class Solution:
    """
    Next permutation meaning:
    If our array is [2,4,1,7,5,0] then we say our number is 241750
    we need to arrange digits of this number such that they are greater from this number. Thus our permutations will be:
    1. 245017
    2. 245071
    3. 245701
    4. 245710
    5. 247015 .... and so on. The next permutation means for our array the immediate largest combination of the digits. In following example
    it is 245017


    To find this next larger permutation we need to find the pivot, which an element from the right of array such that it is smaller than
    element which is to its right. That is from right we start with index i. So arr[i-1] < arr[i]. 
    In the given array we have  [2,4,1,7,5,0]: starting from right 5 < 0 no. 7 < 5 no. 1 < 7. yes. pivot_index = 2 and pivot = 1

    now from pivot to the right of array we find out the smallest element which is greater than pivot. This is out swap candidate. For this
    we run a loop from pivot to end of array in reverse and make the first greater element from pivot as candidate. 

    Note: the first greater element is always the candidate and we will break the loop there. Since any other elements to the left are always
    greater than their right element till pivot. 

    For our example first 0 > 1 no. 5 > 1 yes. Break. 

    Swap candidate and pivot ->  [2,4,5,7,1,0]

    Arrange all the elements after pivot_index in aescending order. [using reverseSegment] ->  [2,4,5,0,1,7]

    Condition where no pivot is found: 
        This means that the digits are already arranged in their highest possible permutation. for our exampel highest permutation will be 
        754210. That is all number are in descending order and therefore we couldn't find the pivot. In this case simply arrange all the numbers
        to aescending order -> 012457. Which will be next permutation considering circular loop of permutation table. 
    """
    def reverseSegment(self, arr, start, end):
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start = start + 1
            end = end - 1
            
    def nextPermutation(self, arr):
        n = len(arr)
        pivot_index = -1

        for i in range(n-1,0,-1):
            if (arr[i] > arr [i-1]):
                pivot_index = i-1
                pivot = arr[i-1]
                break
            
        if (pivot_index == -1):
            self.reverseSegment(arr,0, n-1)
            return arr
        
        candidate_index = -1
        for i in range (n-1,pivot_index,-1):
            if (arr[i] > pivot):
                candidate_index = i
                break
        
        arr[pivot_index], arr[candidate_index] = arr[candidate_index], arr[pivot_index]
        self.reverseSegment(arr, pivot_index+1, n-1)
        
        return arr
        
test = Solution()
arr = [2,4,1,7,5,0]
print(test.nextPermutation(arr))