class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for text in strs:
            s += str(len(text)) + "#" + text
        return s

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        arr = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            arr.append(s[j:j+length])
            i = j + length
        return arr