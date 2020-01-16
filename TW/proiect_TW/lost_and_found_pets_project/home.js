
var date;

function saveJSON(){
    var myJSON = JSON.stringify(date);
    localStorage.setItem("date", myJSON);
}

window.onload = function () {

    var retrivedJSON = localStorage.getItem("date");
    if(retrivedJSON === null) {
        var culoare = "#FFFFFF";
        var accesari = 0;
        date = {"culoare": culoare, "accesari": accesari};
        saveJSON();
    }
    else {
        date = JSON.parse(retrivedJSON);
        document.body.style.backgroundColor = date.culoare;
    }

    date.accesari += 1;
    saveJSON();

    let startButton = document.getElementById("startRandom");
    var colorChange;
    startButton.onclick = function () {
          colorChange = setInterval(changeColor, 3000, document.body);
    }

    function changeColor(param1){
        let letters = '0123456789ABCDEF';
        date.culoare = "#";
        for(i = 0; i < 6; ++i){
            date.culoare += letters[Math.floor(Math.random()*16)]
        }
        param1.style.backgroundColor = date.culoare;
        saveJSON();
    }

    let stopButton = document.getElementById("stopColor");

    stopButton.onclick = function () {
        clearInterval(colorChange);
    }

    var b = document.getElementById("Seteaza_Culoarea");
    b.onclick = function () {
        var colectia = document.getElementsByName("culoareSite");
        for (let x of colectia) {
            if (x.checked) {
                date.culoare = x.value;
                document.body.style.backgroundColor = date.culoare;
                saveJSON();
            }
        }
    }

    var br = document.getElementById("random");
    br.onclick = function () {
        let letters = '0123456789ABCDEF';
        date.culoare = "#";
        for(i = 0; i < 6; ++i){
            date.culoare += letters[Math.floor(Math.random()*16)]
        }
        document.body.style.backgroundColor = date.culoare;
        saveJSON();
    }
    document.onkeydown = function (event) {

        if(event.key.toLowerCase() === "arrowleft"){
            let pozitie = document.getElementById("personalizare");
            let margine = getComputedStyle(pozitie).marginLeft;
            if(parseInt(margine) > 10){
                pozitie.style.marginLeft = parseInt(margine) - 5 + "px";
            }
        }
        if(event.key.toLowerCase() === "arrowright"){
            let pozitie = document.getElementById("personalizare");
            let margine = getComputedStyle(pozitie).marginLeft;
            if(parseInt(margine) < 200){
                pozitie.style.marginLeft = parseInt(margine) + 5 + "px";
            }
        }

    }

}