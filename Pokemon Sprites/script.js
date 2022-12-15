// https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png

// Select Container
const container = document.querySelector('#container');
// We want to loop thru the api and change the number at the end of the src
const URL = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'
for (let i = 1; i < 152; i++) {
    const pokemon = document.createElement('div')
    pokemon.classList.add('pokemon')
    const label = document.createElement('span')
    label.innerText = `${i}`;
    const image = document.createElement('img');
    // Set the source of the create image element
    image.src = `${URL}${i}.png`
    pokemon.appendChild(image)
    pokemon.appendChild(label)
    container.appendChild(pokemon)
}