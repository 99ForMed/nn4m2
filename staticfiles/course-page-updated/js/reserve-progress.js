currentReservePagePhase = 0;

function progressPhase(){
    currentReservePagePhase += 1;
    var phases = document.querySelectorAll('.phase')
    for(i = 0; i < phases.length; i++){
        phases[i].style.display = 'none';
    }
    document.querySelector('.phase'+currentReservePagePhase).style.display = ''
    
    updateProgressBar(currentReservePagePhase)
    

}

function updateProgressBar(currentReservePagePhase){
    var circles = document.querySelectorAll('.milestone');

    for(i = 0; i< circles.length; i++){
        circles[i].classList.remove('active');
        
    }
    
    document.querySelector('.milestone'+currentReservePagePhase).classList.add('active');
    
}

progressPhase();