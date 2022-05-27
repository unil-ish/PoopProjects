import senticnet
import play
import speech
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
    speech1 = speech.Speech('I really love cholocate. It makes me the happiest man in the world.', 2, 2)
    speech1.disambiguate()
    s = senticnet.Senticnet()
    print(speech1.getEmotions(s))
    

    return

def main():
    """ Main function """
    debug()

if __name__ == '__main__':
    main()
