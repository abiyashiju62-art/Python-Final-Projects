player1_score = 0 #Tracks player1's total wins
player2_score = 0 #Tracks player2's total wins
draw_count =0 #tracks the total no.of draws

winning_combination = [
   [0, 1, 2],   #store all possible winning combinations
   [3, 4, 5],
   [6, 7, 8],
   [0, 3, 6],
   [1, 4, 7],
   [2, 5, 8],
   [0, 4, 8],
   [6, 4, 2]
    ]
print("Welcome To Tic-Tac-Toe Game!")
input("Press Enter to Play")

def reset_board(): #resets the gaming borad to its original state
 cell =[1,2,3,4,5,6,7,8,9]
 return cell

def play_game(): #handles one complete round of the game
  global player1_score, player2_score, draw_count
  cell = reset_board() 
  mark = input("\nwho wants to play as X?\n1.Player 1\n2.Player 2\nEnter your choice: ").strip() #let players choose who play as x
  while mark!="1" and mark!="2":
    print("Enter either 1 or 2 to choose!")
    mark = input("who wants to play as X?\n1.Player 1\n2.Player 2\nEnter your choice: ").strip()
  if mark == "1":
      player1_mark = "X" 
      player2_mark = "O"
  elif mark == "2":
     player1_mark = "O" 
     player2_mark ="X"
  print("Player 1:", player1_mark)
  print("Player 2:", player2_mark)

  vaild_move = True #controls the main game loop
  while vaild_move :
  
   vaild_move1 = True #Handles player1's turn
   while vaild_move1:

    try: #handles non-numeric input
     position1 = int(input("\nEnter the position for player1:"))
     if position1 > 9 or position1 <1:
      print("Invaild input! Please enter a number between 1 and 9")
      continue
    except ValueError:
     print("Invaild input! Please enter a number")
     continue
    if cell[position1-1] == position1: #places player 1's mark on the borad
     cell[position1-1] = player1_mark
     vaild_move1 = False
    else:
     print("Position already occupied,Try again!")
  
   print(cell[0],"|",cell[1],"|",cell[2]) #displays the game borad
   print("--+--+--")
   print(cell[3],"|",cell[4],"|",cell[5])
   print("--+--+--")
   print(cell[6],"|",cell[7],"|",cell[8])

   winner = None  
   for i in winning_combination: #check whether the board is full
    if cell[i[0]] ==cell[i[1]] == cell[i[2]]:
     winner = cell[i[0]]
   if winner != None:
    print("\nWinner",winner)
    if winner == player1_mark:
     player1_score +=1
    elif winner == player2_mark:
     player2_score +=1  
    break #exits the loop
   
   count = 0   #check wheather the board is full
   for i in cell:
    if type(i)!= int:
     count +=1
   if count == 9 :
    print("\nDraw")
    draw_count +=1
    break

   vaild_move2 = True #handles player2's turn
   while vaild_move2:

    try: #handles non-numeric input
     position2 = int(input("\nEnter the position for player2:"))
     if position2 >9 or position2 <1 :
      print("Invaild input! Please enter a number between 1 and 9")
      continue
    except ValueError:
     print("Invaild input! Please enter a number")
     continue
    if cell[position2-1] == position2: #places player 2's mark on the board
      cell[position2-1] = player2_mark
      vaild_move2 = False
    else:
     print("Position already occupied,Try again!",position2)

   print(cell[0],"|",cell[1],"|",cell[2]) #diaplay the game borad
   print("--+--+--")
   print(cell[3],"|",cell[4],"|",cell[5])
   print("--+--+--")
   print(cell[6],"|",cell[7],"|",cell[8])

   winner = None
   for i in winning_combination: #checks foe a winning combination
    if cell[i[0]] ==cell[i[1]] == cell[i[2]]:
      winner = cell[i[0]]
   if winner != None:
    print("\nWinner:",winner)
    if winner == player1_mark:
      player1_score +=1
    elif winner == player2_mark:
      player2_score +=1 
    break #exit  the loop
   
   count = 0 #checks whether the borad is full
   for i in cell:
    if type(i)!= int:
     count +=1
   if count == 9 :
    print("\nDraw")
    draw_count +=1
    break
   
  print("\nplayer 1 score:",player1_score) 
  print("player 2 score:",player2_score)
  print("Number of draws:",draw_count)
  
play_game()

play_again = True
while play_again: #handles replaying the game
 choice = input("\nDo you want to play again? (Yes/No)").strip().upper()
 while choice!= "YES" and choice!="NO":
  print("Enter either 'Yes' or 'No'")
  choice =input("Do you want to play again? (Yes/No)").strip().upper()
 if choice == "YES":
  play_game()
 else:
  print("\nThank you for playing Tic-Tac_Toe!")
  play_again = False #ends the replay loop
