from person import Person
from deck import Deck
import time
from strategy import Strategy
from auto_game import AutoGame

class Game:

    def __init__(self, player, dealer):
        self.deck = None
        self.dealer = dealer
        self.player = player
        self.decks_played = []
        self.num_of_games = 0

    def start(self):
        game_mode = raw_input('Would you like to play in manual or automatic mode? (m/a): ')

        # Manual game
        if game_mode.upper() == 'M':
            question = 'Would you like to play a new deck? (y/n)'
            reply = raw_input(question)
            while reply.upper() == 'Y':
                self.deck = Deck()
                self.deck.shuffle()
                whole_deck_played = self.play_deck_manually()
                self.decks_played.append(whole_deck_played)
                print('List of played decks: {}'.format(self.decks_played))
                reply = raw_input(question)
            exit()

        # Automatic game

        # Get a number of required games to play
        num_of_auto_games = int(raw_input('Enter number of games: '))
        self.deck = Deck()
        self.deck.shuffle()
        whole_deck_played = self.play_deck_automatically(num_of_auto_games)[0]
        self.decks_played.append(whole_deck_played)
        num_of_player_wins = self.play_deck_automatically(num_of_auto_games)[1]
        num_of_dealer_wins = self.play_deck_automatically(num_of_auto_games)[2]
        total_num_of_games = self.play_deck_automatically(num_of_auto_games)[3]
        num_of_draws = self.play_deck_automatically(num_of_auto_games)[4]
        print('Player wins: {}'.format(num_of_player_wins))
        print('Dealer wins; {}'.format(num_of_dealer_wins))
        print('Total games: {}'.format(total_num_of_games))
        print('Draws: {}'.format(num_of_draws))

            # take_another_card = strategy.next_card(dealer=self.dealer, player=self.player, deck=self.deck)

    #     -----------------------STUFF FOR MANUAL GAME-------------------------

    def play_deck_manually(self):
        '''
        plays deck manually
        :return: True if whole deck is played. False if not the whole deck is played
        '''
        reply1 = "y"
        # The whole deck is played if there are less than 8 cards left in the deck
        while self.deck.cards_left() >= 8 and reply1.upper() == 'Y':
            print('\n\n========== Starting new round ==========\n')
            self.dealer.reset()
            self.player.reset()
            for i in range(2):
                self.player.take_card(self.deck.get_card())
                self.dealer.take_card(self.deck.get_card())
            self.show_players_cards()

            # deal the player
            result = self.deal_player_manually()
            if result == 'BUSTED':
                play_more = self.declare_winner()
                if play_more:
                    continue
                else:
                    reply1 = 'n'
                    return False

            # deal the dealer
            print('\nCards are now being dealt to the dealer... \n')
            self.show_players_cards(show_secret_card=True)
            result = self.deal_dealer(self.player.get_score())
            if result == 'BUSTED':
                play_more = self.declare_winner()
                if play_more:
                    continue
                else:
                    reply1 = 'n'
                    return False

            elif result == 'DRAW':
                play_more = self.declare_winner()
                if play_more:
                    continue
                else:
                    reply1 = 'n'
                    return False

            else:
                play_more = self.declare_winner()
                if play_more:
                    continue
                else:
                    reply1 = 'n'
                    return False

        return True

    def deal_dealer(self, player_score):
        dealer_score = self.dealer.get_score()

        dealer_busted = False
        while dealer_score <= player_score and dealer_score <= 21:

            if dealer_score == player_score and dealer_score > 18:
                return 'DRAW'

            elif dealer_busted:
                return 'BUSTED'

            elif dealer_score > player_score and dealer_score <= 21:
                return 'WIN'

            else:
                print('\n----- dealer is getting a new card...')
                time.sleep(2)
                self.dealer.take_card(self.deck.get_card())
                dealer_score = self.dealer.get_score()
                self.show_players_cards(show_secret_card=True)
                dealer_busted = self.check_busted(self.dealer)

        return 'WIN'

    def deal_player_manually(self):
        question = 'Would you like another card? (y/n): '
        reply = raw_input(question)
        while reply.upper() == 'Y':
            self.player.take_card(self.deck.get_card())
            self.show_players_cards()

            # check if player is busted
            player_busted = self.check_busted(self.player)
            if player_busted:
                return 'BUSTED'

            reply = raw_input(question)
        return 'CONTINUE'

    def declare_winner(self):
        # self.show_players_cards(show_secret_card=True)

        # check if player is busted
        if self.player.get_score() > 21:
            print('\n\n P L A Y E R || B U S T E D \n')
            self.dealer.add_new_win()
            print('\n D E A L E R || W I N S \n')
        elif self.dealer.get_score() > 21:
            print('\n\n D E A L E R || B U S T E D \n')
            self.player.add_new_win()
            print('\n P L A Y E R || W I N S \n')

        # check a winner
        elif self.dealer.get_score() > self.player.get_score():
            print('\n D E A L E R || W I N S \n')
            self.dealer.add_new_win()
        elif self.player.get_score() > self.dealer.get_score():
            print('\n P L A Y E R || W I N S \n')
            self.player.add_new_win()

        # declare a draw
        else:
            print('\n\n ~~ IT\'S A DRAW ~~ \n')

        self.add_game()
        num_of_player_wins = self.player.get_num_of_wins()
        num_of_dealer_wins = self.dealer.get_num_of_wins()
        print('Player wins: {}'.format(num_of_player_wins))
        print('Dealer wins: {}'.format(num_of_dealer_wins))

        print('Total games: {}\n'.format(self.num_of_games))

        # ask if player wants to continue game
        reply1 = raw_input('Would you like to play again? (y/n): ')
        if reply1.upper() == 'Y':
            return True
        else:
            return False

    #     --------------------------------STUFF FOR AUTOMATIC GAME------------------------------


    def play_deck_automatically(self, num_of_auto_games):
        '''
        plays deck manually
        :return: True if whole deck is played. False if not the whole deck is played
        '''
        # The whole deck is played if there are less than 8 cards left in the deck
        while self.deck.cards_left() >= 8:
            self.dealer.reset()
            self.player.reset()
            for i in range(2):
                self.player.take_card(self.deck.get_card())
                self.dealer.take_card(self.deck.get_card())
            self.show_players_cards()

            # deal the player
            result = self.deal_player_automatically()
            if result == 'BUSTED':
                play_more, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws = self.declare_winner_auto(num_of_auto_games)
                if play_more:
                    continue
                else:
                    return (False, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws)

            # deal the dealer
            self.show_players_cards(show_secret_card=True)
            result = self.deal_dealer_auto(self.player.get_score())
            if result == 'BUSTED':
                play_more, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws = self.declare_winner_auto(num_of_auto_games)
                if play_more:
                    continue
                else:
                    return (False, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws)

            elif result == 'DRAW':
                play_more, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws = self.declare_winner_auto(num_of_auto_games)
                if play_more:
                    continue
                else:
                    return (False, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws)

            else:
                play_more, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws = self.declare_winner_auto(num_of_auto_games)
                if play_more:
                    continue
                else:
                    return (False, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws)

        return (True, None, None, None, None)


    def deal_player_automatically(self):
        strategy = Strategy()
        reply = strategy.next_card(dealer=self.dealer, player=self.player, deck=self.deck)
        while reply == True:
            self.player.take_card(self.deck.get_card())

            # check if player is busted
            player_busted = self.check_busted(self.player)
            if player_busted:
                return 'BUSTED'

            reply = strategy.next_card(dealer=self.dealer, player=self.player, deck=self.deck)
        return 'CONTINUE'


    def deal_dealer_auto(self, player_score):
        dealer_score = self.dealer.get_score()

        dealer_busted = False
        while dealer_score <= player_score and dealer_score <= 21:

            if dealer_score == player_score and dealer_score > 18:
                return 'DRAW'

            elif dealer_busted:
                return 'BUSTED'

            elif dealer_score > player_score and dealer_score <= 21:
                return 'WIN'

            else:
                self.dealer.take_card(self.deck.get_card())
                dealer_score = self.dealer.get_score()
                dealer_busted = self.check_busted(self.dealer)

        return 'WIN'


    def declare_winner_auto(self, num_of_auto_games):
            '''
            declares winner based on person scores
            :return:
            '''

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
            total_num_of_games = self.num_of_games
            num_of_draws = total_num_of_games - (num_of_player_wins + num_of_dealer_wins)

            # check if total_num_of_auto_games has been reached
            if total_num_of_games >= num_of_auto_games:
                return (False, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws)
            else:
                return (True, num_of_player_wins, num_of_dealer_wins, total_num_of_games, num_of_draws)

    def add_games_played(self):
        self.num_of_games += 1
        print(self.num_of_games)



    def show_players_cards(self, show_secret_card=False):
        print('\nDealer\'s cards: ')
        for card in self.dealer.cards:
            if self.dealer.cards.index(card) == 0:
                if show_secret_card:
                    card.show()
                else:
                    print('(?, ?)')
            else:
                card.show()
        if show_secret_card:
            print('Score: {}'.format(self.dealer.get_score()))

        print('\nPlayer\'s cards: ')
        for card in self.player.cards:
            card.show()
        print('Score: {}'.format(self.player.get_score()))


    def check_busted(self, person):
        if person.get_score() > 21:
            return True
        else:
            return False

    def add_game(self):
        self.num_of_games += 1

