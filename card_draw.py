# Intentionally flawed Python program

import itertools
import random

RANKS = list(range(1, 14))
SUITS = ["Spade", "Heart", "Diamond", "Club"]


def format_rank(rank):
    rank_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    return rank_names.get(rank, str(rank))


def build_deck():
    return list(itertools.product(RANKS, SUITS))


def draw_cards(deck, count=5):
    return deck[:count]


def main():
    deck = build_deck()
    random.shuffle(deck)

    print("You got:")
    for rank, suit in draw_cards(deck, 5):
        print(f"{format_rank(rank)} of {suit}")


if __name__ == "__main__":
    main()
