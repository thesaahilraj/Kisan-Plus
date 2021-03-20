
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

// document.querySelector('#predict-btn').addEventListener('click', (e) => {
//     e.preventDefault()
//     var form = document.querySelector("#crop-predict")

// })
