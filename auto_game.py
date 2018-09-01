from person import Person
from deck import Deck
import time
from strategy import Strategy

class AutoGame:

    def __init__(self, player, dealer):
        self.deck = None
        self.dealer = dealer
        self.player = player
        self.decks_played = []
        self.num_of_games = 0

    def play_game(self, num_of_auto_games):
        #TODO: code the logic
        winning_percentage = None
        player = Person()
        dealer = Person()
        player, num_of_games_played = self.play_deck(player, dealer)
        return winning_percentage

    def play_deck(self, player, dealer):
    #     TODO: code the logic
        num_of_games_played = None
        return (player, num_of_games_played)






    def declare_winner_auto(self):

        # self.show_players_cards(show_secret_card=True)

        # check if player is busted
        if self.player.get_score() > 21:
            self.dealer.add_new_win()
            self.add_game()
        elif self.dealer.get_score() > 21:
            self.player.add_new_win()
            self.add_game()

        # check a winner
        elif self.dealer.get_score() > self.player.get_score():
            self.dealer.add_new_win()
            self.add_game()
        elif self.player.get_score() > self.dealer.get_score():
            self.player.add_new_win()
            self.add_game()

        # declare a draw
        else:
            self.add_game()

        num_of_player_wins = self.player.get_num_of_wins()
        num_of_dealer_wins = self.dealer.get_num_of_wins()
        print('Player wins: {}'.format(num_of_player_wins))
        print('Dealer wins: {}'.format(num_of_dealer_wins))
        print('Total games: {}\n'.format(self.num_of_games))

        # ask if player wants to continue game
        lets_play_again = 'Y'
        if lets_play_again == 'Y':
            return True
        else:
            return False

    # def play_deck_automatically(self):
    #     '''
    #             plays deck manually
    #             :return: True if whole deck is played. False if not the whole deck is played
    #             '''
    #     # The whole deck is played if there are less than 8 cards left in the deck
    #     while self.deck.cards_left() >= 8:
    #         self.dealer.reset()
    #         self.player.reset()
    #         for i in range(2):
    #             self.player.take_card(self.deck.get_card())
    #             self.dealer.take_card(self.deck.get_card())
    #         # self.show_players_cards()
    #
    #         # deal the player
    #         result = self.deal_player_automatically()
    #         if result == 'BUSTED':
    #             play_more = self.declare_winner_auto()
    #             if play_more:
    #                 continue
    #             else:
    #                 return False
    #
    #         # deal the dealer
    #         # self.show_players_cards(show_secret_card=True)
    #         result = self.deal_dealer_auto(self.player.get_score())
    #         if result == 'BUSTED':
    #             play_more = self.declare_winner_auto()
    #             if play_more:
    #                 continue
    #             else:
    #                 return False
    #
    #         elif result == 'DRAW':
    #             play_more = self.declare_winner_auto()
    #             if play_more:
    #                 continue
    #             else:
    #                 return False
    #
    #         else:
    #             self.declare_winner_auto()
    #
    #     return True
    #
    #
    # def deal_player_automatically(self):
    #     strategy = Strategy()
    #     reply = strategy.next_card(dealer=self.dealer, player=self.player, deck=self.deck)
    #     while reply == True:
    #         self.player.take_card(self.deck.get_card())
    #
    #         # check if player is busted
    #         player_busted = self.check_busted(self.player)
    #         if player_busted:
    #             return 'BUSTED'
    #
    #         reply = strategy.next_card(dealer=self.dealer, player=self.player, deck=self.deck)
    #     return 'CONTINUE'