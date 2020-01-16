
window.onload = function () {

    var x = document.querySelectorAll(".anim_caut");

    //var w = document.getElementById("cont_wiki");

    for (let elem of x){
        let parent = elem.parentElement;

        elem.onclick = function () {
            alert("Se va deschide o pagina wikipedia!")
            let frame = document.createElement("iframe");
            frame.src = elem.dataset.url;

            frame.className = "wikiStyle";

            frame.style.width = "500px";
            frame.style.height = "500px";

            frame.onclick = function () {
                parent.removeChild(frame);
            }
            parent.appendChild(frame);
        }
    }
}