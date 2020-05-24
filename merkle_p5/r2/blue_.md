<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### blue()
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

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
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
blue(<font color="#996600">cor</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
cor
qualquer valor do tipo de dados color
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[red() ](red_)[green() ](green_)[hue() ](hue_)[saturation() ](saturation_)[brightness() ](brightness_)
