var box;
function startDrag() {
    box = event.target;
}

function stopDrag() {
    event.preventDefault();
    if (event.target.className == "box") {
        event.target.appendChild(box);
    }
}
function noDrop() {
    event.preventDefault();
}
