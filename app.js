var express = require('express');
var Bleacon = require('bleacon');
var app = express();
var http = require('http');
var server = http.createServer(app);
var io = require('socket.io').listen(server);

app.use('/static', express.static(__dirname + '/static'));
var users = 0;

Bleacon.on('discover', function(bleacon) {
  console.log('bleacon found: ' + JSON.stringify(bleacon));
  io.emit('beacon', {for: 'everyone', beacon: bleacon});
});

Bleacon.startScanning();

app.get('/', function(req, res){
  res.sendfile('templates/index.html');
});

io.on('connection', function(socket){
  users = users + 1;
  console.log('a user connected', users);
  io.emit('users', {for: 'everyone', count: users});

  socket.on('disconnect', function(socket){
    users = users - 1;
    console.log('a user disconnected', users);
    io.emit('users', {for: 'everyone', count: users});
  });

});


server.listen(3000, function() {
    console.log('Listening on port %d', server.address().port);
});
