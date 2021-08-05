class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        graph = defaultdict(int)
        for a, b, amount in transactions:
            graph[a] += amount
            graph[b] -= amount

        list1 = [v for k, v in graph.items() if v > 0]
        list2 = [v for k, v in graph.items() if v < 0]

        result = len(graph) + 1
        def backtracking(list1, list2, count):
            nonlocal result

            if not list1 and not list2:
                result = min(result, count)
                return

            value = list2[0]
            for i, amount in enumerate(list1):
                if amount == -value:
                    backtracking(list1[:i]+list1[i+1:], list2[1:], count+1)
                    return  # pruning

                if amount > -value:
                    list1[i] += value
                    backtracking(list1, list2[1:], count+1)
                    list1[i] -= value
                elif amount < -value:
                    list2[0] += amount
                    backtracking(list1[:i]+list1[i+1:], list2, count+1)
                    list2[0] -= amount

        backtracking(list1, list2, 0)
        return result
