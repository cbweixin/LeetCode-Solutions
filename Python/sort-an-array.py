# Time:  O(nlogn)
# Space: O(n)

# merge sort solution
class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSort(start, end, lower, upper, nums):
            if end - start <= 1:
                return
            mid = start + (end - start) / 2
            mergeSort(start, mid, lower, upper, nums)
            mergeSort(mid, end, lower, upper, nums)
            r = mid
            tmp = []
            for i in xrange(start, mid):
                while r < end and nums[r] < nums[i]:
                    tmp.append(nums[r])
                    r += 1
                tmp.append(nums[i])
            nums[start:start+len(tmp)] = tmp

        mergeSort(0, len(nums), float("-inf"), float("inf"), nums)
        return nums


# Time:  O(nlogn), on average
# Space: O(logn), on average
import random
# quick sort solution
class Solution2(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def kthElement(nums, left, mid, right, compare):
            def PartitionAroundPivot(left, right, pivot_idx, nums, compare):
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in xrange(left, right):
                    if compare(nums[i], nums[right]):
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1

                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            right -= 1
            while left <= right:
                pivot_idx = random.randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums, compare)
                if new_pivot_idx == mid - 1:
                    return
                elif new_pivot_idx > mid - 1:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < mid - 1.
                    left = new_pivot_idx + 1
                    
        def quickSort(start, mid, end, nums):
            if end - start <= 1:
                return
            kthElement(nums, start, mid, end, lambda a, b: a < b)
            mid = start + (end - start) / 2
            quickSort(start, start + (mid - start) / 2, mid, nums)
            quickSort(mid, mid + (end - mid) / 2, end, nums)

        quickSort(0, len(nums) / 2, len(nums), nums)
        return nums