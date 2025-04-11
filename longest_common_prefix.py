class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix =""

        if not strs:
            return prefix

        prefix = strs[0]
        
        for i in strs[1:]:
            
            if not i.startswith(prefix):
                
                while not i.startswith(prefix):
                    prefix = prefix[:-1]
                    

        return prefix