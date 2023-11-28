k_board = "qwertyuiopasdfghjkl;zxcvbnm,./"
step = {"R": -1, "L": 1}[input()]
print("".join([k_board[k_board.find(letter) + step] for letter in input()]))
