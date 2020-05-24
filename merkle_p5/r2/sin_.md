<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### sin()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos
<img border="0" height="100" src="media/sin_.gif" width="100"/>

```pde
float a = 0.0; 
float inc = TWO_PI/25.0; 
 
for(int i=0; i<100; i=i+4) { 
  line(i, 50, i, 50+sin(a)*40.0); 
  a = a + inc; 
} 

```
<img height="25" src="../images/1pix.gif" width="1"/>

#### Descrição
Calcula o seno de um ângulo. Esta função espera que os valores do parâmetro**angulo** correspondam a valores em radianos (valores entre 0 e 2*PI). Valores são retornados no intervalo entre -1.0 e 1.0.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
sin(<font color="#996600">rad</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
rad
float: an angle in radians<description>
</description>
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
float
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web & Applicações
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[cos()](cos_)[radians()](radians_)
