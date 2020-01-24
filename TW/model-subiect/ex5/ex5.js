
window.addEventListener("click", function (event) {
    var elem = document.createElement("div");

    document.body.appendChild(elem);
    elem.style.position="absolute";
    elem.className = "animat";

    stil = getComputedStyle(elem);



    elem.style.top = event.pageY - parseInt(stil.height)/2 + "px";
    elem.style.left = event.pageX - parseInt(stil.height)/2 + "px";

    var rand = Math.floor(Math.random()*2);
    if(rand === 0){
        elem.style.animationName = "miscare1";
    }
    else{
        elem.style.animationName = "miscare2";
    }

    elem.onclick = function (e) {
        e.stopPropagation();
    }

})
