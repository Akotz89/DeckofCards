# Aaron Kotz, CIS261, Deckof Cards

import random
import os

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self):
        self.deck = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards):
        if num_cards > len(self.deck):
            raise ValueError("Not enough cards in the deck to deal.")
        dealt_cards = [self.deck.pop() for _ in range(num_cards)]
        return dealt_cards

    def count(self):
        return len(self.deck)

def main():
    deck = Deck()
    print("Card Dealer")
    print("I have shuffled a deck of 52 cards.")
    
    while True:
        try:
            num_cards = int(input("How many cards would you like?: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    dealt_cards = deck.deal(num_cards)
    
    print("\nHere are your cards:")
    for card in dealt_cards:
        print(card)
    
    print(f"\nThere are {deck.count()} cards left in the deck.")
    print("\nGood luck!")


if __name__ == "__main__":
    main()

