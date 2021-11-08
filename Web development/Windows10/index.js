function start() {
    let menu = document.getElementById("startmenu");

    if(menu.style.display != "block"){
        menu.style.display = "block";
    }
    else{
        menu.style.display = "none";
    }
}

function refresh() {
    let plate = document.getElementById("ref");

    if(plate.style.display != "block"){
        plate.style.display = "block";
    }
    else{
        plate.style.display = "none";
    }
}