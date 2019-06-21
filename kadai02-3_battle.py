import kadai02_2_RandomizedCards

print('\nPlayer1')
player1 = kadai02_2_RandomizedCards.main()
print('\nPlayer2')
player2 = kadai02_2_RandomizedCards.main()

print()
if player1[0] < player2[0]:
    print('Player1 の勝ち！！！')
elif player1[0] > player2[0]:
    print('Player2 の勝ち！！！')
else:
    for i in range(1, len(player1)):
        if player1[i] < player2[i]:
            print('Player1 の勝ち！！！')
            break
        elif player1[i] > player2[i]:
            print('Player2 の勝ち！！！')
            break
    else:
        print('引き分け！！！')