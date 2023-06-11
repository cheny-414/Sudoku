from tkinter import *
from Solver import *

root = Tk()
root.title("Sudoku Solver")
root.geometry("540x600")

instructionsLabel = Label(root, text="Fill in initial numbers and click \"Solve\"")
instructionsLabel.grid(row=0, column=1, columnspan=10)

errorLabel = Label(root, text="", fg="red")
errorLabel.grid(row=15, column=1, columnspan=10, pady=5)

solvedLabel = Label(root, text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

cells = {}


def ValidateNumber(P):
    out = (P.isdigit() or P == "") and len(P) < 2
    return out


reg = root.register(ValidateNumber)


def draw3x3Grid(row, column, bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root, width=5, bg=bgcolor, justify="center", validate="key", validatecommand=(reg, "%P"))
            e.grid(row=row + i + 1, column=column + j + 1, sticky="nsew", padx=1, pady=1, ipady=5)
            cells[(row + i + 1, column + j + 1)] = e


def draw9x9Grid():
    color = "#D0ffff"
    for rowNo in range(1, 10, 3):
        for colNo in range(0, 9, 3):
            draw3x3Grid(rowNo, colNo, color)
            if color == "#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"


def clearValues():
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        for col in range(1, 10):
            cell = cells[(row, col)]
            cell.delete(0, "end")


def getValues():
    board = []
    errorLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2, 11):
        rows = []
        for col in range(1, 10):
            val = cells[(row, col)].get()
            if val == "":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)

def updateValues(s):
    sol = solver(s)
    if sol != "No":
        for row in range(2, 11):
            for col in range(1, 10):
                cells[(row, col)].delete(0, "end")
                cells[(row, col)].insert(0, sol[row-2][col-1])
        solvedLabel.configure(text = "Sudoku is solved! :)")
    else:
        errorLabel.configure(text="Can't solve this sudoku :(")


btn = Button(root, command=getValues, text="Solve", width=10)
btn.grid(row=20, column=1, columnspan=5, pady=20)

btn = Button(root, command=clearValues, text="Clear", width=10)
btn.grid(row=20, column=5, columnspan=5, pady=20)

draw9x9Grid()
root.mainloop()
