class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        global _max
        _max = 0
        """
        :Helper function to explore the different strings which can be built
        :result : list[str]
        :current: str
        :lcount: The count of left parenthesis
        :maxcount: The amount of removals performed
        :s: the orignal string
        """
        def DFS(result, current, lcount, maxcount, s):
            global _max
            if(len(s) == 0):
                if(lcount == 0 and len(current) != 0):
                    if maxcount > _max:
                        _max = maxcount
                    if _max == maxcount and (current not in result):
                        result.append(current)
                return
            else:
                if s[0] == '(':#if its a left parenthesis
                    temp = list(current)
                    current.append('(')
                    DFS(result, current, lcount + 1, maxcount + 1, s[1:])#Either we use it
                    current = list(temp)
                    DFS(result, current, lcount, maxcount, s[1:])#Or we dont
                elif s[0] == ')':
                    if(lcount > 0):#if it is valid to place a right paranthesis
                        temp = list(current)
                        current.append(')')
                        DFS(result, current, lcount - 1, maxcount, s[1:])#Either we use it
                        current = list(temp)
                    DFS(result, current, lcount, maxcount, s[1:])#Or we dont
                else:#if its any other character
                    current.append(s[0])
                    DFS(result, current, lcount, maxcount, s[1:])



        result = []
        DFS(result,[],0,0,s)
        if(len(result) == 0):
            result.append([''])
        return ["".join(string) for string in result]
