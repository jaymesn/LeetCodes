class Solution(object):
    def lengthOfLongestSubstring(self, s:str ) -> [int,str]: 
        """
        :type s: str
        :rtype: int
        """
        
        largestsubstring = ""
        substring = ""
        contains:dict[str,int] = {}

        for i in range( len(s) ):
            value = contains.get(s[i])


            print(s[i],i,contains)
            if not value:
                contains[s[i]] = i 
            else:


                if(len(substring) > len(largestsubstring)):
                    largestsubstring = substring
                    contains = {}
                    substring = ""
                else:
                    0
            substring += s[i]


        return [len(largestsubstring),largestsubstring] 
        
     
solution = Solution().lengthOfLongestSubstring
examples = [
    ["abcabcbb",[3,"abc"]],
    ["bbbbb",[1,"b"]],
    ["pwwkew",[3,"wke"]]
]
for item in examples:
    print(solution(item[0]))