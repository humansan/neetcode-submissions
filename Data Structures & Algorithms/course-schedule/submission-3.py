class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        
        course_reqs = defaultdict(list)

        for a, b in prerequisites:
            course_reqs[a].append(b)
        
        course_state = [0] * numCourses

        def dfs(course):
            if course_state[course] == 1:
                return False
            
            if course_state[course] == 0:
            
                course_state[course] = 1

                for next_course in course_reqs[course]:
                    if not dfs(next_course): 
                        return False
                
                course_state[course] = 2
                
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

