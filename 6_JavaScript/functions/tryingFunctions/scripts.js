
function a(){
    console.log("a")
    console.log(this)
    return this
}

b = function(){
    console.log("b")
    console.log(this)
    return this
};

(function c(){
    console.log("c")
    console.log(this)
})();

d = () => {
    console.log("d")
    console.log(this)
    return this
}

a1 = a()
b1 = b()
d1 = d()

