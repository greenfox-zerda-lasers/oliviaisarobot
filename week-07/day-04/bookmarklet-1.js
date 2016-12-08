var bookmarklet = document.querySelector('a');
bookmarklet.setAttribute('href', "javascript: (function() {var allheadings = document.querySelectorAll('h1'); for (var i = 0; i < allheadings.length; i++) { allheadings[i].textContent = 'Green Fox Academy Conquers the World'};})()");
