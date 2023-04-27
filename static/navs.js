function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
function getout(){
document.getElementById("menu").style.display="none";
}

const nav1 =document.querySelector(".navigation");
let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
    if(
        lastScrollY < window.scrollY
      
    )
    {
        nav1.classList.add("navigation--hidden");
  
    } else {
        nav1.classList.remove("navigation--hidden");
        
    }
    lastScrollY = window.scrollY
});

