async function generateHome() {
	removeInitial();
	document.getElementById("home").style.display = "block";
	document.getElementById("displaycart").style.display = "none";
	document.getElementById("assistant").style.display = "none";
	removevoicedots();
}
async function generateTable() {
	removeInitial();
	document.getElementById("test").innerHTML = "";
	document.getElementById("home").style.display = "none";
	document.getElementById("displaycart").style.display = "block";
	document.getElementById("assistant").style.display = "none";
	removevoicedots();
	var data = document.getElementById("data").value;
	eel.eel_printer()(dispTable);
}

async function generateAssistant() {
	removeInitial();
	document.getElementById("home").style.display = "none";
	document.getElementById("displaycart").style.display = "none";
	document.getElementById("assistant").style.display = "block";
	// for(i=0;i<voicedots.length;i++){
	// 	voicedots[i].classList.toggle("active");
	// }
	togglevoicedots();
	eel.tryblock();
	// var x = await 
	// eel.myCommand()(dispTable);
	// for(i=0;i<voicedots.length;i++){
	// 	voicedots[i].classList.remove("active");
	// }
}
async function generateBill() {
	var data = document.getElementById("data").value;
	eel.eel_printer()(dispTable);
}

function removeInitial(){
	sections=document.getElementsByTagName("section");
	for(i=0;i<sections.length;i++){
		sections[i].classList.remove("initial");
	}
}
// function setImage(string) {
// 	alert(string)
// 	document.getElementById("test").innerHTML = string
// }
eel.expose(right_printer);
function right_printer(str) {
	  var chat = document.getElementById("chat");
	  var chathtml = "<div class='message-orange'><p class='message-content'>";
	  chathtml += str;
	  chathtml += "</p></div>";
	  chat.innerHTML += chathtml;
}

eel.expose(left_printer);
function left_printer(str) {
	  var chat = document.getElementById("chat");
	  var chathtml = "<div class='message-blue'><p class='message-content'>";
	  chathtml += str;
	  chathtml += "</p></div>";
	  chat.innerHTML += chathtml;
}
function togglevoicedots(){
	var voicedots = document.getElementsByClassName("voicedot");
	for(i=0;i<voicedots.length;i++){
		voicedots[i].classList.toggle("active");
	}
}

function removevoicedots(){
	var voicedots = document.getElementsByClassName("voicedot");
	for(i=0;i<voicedots.length;i++){
		voicedots[i].classList.remove("active");
	}
}
function dispTable(table) {
	var tablehtml ="<table class='sqldisp'>";
	var i,j=0;
	for(i=0;i<table.length;i++){
		if(i%2==0){
			tablehtml+="<tr style='background: lavender'>";
		}
		else{
			tablehtml+="<tr style='background: white'>"	;
		}
		for(j=0;j<table[i].length;j++){
			tablehtml += "<td><pre>"+table[i][j]+"\t</pre><td>";
		}
		tablehtml+="</tr>";
	}
	tablehtml+="</table>";
	document.getElementById("test").innerHTML = tablehtml;
	// var voicedots = document.getElementsByClassName("voicedot")
	// for(i=0;i<voicedots.length;i++){
	// 	voicedots[i].classList.remove("active");}
}