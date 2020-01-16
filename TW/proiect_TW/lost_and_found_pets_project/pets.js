
window.addEventListener("load", setTime)

function setTime(){
    var myTime = setInterval(currentTime, 1000);

    function currentTime() {
        let d = new Date();
        let t = d.toLocaleTimeString();
        document.getElementById("showTime").innerHTML = t;
    }
}

// flex
// relative
// inline-block
// transition
// selectare dupa clasa
