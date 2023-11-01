const grandparent = document.querySelector(".grandparent");
const parent = document.querySelector(".parent");
const child = document.querySelector(".child");

grandparent.addEventListener("click", function (event) {
    console.log(event.target.classList);
});
// parent.addEventListener(
//     "click",
//     function () {
//         console.log("Parent was clicked.");
//     },
//     true
// );
// child.addEventListener(
//     "click",
//     function (event) {
//         console.log("Child was clicked.");
//         event.stopPropagation();
//     },
//     false
// );
