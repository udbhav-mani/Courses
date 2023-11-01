document.forms.myForm.onchange = outputCal;

function outputCal() {
    function docId() {
        let r = document.querySelector(arguments[0]);
        r = r.value == "on" ? r.checked : Number(r.value);
        return r;
    }
    let age = docId("#age");
    let height = docId("#heightFeet") * 12 + docId("#heightInches");
    let weight = docId("#weight");
    let lifeStyle = docId("#lifeStyle") * 0.2 + 1;
    let result = docId("#m")
        ? lifeStyle * (66 + 6.2 * weight + 12.7 * height - 6.76 * age)
        : lifeStyle * (655.1 + 4.35 * weight + 4.7 * height - 4.7 * age);
    document.getElementById("output").innerHTML =
        Math.round(result) + " calories needed per day.";
}
