class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(2):
            for j in nums:
                output.append(j)
        return output