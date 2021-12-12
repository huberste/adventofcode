#!/usr/bin/env python3

f = open('input', 'r')
lines = []
line = f.readline()
numbers = list(map(int, line.rstrip().split(",")))

boards = [] # first dimension: board num. second dimension: row. third dimension: column
line = f.readline()
line = f.readline()
board = []
while line:
    if line.rstrip() == "":
        boards.append(board)
        board = []
    else:
        board.append(list(map(int, line.rstrip().split())))
    line = f.readline()

marked = [ [ [0 for col in range(5) ] for row in range(5) ] for board in range(len(boards))] # first dimension: board num. second dimension: row. third dimension: column

winners = []
scores = []
for number in numbers:
    # mark boards
    for board in range(len(boards)):
        if board in winners:
            continue
        won = 0
        #print("board", board)
        for row in range(len(boards[board])):
            for col in range(len(boards[board][row])):
                if boards[board][row][col] == number:
                    marked[board][row][col] = 1
                    # check winners
                    # check col
                    for check_col in range(len(boards[board][row])):
                        if not (marked[board][row][check_col] == 1):
                            break
                        elif check_col == len(boards[board][row]) -1:
                            winners.append(board)
                            print("bingo!")
                            won = 1
                    # check row
                    for check_row in range(len(boards[board])):
                        if not (marked[board][check_row][col] == 1):
                            break
                        elif check_row == len(boards[board]) -1:
                            winners.append(board)
                            print("bingo!")
                            won = 1
                if won == 1:
                    break
            if won == 1:
                break
        # calculate score:
        if won == 1:
            score = 0
            for row in range(len(boards[board])):
                for col in range(len(boards[board][row])):
                    if (marked[board][row][col] == 0):
                        score += boards[board][row][col]
            score = score * number
            scores.append(score)

print("first winner:", winners[0], "score:", scores[0])
print("last winner:", winners[-1], "score:", scores[-1])
#print(winners)
