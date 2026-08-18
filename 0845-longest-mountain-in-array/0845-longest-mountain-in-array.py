class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0
        res = 0
        idx = 1
        while idx < len(arr) - 1:
            if arr[idx - 1] < arr[idx] > arr[idx + 1]:
                l = r = idx
                while l > 0 and arr[l] > arr[l - 1]:
                    l -= 1
                while r + 1 < len(arr) and arr[r] > arr[r + 1]:
                    r += 1
                res = max(res, (r - l + 1))
            idx += 1

        return res

        