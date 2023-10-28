
adj = ["super", "bad", "angry", "good", "lol"]
function displayName() {
    let target = document.getElementById("output")
    randomIndex = Math.floor(Math.random() * adj.length)
    ques = prompt("What is your name")
    console.log( adj[randomIndex] + " " + ques)
    target.innerHTML = adj[randomIndex] + " " + ques    
    
}