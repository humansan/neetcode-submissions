class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # cycle detection in directed graph

        # start a dfs on the course, check that each of the dependencies are valid
        # when dependency is marked as valid (meaning there are no downstream cycles)
        # at the end you want every course to be marked as valid

        # to check for cycles in the dfs, when you start a dfs on a node, mark it as currently being checked, if any node that is currently being checked is revisited, then there's a cycle
        # if you can exit the dfs with no downstream node having a cycle, then that node (and all of the downstream nodes) have no cycle

        # initially all the nodes are unvisited

        # 0, 1, 2 are states for unvisited, visiting, and completed checking
        # if a node is completed checking, then we don't have to check it in the future
        # suppose 2 courses have the same prereq, when one of those courses are checked, that prereq is also checked, so the 2nd time, we don't have to run dfs again

        # adjacency list

        adj_list = defaultdict(list)
        for a, b in prerequisites:
            # edges to be from course -> prereq (so that we check prereqs in dfs)
            adj_list[a].append(b)

        states = [0] * numCourses

        # we have to build the actual order of courses
        # whenever a course is checked, and it becomes visited, we add it to the order
        output = []
        
        def dfs(course):
            if states[course] == 2:
                return True
            if states[course] == 1:
                return False
            
            states[course] = 1
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            
            # if all prereqs are valid
            states[course] = 2
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return output

