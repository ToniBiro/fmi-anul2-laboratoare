

window.onload = function () {
    //
    // var img = document.createElement("img");
    // img.src = "5.png"
    // document.body.appendChild(img);
    //
    // img.style.width = "20%";
    // img.style.height = "auto";
    //
    //
    // img.onclick = function () {
    //     document.body.removeChild(img);
    // }
    // // }
    // //
    // // var txn = document.createTextNode("___first text node___");
    // // var fig = document.createElement("figure");
    // // var figc = document.createElement('figcaption');
    // // var img1 = document.createElement('img');
    // //
    // // figc.appendChild(txn);
    // //
    // // fig.appendChild(img1);
    // // fig.appendChild(figc);
    // // img1.src = '5.png';
    // //
    // // document.body.appendChild(fig);
    // //
    // //
    // // var u = document.querySelector("ul");
    // // var l = document.querySelector("li");
    // // l.onclick = function()
    // // {
    // //     alert("Ai apasat primul ele din lista!");
    // // }
    // // alert(u.innerHTML += "<li class='par'>al treile rand din lista</li>");
    // // u.appendChild(l)
    // //
    // // var col1 = document.getElementsByTagName("li")
    // // for (let i = 0; i < col1.length-1; i++)
    // //     col1[i].style.color = "aqua"
    // // alert(col1.length)
    // //
    // // var col2 = document.getElementsByClassName("par")
    // // for (let i = 0; i < col2.length; ++i)
    // //     col2[i].style.backgroundColor = "purple"
    // // var col3 = document.querySelectorAll("li:nth-of-type(2n)")
    // // for (let i = 0; i < col3.length; ++i)
    // //     col3[i].style.backgroundColor = "green"
    //
    //
    // var r = document.querySelector("p#r");
    // r.style.color = "green"
    //
    // var parag = document.querySelectorAll("p");
    //
    // for (let i = 0; i < parag.length; ++i) {
    //     parag[i].classList.add("b");
    //     parag[i].onclick = function () {
    //         alert(this);
    //         alert(i);
    //     }
    // }
    //
    // var t = document.querySelector("input[type='text']");
    // var b = document.querySelector("input[type='button']");
    // b.onclick = function () {
    //     alert(t.value)
    //
    //
    //     var colectia_2 = document.getElementsByName("r1");
    //     console.log(colectia_2)
    //     for (let x of colectia_2) {
    //         if (x.checked) {
    //             let culoare = x.value;
    //             t.style.backgroundColor = culoare;
    //             console.log(t);
    //         }
    //     }
    // }
    //
    // var rand_b = document.getElementById('rand_b');
    // rand_b.dist = 0;
    // cifre = "0123456789abcdef";
    // numar = '';
    // function random_color() {
    //     numar = ''
    //     for(let i = 0; i < 6; i++){
    //         numar += cifre[Math.floor(Math.random() * 16)];
    //     }
    //     document.body.style.backgroundColor = '#' + numar;
    //
    //
    //
    //     rand_b.dist += 10;
    //     rand_b.style.left = rand_b.dist + "px";
    //
    //     return numar;
    // }
    //
    // var interval = setInterval(random_color, 1500);
    // //
    // // var stil = getComputedStyle(rand_b);
    // // alert(stil.width)
    // // alert(rand_b.style.width)
    //
    //
    //
    // rand_b.onclick = function () {
    //     clearInterval(interval);
    // }
    // //
    // // for(var i = 0; i < 10; ++i){
    // //     setTimeout(function (){alert(i)}, 100*(i+1));
    // // }
    // //c = document.querySelectorAll("p")
    // // for(var i = 0; i < 10; ++i){
    // //     setTimeout(function (p) {alert(p)}, 100*(i+1), i);
    // //
    // // }
    // // for(let i = 0; i < parag.length; ++i){
    // //     var val = random_color();
    // //     setTimeout(function () {parag[i].style.backgroundColor = '#' + val}, 1000*(i+1));
    // // }
    //
    // var body_event = document.getElementsByTagName("body");
    // var div_event = document.getElementsByClassName("input_div");
    // var p_event = document.getElementById("event_listener_test");
    //
    // p_event.addEventListener("click", function () {alert("paragraf click event")}, true);
    // body_event[0].addEventListener("click", function (event) {alert("body click event"); alert(event.target)}, false);
    // div_event[0].addEventListener("click", function () {alert("div click event")}, true);
    //
    // var mouse_par = document.getElementById("mouse_p");
    //
    // body_event[0].onmousemove = function (e1) {
    //     mouse_par.style.left = e1.pageX + "px";
    //     mouse_par.style.top = e1.pageY + "px";
    // }
    // var arrow_pp = document.getElementById("arrow_p")
    //
    //
    // arrow_pp.style.left = getComputedStyle(arrow_pp, null).left
    // arrow_pp.style.top = getComputedStyle(arrow_pp, null).top
    //
    // body_event[0].onkeydown = function (event) {
    //     var press = event.key;
    //     if(press == "ArrowRight"){
    //         arrow_pp.style.left = (parseInt(arrow_pp.style.left) + 10) + "px"
    //     }
    //
    //     if(press == "ArrowLeft"){
    //         arrow_pp.style.left = (parseInt(arrow_pp.style.left) - 10) + "px"
    //     }
    //     if(press == "ArrowUp") {
    //         arrow_pp.style.top = (parseInt(arrow_pp.style.top) - 10) + "px"
    //     }
    //     if(press == "ArrowDown"){
    //         arrow_pp.style.top = (parseInt(arrow_pp.style.top) + 10) + "px"
    //     }
    // }
    //
    //
    // body_event[0].addEventListener("keydown", function(event){console.log(event.target); event.preventDefault();}, true);
    //
    //

    var ancora = document.getElementById("idAncora");
    var ancora2 = document.getElementById("idAncora2");

    var vector = {prop1: 4, prop2: 33};
    var d;
    ancora.onclick = function(){
        d = new Date();
        localStorage.setItem(ancora.href, d);
    }
    ancora2.onclick = function(){

        var data = new Date();
        localStorage.setItem(ancora2.href, data);
    }
    ancora2.onmouseover = function () {
        var retrive = localStorage.getItem(ancora.href);
        var retrive2 = localStorage.getItem(ancora2.href);
        if (retrive != null) {
            ancora.innerHTML = retrive;
        }
        if (retrive2 != null) {
            ancora2.innerHTML = retrive2;
        }
    }

    alert(ancora.href)

    var cn = document.body.childNodes;
    var c = document.body.children;

    for (elem in cn){
        alert(elem);
    }

    alert(cn);
    for(elem of c){
        alert(elem);
    }
    alert(c);

    var myJSON = JSON.stringify(vector);
    localStorage.setItem("testJSON", myJSON);

    alert(myJSON);

    var retrivedJSON = localStorage.getItem("testJSON");
    var retrivedObj = JSON.parse(retrivedJSON);

    ancora2.onmouseover = function () {
        if(retrivedObj != null)
            alert(retrivedObj.prop1);
    }

    var xhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
    if (readyState == 4 && status == 200) {
      document.getElementById("demo").innerHTML = responseText;
    }
  };
  xmlhttp.open("GET", "xmlhttp_info.txt", true);
  xmlhttp.send();

}
