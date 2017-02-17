/**
 * Control Panel module
 * by Tibor
 * Methods
 *  - play(url)
 *  - next
 *  - previous
 */
 var ControlPanel = (function () {
 // 	var trackDir = 'file:///C:/dev/greenfox/syllabus/solutions-reviews/foxplayer/server/tracks/';
 	var root = document.querySelector('#control-panel');
 	var prevButton = root.querySelector('#audio-rewind');
 	var nextButton = root.querySelector('#audio-forward');
 	var playButton = root.querySelector('#audio-play');
 	var seekBar = root.querySelector('.progress');
 	var timerLabel = root.querySelector('#audio-timer');
 // 	var loadButton = root.querySelector('button'); // This is temporary

 // 	loadButton.addEventListener('click', function(){
 // 		load('01 Nightkraken.mp3');
 // 		console.log('loaded');
 // 	});

 	playButton.addEventListener('click', togglePlay);

  window.addEventListener('keydown', function(event) {
    if (event.keyCode === 32) {
      togglePlay();
    }
  })

  window.addEventListener('keydown', function(event) {
    if (event.keyCode === 78) {
      toggleNext();
    }
  })

  window.addEventListener('keydown', function(event) {
    if (event.keyCode === 80) {
      togglePrevious();
    }
  })

  window.addEventListener('keydown', function(event) {
    if (event.keyCode === 27) {
      Audio.mute();
    }
  })

  function togglePlay() {
    if( Audio.paused() ){
 			this.innerHTML = 'PAUSE';
 			Audio.play();
 		} else {
 			this.innerHTML = 'PLAY';
 			Audio.pause();
 		}
  }

 	function load(fileName) {
		Audio.load(trackDir + fileName);

		Audio.onUpdate(function( percent, time ){
			seekBar.value = percent;
			timerLabel.innerHTML = format(time);
		});
		// audio.onComplete(function(){
		// 	console.log('READY');
		// });
 	}

	function format(s) {
        var s = Math.floor((s) % 60);
        if (s < 10) { s = "0"+s; }
        return Math.floor(s/60) + ":" + s;
	}

 	return {
 		// play: play
 	}

 })();
