
#### Nome
### blue()

#### Exemplos
<img border="0" height="100" src="media/blue_.gif" width="100"/>

```pde
noStroke(); 
color c = color(0, 126, 255); 
fill(c); 
rect(15, 20, 35, 60); 
float value = blue(c);  // Atribui 255 à value
fill(value); 
rect(50, 20, 35, 60); 

```

#### Descrição
Extrai o valor de azul de uma cor,  já feita a escala de acordo com o**coloMode()**
corrente. este valor é sempre retornado como um float, e
portanto, deve-se tomar o cuidado de não atribuí-lo a
variáveis do tipo inteiro.

A função**blue()**
é fácil de utilizar e entender, mas é mais lenta
que outra técnica. Para se obter os mesmos resultados em maior
velocidade, mas trabalhando em**colorMode(RGB, 255)**, utiliza-se
um máscara de bitspara remover os demais componentes de cor. Por
exemplo, as duas linhas de código são equivalentes:```pde
float r1 = blue(myColor);
float r2 = myColor & 0xFF;
```

#### Sintaxe
```pde
blue(cor)

```
Parâmetros
cor
qualquer valor do tipo de dados color

#### Retorno

	
float

#### Utilização

	
Web & Applicações

#### Relacionado
[red() ](red_)[green() ](green_)[hue() ](hue_)[saturation() ](saturation_)[brightness() ](brightness_)
