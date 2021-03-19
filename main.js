
// ******SCROOL TO TOP******** 

var scrollToTopBtn = document.getElementById("scrollToTopBtn");
var rootElement = document.documentElement;

function scrollToTop() {
    
    rootElement.scrollTo({
        top: 0,
        behavior: "smooth"
      })
  }
  
  scrollToTopBtn.addEventListener("click", scrollToTop)