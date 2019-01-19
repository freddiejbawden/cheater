VALUES = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class AIPlayer:
    def __init__(self, starting_hand):
        self.cards = {}
        for value in VALUES:
            self.cards[value] = 0
        self.add_cards_to_hand(starting_hand)



    def add_cards_to_hand(self, card_str):
        new_cards = card_str.split(" ")
        for new_card in new_cards:
            self.cards[new_card] += 1

    def other_players_play(self, played_value, number_played):
        if self.cards[played_value] - number_played < 0:
            return "CHEAT"
        else:
            return self.predict_other_player()

    def predict_other_player(self):
        # Add predicting emotions
        return "TRUTH"