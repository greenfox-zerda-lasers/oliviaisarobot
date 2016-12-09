var imageGallery = [
  {
    url: 'url(images/01.jpg)',
    title: 'Entwined lives',
    author: 'by Tim Laman, US',
    description: 'An endangered young male Bornean Orangutan climbs over 30 meters up in the rain forest of Gunung Palung National Park in Indonesian Borneo. The park is one of the few protected orangutan environments in Borneo.'
  },
  {
    url: 'url(images/02.jpg)',
    title: 'The alley cat',
    author: 'by Nayan Khanolkar, India',
    description: 'At night, in a suburb of Mumbai bordering Sanjay Gandhi National Park, leopards slip ghost-like through the maze of alleys, looking for food. Especially stray dogs.'
  },
  {
    url: 'url(images/03.jpg)',
    title: 'The moon and the crow',
    author: 'by Gideon Knight, UK',
    description: 'A crow perching in a tree is a common scene in a London park, but when set against the blue light of dusk and a full moon it felt "almost supernatural, like something out of a fairy tale," says Gideon.'
  },
  {
    url: 'url(images/04.jpg)',
    title: 'The pangolin pit',
    author: 'by Paul Hilton, UK/Australia',
    description: 'Paul Hilton captured this scene of some 4,000 defrosting pangolins from one of the largest seizures on record of the heavily trafficked animals. The scaly mammals are prized in China and Vietnam for their exotic meat and for their scales used in traditional medicine.'
  },
  {
    url: 'url(images/05.jpg)',
    title: 'Snapper party',
    author: 'by Tony Wu, US',
    description: 'Thousands of two‑spot red snapper fish gather to spawn around Palau in the western Pacific Ocean for several days each month in sync with the full moon of the lunar cycle.'
  },
  {
    url: 'url(images/06.jpg)',
    title: 'Requiem for an owl',
    author: 'by Mats Andersson, Sweden',
    description: 'A solitary Eurasian pygmy owl was photographed by Mats Andersson after he discovered the owl\'s mate lying dead on the forest floor. "The owl\'s resting posture reflected my sadness for its lost companion," says Andersson.'
  },
  {
    url: 'url(images/07.jpg)',
    title: 'A tale of two foxes',
    author: 'by Don Gutoski, Canada',
    description: 'In the Canadian tundra, the range of red foxes is extending northwards, where they increasingly cross paths with their smaller relatives, the Arctic fox. For Arctic foxes, red foxes now represent not just their main competitor - both hunt small animals such as lemmings - but also their main predator.'
  },
  {
    url: 'url(images/08.jpg)',
    title: 'Still life',
    author: 'by Edqin Giebers, The Netherlands',
    description: 'Suspended near the surface, a crested newt pauses to rest in the cold waters of early spring.'
  },
];

var imgUrl = document.querySelector('.photo-display');
var imgTitle = document.getElementById('title');
var imgAuthor = document.getElementById('author');
var imgDescription = document.getElementById('description');

var imgGallery = document.querySelector('.gallery');

var leftButton = document.querySelector('.left');
var rightButton = document.querySelector('.right');

var current = 0;

var allThumbnails = function() {
  for (var i = 0; i < imageGallery.length; i++) {
    var newThumb = document.createElement('div');
    var newImg = document.createElement('img');
    if (i === current) {
      newThumb.className = 'thumbnail selected';
    } else {
      newThumb.className = 'thumbnail';
    }
    newImg.setAttribute('src', 'images/0' + (i + 1) + '.jpg');
    newImg.setAttribute('alt', imageGallery[i].title);
    newImg.dataset.key = i;
    newThumb.appendChild(newImg);
    imgGallery.appendChild(newThumb);
  }
}

allThumbnails();
var imgThumbnails = document.querySelectorAll('.thumbnail');

function displayImage() {
  imgUrl.style.backgroundImage = imageGallery[current].url;
  imgTitle.textContent = imageGallery[current].title;
  imgAuthor.textContent = imageGallery[current].author;
  imgDescription.textContent = imageGallery[current].description;
}

function nextImage() {
  if (current !== imageGallery.length - 1) {
    imgThumbnails[current].classList.remove('selected');
    current++;
    displayImage();
    imgThumbnails[current].classList.add('selected');
  } else {
    imgThumbnails[current].classList.remove('selected');
    current = 0;
    displayImage();
    imgThumbnails[current].classList.add('selected');
  }
};

function previousImage() {
  if (current !== 0) {
    imgThumbnails[current].classList.remove('selected');
    current--;
    displayImage();
    imgThumbnails[current].classList.add('selected');
  } else {
    imgThumbnails[current].classList.remove('selected');
    current = imageGallery.length - 1;
    displayImage();
    imgThumbnails[current].classList.add('selected');
  }
};

function navigate() {
  var prev = current;
  current = this.dataset.key;
  imgThumbnails[prev].classList.remove('selected');
  displayImage();
  imgThumbnails[current].classList.add('selected');
};

rightButton.addEventListener('click', nextImage);
leftButton.addEventListener('click', previousImage);

imgThumbnails.addEventListener('click', navigate);
