import random

domino = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],
          [1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],
          [2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],
          [3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
pc = []
user = []

for i in range(0,7):

    user.append(random.choice(domino))
    domino.remove(user[-1])
    pc.append(random.choice(domino))
    domino.remove(pc[-1])


for i in range(6,-1,-1):
    
    if [i,i] in user:
        snake = [i,i]
        user.remove(snake)
        print(f"Stock pieces: {domino}")
        print(f"Computer pieces: {pc}")
        print(f"player pieces: {user}")        
        print(f"Domino snake: {[snake]}")
        print("Status: player")
        break
    if [i,i] in pc:
        snake = [i,i]
        pc.remove(snake)
        print(f"Stock pieces: {domino}")
        print(f"Computer pieces: {pc}")
        print(f"player pieces: {user}")        
        print(f"Domino snake: {[snake]}")
        print("Status: computer")
        break


