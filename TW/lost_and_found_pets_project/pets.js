

window.onload = function () {
    var w = document.getElementById("cont_wiki");
    var x = document.querySelectorAll(".anim_caut");

    for(let i = 0; i < x.length; ++i) {
        x[i].onclick = function () {
            alert("Se va deschide o pagina wikipedia!")
            var frame = document.createElement("iframe");
            frame.src = x[i].dataset.url;

            frame.style.width = "300px";
            frame.style.height = "500px";


            frame.onclick = function () {
                w.removeChild(frame);
            }
            w.appendChild(frame);
        }
    }
}

// flex
// relative
// inline-block
// transition
// selectare dupa clasa
