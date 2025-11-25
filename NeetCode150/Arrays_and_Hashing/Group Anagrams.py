#Bruce break
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []  # 建立一個空的 list，用來存放每個 anagram 群組（每個群組本身也是一個 list）
                     # 最終結果，例如 [["eat","tea","ate"], ["tan","nat"], ["bat"]]
                     # 用list儲存群組, 每個元素都是一個list (group)
        for s in strs:                     # 逐一處理輸入陣列中的每個字串
            placed = False            # 標記這個字串是否已被歸類
            for group in res:         # 逐一檢查 res 中已存在的群組（每個 group 是一個 list）
                if sorted(s) == sorted(group[0]):  # 如果跟群組第一個字串字母組成相同
                    group.append(s)                # 加入該群組
                    placed = True
                    break
            if not placed:             # 如果沒有找到可放的群組，則建立一個新群組 [s] 並加入 res。
                res.append([s])

        return res


#O(n)
from collections import defaultdict #當你用不存在的 key 去取值時，會自動建立一個空的 list 當作該 key 的 value，
                                                         #省去你先檢查 if key not in dict 的步驟。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)  
        #建立一個空的 hash map（字典），型態：defaultdict(list) 意味著 ans 的每個 value 預設都是一個 list
        # key → 分組的「指紋」（identifier），value → 該組所有原始字串的 list。
        # ans 的結構像 { key1: [str1, str2], key2: [str3], ... }
        for s in strs:
            key =  ' '.join(sorted(s)) # ' '.join(['a', 'e', 't']) → "a e t"加到key
            ans[key].append(s)        #把原始字串 s 加入 ans 字典中對應 key 的那個 list。
        return list(ans.values())      #ans.values() 就是 dict_values([["eat","tea","ate"], ["tan","nat"], ["bat"]])
                                                  #題目要求回傳 List[List[str]]




