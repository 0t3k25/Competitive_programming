class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        index1 = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[index1] = nums1[i]
                index1 -= 1
                i -= 1

            elif nums1[i] < nums2[j]:
                nums1[index1] = nums2[j]
                index1 -= 1
                j -= 1

            else:
                nums1[index1] = nums1[i]
                nums1[index1 - 1] = nums2[j]
                index1 -= 2
                i -= 1
                j -= 1

        while j >= 0:
            nums1[index1] = nums2[j]
            index1 -= 1
            j -= 1
