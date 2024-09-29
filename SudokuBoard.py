#  Sudoku board 
import tkinter

board = [[0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]


class Cage:
    def __init__(self,sum,cells):
        self.sum = sum
        self.cells = cells

cages_ = []

# function to print the board
def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-"*21)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def is_valid(board,cages,r,c,n):
    # check row 
    for i in range(0,9):
        if n == board[r][i]:
            return False
        
    # check column 
    for i in range(0,9):
        if n == board[i][c]:
            return False
        
    # check subgrid 
    from_row = (r//3)*3
    from_column = (c//3)*3

    for i in range(from_row, from_row+3):
        for j in range(from_column, from_column+3):
            if n==board[i][j]:
                return False
    
    # check cage 
    cage = Cage(0,[])
    for i in cages:
        for cell in i.cells:
            if all(x == y for x, y in zip(cell, [r,c])):
                cage = i

    board[r][c] = n
    sum = 0
    cage_filled = True
    for cell in cage.cells:
        if 0 != board[cell[0]][cell[1]]:
            sum += board[cell[0]][cell[1]]
        else:
            cage_filled = False
    if cage_filled and sum!=cage.sum:
        board[r][c] = 0
        return False
    board[r][c] = 0
    return True

def solve(board,cages,r=0,c=0):
    if r == 9:
        return True
    elif c == 9:
        return solve(board,cages,r+1,0)
    elif board[r][c] != 0:
        return solve(board,cages, r,c+1)
    else:
        for i in range(1,10):
            if is_valid(board,cages,r,c,i):
                board[r][c] = i
                if solve(board,cages,r,c+1):
                    return True
                board[r][c] = 0
        return False
    
def print_cages():
    print("Cages: ")
    for cage in cages_:
        print("Sum: ", cage.sum)
        for cell in cage.cells:
            print(cell)

m = tkinter.Tk()
m.title("Sudoku Solver")
# 9x9 grid of buttons, when clicked, the button says X and its coordinates appended to a list
selected_buttons = []


def button_click(row, col):
    if [row, col] in selected_buttons:
        selected_buttons.remove([row, col])
        buttons[row][col].config(text=" ")
    else:
        selected_buttons.append([row, col])
        buttons[row][col].config(text="X")

buttons = [[0 for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        buttons[i][j] = tkinter.Button(m, text=" ", width=2, height=2, command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)

# create cage
def create_cage():
    cage = Cage(int(sum_input.get()), selected_buttons[:])
    cages_.append(cage)
    for button in selected_buttons:
        buttons[button[0]][button[1]].config(text="*")
    selected_buttons.clear()


create_cage_button = tkinter.Button(m, text="Create Cage", width=2, command=create_cage)
create_cage_button.grid(row=9, column=3)

# text input for sum of selected buttons
sum_input = tkinter.Entry(m, width=2)
sum_input.grid(row=9, column=5)

    


# Run the main loop
m.mainloop()

# after exiting the GUI, print the board
solve(board,cages_)
print_board(board)