class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for word in strs:
            final_string += f"{len(word)}#{word}"
        print(final_string)
        return final_string

    def decode(self, s: str) -> List[str]:
        list_of_strings = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            list_of_strings.append(s[j+1:j+1+length])
            i = j + 1 + length
        return list_of_strings

