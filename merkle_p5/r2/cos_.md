<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### cos()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/cos_.gif" width="100"/>

```pde
float a = 0.0; 
float inc = TWO_PI/25.0; 
for(int i=0; i<25; i++) { 
  line(i*4, 50, i*4, 50+cos(a)*40.0); 
  a = a + inc; 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Calcula o coseno de um ângulo. Esta função espera que os valores do parâmetro**angulo** correspondam a valores em radianos (valores entre 0 e 2*PI). Valores são retornados no intervalo entre -1.0 e 1.0.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
cos(<font color="#996600">angulo</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
angulo
float: um ângulo em radianos<description>
</description>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[sin()](sin_)[tan()](tan_)
