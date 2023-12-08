class Card:
    def __init__(self, type: str) -> None:
        self.type = type

    def get_value(self, part2: bool = False):
        sort_vals = "0123456789ABC"
        sorted_cards = "AKQJT98765432" if not part2 else "AKQT98765432J"
        return sort_vals[sorted_cards.index(self.type)]


class Hand:
    def __init__(self, data: str, part2: bool = False) -> None:
        cards_str, bid_str = data.split()
        self.bid = int(bid_str)
        self.cards = [Card(c) for c in cards_str]
        self.part2 = part2

    def _possible_hands(self, cards: list[Card], acc):
        # Calculate all possible hands so they can be ranked and the strongest picked
        pass

    def _histogram(self, cards: list[Card] = None):
        use_cards = self.cards if cards is None else cards
        card_types = [c.type for c in use_cards]
        return list(set([(c, card_types.count(c)) for c in card_types]))

    def rank_value(self, cards: list[Card] = None):
        use_cards = self.cards if cards is None else cards
        histogram = self._histogram(use_cards)
        max_count = max([h[1] for h in histogram])
        if len(histogram) == 1:
            return "0"  # "five_of_a_kind"
        if len(histogram) == 2:
            if max_count == 4:
                return "1"  # "four_of_a_kind"
            return "2"  # "full_house"
        if len(histogram) == 3:
            if max_count == 3:
                return "3"  # "three_of_a_kind"
            if max_count == 2:
                return "4"  # "two_pair"
        if max_count == 2:
            return "5"  # "one_pair"
        return "6"  # "high_card"

    def cards_value(self, cards: list[Card] = None):
        use_cards = self.cards if cards is None else cards
        return "".join([str(c.get_value()) for c in use_cards])

    def hand_value(self, cards: list[Card] = None):
        use_cards = self.cards if cards is None else cards
        return "{}{}".format(self.rank_value(use_cards), self.cards_value(use_cards))


def part1(lines: list[str]):
    hands = [Hand(line) for line in lines]
    hands.sort(key=lambda h: h.hand_value(), reverse=True)
    return sum([h.bid * (idx + 1) for idx, h in enumerate(hands)])


with open("input.txt", "r") as f:
    lines = f.readlines()

print("P1: {}".format(part1(lines)))
