class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for text in strs:
            s += str(len(text)) + "&&" + text + "$$"

    def decode(self, s: str) -> List[str]:
        arr = []
        secs = s.split("$$")[::-1]
        for sec in secs:
            l, text = sec.split("&&")
            arr.append(text)
        return arr