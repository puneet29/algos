class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"\u2000{s}\u2001"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        temp_word = ""
        for char in s:
            if char == "\u2000":
                temp_word = ""
                continue
            if char == "\u2001":
                res.append(temp_word)
                continue
            temp_word += char
        return res
