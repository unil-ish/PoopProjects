import senticnet
import play

def debug():
    """
        =================
          VARIOUS TESTS
        =================
    """

    """
    s = senticnet.Senticnet()
    s.emotionsOf("abandon"))

    path = "theater/AbrahamLincolnbyJohnDrinkwater11172.xml"
    p = play.Play(path)

    words = 0
    for c in p.characters:
        words += c.countWords
        print(f"{c.name} has said {c.countWords} words")


    print(f'Total amount of words (count v1) : {words}')
    print(f'Total amount of words (count v2) : {len(p)}')
    """

    return

def main():
    """ Main function """
    debug()

if __name__ == '__main__':
    main()
