window.onload = function () {
    var elem = document.querySelectorAll("div+p");
    for(let i of elem){
        i.onclick = function () {
            this.innerHTML = this.previousElementSibling.querySelectorAll("li").length;
        }
    }
}