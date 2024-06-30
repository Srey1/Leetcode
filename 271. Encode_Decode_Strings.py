class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            output += str(len(string)) + "#" + string
        print("Encoded: " + output)
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        count = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                count += s[i]
                i += 1
            else:
                output.append(s[i+1 : i + int(count)+1])
                i += int(count)+1
                count = ""
        return output
                