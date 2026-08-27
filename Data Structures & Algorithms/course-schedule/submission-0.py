class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #check through all the prereq, using map
        preMap = {i:[] for i in range(numCourses)}
        visit = set()
        for x,y in prerequisites:
            preMap[x].append(y)
        
        
        
        def dfs(x):
            if x in visit:
                return False
            if preMap[x] == []:
                return True
            visit.add(x)
            for y in preMap[x]:
                if not dfs(y):
                    return False
            visit.remove(x)
            preMap[x] = []
            return True
        
        for x in range(numCourses):
            if not dfs(x):
                return False
        return True
