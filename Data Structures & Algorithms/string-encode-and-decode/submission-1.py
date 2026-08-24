class Solution:

    def encode(self, strs: List[str]) -> str:
        separator = "%"
        final_string = ""

        for s in strs:
            final_string += str(len(s)) + separator + s
        
        return final_string
            

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "%":
                j+=1
            str_length = int(s[i:j])
            i = j+1
            string = s[i: i + str_length]
            results.append(string)
            i += str_length
        
        return results

        
        
