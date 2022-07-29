def canFinishbBFS_1(self, numCourses, prerequisites):
        indegree = collections.defaultdict(int)
        adj_list = collections.defaultdict(list)

        for pre in prerequisites:
            indegree[pre[0]] += 1
            adj_list[pre[1]].append(pre[0])

        starts, visited = [i for i in range(numCourses) if not indegree[i]], set()

        while starts:
            node = starts.pop()

            if node in visited:
                continue
            visited.add(node)

            for neigh in adj_list[node]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    starts.append(neigh)
                    
        return len(visited) == numCourses 