class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # 1. (0, 0) -> (x, y)
        # 2. x = abs(x), y = abs(y)
        # 3. [(-1, -1), (x+2, y+2)]
        # 4. (0, 0) ->     <- (x, y),   return step_s + step_e
        # two direction BFS
        # initial: visit, queue, step
        # while: 1, start_position in visit_end, return
        #        2, moves = [(1, 2), (2, 1,), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        #        3 add to visit
                
        x = abs(x)
        y = abs(y)
        queue_s = deque([(0, 0, 0)])
        queue_e = deque([(x, y, 0)])
        visit_s = {(0, 0): 0}
        visit_e = {(x, y): 0}
        moves = [(1, 2), (2, 1,), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
        while True:
            x_s, y_s, step_s = queue_s.popleft()
            if (x_s, y_s) in visit_e:
                return step_s + visit_e[(x_s, y_s)]
            
            x_e, y_e, step_e = queue_e.popleft()
            if (x_e, y_e) in visit_s:
                return step_e + visit_s[(x_e, y_e)]
            
            for a, b in moves:
                    
                new_posi_s = (x_s+a, y_s+b)
                if new_posi_s not in visit_s and -1 <= x_s+a <= x+2 and -1 <= y_s+b <= y+2:
                    queue_s.append((x_s+a, y_s+b, step_s+1))
                    visit_s[(x_s+a, y_s+b)] = step_s+1
                    
                new_posi_e = (x_e+a, y_e+b)
                if new_posi_e not in visit_e and -1 <= x_e+a <= x+2 and -1 <= y_e+b <= y+2:
                    queue_e.append((x_e+a, y_e+b, step_e+1))
                    visit_e[(x_e+a, y_e+b)] = step_e+1
