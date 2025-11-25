#O(n)
#most_common(k):O(m log m)
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)                   # 統計每個數出現的次數 (hashmap)
        top_k_pairs = counts.most_common(k)         # 取得前 k 個 (num, count) 的 tuple
        return [num for num, cnt in top_k_pairs]       # 將每個 tuple(num, cnt) 的第一個元素（數字）抽出來，回傳題目要求的格式 List[int]
