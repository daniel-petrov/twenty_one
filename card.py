class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def show(self):
        print(self.rank, self.suit)

    def get_value(self):
        if self.rank == 'Ace':
            return 1
        if self.rank == 'King' or self.rank == 'Queen' or self.rank == 'Jack':
            return 10
        else:
            return int(self.rank)

