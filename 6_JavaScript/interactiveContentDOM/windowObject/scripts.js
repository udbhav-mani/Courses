let target = document.getElementById("output")
target.innerHTML += window.innerHeight + ":" + window.innerWidth
// w = window.open("index2.html");
window.addEventListener("beforeunload", function(){
    alert("Please dont go!!")
}
)
