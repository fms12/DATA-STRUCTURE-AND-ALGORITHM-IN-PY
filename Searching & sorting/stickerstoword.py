#BFS garantees the final result will be minimal. The idea is that we start from the target and apply stickers until target is empty. 
#Then we return the steps. Imagine this is a N-ary tree and at each level we try all the candidates.
#To pass all the test cases we need to apply two key optimizations
#Use a hashmap to store all the stickers. The key will be 26 letters and value will be all the stickers that contain the key. When we choose candidates, we subjectively choose stickers that contain the first letter of the target.
#For the same target, there might be multiple ways to reach. So we use a visited set to store all the visited target. If we find a target that we visited before, we can simply skip it

def minStickers(self, stickers: List[str], target: str) -> int:
    tgt = Counter(target)
    sticker_map = defaultdict(list)
    visited = set()
	
    for sticker in stickers:
        for c in set(sticker):
            sticker_map[c].append(Counter(sticker))
    
	# cnt2str is to convert a hashmap back to string in order to store in the set
    def cnt2str(counter):
        return ''.join([k * v for k, v in counter.items()])
    
    def bfs(tgt, visited):
        queue = deque([(tgt, 0)])
        while queue:
            cur, step = queue.popleft()
            if not cur: return step    
            if cnt2str(cur) in visited: continue
            visited.add(cnt2str(cur))
            k = [x for x in cur.keys()][0]      
            for st in sticker_map[k]:                         
                cur_copy = cur.copy()
                for k in cur.keys():
                    cur_copy[k] -= st[k]
                    if cur_copy[k] <= 0: del cur_copy[k]
                queue.append((cur_copy, step + 1))               
        return -1
    return bfs(tgt, visited)
