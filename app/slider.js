box_color_scale = ['#67ce23','#73c823','#7dc123','#85bb23','#8eb423','#94ae23','#9ba823','#a1a123','#a69a23','#ab9423','#b08c23','#b48523','#b87d23','#bc7623','#bf6d23','#c36423','#c65c23','#c95123','#cb4623','#ce3923']
function updateThermometer(val) {
  $('#t').css('height',val + '%');
  return
}

$(document).ready(function() {

  $('#thermo_range').change(function() {
    updateThermometer(this.value)
  });
  at = ['a','b','c','d']
  vl = [20,30,60,70]
  for (var i = 0; i < 4; i++) {
    $('#attribute_values').append(create_attribute_box(at[i],vl[i]))
  }

})


function create_attribute_box(att,val) {
  var cont = document.createElement('div');
  var att_span =  document.createElement('span');
  att_span.innerHTML = att + ': ' + val
  $(cont).append(att_span)
  bg_idx = Math.floor(val/5)
  $(cont).css('background-color',box_color_scale[bg_idx]);
  $(cont).addClass('attribute_box')
  return cont;
}
