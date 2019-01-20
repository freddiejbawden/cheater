from itertools import combinations

VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# We assume the probability of someone calling cheat when you lie is 0.1, this is somewhat optimistic, but could
# be adjusted at a later date
prob_call_cheat = 0.9


def possible_moves(last_move):
    if last_move == "2":
        return ["A", "2", "3", ]
    if last_move == "3":
        return ["2", "3", "4"]
    if last_move == "4":
        return ["3", "4", "5"]
    if last_move == "5":
        return ["4", "5", "6"]
    if last_move == "6":
        return ["5", "6", "7"]
    if last_move == "7":
        return ["6", "7", "8"]
    if last_move == "8":
        return ["7", "8", "9"]
    if last_move == "9":
        return ["8", "9", "10"]
    if last_move == "10":
        return ["9", "10", "J"]
    if last_move == "J":
        return ["10", "J", "Q"]
    if last_move == "Q":
        return ["J", "Q", "K"]
    if last_move == "K":
        return ["Q", "K", "A"]
    if last_move == "A":
        return ["K", "A", "2"]


def possible_cards_to_add_to_pile(cards_in_hand, cards_to_play):
    cards = []
    for value in VALUES:
        for i in range(0, cards_in_hand[value]):
            cards.append(value)
    return combinations(cards, cards_to_play)


class AIPlayer:
    def __init__(self, starting_hand):
        self.our_hand = {}
        self.pile = {}
        self.cards_in_pile = 0
        self.other_player_hand = {}
        for value in VALUES:
            self.our_hand[value] = 0
            self.pile[value] = 0
            self.other_player_hand[value] = 0
        self.add_cards_to_hand(starting_hand)
        self.last_played_value = None

    def add_cards_to_hand(self, card_str):
        new_cards = card_str.split(" ")
        for new_card in new_cards:
            self.our_hand[new_card] += 1

    def other_player_takes_pile(self):
        for value in VALUES:
            self.other_player_hand[value] += self.pile[value]
            self.pile[value] = 0

    def you_take_pile(self, cards):
        for card in cards.split(" "):
            self.our_hand[card] += 1
            if self.other_player_hand[card] > 0:
                self.other_player_hand[card] -= 1
        for value in VALUES:
            self.pile[value] = 0

    def other_players_play(self, played_value, number_played):
        self.cards_in_pile += number_played
        if self.our_hand[played_value] - number_played < 0:
            return "CHEAT"
        else:
            return self.predict_other_player(played_value)

    def predict_other_player(self, played_value):
        # Add predicting emotions
        self.last_played = played_value
        return "TRUTH"

    def play_cards(self):
        if self.last_played is None:
            print("Something")

    def next_best_move(self, last_played_value, cards_in_hand, score_to_date, depth):
        if depth == 0:
            return 0, ""
        else:
            best_score = -float('inf')
            best_move = ""
            if last_played_value is None:
                poss_values = VALUES
            else:
                poss_values = possible_moves(last_played_value)
            for value in poss_values:
                other_player_poss_values = possible_moves(value)
                other_player_poss_values_probs = {}
                for other_player_poss_value in other_player_poss_values:
                    # We assume a uniform distribution for the other players moves, this is somewhat optimistic, but
                    # could be adjusted at a later date
                    other_player_poss_values_probs[other_player_poss_value] = 1 / len(other_player_poss_values)
                for no_cards_played in range(2, 5):
                    new_score = score_to_date + no_cards_played
                    for cards_played in possible_cards_to_add_to_pile(cards_in_hand,
                                                                      no_cards_played):  # -2 as noCardsPlayed starts at 2, but is indexed at 0
                        new_cards_in_hand = cards_in_hand.copy()
                        for card_played in cards_played:
                            new_cards_in_hand[card_played] -= 1
                        if self.our_hand[value] < no_cards_played:
                            if self.other_player_hand[value] + no_cards_played <= 4:
                                new_score = score_to_date - prob_call_cheat * no_cards_played
                                poss_future_scores = 0
                                for other_player_next_value in other_player_poss_values:
                                    score, _ = self.next_best_move(other_player_next_value, new_cards_in_hand,
                                                                   new_score,
                                                                   depth - 1)
                                    poss_future_scores += score * other_player_poss_values_probs[
                                        other_player_next_value]
                                new_score += (1 - prob_call_cheat) * poss_future_scores
                            else:
                                continue
                        else:
                            poss_future_scores = 0
                            for other_player_next_value in other_player_poss_values:
                                score, _ = self.next_best_move(other_player_next_value, new_cards_in_hand, new_score,
                                                               depth - 1)
                                poss_future_scores += score * other_player_poss_values_probs[other_player_next_value]
                            new_score += poss_future_scores
                        #print("%s, %s" % (new_score, "Say: " + str(no_cards_played) + " * " + value + ", Play: " +
                        #                 ",".join(cards_played)))
                        if new_score > best_score:
                            best_score = new_score
                            best_move = "Say: " + str(no_cards_played) + " * " + value + ", Play: " + ",".join(
                                cards_played)
            return best_score, best_move
