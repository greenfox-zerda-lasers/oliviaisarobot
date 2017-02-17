'use strict';

// methods needed
// - load (url)
// - play
// - pause
// - seek (%)
// - volume (0-100)
// - mute
// events needed
// - timeupdate
// - ended

var Audio = (function() {

  var audioNode = document.getElementById('audio');
  var timeCallback = function(){};
  var endCallback = function(){};

  audioNode.addEventListener('timeupdate', function() {
    timeCallback(audioNode.currentTime / audioNode.duration * 100);
  })

  audioNode.addEventListener('ended', function() {
    endCallback();
  })

  function setUpdateEvent(cb) {
    timeCallback = cb;
  }

  function setCompleteEvent(cb) {
    endCallback = cb;
  }

  // IN FRONTEND
  // audio.onUpdate (function (time) {
  //   slider.value = time;
  //   console.log(time);
  // })

  function load(url) {
    audioNode.src = url;
  }

  function play() {
    audioNode.play();
  }

  function pause() {
    audioNode.pause();
  }

  // expects value between 0-100
  function seek(percent) {
    audioNode.currentTime = audioNode.duration * percent / 100;
  }

  // expects value between 0-1
  function volume(vol) {
    if (vol = 0.0) {
      audioNode.muted = true;
    } else {
      audioNode.muted = false;
      audioNode.volume = vol;
    }
  }

  function mute() {
    if (audioNode.muted = false) {
      audioNode.muted = true;
    } else {
      audioNode.muted = false;
    }
  }

  function paused() {
    return audioNode.paused;
  }

  return {
    load: load,
    play: play,
    pause: pause,
    seek: seek,
    onUpdate: setUpdateEvent,
    onComplete: setCompleteEvent,
    volume: volume,
    mute: mute,
    paused: paused,
  }

})();
