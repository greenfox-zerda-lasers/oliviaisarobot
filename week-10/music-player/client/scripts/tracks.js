/**
 * Tracks module
 * by Tibor
 * Methods
 *  - load
 *  - render
 *  - delete
 *  - activate
 * Loads
 *  - AJAX module
 *  - add to playlist
 *  - add to favorite
 *  - activate (current)
 */

var Tracks = (function() {
  var root = document.querySelector('#tracklist');
  var playlistButton = document.querySelector('track-to-playlist');
  var favoriteButton = document.querySelector('track-to-favorite');

  var audioNode = document.querySelector('#now-playing');

  var allTracks = [];
  var currentTracks = [];
  var current = 0;
  var url = '';
  var ajax = new Ajax();

  function render(){
    var listNode = document.querySelector('ol');
 		allTracks.forEach(function(tracklist){
 			var li = _createTracklistItem(tracklist.title, tracklist.artist['0'], tracklist.duration);
 			listNode.appendChild(li);
    });
    current = 0;
  };

  function _createTracklistItem(title, artist, length) {
		var li = document.createElement('li');
    li.className = 'track';
    li.dataset.key = current;
    current++;

    var newNumber = document.createElement('span');
    newNumber.className = 'tracknumber';
    var newTitle = document.createElement('span');
    newTitle.className = 'smalltitle';
    newTitle.innerHTML = title;
    var newArtist = document.createElement('span');
    newArtist.className = 'artistbracket';
    newArtist.innerHTML = artist;
    var newLength = document.createElement('span');
    newLength.className = 'length';
    newLength.innerHTML = format(length);

    li.appendChild(newTitle);
    li.appendChild(newArtist);
    li.appendChild(newLength);

    li.addEventListener('click', activate);

    return li;
	}

  function activate() {
    var all = document.querySelectorAll('.track');
    var prev = current;
    current = this.dataset.key;

    all[prev].className = 'track';
		all[current].className = 'active track';

    displayCurrent(current);

    url = 'root/' + allTracks[current].fileName;

    audioNode.src = url;
    audioNode.play();
  }

  function toggle() {
    if (audioNode.paused) {
      audioNode.play();
    } else {
      audioNode.pause();
    }
  }

  function format(time) {
    var mins = ~~(time / 60);
    var secs = Math.floor(time % 60);
    var ret = "";
    ret += "" + mins + ":" + (secs < 10 ? "0" : "");
    ret += "" + secs;
    return ret;
	}

  function load(id) {
    ajax.getPlaylistById(id, function(res) {
      currentTracks = res;
    });
    console.log(currentTracks);
    console.log(allTracks);
    console.log(id);
    if (id === 1) {
      render();
    } else if (id != 1) {
      allTracks = currentTracks;
      render();
    }
  }

  function displayCurrent(trackno) {
    var currentTitle = document.getElementById('title');
    var currentArtist = document.getElementById('artist');
    var audioLength = document.getElementById('audio-length');
    // var currentArtwork = document.getElementById('artwork');

    currentTitle.innerHTML = allTracks[trackno].title;
    currentArtist.innerHTML = allTracks[trackno].artist;
    // console.log(tracks[trackno]);
    audioLength.innerHTML = format(allTracks[trackno].duration);
    // if (tracklist[trackno].artwork != '') {
    //   currentArtwork.innerHTML = tracks[trackno].artwork;
    // }
  }

  return {
		init: function(){
			ajax.getTracks(function(res){
				allTracks = res;
			});

      window.addEventListener('keydown', function(event) {
        if (event.keyCode === 32) {
          toggle();
        }
      })

			// createButton.addEventListener('click',function(){
			// 	var input = prompt('Enter playlist name');
			// 	ajax.createPlaylists( input, function(rsp){
			// 		console.log(rsp)
			// 		create(input, rsp.id);
			// 	});
			// });

		},

		getTracks: function(){
			return allTracks;
		},

    load: load
	}

})();
