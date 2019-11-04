
window.onload = function () {

    var x = document.getElementById('paragraf_1');

    x.onclick = function () {
        var img = document.createElement("img");
        img.src = "5.png"
        document.body.appendChild(img);

        img.style.width = "20%";
        img.style.height = "auto";


        img.onclick = function () {
        document.body.removeChild(img);
        }
    }

    var txn = document.createTextNode("___first text node___");
    var fig = document.createElement("figure");
    var figc = document.createElement('figcaption');
    var img1 = document.createElement('img');

    figc.appendChild(txn);

    fig.appendChild(img1);
    fig.appendChild(figc);
    img1.src = '5.png';

    document.body.appendChild(fig);


    var u = document.querySelector("ul");
    var l = document.querySelector("li");
    l.onclick = function()
    {
        alert("Ai apasat primul ele din lista!");
    }
    alert(u.innerHTML += "<li class='par'>al treile rand din lista</li>");
    u.appendChild(l)

    var col1 = document.getElementsByTagName("li")
    for (let i = 0; i < col1.length-1; i++)
        col1[i].style.color = "aqua"
    alert(col1.length)

    var col2 = document.getElementsByClassName("par")
    for (let i = 0; i < col2.length; ++i)
        col2[i].style.backgroundColor = "purple"
    var col3 = document.querySelectorAll("li:nth-of-type(2n)")
    for (let i = 0; i < col3.length; ++i)
        col3[i].style.backgroundColor = "green"

}