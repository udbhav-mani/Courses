let img = document.getElementById("image");
img.onmouseover = changeImg;
img.onmouseout = origImg;

let target = document.getElementById("header");
function changeImg() {
    // console.dir(e);
    target.innerHTML = "I am sad 😔😔";
    this.src =
        "https://emojiisland.com/cdn/shop/products/5_large.png?v=1571606116";
}

function origImg() {
    target.innerHTML = "I am happy 😍";
    this.src =
        "https://emojiisland.com/cdn/shop/products/Emoji_Icon_-_Happy_large.png?v=1571606093";
}
