import tkinter

size = 80

root = tkinter.Tk()
root.title('8Queen')
root.resizable(0,0)
#game_frame = tkinter.Frame(root, width = 300, height = 300, borderwidth = 3)
queen_num = 0
red_carpet = [] #塗りつぶし済みのマス


def left_click(event):
    global queen_num
    queen_num += 1
    #event.widgetで該当のオブジェクト（ウィジェット=部品）を取得できる
    #またそのフレームのアトリビュートnumを表示する
    print(event.widget.num)
    frame_x, frame_y = event.widget.num

    #上下
    canvas_list = [[frame_x, y] for y in range(8)]
    #左右
    canvas_list += [[x, frame_y] for x in range(8)if x != frame_x]
    #左上
    i = 1
    while (frame_x - i >= 0) & (frame_y - i >= 0):
        canvas_list.append([frame_x - i,frame_y - i])
        i += 1
    #左下
    i = 1
    while (frame_x - i >= 0) & (frame_y + i < 8):
        canvas_list.append([frame_x - i,frame_y + i])
        i += 1
    #右上
    i = 1
    while (frame_x + i <8) & (frame_y - i >= 0):
        canvas_list.append([frame_x + i,frame_y - i])
        i += 1
    #右下
    i = 1
    while (frame_x + i < 8) & (frame_y + i < 8):
        canvas_list.append([frame_x + i,frame_y + i])
        i += 1

    global red_carpet

    red_carpet += canvas_list
    red_carpet = list(set(map(tuple,red_carpet)))

    red_num = len(red_carpet)

    for x, y in canvas_list:
        canvas = tkinter.Canvas(frame_list[x][y], bg = '#FF3F00')
        canvas.place(x=0, y=0)

    canvas = tkinter.Canvas(frame_list[frame_x][frame_y], bg = '#FF3F00')
    canvas.create_oval(size/4, size/4, size*3/4, size*3/4, fill="black")
    canvas.place(x=0, y=0)

    if red_num == 8 * 8:
        if queen_num < 8:
            print('Game Over!!!!!!!!!!!')
        else:
            print('Clear!')

 
#繰り返し作成したフレーム格納用リスト
frame_list = [[''] * 8 for i in range(8)]
#for文の入れ子構造にして、9×9回繰り返す
for y in range(8):
    for x in range(8):
        #タテヨコ30pxの小さいフレームを量産。
        frame = tkinter.Frame(root, width = size, height = size, bd = 1, relief = 'sunken')
        #bindメソッドを使うと、そのオブジェクトにイベントを定義できる。
        #第一引数に<1>を指定すると左クリックした際のイベントとなる
        #第二引数には呼び出される関数（4行目から定義しているleft_click関数）を記述する
        frame.bind("<1>", left_click)
        #frameにnumアトリビュートを定義する
        frame.num = [y, x]
        #作成したフレームをフレームのリストに格納する。これでインデックス番号でアクセスすることで
        #各フレームを操作できる
        frame_list[y][x] = frame
        #gridを使ってフレームを配置する。packと違いgridを使うと、タテヨコ均等に8列x8列に配置できる
        #rowでヨコ、columnでタテを指定している
        frame.grid(row=x, column=y)

root.mainloop()