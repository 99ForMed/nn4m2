document.getElementById("modal-1").addEventListener("wheel", function (event) {
  event.preventDefault();
  document.getElementById("modal-body-1").scrollLeft += event.deltaY;
});

document.getElementById("modal-2").addEventListener("wheel", function (event) {
  event.preventDefault();
  document.getElementById("modal-body-2").scrollLeft += event.deltaY;
});

document.getElementById("modal-3").addEventListener("wheel", function (event) {
  event.preventDefault();
  document.getElementById("modal-body-3").scrollLeft += event.deltaY;
});

var modal1, modal2, modal3;

window.onload = (event) => {
  modal1 = new bootstrap.Modal(document.getElementById("modal-2"), {
    keyboard: false,
  });

  modal2 = new bootstrap.Modal(document.getElementById("modal-2"), {
    keyboard: false,
  });

  modal3 = new bootstrap.Modal(document.getElementById("modal-3"), {
    keyboard: false,
  });

  // modal3.toggle();

  // modal1.hide();
  // modal2.hide();
  // modal3.hide();
}

var sections = document.querySelectorAll(".modal-1 .section");

// Modal 1 indicator logic
for (i = 0; i < sections.length; i++) {
  sections[i].addEventListener("mouseover", function (e) {
    var section_num = parseInt(
      e.target.closest(".section").classList[1].slice(7)
    );

    var indicators = document.querySelectorAll(".modal-1-indicator");

    for (i = 0; i < indicators.length; i++) {
      indicators[i].classList.remove("current");
    }
    
    if (section_num < 2) {
      indicators[0].classList.add("current");
    } else if (section_num < 5) {
      indicators[1].classList.add("current");
    } else if (section_num < 12) {
      indicators[2].classList.add("current");
    } else {
      console.log("error, section_number not being read properly.");
    }
  });
}

var sections2 = document.querySelectorAll(".modal-2 .section");

// Modal 2 indicator logic
for (i = 0; i < sections2.length; i++) {
  sections2[i].addEventListener("mouseover", function (e) {
    
    var section_num = parseInt(
      e.target.closest(".section").classList[1].slice(7)
    );

    var indicators = document.querySelectorAll(".modal-2-indicator");

    for (i = 0; i < indicators.length; i++) {
      indicators[i].classList.remove("current");
    }

    console.log(section_num)
    if (section_num < 13) {
      indicators[0].classList.add("current");
    } else if (section_num < 16) {
      indicators[1].classList.add("current");
    } else if (section_num < 19) {
      indicators[2].classList.add("current");
    } else {
      console.log("error, section_number not being read properly.");
    }
  });
}

var sections3 = document.querySelectorAll(".modal-3 .section");

// Modal 3 indicator logic
for (i = 0; i < sections3.length; i++) {
  sections3[i].addEventListener("mouseover", function (e) {
    var section_num = parseInt(
      e.target.closest(".section").classList[1].slice(7)
    );

    var indicators = document.querySelectorAll(".modal-3-indicator");

    for (i = 0; i < indicators.length; i++) {
      indicators[i].classList.remove("current");
    }
    console.log(section_num)
    if (section_num < 20) {
      indicators[0].classList.add("current");
    } else if (section_num < 25) {
      indicators[1].classList.add("current");
    } else {
      console.log("error, section_number not being read properly.");
    }
  });
}
