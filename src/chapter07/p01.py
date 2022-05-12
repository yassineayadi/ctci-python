import random
from abc import ABC
from dataclasses import dataclass
from enum import Enum
from typing import Set, List


class Suite(Enum):
    Club = "club"
    Diamond = "diamond"
    Hearts = "hearts"
    Spades = "spades"


@dataclass(frozen=True)
class Card:
    """Card belonging to a generic deck of cards."""

    suite: Suite
    value: int


@dataclass
class Deck:
    """Generic deck of cards."""

    cards: Set[Card]
    type: str
    size: int


@dataclass
class Hand:
    cards: List[Card]

    def add_card(self, card: Card):
        self.cards.append(card)

    @property
    def size(self):
        return len(self.cards)

    @property
    def score(self):
        return sum(card.value for card in self.cards)

    @property
    def misses_cards(self):
        return False


class BlackJackHand(Hand):
    @property
    def misses_cards(self):
        return self.size <= 7

    @property
    def score(self):
        return super().score


class CardGame(ABC):
    pass


class BlackJack(CardGame):
    def __init__(self, number_of_decks: int, number_of_players: int):
        decks = []
        for deck in range(number_of_decks):
            decks.append(create_deck_of_cards("black_jack"))
        cards = [card for deck in decks for card in deck.cards]
        self.cards = cards
        self.number_of_players = number_of_players

    @property
    def remaining_cards(self) -> int:
        return len(self.cards)

    def shuffle_cards(self) -> None:
        cards = self.cards
        shuffled = []
        for i in range(self.remaining_cards):
            card = random.choice(self.cards)
            cards.remove(card)
            shuffled.append(card)
        self.cards = shuffled

    def distribute(self, hand: BlackJackHand):
        while hand.misses_cards:
            self.deal_card(hand)

    def deal_card(self, hand: Hand):
        if self.remaining_cards:
            card = self.cards.pop()
            hand.cards.append(card)


def generate_set_of_cards() -> Set:
    card_set = set()
    for suite in Suite:
        for number in range(1, 14):
            card_set.add(Card(suite, number))
    return card_set


def create_deck_of_cards(deck_type: str):
    supported_decks = ["black_jack"]
    if deck_type not in supported_decks:
        raise ValueError(f"Unsupported Deck type {deck_type}")

    if deck_type == "black_jack":
        card_set = generate_set_of_cards()
        size = len(card_set)
        return Deck(card_set, deck_type, size)


SUPPORTED_GAMES = {"black_jack": BlackJack}


def initialize_game(game_type: str, *args, **kwargs):
    game = SUPPORTED_GAMES[game_type]
    return game(*args, **kwargs)
