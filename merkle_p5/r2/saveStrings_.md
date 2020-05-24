<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### saveStrings()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
String words = "apple bear cat dog"; 
String list[] = splitStrings(words); 
 
// agora escreva as stings em um arquivo, cada uma em uma linha separada
saveStrings("nouns.txt", list); 

```

#### Descrição
Escreve um array de strings em um arquivo. Este arquivo é
salvo na pasta de esboços, a qual pode ser aberta ao
selecionar "Show sketch folder" do  menu  "Sketch".
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
saveStrings(<font color="#996600">filename</font>, <font color="#996600">strings</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
filename
nome do arquivo a escrever
strings
array de string a ser escrito no arquivo
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[loadStrings()](loadStrings_)[loadBytes() ](loadBytes_)[saveBytes()](saveBytes_)
