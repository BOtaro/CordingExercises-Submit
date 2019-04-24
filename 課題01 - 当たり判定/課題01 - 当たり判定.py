def main(input_line):
    def collision_judge(o_x, o_y, o_w, o_h, t_x, t_y, t_w, t_h):
        #左上隅、左下隅、右上隅、右下隅をチェック
        if (t_x <= o_x <= t_x + t_w) & (t_y <= o_y <= t_y + t_h) \
        or (t_x <= o_x <= t_x + t_w) & (t_y <= o_y + o_h <= t_y + t_h) \
        or (t_x <= o_x + o_w <= t_x + t_w) & (t_y <= o_y <= t_y + t_h) \
        or (t_x <= o_x + o_w <= t_x + t_w) & (t_y <= o_y + o_h <= t_y + t_h):
            return True
        else:
            return False

    #自機の座標・幅・高さを代入
    jiki_x, jiki_y, jiki_w, jiki_h = list(map(int, input_line.split('\n')[0].split()))
    tekiki_num = int(input_line.split('\n')[1])
    result = [False] * tekiki_num

    #敵機の座標・幅・高さを配列に代入
    tekiki_x, tekiki_y, tekiki_w, tekiki_h = [0] * tekiki_num, [0] * tekiki_num, [0] * tekiki_num, [0] * tekiki_num
    for i in range(tekiki_num):
        tekiki_x[i], tekiki_y[i], tekiki_w[i], tekiki_h[i] = list(map(int, input_line.split('\n')[2 + i].split()))

    #自機の４隅をチェック
    for i in range(tekiki_num):
        if collision_judge(jiki_x, jiki_y, jiki_w, jiki_h, tekiki_x[i], tekiki_y[i], tekiki_w[i], tekiki_h[i]):
            result[i] = True

    #敵機の４隅をそれぞれチェック
    for i in range(tekiki_num):
        if collision_judge(tekiki_x[i], tekiki_y[i], tekiki_w[i], tekiki_h[i], jiki_x, jiki_y, jiki_w, jiki_h):
            result[i] = True

    #結果出力
    for i, r in enumerate(result):
        if r:
            print('敵機{}が当たり'.format(i + 1))
    print('\n')

input_line = '''100 100 70 100
3
50 60 100 50
10 120 100 50
165 115 70 70'''

print('テストデータ１')
main(input_line)

#敵機１だけ当たるパターン
input_line2 = '''100 100 70 100
3
50 60 100 50
1000 120 100 50
1000 115 70 70'''

print('テストデータ２ 敵機１だけ当たるパターン')
main(input_line2)

#敵機２だけ当たるパターン
input_line2 = '''100 100 70 100
3
50 60 100 50
10 120 100 50
1000 115 70 70'''

print('テストデータ３ 敵機1と2が当たるパターン')
main(input_line2)