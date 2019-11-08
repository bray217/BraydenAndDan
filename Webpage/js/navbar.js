document.addEventListener('DOMContentLoaded', function() { //differnt event handler for makig sure the page has loaded before changing it.
    window.addEventListener('scroll', scrollFunction);
      //listener for scrolling
    //variable declaring
    var header = document.getElementById("myHeader");
    var navButton1 = document.getElementById("navButton1"); //have to have 6 because each button has to have a unique id, it doesn't work otherwise.
    var navButton2 = document.getElementById("navButton2");
    var navButton3 = document.getElementById("navButton3");
    var navButton4 = document.getElementById("navButton4");
    var navButton5 = document.getElementById("navButton5");
    var navButton6 = document.getElementById("navButton6");
    var title = document.getElementById("title");
    var sticky = header.offsetTop;

    function scrollFunction() {
      console.log("scrollFunction working")
      if (window.pageYOffset > sticky){
        header.classList.add("sticky"); //adds a HTML class atribute to header, this has spesfic CSS to make it scroll
        navButton1.style.fontSize = "16px"; //changing the font size of everything in the header.
        navButton2.style.fontSize = "16px";
        navButton3.style.fontSize = "16px";
        navButton4.style.fontSize = "16px";
        navButton5.style.fontSize = "16px";
        navButton6.style.fontSize = "16px";
        title.style.fontSize="35px";
      } else{
        header.classList.remove("sticky");  //removes everything when it hits the top.
        navButton1.style.fontSize = "22px";
        navButton2.style.fontSize = "22px";
        navButton3.style.fontSize = "22px";
        navButton4.style.fontSize = "22px";
        navButton5.style.fontSize = "22px";
        navButton6.style.fontSize = "22px";
        title.style.fontSize="50px";
      }
    }
  })