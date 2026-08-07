class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ''

        for s in strs:
            encodedString += f"#{len(s)}#{s}"

        return encodedString

    def decode(self, s: str) -> List[str]:
        print(s)
        
        result = []

        i = 0

        while i < len(s):
            number = ''
            
            if s[i] == '#':
                i += 1

                while s[i] != '#':
                    number += s[i]
                    i += 1
                        
                result.append(s[i+1:i+1+int(number)])

            i += int(number) + 1

        return result
            

        
