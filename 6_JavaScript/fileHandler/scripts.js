let inputFile = document.getElementById("importFile");
inputFile.addEventListener("change", function () {
    let fileReader = new FileReader();
    fileReader.readAsText(this.files[0]);
    fileReader.onload = function (file) {
        console.log(file.target.result);
    };
});
