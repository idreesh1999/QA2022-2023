function sayHi() {
    alert("Suh dude");
}

function changeColour() {
    
    let col = document.getElementById("changing-id").style.color;
    if (col === "red" ) {
        
        document.getElementById("changing-id").style.color = "blue"
     
    } else {
        
        document.getElementById("changing-id").style.color = "red"
    }
}