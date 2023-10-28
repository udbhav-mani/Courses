function cFun() {
    var p = event.target;
    if (p.name == "e1") {
        message("First Name Changed to  " + p.value);
    } else {
        message("Last Name Changed to  " + p.value);
    }
}

function sendInfo() {
    var p = event.target.parentElement;
    message("Welcome " + p.e1.value + " " + p.e2.value);
}

function message(m) {
    document.getElementById("wrapper").innerHTML = m;
}
