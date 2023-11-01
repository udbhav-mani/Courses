"use strict";

const btn = document.querySelector(".btn-country");
const countriesContainer = document.querySelector(".countries");
function renderError(err) {
    countriesContainer.insertAdjacentText("beforeend", err);
    countriesContainer.style.opacity = 1;
}
function renderCountry(data, className = "") {
    const html = `<article class=${className}>
    <img class="country__img" src="${data.flags.png}" alt="" />
    <div class="country__data">
        <h3 class="country__name">${data.name}</h3>
        <h4 class="country__region">${data.region}</h4>
        <p class="country__row"><span>👫</span>${(
            +data.population / 1000000
        ).toFixed(2)}mn people</p>
        <p class="country__row"><span>🗣️</span>${data.languages[0].name}</p>
        <p class="country__row"><span>💰</span>${data.currencies[0].code}</p>
    </div>
</article>`;
    countriesContainer.insertAdjacentHTML("beforeend", html);
    countriesContainer.style.opacity = 1;
}

// function getData(country) {
//     const request = new XMLHttpRequest();
//     request.open(
//         "GET",
//         `https://countries-api-836d.onrender.com/countries/name/${country}/`
//     );
//     request.send();
//     request.addEventListener("load", function () {
//         var [data] = JSON.parse(this.responseText);
//         console.log(data);
//         renderCountry(data, "country");
//         let [neighbouringCountry] = data.borders;
//         const request2 = new XMLHttpRequest();
//         request2.open(
//             "GET",
//             `https://countries-api-836d.onrender.com/countries/alpha/${neighbouringCountry}/`
//         );
//         request2.send();
//         request2.addEventListener("load", function () {
//             var data = JSON.parse(this.responseText);
//             console.log(data);
//             renderCountry(data, "neighbour");
//         });
//     });
// }

// using promises

function getData(country) {
    fetch(`https://countries-api-836d.onrender.com/countries/name/${country}/`)
        .then((response) => {
            if (!response.ok) {
                throw new Error("No such country found");
            }
            return response.json();
        })
        .then(([data]) => {
            renderCountry(data, "country");
            let [neighbouringCountry] = data.borders;
            if (!neighbouringCountry) {
                throw new Error("No neighbour countries found");
            }
            return fetch(
                `https://countries-api-836d.onrender.com/countries/alpha/${neighbouringCountry}/`
            );
        })
        .then((response) => response.json())
        .then((data) => renderCountry(data, "neighbour"))
        .catch((err) => {
            renderError(err);
            console.error(err);
        });
}

getData("japan");
// getData("bharat");
// getData("germany");
// getData("poland");
// getData("italy");
// getData("france");
// getData("japan");
// getData("indonesia");
