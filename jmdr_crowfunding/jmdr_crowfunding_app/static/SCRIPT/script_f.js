// INTENTO 1
// 'use strict'

// const grande    =document.querySelector('.grande')
// const punto     =document.querySelectorAll('.punto')

// punto.forEach( (cadapunto, i) => {
//     punto[i].addEventListener('click', () =>{

//         let posicion = i
//         let operacion = posicion * -25

//         grande.style.transform = `translateX(${operacion}%)`

//         punto.forEach( (cadapunto, i) => {
//             punto[i].classList.remove('activo')
//         })
//         punto[i].classList.add('activo')
//     })
// })

// INTENTO 2
// const prev = document.querySelector('.prev');
// const next = document.querySelector('.next');
// const images = document.querySelector('.carousel').children;
// const totalImages = images.length;
// let index = 0;

// prev.addEventListener('click', () => {
//   nextImage('prev');
// })

// next.addEventListener('click', () => {
//   nextImage('next');
// })

// function nextImage(direction) {
//   if(direction == 'next') {
//     index++;
//     if(index == totalImages) {
//       index = 0;
//     }
//   } else {
//     if(index == 0) {
//       index = totalImages - 1;
//     } else {
//       index--;
//     }
//   }

//   for(let i = 0; i < images.length; i++) {
//     images[i].classList.remove('main');
//   }
//   images[index].classList.add('main');
// }

// INTENTO 3
var slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}