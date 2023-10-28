var output = document.getElementById("wrapper");
document.getElementById("id1").onclick = myFun;
document.getElementById("id2").onclick = myFun;
document.getElementById("id3").onclick = myFun;

function myFun() {
    console.dir(this);
    this.value = "CLICKED";
    output.innerHTML = "WORKED";
}
