# Como usar Unfolding

## Tutorial básico mostrando como usar Unfolding Maps.

Este tutorial originalmente escrito em inglês e disponibilizado [aqui](http://unfoldingmaps.org/tutorials/basic-how-to-use-unfolding) nos termos da MIT License, está sendo traduzido e publicado sob a mesma licença por Monica Rizzolli https://github.com/arteprog/Processando-Processing. Se você encontrar erros ou tiver comentários, entre em contato (reportando o original ou a tradução).

Pré-requisito: Você já deve ter instalado o Unfolding para seu ambiente de programação. (Caso contrário, faça agora: [Unfolding para Processing](http://unfoldingmaps.org/tutorials/getting-started-in-processing.html) ou [Unfolding para Eclipse](http://unfoldingmaps.org/tutorials/getting-started-in-eclipse.html).)

Vamos começar com nosso sketch básico de Unfolding.

```java
UnfoldingMap map;
 
void setup() {
        size(800, 600);
        map = new UnfoldingMap(this);
        MapUtils.createDefaultEventDispatcher(this, map);
}
 
void draw() {
    map.draw();
}
```

# *Geolocation* e posições na tela

Você pode facilmente converter uma posição de tela para um local, e vice-versa. Como exemplo, vamos exibir a posição geográfica do ponteiro do mouse.

IMAGEM

Aqui, obtemos a localização do mapa na posição atual do mouse, e mostramos sua latitude e longitude como texto preto.

```java
void draw() {
    map.draw();
    Location location = map.getLocation(mouseX, mouseY);
    fill(0);
    text(location.getLat() + ", " + location.getLon(), mouseX, mouseY);
}
```

# Estilos de mapa

