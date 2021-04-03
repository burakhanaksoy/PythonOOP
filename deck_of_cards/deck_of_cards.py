import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f'{self.value} of {self.suit}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw(self):
        return self.cards.pop()


class Player:
    def __init__(self, name='default name'):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.draw())
        return self

    def show_hand(self):
        for c in self.hand:
            c.show()

    def discard(self):
        self.hand.pop()
        return self


deck = Deck()
deck.shuffle()

p = Player('Burak')
p.draw(deck).draw(deck).draw(deck)
print('*' * 50)
p.show_hand()
print('*' * 50)
print(len(deck.cards))  # prints 49 -> (52-3) since we draw 3 cards
p.discard().discard().discard()
print(p.show_hand())
