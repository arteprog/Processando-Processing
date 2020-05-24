
#### Nome
### param()

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

#### Sintaxe
```pde
param(s)

```
Parâmetros
s
String: nome do parâmetro a ler

#### Retorno

	
String

#### Utilização

	
Web
