const container = document.querySelector(".container");
const startGame = document.querySelector(".startGame");
const scoreArea = document.querySelector(".score");
let player = {
    score: 0,
};
startGame.addEventListener("click", function () {
    startGame.style.display = "none";
    let ranTime = Math.random() * 2000 + 1000;
    setTimeout(makeItem, ranTime);
});

function makeItem() {
    let boundary = container.getBoundingClientRect();
    let div = document.createElement("div");
    div.style.position = "absolute";
    div.style.left = Math.random() * boundary.width + "px";
    div.style.top = Math.random() * boundary.height + "px";
    div.style.width = Math.random() * 10 + 40 + "px";
    div.style.height = Math.random() * 10 + 40 + "px";
    div.style.borderRadius = "10%";
    div.style.cursor = "pointer";
    div.style.backgroundColor = "#" + Math.random().toString(16).substr(-6);
    div.style.border = "1px solid black";
    div.startTime = Date.now();
    div.addEventListener("click", function () {
        let endTime = Date.now();
        let diff = (endTime - div.startTime) / 1000;
        scoreArea.innerHTML = "Clicked in " + diff + "seconds";
        //startGame.style.display = "block";
        clearTimeout(div.timer);
        container.removeChild(div);
        makeItem();
    });
    div.timer = setTimeout(function () {
        container.removeChild(div);
        makeItem();
    }, 1000);
    container.appendChild(div);
}
