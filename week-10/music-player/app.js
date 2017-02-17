'use strict';

var mysql = require('mysql');
var express = require('express');
var app = express();
var fs = require('fs');
var bodyParser = require('body-parser');
var meta = require('musicmetadata');
var async = require('async');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "",
  database: "mydb"
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

app.get('/playlists', function(req, res) {
  con.query('SELECT * FROM playlists', function(err, rows, fields) {
    if (err) throw err;
    res.send(rows);
  });
});

app.post('/playlists', function(req, res) {
  con.query({
    sql: 'INSERT INTO `playlists` (`name`) VALUES ("'+req.body.name+'")',
    // values: ['3', ]
  }, function(err, rows, fields) {
    if (err) throw err;
    res.send(rows);
  });
});

app.get('/tracks', function(req, res) {
  fs.readdir('./root', function (err, files) {
		var coll = [];
    // console.log(files);
		async.each(
			files,
			function (file, callback){
				meta(fs.createReadStream('./root/' + file), { duration: true }, function (err, metadata) {
					metadata.fileName = file;
					coll.push(metadata);
				 	callback();
				});
			},
			function(err) {
        if (err) throw err;
  			res.json(coll);
			}
		);
	});
});

app.get('/files', function(req, res) {
  con.query('SELECT * FROM tracks', function(err, rows, fields) {
    if (err) throw err;
    res.send(rows);
  });
})

// app.get('tracks/:id'), function(req, res) {
//   var playlistIds = []
//     playlists.forEach(function(e) {
//       playlistIds.push(e.id);
//     });
//     // console.log(playlistIds);
//     if (false === playlistIds.includes(req.params.id)) {
//       res.sendStatus(404);
//       console.log('ID does not exist');
//     } else {
//       function remaining(el) {
//         return el.playlist_id.includes(req.params.id);
//       }
//       var temp = tracks.filter(remaining);
//       // console.log(temp);
//       res.json(temp);
//     }
// }

app.get('/files/:id', function(req, res) {
  if (req.params.id == '1') {
    con.query('SELECT * FROM tracks', function(err, rows) {
      if (err) throw err;
      res.json(rows);
    });
  } else if (req.params.id != '1') {
    con.query('SELECT * FROM tracks WHERE playlist_id=?', [req.params.id], function(err, rows) {
      if (err) throw err;
      res.json(coll);
    });
  }
});

// fs.readdir('./root', function (err, files) {
//   var coll = [];
//   console.log(files);
//   async.each(files, function (file, callback) {
//       meta(fs.createReadStream('./root/' + file), function (err, metadata) {
//         coll.push(metadata);
//         callback();
//       });
//   }, function(err) {
//     if (err) throw err;
//     console.log(coll);
//   })
// });
//
// app.delete('/playlists/:id', function (req, res) {
//   function remaining(el) {
//     return el.id != req.params.id;
//   }
//   playlists = playlists.filter(remaining);
//   res.json(playlists);
// })
//
// app.get('/playlist-tracks', function (req, res) {
//   res.json(tracks);
// })
//
// app.get('/playlist-tracks/:id', function (req, res) {
//   var playlistIds = []
//   playlists.forEach(function(e) {
//     playlistIds.push(e.id);
//   });
//   // console.log(playlistIds);
//   if (false === playlistIds.includes(req.params.id)) {
//     res.sendStatus(404);
//     console.log('ID does not exist');
//   } else {
//     function remaining(el) {
//       return el.playlist_id.includes(req.params.id);
//     }
//     var temp = tracks.filter(remaining);
//     // console.log(temp);
//     res.json(temp);
//   }
// })
//

app.listen(3000, function(req, res) {
  console.log('Server is running on port 3000')
});

// con.end();
