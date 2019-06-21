from collections import Counter
from statistics import mode

def main(input_str):
    suit = ['S', 'C', 'D', 'H']     #スペードを S、クラブを C、ダイヤをD、ハートを H で表す
    ace = [None, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    lank = [1, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]    #カードのランク（数字） 小さい方が強い

    def isStraight(cards):
        if sorted([n[1] for n in cards]) in [list(range(min([n[1] for n in cards]), min([n[1] for n in cards]) + 5))] + [[1,10,11,12,13]]:
            return True
        else:
            return False

    def isFlush(cards):
        if len(list(set([s[0] for s in cards]))) == 1:
            return True
        else:
            return False
    
    def straightLank(cards):
        if sorted([n[1] for n in cards]) == [1, 2, 3, 4, 5]:
            return 9
        else:
            return min([lank.index(n[1]) for n in cards])


    #スートは スペードが スペードが 0、クラブが 1、ダイヤが 、ダイヤが 2、ハートが 3
    cards = [list(map(int, x.split())) for x in input_str.split('\n')]
    
    #カード情報出力
    for i in range(5):
        print(suit[cards[i][0]] + ace[cards[i][1]], end=' ')
    print()

    if isFlush(cards) & (sorted([n[1] for n in cards]) == [1,10,11,12,13]):
        print('ロイヤル・ストレート・フラッシュ')
        return 0

    elif isFlush(cards) & isStraight(cards):
        print('ストレート・フラッシュ')
        return [1, straightLank(cards)]

    elif 4 in Counter([n[1] for n in cards]).values():
        print('フォーカード')
        return [2, lank.index(mode([n[1] for n in cards]))]

    elif len(list(set([n[1] for n in cards]))) == 2:    #カードの数字の配列の重複する要素を除いた要素数が2、かつフォーカードでない、すなわちフルハウス
        print('フルハウス')
        return [3, lank.index(mode([n[1] for n in cards]))]

    elif isFlush(cards):
        print('フラッシュ')
        return [4, min([lank.index(n[1]) for n in cards])]

    elif isStraight(cards):
        print('ストレート')
        return [5, straightLank(cards)]

    elif 3 in Counter([n[1] for n in cards]).values():
        print('スリーカード')
        return [6, lank.index(mode([n[1] for n in cards]))]

    elif list(Counter([n[1] for n in cards]).values()).count(2) == 2:
        print('ツーペア')
        pair1, pair2, kicker = [x[0] for x in Counter([n[1] for n in cards]).most_common()]
        return [7, min(lank.index(pair1), lank.index(pair2)), max(lank.index(pair1), lank.index(pair2)), lank.index(kicker)]

    elif len(list(set([n[1] for n in cards]))) == 4:
        print('ワンペア')
        c = [lank.index(x[0]) for x in Counter([n[1] for n in cards]).most_common()]
        return [8, c[0]] + sorted(c[1:])

    else:
        print('ハイカード')
        return [9] + sorted([lank.index(x[1]) for x in cards])

if __name__ == "__main__":

    rsf_str = '''0 01
    0 12
    0 13
    0 11
    0 10'''

    print(main(rsf_str), '\n')

    sf_str = '''0 02
    0 06
    0 03
    0 05
    0 04'''

    print(main(sf_str), '\n')

    fc_str = '''0 12
    2 12
    0 10
    3 12
    0 12'''

    print(main(fc_str), '\n')

    fh_str = '''0 13
    2 13
    0 12
    3 12
    0 13'''

    print(main(fh_str), '\n')

    fl_str = '''1 13
    1 12
    1 01
    1 02
    1 11'''

    print(main(fl_str), '\n')

    st_str = '''0 08
    2 09
    0 11
    3 10
    0 12'''

    print(main(st_str), '\n')

    sc_str = '''0 13
    2 13
    0 11
    3 13
    0 12'''

    print(main(sc_str), '\n')

    tp_str = '''0 13
    2 13
    0 11
    3 01
    0 01'''

    print(main(tp_str), '\n')

    op_str = '''0 13
    2 13
    0 11
    3 02
    0 12'''

    print(main(op_str), '\n')

    hc_str = '''0 13
    2 07
    0 11
    3 02
    0 12'''

    print(main(hc_str), '\n')