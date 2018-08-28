from deck import Deck
from card import Card

class Person:

    def __init__(self, role,):
        self.role = role
        self.cards = []
        self.num_of_wins = 0

    # def set_num_of_wins(self, wins):
    #     self.num_of_wins = wins

    def get_cards(self):
        return self.cards

    def get_num_of_wins(self):
        return self.num_of_wins

    def add_new_win(self):
        self.num_of_wins += 1

    def take_card(self, card):
        self.cards.append(card)

    def get_score(self):
        score = 0
        num_of_aces = 0
        for card in self.cards:
            if card.rank == 'King' or card.rank == 'Queen' or card.rank == 'Jack':
                card_rank = 10
            elif card.rank == 'Ace':
                card_rank = 11
                num_of_aces += 1
            else:
                card_rank = int(card.rank)

            score += card_rank

        while score > 21:
            if num_of_aces > 0:
                score -= 10
                num_of_aces -= 1
            else:
                return score

        return score

    def get_role(self):
        return self.role

    def show_cards(self):
        for card in self.cards:
            card.show()

    def reset(self):
        self.cards = []
