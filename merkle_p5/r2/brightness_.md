
#### Nome
### brightness()

#### Exemplos
<img border="0" height="100" src="media/brightness_.gif" width="100"/>

```pde
noStroke(); 
colorMode(HSB, 255); 
color c = color(0, 126, 255); 
fill(c); 
rect(15, 20, 35, 60); 
float value = brightness(c);  // Atribui 255 a "value"
fill(value); 
rect(50, 20, 35, 60); 

```

#### Descrição
Extrai o valor do brilho de uma cor

#### Sintaxe
```pde
brightness(cor)

```
Parâmetros
cor
qualquer valor do tipo de dados color



#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[red() ](red_
)
[green() ](green_
)
[blue() ](blue_
)
[hue() ](hue_
)
[saturation() ](saturation_
)

