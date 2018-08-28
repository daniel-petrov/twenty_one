from card import Card
from random import shuffle

class Deck:

    def __init__(self):
        suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
        ranks = ['Ace', 'King', 'Queen', 'Jack', '10', '9', '8', '7', '6', '5', '4', '3', '2']
        self.cards = []

        for rank in ranks:
            for suit in suits:
                card = Card(rank, suit)
                self.cards.append(card)

    def get_cards(self):
        return self.cards

    def shuffle(self):
        shuffle(self.cards)

    def show_cards(self):
        for card in self.cards:
            card.show()

    def get_card(self):
        card = self.cards.pop()
        return card

    def cards_left(self):
        return len(self.cards)

    def get_leftovers(self):
        leftovers = {}
        for card in self.cards:
            card_val = card.get_value()
            if card_val in leftovers:
                leftovers[card_val] += 1
            else:
                leftovers[card_val] = 1
        return leftovers
