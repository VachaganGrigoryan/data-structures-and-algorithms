
def solution(src, dest):
    
    sx, sy = src//8, src%8
    dest = dest//8, dest%8

    if (sx, sy) == dest:
        return 0

    board = [[0]*8 for _ in range(8)]
    
    direction = [(x, y) for y in (-2, -1, 1, 2) for x in (-2, -1, 1, 2) if abs(x)!=abs(y)]
              
    tmp = [(sx, sy)]

    while tmp:
        x, y = tmp.pop(0)

        for dx, dy in direction:
            nx, ny = x+dx, y+dy
            if -1 < nx < 8 and -1 < ny < 8 and board[nx][ny]==0:
                board[nx][ny] = board[x][y] + 1
                if (nx, ny) == dest:
                    return board[nx][ny]
                tmp.append((nx, ny))             
 
    return board[dest[0]][dest[1]]




# Input:
print(solution(0, 1))
# Output:
    # 3

# Input:
print(solution(10, 36))
# Output:
    # 3

# Input:
print(solution(0, 36))
# Output:
    # 3

# Input:
print(solution(19, 36))
# Output:
    # 1


print (solution(19, 36))
print (solution(0, 1))
print (solution(0, 63))
print (solution(0, 0))