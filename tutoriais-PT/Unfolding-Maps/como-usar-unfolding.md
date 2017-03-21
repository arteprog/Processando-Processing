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

![geolocation](https://github.com/arteprog/Processando-Processing/blob/master/tutoriais-PT/Unfolding-Maps/assets/imagens/mouse-geolocation.png?raw=true)

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

Unfolding exibe mapas em um estilo padrão, com dados cartográficos do OpenStreetMaps e blocos do Cloudmade. Para usar outro estilo de mapa, basta especificá-lo como segundo parâmetro ao construir um UnfoldingMap.

```java
map = new UnfoldingMap(this, new Microsoft.AerialProvider());
```

(Não se esqueça de importar ``` de.fhpotsdam.unfolding.providers.* ```)

Desta forma, você pode facilmente alternar para um dos tipos de mapa pré-configurados. Para ver os diferentes estilos do mapa, vá para o tutorial MapProvider & Tiles. Lá você também encontrará como criar seu próprio provedor de mapa, e até mesmo como criar um estilo de mapa completamente novo.

![sat](https://github.com/arteprog/Processando-Processing/blob/master/tutoriais-PT/Unfolding-Maps/assets/imagens/provider-sat.png?raw=true)

![toner](https://github.com/arteprog/Processando-Processing/blob/master/tutoriais-PT/Unfolding-Maps/assets/imagens/provider-toner.png?raw=true)

Tenha em mente que você precisa verificar os termos e condições dos provedores de mapas sobre como você pode usar seus padrões de mapa. Estamos fornecendo exemplos de provedores apenas para fins educacionais.

# Zoom e panorâmica do mapa

