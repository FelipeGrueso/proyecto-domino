import random
print("=" * 70)
domino = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],
          [1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],
          [2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],
          [3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
pc = []
user = []
acumuladora = 0
status = str()
turno = str()
cantidades = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(0, 7):

    user.append(random.choice(domino))
    domino.remove(user[-1])
    pc.append(random.choice(domino))
    domino.remove(pc[-1])

for i in range(6,-1,-1):
    
    if [i,i] in user:
        snake = [i,i]
        user.remove(snake)
        print(f"Stock size: {len(domino)}")
        print(f"Computer pieces: {len(pc)}")
        print()
        print(snake)
        status = "Computer is about to make a move. Press Enter to continue..."
        turno = "pc"
        snake = [snake]
        break
    
    elif [i,i] in pc:
        snake = [i,i]
        pc.remove(snake)
        print(f"Stock size: {len(domino)}")
        print(f"Computer pieces: {len(pc)}")
        print()
        print(snake)
        print()
        status = "It's your turn to make a move. Enter your command."
        turno = "user"
        snake = [snake]
        break

while 1:
 
    if turno == "user":

        try:

            print("Your pieces:")

            if len(user) == 0:
                print("\nStatus: The game is over. You won!")
                break

            if len(pc) == 0:
                print("Status: The game is over. The computer won!")
                break

            n = 0
            contador = 1
            while n<len(user):
                print(f"{contador}:{user[n]}")
                n += 1
                contador += 1

            print(f"\nStatus: {status}")
            jugada = int(input())

               
            if jugada == 0:
                user.append(random.choice(domino))
                domino.remove(user[-1])
            
            elif jugada < 0: 
                snake.insert(0,user[abs(jugada)-1])
                user.remove(user[abs(jugada)-1])

                
            elif jugada > 0:
                snake.append(user[abs(jugada)-1])
                user.remove(user[abs(jugada)-1])
                
            print("="*70)
            print(f"Stock size: {len(domino)}")
            print(f"Computer pieces: {len(pc)}")
            print()

            for h in snake:
                for i in h:
                    cantidades[i] += 1
                    if cantidades[i] == 8:
                        if snake[0][0] == snake[-1][-1]:
                            print("Status: The game is over. It's a draw!")
                            freno = i
                            break
            cantidades = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

            if len(snake) <= 6:

                for f in snake:
                    print(f, end="")
                print()
                    
            else:
                print(f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}")


            turno = "pc"
            status = "Computer is about to make a move. Press Enter to continue..."
            
        except:
            print("Invalid input. Please try again.")
            

    elif turno == "pc":
        
        try:

            print("\nYour pieces:")

            if len(pc) == 0:
                print("Status: The game is over. The computer won!")
                break
            
            if len(user) == 0:
                print("\nStatus: The game is over. You won!")
                break

            n = 0
            contador = 1
            
            while n<  len(user):
                print(f"{contador}:{user[n]}")
                n += 1
                contador += 1
            print(f"\nStatus: {status}")

            continuar = (input())
            jugada =  random.choice(range(- len(pc), len(pc) -1))
            if jugada <= 0:
                snake.insert(0, pc[abs(jugada)-1])

            elif jugada >0:
                snake.append(pc[abs(jugada)-1])
                
            pc.remove(pc[abs(jugada)-1])

            print("="*70)
            print(f"Stock size: {len(domino)}")
            print(f"Computer pieces: {len(pc)}")
            print()

            for h in snake:
                for i in h:
                    cantidades[i] += 1
                    if cantidades[i] == 8:
                        if snake[0][0] == snake[-1][-1]:
                            print("Status: The game is over. It's a draw!")
                            freno = i
                            break
                        
            cantidades = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

            if len(snake) <= 6:

                for f in snake:
                    print(f, end="")
                print()
                print()
                
            else:
                print(f"{snake[0]}{snake[1]}{snake[2]}...{snake[-3]}{snake[-2]}{snake[-1]}\n")

            turno = "user"
            status = "It's your turn to make a move. Enter your command."
            
        except Exception:
            print("Invalid input. Please try again.")
            



            
    

    
