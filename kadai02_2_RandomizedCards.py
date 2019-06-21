import kadai02_ver2
from random import randrange

def main():
    cards = []
    while len(set(cards)) < 5:
        cards.append(str(randrange(1,4)) + ' ' + str(randrange(1,14)).zfill(2))
    cards = list(set(cards))

    input_str = '\n'.join(cards)
    return kadai02_ver2.main(input_str)

if __name__ == "__main__":
    main()