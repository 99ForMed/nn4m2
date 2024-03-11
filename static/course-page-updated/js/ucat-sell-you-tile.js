let allStudentTiles = document.querySelectorAll('.past-student-wrapper');
let targetTile = allStudentTiles[7];

targetTile.querySelector('.name').innerHTML = "You"
targetTile.querySelector('.percentile-numeral').innerHTML = "99th"
targetTile.querySelector('.score').innerHTML = "Scored: 3330"
targetTile.querySelector('.past-student').style.background = 'linear-gradient(180deg, #064117 0%, rgba(28, 28, 28, 0.45) 100%)'
targetTile.style.transform = 'scale(1.1)';
targetTile.querySelector('.past-student').classList.remove('active');
targetTile.querySelector('.past-student-testimonial').classList.remove('active');