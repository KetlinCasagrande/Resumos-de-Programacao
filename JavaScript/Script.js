function toggleMode() {
    const html = document.documentElement
    html.classList.toggle("light")
    const img = document.querySelector("#profile img")








    if(html.classList.contains('light')) {
        img.setAttribute('src', './assets/Meu Avatar L.png')
        img.setAttribute('alt', 'Nova foto adicionada onde a kétlin esta com os olhos fechados por causa da claridade, foto ainda no carro com o vestido de cor rosa e uma tiara de perolas na cabeça')

    } else {
        img.setAttribute('src', './assets/Meu Avatar.png')


        }

        
    }



