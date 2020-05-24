
#### Nome
### endShape()

#### Exemplos
<img border="0" height="100" src="media/endShape_.gif" width="100"/>

```pde
beginShape(LINE_STRIP); 
vertex(30, 20); 
vertex(85, 20); 
vertex(85, 75); 
vertex(30, 75); 
endShape(); 

```

#### Descrição
A função `endShape()` trabalha em conjunto com a função `beginShape()` e só pode ser chamada aplós a última. Quando ` endShape()`é chamada, todos os dados definidos desde a chamada prévia a `beginShape()` sao escritos no *buffer* de imagem.

#### Sintaxe
```pde
beginShape()

```

#### Retorno

	
Nenhum

#### Utilização

	
Web & Applicações

#### Relacionado
[beginShape()](beginShape_
)

