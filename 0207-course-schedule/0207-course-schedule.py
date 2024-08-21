# There are a total of numCourses courses you have to take
# You have to take numCourses

# labeled from 0 to numCourses - 1
# courses are labeled from 0 to numCourses - 1

#  You are given an array prerequisites 
#  There is an array of prerequisites

#  where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

#  [ai, bi] or [course, prereq]

# Return true if you can finish all courses. Otherwise, return false

# Turn the prereqs into a graph and check if there are any cycles

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_dict = {i: [] for i in range(numCourses)}

        for prereq in prerequisites:
                prereqs_dict[prereq[0]].append(prereq[1])

        visited = [0] * numCourses

        def hasCycle(i):
            if visited[i] == 1:
                return True
            if visited[i] == 2:
                return False

            visited[i] = 1

            for prereq in prereqs_dict[i]:
                if hasCycle(prereq):
                    return True

            visited[i] = 2

            return False


        for i in range(numCourses):
            if hasCycle(i):
                return False

        return True 