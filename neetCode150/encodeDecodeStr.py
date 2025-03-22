class Solution:

    def encode(self, strs: List[str]) -> str:
        toReturn = ""
        for s in strs:
            toReturn += f"{(len(s) + 3):03d}" + s
        return toReturn

    def decode(self, s: str) -> List[str]:
        out_list = []
        i = 0
        while i < len(s):
            num_chars = int(s[i:i+3])
            out_list.append(s[i+3: i+num_chars])
            i += num_chars
        return out_list




