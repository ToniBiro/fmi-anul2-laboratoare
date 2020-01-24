// window.onkeydown=function(e){
// 	var dvs=document.getElementsByClassName("d1");
// 	if (e.key=='q') pas = 1;
// 	else if(e.key=='w') pas=-1;
// 		else pas = 0
//
// 	for(dv of dvs){
// 		inalt=parseInt(getComputedStyle(dv).height);
// 		inalt=Math.max(inalt+pas,0);
// 		dv.style.height=inalt+"px";
// 	}
// }



window.addEventListener("keydown", function(e){
	let pas;
	var dvs=document.getElementsByClassName("d1");
	if (e.key === 'q') pas = 1;
	else if(e.key === 'w') pas=-1;
		else pas = 0;
	for(dv of dvs){

		var inalt = parseInt(getComputedStyle(dv).height);

		if (inalt + pas > 0) {
			dv.style.height = inalt + pas + "px";
		}
	}
});