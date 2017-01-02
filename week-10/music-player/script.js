
var tracklist = document.getElementById('tracklist');

var current = 0;

var listAllTracks = function() {
  for (var i = 0; i < audioCollection.length; i++) {
    var newTrack = document.createElement('li');
    newTrack.dataset.key = i;
    var newNumber = document.createElement('span');
    newNumber.className = 'tracknumber';
    newNumber.innerHTML = i + 1;
    var newTitle = document.createElement('span');
    newTitle.className = 'smalltitle';
    newTitle.innerHTML = audioCollection[i].title;
    var newArtist = document.createElement('span');
    newArtist.className = 'artistbracket';
    newArtist.innerHTML = audioCollection[i].artist;
    var newLength = document.createElement('span');
    newLength.className = 'length';
    newLength.innerHTML = audioCollection[i].length;
    if (i === current) {
      newTrack.className = 'active track';
    } else {
      newTrack.className = 'track';
    }
    tracklist.appendChild(newTrack);
    newTrack.appendChild(newNumber);
    newTrack.appendChild(newTitle);
    newTrack.appendChild(newArtist);
    newTrack.appendChild(newLength);
  }
}

listAllTracks();
var allTracks = document.querySelectorAll('.track');
var currentTitle = document.getElementById('title');
var currentArtist = document.getElementById('artist');
var currentArtwork = document.getElementById('artwork');

var nowPlaying = document.getElementById('now-playing');
nowPlaying.src = audioCollection[current].url;

function selectTrack() {
  var prev = current;
  current = this.dataset.key;
  allTracks[prev].className = 'track';
  allTracks[current].className = 'active';
  nowPlaying.src = audioCollection[current].url;
}

allTracks.forEach( function(e) {
  e.addEventListener('click', selectTrack);
})

function pauseAndPlay(e) {
  e = window.event;

  if (e.keyCode === '19') {

  }
}

window.addEventListener('keypress', pauseAndPlay);

var listCurrent = function() {
  currentTitle.innerHTML = audioCollection[current].title;
  currentArtist.innerHTML = audioCollection[current].artist;
  if (audioCollection[current].artwork != '') {
    currentArtwork.innerHTML = audioCollection[current].artwork;
  }
}

listCurrent();

function createPlaylist(input) {
  var newPlaylist = document.createElement('li');
  newPlaylist.innerHTML = input;
  playlistContainer.appendChild(newPlaylist);
}

var addPlaylist = document.querySelector('.new-playlist');
var playlistContainer = document.getElementById('allplaylists');
// addPlaylist.addEventListener('click', createPlaylist(input));

// var audio = (function() {
//
//   var audioTitle = "Track title";
//   var audioArtist = "Artist";
//   var audioLength = "00:00";
//
//   function setAudioTitle(title) {
//     audioTitle = title;
//   }
//
//   function setAudioArtist(artist) {
//     audioArtist = artist;
//   }
//
//   function setAudioLength(length) {
//     audioLength = length;
//   }
//
//   return {
//     setTitle: setAudioTitle,
//     setArtist: setAudioArtist,
//     setLength: setAudioLength
//   };
//
// })();
