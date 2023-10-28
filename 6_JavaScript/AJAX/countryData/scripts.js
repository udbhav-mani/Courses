"use strict";

const btn = document.querySelector(".btn-country");
const countriesContainer = document.querySelector(".countries");

const request = new XMLHttpRequest();
request.open("GET", "https://restcountries.com/v3.1/name/india");
request.send();

request.addEventListener("load", function () {
    var data = JSON.parse(this.responseText);
    console.log(data[0]);
    const html = `<article class="country">
    <img class="country__img" src="${data[0].flags.png}" alt="" />
    <div class="country__data">
        <h3 class="country__name">${data[0].name.common}</h3>
        <h4 class="country__region">${data[0].region}</h4>
        <p class="country__row"><span>👫</span>${data[0].population} people</p>
        <p class="country__row"><span>🗣️</span>LANG</p>
        <p class="country__row"><span>💰</span>CUR</p>
    </div>
</article>`;
    countriesContainer.insertAdjacentHTML("beforeend", html);
});
