from person import Person
from deck import Deck
from card import Card

class Strategy:

    def __init__(self, threshold=0.6):
        self.threshold = threshold

    def next_card(self, dealer, player, deck):
        # adding 1 because we're not checking dealer's secret card
        num_of_cards_left = len(deck.get_cards()) + 1
        leftovers = deck.get_leftovers()
        player_score = player.get_score()
        dealers_cards = dealer.get_cards()
        players_cards = player.get_cards()

        dealer_secret_card = dealers_cards[1]
        val_of_secret_card = dealer_secret_card.get_value()
        leftovers[val_of_secret_card] += 1

        max_safe_score_for_player = 21 - player_score
        if max_safe_score_for_player >= 10:
            max_safe_score_for_player = 10
        num_of_safe_cards = 0

        for i in range(1, max_safe_score_for_player + 1):
            num_of_cards = leftovers[i]
            num_of_safe_cards = num_of_safe_cards + num_of_cards

        prob_of_not_busting = float(num_of_safe_cards)/float(num_of_cards_left)
        prob_of_busting = 1 - prob_of_not_busting

        if prob_of_busting <= self.threshold:
            return True
        return False