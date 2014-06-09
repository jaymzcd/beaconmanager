var socket = io();

socket.on('beacon', function(data){
  var beacon = data['beacon'];
  var rssi_bin = Math.floor(Math.abs(beacon['rssi']) / 10);
  var date = new Date();

  var beacon_html_id = beacon['uuid'] + '-' + beacon['major'] + '-' + beacon['minor'];
  var beacon_id_str = '#' + beacon_html_id;
  var beacon_item = '<div class="beacon beacon_rssi_' + rssi_bin + ' proximity_' + beacon['proximity'] + '" id="' + beacon_html_id + '"></div>';
  var beacon_summary = '<ul><li><a href="/uuid/' + beacon['uuid'] + '/' + beacon['major'] + '/' + beacon['minor'] + '/' + '">' + beacon['uuid'] + '</a></li><li>Major: ' + beacon['major'] + ', Minor: ' + beacon['minor'] + '</ul><div class="beacon_live_data"></div>';
  var beacon_livedata = '<p>RSSI: ' + beacon['rssi'] + ' (<span class="beacon_proximity">' + beacon['proximity'] + '</span>) ';
  beacon_livedata += ', Last seen: ' + date.toLocaleTimeString() + '</p>';

  if (beacon['major'] == 10) {
    var opt = {
      type: "basic",
      title: "Primary Title",
      message: "Primary message to display",
      iconUrl: "url_to_small_icon"
    }
  }

  if($(beacon_id_str).length == 0) {
    $('#beacons').append(beacon_item);
    $(beacon_id_str).fadeIn().html(beacon_summary).children('.beacon_live_data').html(beacon_livedata).fadeIn();
  } else {
    $(beacon_id_str).children('.beacon_live_data').fadeOut('slow', function() {
      $(beacon_id_str).html(beacon_summary);
      $(beacon_id_str).children('.beacon_live_data').html(beacon_livedata).fadeIn();
    });
  }

  $.post('/', {
    uuid: beacon['uuid'],
    major: beacon['major'],
    minor: beacon['minor']
  });

});


socket.on('users', function(data) {
  var label = data['count'];
  
  if(data['count'] == 1) {
    label += ' user';
  } else {
    label += ' users';
  }

  $('#active_users').text(label);
});
