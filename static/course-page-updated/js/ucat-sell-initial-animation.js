document.addEventListener("DOMContentLoaded", function() {
    const pastStudents = document.querySelector('.past-students');
    const bottomCopy = document.querySelector('.bottom-copy');
    const miniNav = document.querySelector('.mini-nav');
    const ucatsell = document.querySelector('.ucat-sell');
    const aceUcatCopy = document.querySelector('.ace-the-ucat-copy')
    const vw = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0)
    const vh = Math.max(document.documentElement.clientHeight || 0, window.innerHeight || 0)
    const navbar = document.querySelector('.navbar')

    if(vw > 992){
        window.addEventListener('scroll', function() {
            const scrollPosition = window.scrollY;
    
            pastStudents.style.transition = 'all 0.8s'
            bottomCopy.style.transition = 'all 0.8s'
            aceUcatCopy.style.transition = 'all 0.8s'
            ucatsell.style.transition = 'all 0.8s'
    
            if (scrollPosition > 1000) {
                // Action 1: Scale .past-students to double its size
                ucatsell.style.transform = 'translateY(-105vh)'
                pastStudents.style.transform = '';
                bottomCopy.style.transform = '';
                aceUcatCopy.style.transform = 'translateY(-100px)';
                ucatsell.style.visibility = 'hidden'
                navbar.style.backgroundColor = "#111111"
    
            }else if (scrollPosition > 500) {
                // Action 1: Scale .past-students to double its size
                pastStudents.style.transform = 'scale(2) translateY(-50vh)';
                bottomCopy.style.transform = 'scale(2) translateY(-15vh)';
                aceUcatCopy.style.transform = 'scale(2) translateY(-10vh)';
                ucatsell.style.transform = ''
                ucatsell.style.visibility = ''
                ucatsell.style.opacity = ''
                navbar.style.backgroundColor = "rgba(0,0,0,0)"
                
            }else if(scrollPosition <= 100){
                pastStudents.style.transform = '';
                bottomCopy.style.transform = '';
                aceUcatCopy.style.transform = '';
                ucatsell.style.transform = ''
                ucatsell.style.opacity = ''
                navbar.style.backgroundColor = "#0D1810"
                
    
    
            }
    
            
    
           
        });
    }else{
        window.addEventListener('scroll', function() {
            const scrollPosition = window.scrollY;
    
            pastStudents.style.transition = 'all 0.8s'
            bottomCopy.style.transition = 'all 0.8s'
            aceUcatCopy.style.transition = 'all 0.8s'
            ucatsell.style.transition = 'all 0.8s'
    
            if (scrollPosition > 1000) {
                // Action 1: Scale .past-students to double its size
                ucatsell.style.transform = 'translateY(-105vh)'
                pastStudents.style.transform = '';
                bottomCopy.style.transform = '';
                aceUcatCopy.style.transform = 'translateY(-100px)';
                ucatsell.style.visibility = 'hidden'
                
    
            }else if (scrollPosition > 300) {
                // Action 1: Scale .past-students to double its size
                pastStudents.style.transform = 'scale(1.5) translateY(-50vh)';
                bottomCopy.style.transform = 'scale(1.2) translateY(-15vh)';
                aceUcatCopy.style.transform = 'scale(1.2) translateY(-10vh)';
                ucatsell.style.transform = ''
                ucatsell.style.visibility = ''
                ucatsell.style.opacity = ''
            }else if(scrollPosition <= 100){
                pastStudents.style.transform = '';
                bottomCopy.style.transform = '';
                aceUcatCopy.style.transform = '';
                ucatsell.style.transform = ''
                ucatsell.style.opacity = ''
            }
    
            
    
            
        });
    }
    
});