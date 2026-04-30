class Solution:

    def encode(self, strs: List[str]) -> str:
        return strs.concat("--")

    def decode(self, s: str) -> List[str]:
        return s.split("--")