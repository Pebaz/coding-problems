"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

For example, given the following board:

[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.
"""


def find_path(board, start, end):
	bad = [
		(x, y)
		for x in range(len(board[0]))
		for y in range(len(board))
		if board[y][x] and (x, y) not in (start, end)
	]

	good = [
		(x, y)
		for x in range(len(board[0]))
		for y in range(len(board))
		if not board[y][x] and (x, y) != start
	]

	def path(board, pos, end):
		x, y = pos
		trend = (1 if end[0] - x > 0 else -1, 1 if end[1] - y > 0 else -1)

		if (x, y + trend[1]) in good:
			return (x, y + trend[1])
		elif (x + trend[0], y) in good:
			return (x + trend[0], y)

		elif (x, y - trend[1]) in good:
			return (x, y - trend[1])
		elif (x - trend[0], y) in good:
			return (x - trend[0], y)

		else:
			return None

	pos = start; count = 0

	while pos != end:
		tmp = path(board, pos, end)
		if not tmp:
			return tmp
		good.remove(tmp)
		pos = tmp
		print(pos, end)
		count += 1

	return count
	


t = True
f = False
board = [
	[f, f, f, f],
	[t, t, f, t],
	[f, f, f, f],
	[f, f, f, f]
]
#assert(find_path(board, (3, 0), (0, 0)) == 7)
print(find_path(board, (0, 3), (0, 0)))
