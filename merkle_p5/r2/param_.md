<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### param()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
// Lê o valor "52" do texto abaixo incorporado em uma página HTML 
// <applet code="param_" archive="param_.jar" width=100 height=100> 
// <param name="back" VALUE="51">  
// </applet> 
String bs= param("back"); 
int bi = Integer.parseInt(bs); 
background(bi); 

```

#### Descrição
Lê o valor de um param. Valores são
frequentemente lidos como uma String, de modo que quando se quer que
eles sejam de outro tipo de dado, estes precisam ser convertidos, A
função**param()**  funcionará apenas em navegador web.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
param(<font color="#996600">s</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
s
String: nome do parâmetro a ler
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
String
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Web
<img height="25" src="../images/1pix.gif" width="1"/>
