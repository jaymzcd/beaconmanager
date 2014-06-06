var express = require('express');
var Bleacon = require('bleacon');
var app = express();
var fs = require('fs');
var http = require('http');
var querystring = require('querystring');
var server = http.createServer(app);
var io = require('socket.io').listen(server);

app.use('/static', express.static(__dirname + '/static'));
app.use(express.urlencoded());

var users = 0;

Bleacon.on('discover', function(bleacon) {
  console.log('bleacon found: ' + JSON.stringify(bleacon));
  io.emit('beacon', {for: 'everyone', beacon: bleacon});
});

Bleacon.startScanning();

app.get('/uuid/:beacon/:major/:minor/', function(req, res){
  res.sendfile('templates/beacon.html');
});

app.post('/uuid/:beacon/:major/:minor/', function(req, res){
    var filePath = __dirname + '/public/' + req.params.beacon + '.json';
    fs.writeFile(filePath, req.body.data, function () {
        res.redirect('/data/' + req.params.beacon + '/' + req.params.major + '/' + req.params.minor + '/');
    });
});

app.get('/data/:beacon/:major/:minor/', function(req, res){
  var filePath = __dirname + '/public/' + req.params.beacon + '.json';
  fs.readFile(filePath, function(err, data) {
    res.send(data);
  });
});

app.get('/', function(req, res){
  res.sendfile('templates/index.html');
});

app.post('/', function(req, res){

  var data = querystring.stringify({
        uuid: req.body.uuid,
        major: req.body.major,
        minor: req.body.minor
      });

  var options = {
      host: 'localhost',
      port: 8000,
      path: '/beacon/add/',
      method: 'POST',
      headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Content-Length': Buffer.byteLength(data)
      }
  };

  var req = http.request(options, function(res) {
      res.setEncoding('utf8');
      res.on('data', function (chunk) {
          console.log("body: " + chunk);
      });
  });

  req.write(data);
  req.end();

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
