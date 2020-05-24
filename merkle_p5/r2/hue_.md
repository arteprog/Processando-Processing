
#### Nome
### hue()

#### Exemplos
<img border="0" height="100" src="media/hue_.gif" width="100"/>

```pde
noStroke(); 
colorMode(HSB, 255); 
color c = color(0, 126, 255); 
fill(c); 
rect(15, 20, 35, 60); 
float value = hue(c);  // Atribui 0 a "value"
fill(value); 
rect(50, 20, 35, 60); 

```

#### Descrição
Extrai o valor do matiz de uma cor

#### Sintaxe
```pde
hue(cor)

```
Parâmetros
cor
qualquer valor do tipo de dados color

#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[red() ](red_)[green() ](green_)[blue() ](blue_)[saturation() ](saturation_)[brightness() ](brightness_)
