#SudokuGui
import SudokuBoard
import tkinter
m = tkinter.Tk()

class Cage:
    def __init__(self,sum,cells):
        self.sum = sum
        self.cells = cells

# Set the title of the window
m.title("Sudoku Solver")
# 9x9 grid of buttons, when clicked, the button says X and its coordinates appended to a list
selected_buttons = []
cages = []

def button_click(row, col):
    selected_buttons.append([row, col])
    buttons[row][col].config(text="X")

buttons = [[0 for i in range(9)] for j in range(9)]
for i in range(9):
    for j in range(9):
        buttons[i][j] = tkinter.Button(m, text=" ", width=2, height=2, command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j)


# function to print cage
def print_cage(cage):
    print ("Sum: ", cage.sum)
    for cell in cage.cells:
        print(cell)

# create cage
def create_cage():
    cage = Cage(int(sum_input.get()), selected_buttons)
    cages.append(cage)
    for button in selected_buttons:
        buttons[button[0]][button[1]].config(text="*")
    print_cage(cage)
    selected_buttons.clear()


create_cage_button = tkinter.Button(m, text="Create Cage", width=2, command=create_cage)
create_cage_button.grid(row=9, column=3)

# text input for sum of selected buttons
sum_input = tkinter.Entry(m, width=2)
sum_input.grid(row=9, column=5)

sb = SudokuBoard()
sb.cages = cages
sb.board = [[0 for i in range(9)] for j in range(9)]
sb.print_board(sb.board)
sb.solve(sb.board)
sb.print_board(sb.board)


# Run the main loop
m.mainloop()