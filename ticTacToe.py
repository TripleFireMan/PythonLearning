board = {'top-L':' ','top-M':' ','top-R':' ',
		 'mid-L':' ','mid-M':' ','mid-R':' ',
		 'bottom-L':' ','bottom-M':' ','bottom-R':' '}
def printBoard(board):
	print(board['top-L']+' | '+board['top-M']+' | '+ board['top-R'])
	print('---------')
	print(board['mid-L']+' | '+board['mid-M']+' | '+ board['mid-R'])
	print('---------')
	print(board['bottom-L']+' | '+board['bottom-M']+' | '+ board['bottom-R'])

printBoard(board)


turn = 'X'

for x in xrange(0,9):
	printBoard(board)
	print('Turn for ' + turn + '. Move to place?')
	place = raw_input()
	board[place] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

printBoard(board)
