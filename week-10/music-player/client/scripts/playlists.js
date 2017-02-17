/**
 * Playlists module
 * by Tibor
 * Methods
 *  - init OK
 *  - render OK
 *  - create OK
 *  - delete
 *  - activate
 * Loads
 *  - AJAX module
 */

var Playlists = (function () {
	var root = document.querySelector('#allplaylists');
	var listNode = root.querySelector('ul');
	var createButton = document.querySelector('#create-playlist-button');
	var playlistDialog = document.querySelector('#new-playlist');
	var cancelButton = document.querySelector('#cancel');
	var submitButton = document.querySelector('#submit');

	var playlists = [];
	var current = 0;
	var ajax = new Ajax();

	function render(){
		playlists.forEach(function(playlist){
			var li = _createPlaylistItem(playlist.name, playlist.system);
			listNode.appendChild(li);
		});
	}

	function create(name, system){
		var li = _createPlaylistItem(name, system);
		listNode.appendChild(li);
	}

	function _createPlaylistItem(name, system) {
		var li = document.createElement('li');
		li.className = 'playlist';
		li.dataset.key = current;
		current++;

		li.innerHTML = name;

		if (system != 0) {
			var del = document.createElement('span');
			del.className = 'delButton';
			del.innerHTML = '&#x2716;';
			li.appendChild(del);
		}

		li.addEventListener('click', activate);
		return li;
	}

	// delete function

	function activate() {
		var allPlaylists = document.querySelectorAll('.playlist');
		current = this.dataset.key;

		allPlaylists.forEach(function(e){
			e.className = 'playlist'
		})

		allPlaylists[current].className = 'active playlist'

		// console.log(current);
		// console.log('clicked');

		Tracks.load(parseInt(current) + 1);
  }

	function validateNewPlaylist(input) {
		var allowed = /[^a-zA-Z0-9]/;
		if (allowed.test(input)) {
			return true;
		}
	}

	return {
		init: function(){
			ajax.getPlaylists(function(res){
				playlists = res;
				render(playlists);
			});

			createButton.addEventListener('click',function(){
				if (playlistDialog.className = "hide") {
					playlistDialog.className = "show";
				}
			});

			cancelButton.addEventListener('click', function() {
			  playlistDialog.className = "hide";
			});


			submitButton.addEventListener('click', function() {
				var input = document.querySelector('#name-playlist');

				ajax.createPlaylist(input.value, function(){
					if (validateNewPlaylist(input.value)) {
						create(input.value, 0);
					} else {
						alert("Please name the playlist!");
					}
				})
			})
		},

		getPlaylists: function(){
			return playlists;
		},
	}
})();
