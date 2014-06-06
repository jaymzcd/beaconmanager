var socket = io();
socket.on('beacon', function(data){
  var beacon = data['beacon'];
  var rssi_bin = Math.floor(Math.abs(beacon['rssi']) / 10);

  var beacon_html_id = beacon['uuid'] + '-' + beacon['major'] + '-' + beacon['minor'];
  var beacon_id_str = '#' + beacon_html_id;
  var beacon_item = '<div class="beacon btn-primary beacon_rssi_' + rssi_bin + '" id="' + beacon_html_id + '"></div>';
  var beacon_summary = '<ul><li>' + beacon['uuid'] + '</li><li>Major: ' + beacon['major'] + ', Minor: ' + beacon['minor'] + '</ul><div class="beacon_live_data"></div>';
  var beacon_livedata = 'RSSI: ' + beacon['rssi'] + ' (<span class="beacon_proximity proximity_' + beacon['proximity'] + '">' + beacon['proximity'] + '</span>)';

  if($(beacon_id_str).length == 0) {
    $('#beacons').append(beacon_item);
    $(beacon_id_str).fadeIn().html(beacon_summary).children('.beacon_livedata').html(beacon_livedata).fadeIn();
  } else {
    $(beacon_id_str).children('.beacon_live_data').fadeOut('slow', function() {
      $(beacon_id_str).html(beacon_summary);
      $(beacon_id_str).children('.beacon_live_data').html(beacon_livedata).fadeIn();
    });
  }

});

socket.on('users', function(data) {
  $('#active_users').text(data['count']);
});
