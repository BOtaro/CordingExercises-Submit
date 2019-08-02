import tkinter, random

#settings
rows = 31
cols = 21

square_size = 30

root = tkinter.Tk()
root.title("壁伸ばし法による迷路の自動生成")
root.resizable(0,0)
frame = tkinter.Frame(root, width=rows*square_size*1.1, height=cols*square_size*1.1)
frame.grid()

#True が道、 False が壁
#board_list = [[True if x not in [0, rows-1] and y not in [0,cols-1] and (x%2 or y%2) else False for y in range(cols)] for x in range(rows)]
#0が外壁、1が中壁、2が道
board_list = [[0 if x in [0, rows-1] or y in [0,cols-1] else 2 if x%2 or y%2 else 1 for y in range(cols)] for x in range(rows)]
print(rows, cols)

nodes = []
for i, row in enumerate(board_list):
    for j, cell in enumerate(row):
        if cell == 1:
            nodes.append([i,j])

def hoge():
    while nodes != []:
        path = []
        #選択中の柱の座標
        x, y = random.choice(nodes)

        around = [[x-2,y],[x,y-2],[x+2,y],[x,y+2]]
        random.shuffle(around)

        for a, b in around:
            if [a, b] in nodes:
                x, y = [a, b]
                nodes.remove([a, b])
                path.append([a, b])
                break
            else:
                path.append([a, b])
                for i, tmp in enumerate(path[:-1]):
                    board_list[tmp[0]][tmp[1]] = 1
                    board_list[int((tmp[0]+path[i+1][0])/2)][int((tmp[1]+path[i+1][1])/2)] = 1
                path = []
                hoge()
        else:
            x, y = path[-1]

hoge()

for y in range(cols):
    print(''.join(['□' if board_list[x][y] == 2 else '■' for x in range(rows)]))
