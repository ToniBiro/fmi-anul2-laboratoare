

window.onload = function () {

    var x = document.getElementById('paragraf_1');
    //

        var img = document.createElement("img");
        img.src = "5.png"
        document.body.appendChild(img);

        img.style.width = "20%";
        img.style.height = "auto";


        img.onclick = function () {
            document.body.removeChild(img);
        }
        // }
        //
        // var txn = document.createTextNode("___first text node___");
        // var fig = document.createElement("figure");
        // var figc = document.createElement('figcaption');
        // var img1 = document.createElement('img');
        //
        // figc.appendChild(txn);
        //
        // fig.appendChild(img1);
        // fig.appendChild(figc);
        // img1.src = '5.png';
        //
        // document.body.appendChild(fig);
        //
        //
        // var u = document.querySelector("ul");
        // var l = document.querySelector("li");
        // l.onclick = function()
        // {
        //     alert("Ai apasat primul ele din lista!");
        // }
        // alert(u.innerHTML += "<li class='par'>al treile rand din lista</li>");
        // u.appendChild(l)
        //
        // var col1 = document.getElementsByTagName("li")
        // for (let i = 0; i < col1.length-1; i++)
        //     col1[i].style.color = "aqua"
        // alert(col1.length)
        //
        // var col2 = document.getElementsByClassName("par")
        // for (let i = 0; i < col2.length; ++i)
        //     col2[i].style.backgroundColor = "purple"
        // var col3 = document.querySelectorAll("li:nth-of-type(2n)")
        // for (let i = 0; i < col3.length; ++i)
        //     col3[i].style.backgroundColor = "green"

        alert(this);

        var r = document.querySelector("p#r");
        r.style.color = "green"

        var parag = document.querySelectorAll("p");

        for (let i = 0; i < parag.length; ++i) {
            parag[i].classList.add("b");
            parag[i].onclick = function () {
                alert(this);
                alert(i);
            }
        }

        var t = document.querySelector("input[type='text']");
        var b = document.querySelector("input[type='button']");
        b.onclick = function () {
            alert(t.value)


            var colectia_2 = document.getElementsByName("r1");
            console.log(colectia_2)
            for (let x of colectia_2) {
                if (x.checked) {
                    let culoare = x.value;
                    t.style.backgroundColor = culoare;
                    console.log(t);
                }
            }
        }

        var rand_b = document.getElementById('rand_b');
        rand_b.dist = 0;
        cifre = "0123456789abcdef";
        numar = '';
        function random_color() {
            numar = ''
            for(let i = 0; i < 6; i++){
                numar += cifre[Math.floor(Math.random() * 16)];
            }
            document.body.style.backgroundColor = '#' + numar;



            rand_b.dist += 10;
            rand_b.style.left = rand_b.dist + "px";

            return numar;
        }

        var interval = setInterval(random_color, 1500);

        var stil = getComputedStyle(rand_b);
        alert(stil.width)
        alert(rand_b.style.width)



        rand_b.onclick = function () {
            clearInterval(interval);
        }
        //
        // for(var i = 0; i < 10; ++i){
        //     setTimeout(function (){alert(i)}, 100*(i+1));
        // }
        //c = document.querySelectorAll("p")
        // for(var i = 0; i < 10; ++i){
        //     setTimeout(function (p) {alert(p)}, 100*(i+1), i);
        //
        // }
        for(let i = 0; i < parag.length; ++i){
            var val = random_color();
            setTimeout(function () {parag[i].style.backgroundColor = '#' + val}, 1000*(i+1));
        }
        ;
}