var config = {
  'number_of_cards_removed':10
}
function create_deck() {
  deck = []
  for (var s = 0; s < 4; s++) {
    for (var v = 1; v = 14; v++) {
      deck.push({value:v,suit:s})
    }
  }
  return deck
}
function getRandomSubarray(arr, size) {
    var shuffled = arr.slice(0), i = arr.length, temp, index;
    while (i--) {
        index = Math.floor((i + 1) * Math.random());
        temp = shuffled[index];
        shuffled[index] = shuffled[i];
        shuffled[i] = temp;
    }
    return shuffled.slice(0, size);
}
function prepare_deck() {
  deck = create_deck()
  deck = getRandomSubarray(deck, config["number_of_cards_removed"])
  return deck
}
function get_card_ui(card) {
  card = document.createElement('div')
  card_span = document.createElement('span')
  suits = [♥,♦,♠,♣]
  if (card["value"] == 1) {
    card_span.innerHTML = "A" + suits[card["suit"]]
  } else if (card["value"] == 11) {
    card_span.innerHTML = "J" + suits[card["suit"]]
  }else if (card["value"] == 12) {
    card_span.innerHTML = "Q" + suits[card["suit"]]
  }else if (card["value"] == 13) {
    card_span.innerHTML = "K" + suits[card["suit"]]
  }
  if (card["suit"] <= 1) {
    $(card_span).addClass('red')
  } else {
    $(card_span).addClass('black')
  }
  card.append(card_span)
  $(card).addClass('card');

}
