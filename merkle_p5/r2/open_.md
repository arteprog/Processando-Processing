<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### open()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
void setup() { 
  size(200, 200); 
} 
 
void draw() { 
 
} 
 
void mousePressed() { 
  println("Opening Process_4"); 
  open("Process_4.exe"); 
} 
 

```

#### Descrição
Tenta abrir um arquivo ou processo através do sistema opecadional da plataforma.  O parâmetro**arquivo**
é uma String que especifica o local e o nome do arquivo.
 Qaundo se executam rascunhos no ambiente Processing a
localização padrão dos arquivos é a mesma
do arquivo Processing.exe.  Também é possível
utilizar o camminho absoluto do arquivo. Certifiques-se de fazer o
arquivo "executável" antes de tentar abri-lo (chmnod +x). O
parâmetro**args** é um array String que é passado para a linha de comando.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
open(<font color="#996600">arquivo</font>)
open(<font color="#996600">args</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
arquivo
String: nome do arquivo
args
String[]: lista de comando passados para a linha de comando
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum ou Process
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application
<img height="25" src="../images/1pix.gif" width="1"/>
