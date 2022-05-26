class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        N = len(arr)
        # up
        while i + 1 < N and arr[i] < arr[i + 1]:
            i += 1

        # peak is first or last
        if i == 0 or i == N - 1:
            return False

        while i + 1 < N and arr[i] > arr[i + 1]:
            i += 1
        return i == N - 1
