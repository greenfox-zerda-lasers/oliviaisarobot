var allImages = document.querySelectorAll('img');

function changeImages() {
  for (var i = 0; i < allImages.length; i++) {
    allImages[i].setAttribute('src', 'https://s-media-cache-ak0.pinimg.com/736x/aa/00/40/aa0040a22096c2fc2d35a91b5fad1d04.jpg');
  }
}

var bookmarklet = document.querySelector('a');
bookmarklet.setAttribute('href', "javascript: var allImages = document.querySelectorAll('img'); for (var i = 0; i < allImages.length; i++) { allImages[i].setAttribute('src', 'https://s-media-cache-ak0.pinimg.com/736x/aa/00/40/aa0040a22096c2fc2d35a91b5fad1d04.jpg');};");
