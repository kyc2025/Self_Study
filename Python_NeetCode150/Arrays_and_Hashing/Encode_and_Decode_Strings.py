class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0      # the s position when decoding
        while i <len(s):
            j=i
            while s[j] != "#":  #it means s[i:j]="4" 
                j+=1
            length = int(s[i:j])   ## length of the next string
        ## the actual string starts after '#'
            word = s[j+1:j+1+length]
            res.append(word)
            i = j + 1 +length
        ##move index to next segment

        #encoded = s.encode(["neet", "code", "love", "you"])
        #"4#neet4#code4#love3#you"