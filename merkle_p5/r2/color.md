
#### Nome
### color

#### Exemplos
<img border="0" height="100" src="media/color.gif" width="100"/>

```pde
color c1 = color(204, 153, 0); 
color c2 = #FFCC00; 
noStroke(); 
fill(c1); 
rect(0, 0, 25, 100); 
fill(c2); 
rect(25, 0, 25, 100); 
color c3 = get(10, 50); 
fill(c3); 
rect(50, 0, 50, 100); 

```

#### Descrição
Tipo de dados para armazenar valores de cores.  Cores podem ser atribuídas através de  e**get()** e**color()**, ou podem ser especificadas diretamente em notação hexadecimal como em**#FFCC00. **Cores
são 32 bits de informação ordenados como
AAAAAAAARRRRRRRRGGGGGGGGBBBBBBBB, onde:  os As contém
o valor alfa;  os Rs o vermelho (*Red*) ou o matiz (*hue*); os Gs o valor verde (*Green*)  ou a saturação (*saturation*);  e os Bs o azul (*Blue*) ou o brilho.

#### Sintaxe
```pde
color var
color var = valuedecor
            
```
Parâmetros
var
nome de variável que faz referência a valor de cor
valordecor
qualquer valor de cor

#### Utilização

	
Web & Applicações

#### Relacionado
[colorMode()](colorMode_)[color()](color_)
