class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        window = deque() 
        res = []
        for r in range(len(nums)):
            cur = nums[r]
            #remove the numbers smaller than the cur number from the right side
            while window and nums[window[-1]] < cur:
                window.pop()
            window.append(r)
            
            #popleft all the elements that are not in the sliding window
            while window[0] < r - k + 1:
                window.popleft()
            #append the max num in the window to the res list 
            if r >= k - 1:
                res.append(nums[window[0]])
        return res
                 
            
        