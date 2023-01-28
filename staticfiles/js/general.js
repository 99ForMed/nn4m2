
try{
    document.getElementById('secondary-qualifiers-part-b').style.display = 'none'
    document.getElementById('secondary-qualifiers-part-c').style.display = 'none';
}catch(e){
    null
}
try{
    document.getElementById('interview-section').style.display = 'none'
    document.getElementById('seminars-section').style.display = 'none'
}catch(e){
    null
}

function activate(id_to_activate, id_to_deactivate, id_to_deactivate2){
    document.getElementById(id_to_activate).classList.add('active');
    document.getElementById(id_to_deactivate).classList.remove('active');
    document.getElementById(id_to_deactivate2).classList.remove('active');
    if(id_to_activate == 'ucat-toggle'){
        document.getElementById('ucat-section').style.display = '';
        document.getElementById('interview-section').style.display = 'none';
        document.getElementById('seminars-section').style.display = 'none';
    }else if(id_to_activate == 'interview-toggle'){
        document.getElementById('ucat-section').style.display = 'none';
        document.getElementById('interview-section').style.display = '';
        document.getElementById('seminars-section').style.display = 'none';
        }
    else{
        document.getElementById('ucat-section').style.display = 'none';
        document.getElementById('interview-section').style.display = 'none';
        document.getElementById('seminars-section').style.display = '';
    }
}

function showPartBEligibilityForm(){

    if(parseInt(document.getElementById('hours-amount').value) > 90){
        document.getElementById('secondary-qualifier-form').submit()
    }else{
        document.getElementById('secondary-qualifiers-part-a').style.display = 'none';
        document.getElementById('secondary-qualifiers-part-b').style.display = '';
    }

    
    
}

function showPartCEligibilityForm(){
    document.getElementById('ucat-plan').setAttribute('readonly', true)
    document.getElementById('commitment-explanation').setAttribute('readonly', true)
    document.getElementById('disappear').style.display = 'none'
    document.getElementById('secondary-qualifiers-part-c').style.display = '';

}

function playPauseVideo() {
    let videos = document.querySelectorAll("landing-vid");
    videos.forEach((video) => {
        // We can only control playback without insteraction if video is mute
        video.muted = true;
        // Play is a promise so we need to check we have it
        let playPromise = video.play();
        if (playPromise !== undefined) {
            playPromise.then((_) => {
                let observer = new IntersectionObserver(
                    (entries) => {
                        entries.forEach((entry) => {
                            if (
                                entry.intersectionRatio !== 1 &&
                                !video.paused
                            ) {
                                video.pause();
                            } else if (video.paused) {
                                
                                video.play();
                            }
                        });
                    },
                    { threshold: 0.2 }
                );
                observer.observe(video);
            });
        }
    });
}

// And you would kick this off where appropriate with:
try{
    playPauseVideo();
}
    
catch(e){
    null
}
    