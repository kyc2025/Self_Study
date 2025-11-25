class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}  #用來記錄字母出現字數

        #計算s中的字母數量
        for ch in s:
            count[ch] = count.get(ch,0)+1
        #減去t中的字母數量
        for ch in t:
            count[ch] = count.get(ch,0)-1
            if count[ch] <0:
                return False

        return True