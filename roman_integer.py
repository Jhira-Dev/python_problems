class Solution:
    def romanToInt(self, s: str) -> int:
        currentNum=0
        twoCombo=""

        dict = {"I": 1,"V":5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        for i in s:
            
            twoCombo=twoCombo+i
            while len(twoCombo) >= 2:
                
                if twoCombo == "IV" or twoCombo == "IX":
                    currentNum = currentNum - 2
                
                elif twoCombo == "XL" or twoCombo == "XC":
                    currentNum = currentNum - 20
                    
                elif twoCombo == "CD" or twoCombo == "CM":
                    currentNum = currentNum - 200
                    
                twoCombo = twoCombo[1:]
                
            currentLetter=dict[i]
            currentNum = currentNum + currentLetter

        return currentNum