'use strict';

var express = require('express');
var app = express();
var mysql = require('mysql');
var bodyParser = require('body-parser');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "greenfox-todo-app"
});

con.connect();

app.use(bodyParser.json());

app.use(
  express.static(__dirname + '/client')
);

app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/todos', function(req, res) {
  con.query('SELECT * FROM todos', function(err, rows, fields) {
    if (err) throw err;
    res.send(rows);
  });
});

app.post('/new', function(req, res) {
  con.query({
    sql: 'INSERT INTO `todos` (`name`) VALUES ("'+req.body.name+'")'}, function(err, rows, fields) {
    if (err) throw err;
    res.send(rows);
  });
});

// PUT request to change todo status

// DELETE request to remove todo

app.listen(3000, function(req, res) {
  console.log('Server is running on port')
});
