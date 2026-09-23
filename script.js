async function pobierzProdukty () {
    const response = await fetch("http://127.0.0.1:8000/produkty");
    const data = await response.json();
    console.log(data);
    return data;
}

function createAndShowProducts (obiektProdukty) {
    const htmlDoWstawienia = obiektProdukty.map((produkt) => {
        return `<div class="item-box">
                    <img src=${produkt.image_url}>
                    <h2>Nazwa: ${produkt.nazwa_produktu}</h2>
                    <p>Cena: ${produkt.cena}</p>
                </div>`;
    }).join("");
    classItemBoxElement.innerHTML = htmlDoWstawienia;
}

const classItemBoxElement = document.querySelector(".items-box");

const buttonDownload = document.querySelector(".download-btn");
buttonDownload.addEventListener("click", async () => {
    const pobraneProdukty = await pobierzProdukty();
    createAndShowProducts(pobraneProdukty);
})

