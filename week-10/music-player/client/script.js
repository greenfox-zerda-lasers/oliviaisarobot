// var audioPlayButton = document.getElementById('audio-play');
// audioPlayButton.addEventListener('click', function(e) {
//   if (nowPlaying.paused) {
//     nowPlaying.play();
//     audioPlayButton.className = "";
//   } else {
//     nowPlaying.pause();
//     audioPlayButton.className = "paused";
//   }
// }, false);

// let httpRequest = new XMLHttpRequest();
// httpRequest.open('GET', 'https://sheetsu.com/apis/v1.0/7654fbe24554', true); // Also try http://444.hu/feed
// httpRequest.send(null);
// httpRequest.onreadystatechange = console.log;

var playlists = JSON.parse(playlists);

// TRACKLIST CONTROLS

var current = 0;

var listAllTracks = function() {
  var tracksContainer = document.getElementById('tracklist');
  for (var i = 0; i < tracklist.length; i++) {
    var newTrack = document.createElement('li');
    newTrack.dataset.key = i;
    var newNumber = document.createElement('span');
    newNumber.className = 'tracknumber';
    newNumber.innerHTML = i + 1;
    var newTitle = document.createElement('span');
    newTitle.className = 'smalltitle';
    newTitle.innerHTML = tracklist[i].title;
    var newArtist = document.createElement('span');
    newArtist.className = 'artistbracket';
    newArtist.innerHTML = tracklist[i].artist;
    var newLength = document.createElement('span');
    newLength.className = 'length';
    newLength.innerHTML = tracklist[i].length;
    if (i === current) {
      newTrack.className = 'active track';
    } else {
      newTrack.className = 'track';
    }
    tracksContainer.appendChild(newTrack);
    newTrack.appendChild(newNumber);
    newTrack.appendChild(newTitle);
    newTrack.appendChild(newArtist);
    newTrack.appendChild(newLength);
  }
}

listAllTracks();

var allTracks = document.querySelectorAll('.track');
var currentTrack = document.getElementById('now-playing');

var listCurrent = function(trackno) {
  var currentTitle = document.getElementById('title');
  var currentArtist = document.getElementById('artist');
  var currentArtwork = document.getElementById('artwork');
  var audioLength = document.getElementById('audio-length');
  currentTitle.innerHTML = tracklist[trackno].title;
  currentArtist.innerHTML = tracklist[trackno].artist;
  currentTrack.src = tracklist[trackno].url;
  audioLength.innerHTML = tracklist[trackno].length;
  if (tracklist[trackno].artwork != '') {
    currentArtwork.innerHTML = tracklist[trackno].artwork;
  }
}

listCurrent(0); // load the first audio file by default

function selectTrack() {
  clearTimer();
  var prev = current;
  current = this.dataset.key;
  currentTrack.src = tracklist[current].url;
  allTracks[prev].className = 'track';
  allTracks[current].className = 'active';
  listCurrent(current); // reloads the selected audio file
  togglePlay();
  // currentTrack.play();
}

allTracks.forEach( function(e) {
  e.addEventListener('click', selectTrack);
})

// AUDIO CONTROLS, need: currentTrack

var playButton = document.getElementById('audio-play');

function togglePlay() {
  if (currentTrack.paused) {
    var playTimer = window.setInterval(increment, 1000);
    currentTrack.play();
    playButton.className = "playing";
    playButton.innerHTML = "&#9612; &#9612;";
  } else {
    clearTimer();
    currentTrack.pause();
    playButton.className = "paused";
    playButton.innerHTML = "&#9656;";
  }
}

var audioTimer = document.getElementById('audio-timer');

var secondCounter = 0
var minuteCounter = 0

function increment() {
  if (secondCounter < 10) {
    audioTimer.innerHTML = '0:0' + secondCounter;
    secondCounter++;
  } else if (secondCounter < 60) {
    audioTimer.innerHTML = '0:' + secondCounter;
    secondCounter++;
  } else if (secondCounter%60 === 0) {
    minuteCounter++;
    secondCounter = 0;
    audioTimer.innerHTML = minuteCounter + ':00';
  }
}

function clearTimer() {
  clearInterval(playTimer);
  secondCounter = 0;
  minuteCounter = 0;
  audioTimer.innerHTML = '0:00';
}

var playTimer = window.setInterval(increment, 1000);

// look up write a proper timer

playButton.addEventListener('click', togglePlay);

// PLAYLIST CONTROLS

var addPlaylist = document.getElementById('new-playlist');
var header = document.getElementById('header');
var playlistContainer = document.getElementById('allplaylists');
var playlistForm = document.getElementById('submit-playlist');

function createPlaylist() {
  header.className = 'hide';
  addPlaylist.className = 'hide';
}

addPlaylist.addEventListener('click', createPlaylist);

function createPlaylist(input) {
  var newPlaylist = document.createElement('li');
  newPlaylist.innerHTML = input;
  playlistContainer.appendChild(newPlaylist);
}
