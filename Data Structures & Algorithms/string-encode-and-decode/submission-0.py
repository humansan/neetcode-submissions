class Solution:

    def encode(self, strs: List[str]) -> str:
        strbuild = ""

        for string in strs:
            length = len(string)
            strbuild += f"{length:03d}{string}"
        
        return strbuild


    def decode(self, s: str) -> List[str]:

        curstring = s
        array = []

        while curstring:
            length = int(curstring[0:3])
            curstring = curstring[3:]
            string = curstring[0:length]
            curstring = curstring[length:]
            array.append(string)
        
        return array

