//Price of Mangoes
function mango(quantity, pricePerMango) {
    let freeMangoes = Math.floor(quantity / 3);
    let paidMangoes = quantity - freeMangoes;
    let totalCost = paidMangoes * pricePerMango;
    return totalCost;
}