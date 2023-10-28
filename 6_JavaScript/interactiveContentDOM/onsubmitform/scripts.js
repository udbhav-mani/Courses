let myForm = document.getElementById("myForm");
myForm.addEventListener("submit", function () {
    console.log(event.target.value);
});