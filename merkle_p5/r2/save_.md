<img height="40" src="../images/1pix.gif" width="100"/>
<img height="1" src="../images/1pix.gif" width="20"/>
<img height="1" src="../images/1pix.gif" width="555"/>

#### Nome
### save()
<img height="25" src="../images/1pix.gif" width="1"/>

#### Exemplos

```pde
line(20, 20, 80, 80); 
// Salva um arquivo TIFF chamado "diagonal.tif" 
save("diagonal.tif"); 
// Salva um arquivo TARGA chamado "cross.tga" 
line(80, 20, 20, 80); 
save("cross.tga"); 

```

#### Descrição
Faz uma imagem da janela de
visualização. Imagens são salvas no formato TIFF
ou TARGA dependendo da extensão do parâmetro**filename**. Se nenhuma estensão é incluída em filename, a imagem será salva com TIFF, e**.tif**  será adicionada ao nome. Este arquivo é
salvo na pasta de esboços, a qual pode ser aberta ao
selecionar "Show sketch folder" do  menu  "Sketch". Não
é possível utilizar a função**save()** quando o programa esta executando em um navegador web.
<img height="25" src="../images/1pix.gif" width="1"/>

#### Sintaxe
```pde
save(<font color="#996600">filename</font>)

```
<img height="25" src="../images/1pix.gif" width="1"/>
Parâmetros
filename
String: qualquer seqüência de letras e números entre aspas
<img height="25" src="../images/1pix.gif" width="1"/>

#### Retorno

	
Nenhum
<img height="25" src="../images/1pix.gif" width="1"/>

#### Utilização

	
Application
<img height="25" src="../images/1pix.gif" width="1"/>

#### Relacionado
[saveFrame()](saveFrame_)
