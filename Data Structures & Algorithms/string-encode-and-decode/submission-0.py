class Solution:

    def encode(self, strs: List[str]) -> str:
        return strs.join("--")

    def decode(self, s: str) -> List[str]:
        return s.split("--")