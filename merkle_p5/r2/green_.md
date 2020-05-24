
#### Nome
### green()

#### Exemplos
<img border="0" height="100" src="media/green_.gif" width="100"/>

```pde
noStroke(); 
color c = color(0, 126, 255); 
fill(c); 
rect(15, 20, 35, 60); 
float value = green(c);  // Atribui 126 a value
fill(value); 
rect(50, 20, 35, 60); 

```

#### Descrição
Extrai o valor de verde de uma cor,  já feita a escala de acordo com o `coloMode()`
corrente. Este valor é sempre retornado como um float, e
portanto, deve-se tomar o cuidado de não atribuí-lo a
variáveis do tipo inteiro.



A função `green()`
é fácil de utilizar e entender, mas é mais lenta
que outra técnica. Para se obter os mesmos resultados em maior
velocidade, mas trabalhando em **colorMode(RGB, 255)**, utiliza-se
um máscara de bitspara remover os demais componentes de cor. Por
exemplo, as duas linhas de código são equivalentes:

```pde
float r1 = green(myColor);
float r2 = myColor >> 8 & 0xFF;
```

#### Sintaxe
```pde
green(cor)

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
[blue() ](blue_
)
[hue() ](hue_
)
[saturation() ](saturation_
)
[brightness() ](brightness_
)
[>> (right shift)](rightshift
)

