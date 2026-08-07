class Solution:

    def encode(self, strs: List[str]) -> str:

        encodedString = ''

        for s in strs:
            encodedString += f"#{len(s)}#{s}"

        return encodedString

    def decode(self, s: str) -> List[str]:

        '''
        Solution

        - think of it as streaming tokens
        - the encoded string will look like #14#HelloHowAreYou#5#World which is #{len}#word#{len}#word
        - parser should check if the element equals # then increase counter and check it it reaches ending #
        '''
        
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
            

        
