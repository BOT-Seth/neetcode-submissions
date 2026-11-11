class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for num in nums:

            frequency[num] = frequency.get(num, 0) + 1

        answer = []

        for i in range(k):
            max_key = max(frequency, key = frequency.get)
            answer.append(max_key)

            frequency[max_key] = 0

        return answer
            
