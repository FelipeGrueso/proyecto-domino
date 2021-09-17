import random
print("="*70)
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
    status = str()

for i in range(6,-1,-1):
    
    if [i,i] in user:
        snake = [i,i]
        user.remove(snake)
        
        print(f"Stock size: {len(domino)}")
        print(f"Computer pieces: {len(pc)}")
        print()
        print(snake)
        print()
        status = "Computer is about to make a move. Press Enter to continue..."
        

        break
    
    if [i,i] in pc:
        snake = [i,i]
        pc.remove(snake)
        print(f"Stock size: {len(domino)}")
        print(f"Computer pieces: {len(pc)}")
        print()
        print(snake)
        print()
        status = "It's your turn to make a move. Enter your command."
        break

print("Your pieces:")
n = 0
contador = 1
while n<len(user):
    print(f"{contador}:{user[n]}")
    n += 1
    contador += 1

print(f"\nStatus: {status}")


