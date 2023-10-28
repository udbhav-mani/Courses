let arr = [1,2,3,4,5,6,7,8,9]
target = document.getElementById("output")
target.innerHTML = arr

function shuffle(){
    shuffler()
    target.innerHTML = arr
}

function shuffler() {
    let randomNumber = Math.floor(Math.random()*arr.length)
    for(let i = 0; i < arr.length; i++){
        let temp = arr[i]
        arr[i] = arr[randomNumber]
        arr[randomNumber] = temp
    }
    return arr
}