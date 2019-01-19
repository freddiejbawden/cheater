
function generate_card_deck() {
  var deck = []
  var suits = ['H','D','S','C']
  for (var s = 0; s < 4; s++) {
    for (var v = 1; v < 14; v++) {
      deck.push({'value':v,'suit':suits[s]})
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
function generate_card_ui(card_value,suit){
  var card = document.createElement('div');
  var value = document.createElement('span');
  var symbol = ''
  if (suit == 'H') {
    symbol = '♥'
  } else if (suit == 'D') {
    symbol = '♦'
  } else if (suit == 'S') {
      symbol = '♠'
  } else {
      symbol = '♣'
  }
  if (card_value == 1) {
      value.innerHTML = 'A' + symbol
  } else if (card_value == 11) {
      value.innerHTML = 'J' + symbol
  } else if (card_value == 12) {
      value.innerHTML = 'Q' + symbol
  } else if (card_value == 13) {
      value.innerHTML = 'K' + symbol
  } else {
    value.innerHTML = card_value + symbol
  }
  $(card).addClass('card');
  if (suit == 'H'||suit =='D') {
    $(value).addClass('red');
  } else {
    $(value).addClass('black');
  }
  $(card).append(value);
  $(card).click(function() {
    $(this).toggleClass('clicked_card')
    
  });
  console.log(card)
  return card
}
function render_player_hand(player_deck) {
  for (var i = 0; i < player_deck.length; i++) {
    var card = generate_card_ui(player_deck[i]['value'],player_deck[i]['suit'])
    $(card).css('left',i*30);
    $(card).css('top',i*-1*100);
    $('.hand').append(card)
  }
  $('.hand').css('margin-bottom',-100*player_deck.length);
}
$(document).ready(function() {
  console.log('test')
  generate_card_deck()
  player_deck = getRandomSubarray(generate_card_deck(),17);
  console.log(player_deck)
  render_player_hand(player_deck)
});
