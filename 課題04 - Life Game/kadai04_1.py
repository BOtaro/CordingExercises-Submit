import tkinter, random

#settings
cols = 65
rows = 35

dead_point_size = 3
life_point_size = 10
border_size = life_point_size + 10


root = tkinter.Tk()
root.title("Conway's Life Game")
root.resizable(0,0)
frame = tkinter.Frame(root, width=cols*border_size*1.1, height=rows*border_size*1.1)
frame.grid()
board_list = [[bool(random.getrandbits(1)) for x in range(cols)] for y in range(rows)]

def draw():
    board = tkinter.Canvas(frame, width=cols*60, height=rows*60)

    for y, line in enumerate(board_list, 1):
        for x, cell in enumerate(line, 1):
            point_size = life_point_size if cell else dead_point_size
            board.create_oval(x*border_size, y*border_size, x*border_size+point_size, y*border_size+point_size, fill="black")
    board.place(x=0, y=0)

def survive():
    global board_list
    new_board_list = [[False] * cols for y in range(rows)]
    for y, line in enumerate(board_list):
        for x, cell in enumerate(line):
            around = [] #自分含む周囲のマス（最大8）
            for line in board_list[max([0,y-1]):min([y+2,rows])]:
                around += line[max([0,x-1]):min([x+2,cols])]
            
            if cell:    #生きている時
                if around.count(True) in [3,4]:
                    new_board_list[y][x] = True
            else:   #死んでいる時
                if around.count(True) == 3:
                    new_board_list[y][x] = True
        
    board_list = new_board_list
    draw()
    root.after(1000, survive)

    
draw()
survive()
root.mainloop()