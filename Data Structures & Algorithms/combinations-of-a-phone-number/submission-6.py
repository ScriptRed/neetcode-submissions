class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        keyToLetter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = [""]
        for d in digits:
            new = []
            for item in res:
                
                for letter in keyToLetter[d]:
                    new.append(item + letter)
            
            res = new

        return res