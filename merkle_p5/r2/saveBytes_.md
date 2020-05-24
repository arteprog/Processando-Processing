<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### saveBytes()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
byte[] nums = { 0, 34, 5, 127, 52}; 
 
// agora escreva os byes em um arquivo
saveBytes("numbers.txt", nums); 

```

#### Descrição
Oposta a**loadBytes()**, escreverá um array de bytes em um arquivo. Este arquivo é
salvo na pasta de esboços, a qual pode ser aberta ao
selecionar "Show sketch folder" do  menu  "Sketch".
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
saveBytes(<font color="#996600">filename</font>, <font color="#996600">bytes</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
filename
nome do arquivo a escrever
bytes
array de bytes a escrever
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadStrings()](loadStrings_)[loadBytes() ](loadBytes_)[saveStrings()](saveStrings_)
