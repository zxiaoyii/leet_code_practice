class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        finder = nums[0]

        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder