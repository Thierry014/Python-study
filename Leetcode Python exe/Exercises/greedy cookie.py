# https://leetcode.com/problems/assign-cookies/


def findContentChildren(g, s) -> int:
        s.sort()
        g.sort()
        
        happy,child = 0,0
        
        
        for cookie in s:
            if child == len(g):
                break
            elif cookie >= g[child]:
                happy += 1
                child += 1
        return happy

print(findContentChildren([1,2],[1,2,3]))


# break 会直接跳出for loop 执行return
# https://www.programiz.com/python-programming/break-continue