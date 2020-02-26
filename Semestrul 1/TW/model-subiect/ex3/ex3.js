

window.addEventListener("load", function(){
	var rng=document.getElementById("rng");
	rng.max=Math.floor(20+Math.random()*20);
	rng.parentNode.insertBefore(document.createTextNode(rng.min),rng);
	rng.parentNode.appendChild(document.createTextNode(rng.max));
	rng.value=rng.min;

	document.getElementById("rng").addEventListener("input", function () {
		document.body.style.fontSize = this.value + "px";
		if(this.value > (parseInt(this.min) + parseInt(this.max))/2){
			document.body.style.color = "#FF0000";
		}
		else{
			document.body.style.color = "#000000";
		}
	})

	var rr = document.querySelectorAll("input[type=radio]");
	for(let r of rr)
		r.name = 'r';
	document.getElementById("btn").addEventListener("click", function () {
		for(let i of document.getElementsByName("r")){
			if(i.checked){
				alert(i.nextSibling.nodeValue)
				this.innerHTML = i.nextSibling.nodeValue;
			}
		}
	})
});