from deck import Deck
from person import Person
from game import Game

if __name__ == '__main__':
    print('hello')

    # deck.show_cards()
    #
    # print('-----')
    #
    # card = deck.get_card()
    # card.show()
    #
    # print('------')
    #
    # deck.show_cards()

    # person = Person('player')
    # for i in range(4):
    #     card = deck.get_card()
    #     person.take_card(card)
    # person.show_cards()
    # score = person.get_score()
    # print(score)

    # test game
    player = Person('player')
    dealer = Person('dealer')
    game = Game(player=player, dealer=dealer)
    game.start()

    # test for deck.get_leftovers()
    # deck = Deck()
    # deck.shuffle()
    # cards = deck.get_leftovers()
    # print('Inital value of deck: {}'.format(cards))
    # for i in range(10):
    #     card = deck.get_card()
    #     card.show()
    # cards = deck.get_leftovers()
    # print(cards)
