
#### Nome
### saveStrings()

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

#### Sintaxe
```pde
saveStrings(filename, strings)

```
Parâmetros
filename
nome do arquivo a escrever
strings
array de string a ser escrito no arquivo

#### Utilização

	
Application

#### Relacionado
[loadStrings()](loadStrings_)[loadBytes() ](loadBytes_)[saveBytes()](saveBytes_)
