class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        timestamp, username, website = list(zip(*sorted(zip(timestamp, username, website))))
        
        user2web = defaultdict(list)
        for i in range(len(username)):
            user2web[username[i]].append(website[i])
            
        web2count = Counter()
        for user, web in user2web.items():
            web2count.update(Counter(set(combinations(web, 3))))
            
        return sorted(web2count, key = lambda x: (-web2count[x], x))[0]
