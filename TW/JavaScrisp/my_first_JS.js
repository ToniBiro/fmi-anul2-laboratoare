
window.onload = function () {

    var x = document.getElementById('paragraf_1')

    x.onclick = function () {
        var img = document.createElement("img")
        img.src = "5.png"
        document.body.appendChild(img)

        img.style.width = "20%"
        img.style.height = "auto"


        img.onclick = function () {
        document.body.removeChild(img)
        }
    }

    var txn = document.createTextNode("___first text node___")
    var fig = document.createElement("figure")
    var figc = document.createElement('figcaption')
    var img1 = document.createElement('img')

    figc.appendChild(txn)

    fig.appendChild(img1)
    fig.appendChild(figc)
    img1.src = '5.png'

    document.body.appendChild(fig)


    // ???

}