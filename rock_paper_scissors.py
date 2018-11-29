play = True
while play:
    player1_symbol = input("Player 1's turn (r,p,s)")
    player2_symbol = input("Player 2's turn (r,p,s)")
    if (player1_symbol == 'r') & (player2_symbol == 'p'):
        print ("Player 2 wins!")
        play = False
    elif (player1_symbol == 'p') & (player2_symbol == 's'):
        print ("Player 2 wins!")
        play = False
    elif (player1_symbol == 's') & (player2_symbol == 'r'):
        print ("Player 2 wins!")
        play = False
    elif (player2_symbol) == (player1_symbol):
        print ("Guessed the same try again!")
    else:
        print ("Player 1 wins!")
        play = False

