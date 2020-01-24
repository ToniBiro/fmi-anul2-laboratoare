


function myFunc() {
    var but = document.createElement("button");
    var but1 = document.createElement("button");
    var but2 = document.createElement("button");
    var but3 = document.createElement("button");
    var but4 = document.createElement("button");
    var but5 = document.createElement("button");
    var but6 = document.createElement("button");
    var but7 = document.createElement("button");
    var but8 = document.createElement("button");
    var but9 = document.createElement("button");

    var v = [but, but1, but2, but3, but4, but5, but6, but7, but8, but9];

    for(let i = 0; i < 10; ++i) {
        document.body.appendChild(v[i]);
        v[i].innerHTML = 0;
    }

    for(let i = 0; i < 10; ++i) {
        v[i].onclick = setInterval(function () {
            v[i].nextElementSibling.innerHTML += 1

        }, 1000);
    }

}
window.onload = setTimeout(myFunc, 1500)
