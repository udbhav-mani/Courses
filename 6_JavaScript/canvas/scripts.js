let canvas = document.getElementById("canvasId");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
// console.log(window.innerHeight + " " + window.innerWidth);
intervalId = setInterval(() => {
    context = canvas.getContext("2d");
    context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
    context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
    context.fillRect(0, 0, 500, 500);
    context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
    context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
    context.fillRect(
        Math.floor(Math.random() * 1000),
        Math.floor(Math.random() * 1000),
        500,
        500
    );

    context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
    context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
    context.fillRect(
        Math.floor(Math.random() * 1000),
        Math.floor(Math.random() * 1000),
        400,
        400
    );
    context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
    context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
    context.fillRect(
        Math.floor(Math.random() * 1000),
        Math.floor(Math.random() * 1000),
        300,
        300
    );
    context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
    context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
    context.fillRect(
        Math.floor(Math.random() * 1000),
        Math.floor(Math.random() * 1000),
        200,
        200
    );
    context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
    context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
    context.fillRect(
        Math.floor(Math.random() * 1000),
        Math.floor(Math.random() * 1000),
        100,
        100
    );
}, 100);
// intervalId = setInterval(() => {
//     context = canvas.getContext("2d");
//     context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
//     context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
//     context.fillRect(0, 0, 500, 500);
//     context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
//     context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
//     context.fillRect(50, 50, 400, 400);
//     context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
//     context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
//     context.fillRect(100, 100, 300, 300);
//     context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
//     context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
//     context.fillRect(150, 150, 200, 200);
//     context.fillStyle = "#" + Math.floor(Math.random() * 16777215).toString(16);
//     context.rotate((Math.floor(Math.random() * 360) * Math.PI) / 180);
//     context.fillRect(200, 200, 100, 100);
// }, 100);

setTimeout(() => {
    clearInterval(intervalId);
}, 10000);
