<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### tan()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/tan_.gif" width="100"/>

```pde
float a = 0.0; 
float inc = TWO_PI/50.0; 
 
for(int i=0; i<100; i=i+2) { 
  line(i, 50, i, 50+tan(a)*2.0); 
  a = a + inc; 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Calcula a razão entre o seno e o coseno de
um ângulo. Esta função espera que os valores do
parâmetro**angulo** correspondam a valores em radianos (valores entre 0 e PI/2). Valores são retornados no intervalo entre** -infinito** e +infinito. ¡
Calculates the ratio of the sine and cosine of an angle. This function expects the values of the**angle** parameter to be provided in radians (values from 0 to PI*2). Values are returned in the range**infinity** to**-infinity**.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
tan(<font color="#996600">angulo</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
angulo
float: ângulo em radianos<description>
</description>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[cos()](cos_)[sin()](sin_)[radians()](radians_)
