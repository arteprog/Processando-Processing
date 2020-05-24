<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### saturation()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/saturation_.gif" width="100"/>

```pde
noStroke(); 
colorMode(HSB, 255); 
color c = color(0, 126, 255); 
fill(c); 
rect(15, 20, 35, 60); 
float value = saturation(c);  // atribui 126 a "value"
fill(value); 
rect(50, 20, 35, 60); 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Extrai o valor de saturação de uma cor
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
saturation(<font color="#996600">cor</font>)

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
[red() ](red_)[green() ](green_)[blue() ](blue_)[hue() ](hue_)[brightness() ](brightness_)
