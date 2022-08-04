class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
    g = defaultdict(list)
    for flight in flights:
        g[flight[0]].append((flight[2],flight[1]))

    q, seen, mins = [(0,src,())], set(), {src: 0}
    stops = 0
    while q:
        (cost,v1,path) = heappop(q)
        stops += 1
        if 
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == dst and stops <= k: 
                return cost
            else if stops > k:
                return -1
            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return -1