function numCheck() {
    message(!isNaN(event.key));
    return !isNaN(event.key);
}
function numCheck2() {
    message(isNaN(event.key));
    return isNaN(event.key);
}
function message(m) {
    document.getElementById("wrapper").innerHTML = m;
}
