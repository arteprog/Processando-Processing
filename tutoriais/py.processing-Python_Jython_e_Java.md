# Python, Jython e Java

Este tutorial é para o modo Python do Processing. Originalmente publicado por Allison Parish [em inglês](http://py.processing.org/tutorials/python-jython-java/) sob a licença [Creative Commons BY-NC-SA 4.0](http://creativecommons.org/licenses/by-nc-sa/4.0/), traduzido por Alexandre Villares para [https://github.com/arteprog/Processando-Processing](https://github.com/arteprog/Processando-Processing) Se você encontrar erros ou tiver comentários, entre em contato (reportando [o original](https://github.com/processing/processing-docs/issues?state=open) ou [a tradução](https://github.com/arteprog/Processando-Processing/issues)).

Processing.py é baseado na implementação Java do [Processing](http://www.processing.org/). Faz uso do [Jython](http://www.jython.org/), uma implementação de Python que roda na Maquina Virtual Java (JVM, na sigla em inglês), para acessar diretamente a biblioteca Java subjacente. A vantagem desta estratégia é que os seus sketches Processing.py podem fazer praticamente qualquer coisa que um sketch Processing normal pode fazer, e versões novas do Processing.py aproveitam imeditamente as melhorias em performance ou novas features acrescentadas na implementação Java. Quando você faz sketches com Processing.py, você tem acesso à melhor de três diferentes plataformas e ecossistemas de software: Python, Java e Processing.

No entanto, se você já está familiarizado com qualquer uma destas plataformas, você pode descobrir que algumas coisas funcionam de maneira não-intuitiva, ou deixam de funcionar por completo. Este tutorial foi concebido para ajudá-lo a se alfabetizar sobre como Processing.py, Processing, Python e Java todos trabalham em conjunto, para que você possa raciocinar melhor sobre como diagnosticar problemas e utilizar todo o potencial da plataforma.

## Limitações do Jython (e peculiaridades)

Jython é uma implementação do Python que roda na Java Virtual Machine (JVM). Jython foi inicialmente desenvolvido como uma maneira de escrever programas em Python que fazem uso de bibliotecas, frameworks e infraestruturas Java existentes. Jython é projetado para ser o mais compatível possível com todos os programas em Python, e é geralmente tão rápido quanto [CPython](https://en.wikipedia.org/wiki/CPython) (a implementação "referência" do Python, escrita em C) para a maioria das tarefas.

No entanto, Jython tem algumas limitações significativas, especialmente se você está acostumado a trabalhar com CPython. Para mais detalhes, consulte o [FAQ Jython](https://wiki.python.org/jython/JythonFaq) oficial. Aqui vai um resumo das diferenças mais importantes para usuários de Processing.py.

### Versões do Python

A mais recente versão do Jython implementa Python 2.7. Python 2.7 ainda é amplamente utilizado, mas Python 3 (que tem uma série de incompatibilidades com versões anteriores) está ganhando popularidade. Se você é novo em Python, tenha em mente que alguns tutoriais e programas de exemplo que você encontrar na web estarão escritos em Python 3, não Python 2.7, e pode, exigir um pouco de retrabalho para torná-los funcionais em Processing.py.

### Bibliotecas Python

Jython suporta quase toda a biblioteca padrão do Python (isto é, as bibliotecas que vêm com Python quando você o instala). Uma exceção notável é [sqlite3](https://docs.python.org/2/library/sqlite3.html) (embora você possa acessar bancos de dados SQLite usando ODBC, e [há uma issue aberta para o suporte ao sqlite3 no rastreador de bug do Jython](http://bugs.jython.org/issue1682864). Jython *não* suporta bibliotecas Python de terceiros que usam extensões escritas em C. Isto significa que as bibliotecas Python populares como [](http://www.numpy.org/)numpy, [scipy](http://www.scipy.org/) e [scikit-learn](http://scikit-learn.org/stable/) *não vão funcionar* no Jython (e, por esta razão, não funcionarão no Processing.py).

Infelizmente, não há nenhuma maneira fácil de dizer se uma biblioteca usa ou não uma extensão em C (ou se tem como dependência uma biblioteca com uma extensão C) sem tentar instalá-la, apesar de existirem algumas bibliotecas que vêm com uma alternativa puro-Python se for impossível compilar a extensão C.

### Python e Java nem sempre se olham nos olhos

Java é uma linguagem de tipagem estática, enquanto Python tem tipagem dinâmica. Para fazer as duas linguagens conversar, os implementadores do Jython tiveram que preencher esta lacuna. Isto pode ocasionalmente resultar em problemas inesperados ao tentar chamar o código Java a partir Jython, ou ao tentar escrever o código Jython que possa ser chamado a partir de um código Java.

Um exemplo notável é que as classes em Jython são definidos *em tempo de execução* (ao contrário de classes Java puros, que são geralmente definidas em tempo de compilação). Isto significa que um número de características que são importantes para a interoperabilidade com bibliotecas de Processing, como a introspecção de métodos, [às vezes não funcionam como esperado](https://github.com/jdf/processing.py/issues/201). O capítulo [Jython and Java Integration](http://www.jython.org/jythonbook/en/1.0/JythonAndJavaIntegration.html) do livro [The Jython Book](http://www.jython.org/jythonbook/en/1.0/index.html) tem uma série de boas dicas e truques.

## Armadilhas para programadores Python

Uma das metas de Processing.py é seguir a API de Processing padrão, tanto quanto possível. Isso significa que as funções que você pode chamar em Processing "normal" (ou seja, a implementação Java) têm exatamente a mesma funcionalidade em Processing.py.

### Conflitos de nome

Há, no entanto, uma série de funções de Processing cujos nomes conflitam com funções built-in existentes em Python. Para lidar com estes casos, Processing.py implementa funções especiais "wrapper" invocando o código subjacente apropriado com base no número de parâmetros passados para a chamada. Aqui está uma lista de algumas das funções afetadas:

* <b>`filter()`</b>. No Processing, esta função [aplica um filtro ou shader aos pixels do quadro](https://processing.org/reference/filter_.html) atual. Em Python, este é [uma função que constrói uma lista avaliando uma função em cada item de uma lista existente](https://docs.python.org/2/library/functions.html#filter). Processing.py verifica os tipos de variáveis passados para a função em tempo de execução e invoca a função de Processing se os parâmetros coincidir com a assinatura apropriada, e a built-in de Python contrário.

* <b>`map()`</b>. Em Processing,['map()'](https://processing.org/reference/map_.html) é uma das várias funções (juntamente com [`lerp()`](https://processing.org/reference/lerp_.html), [`constrain()`](https://processing.org/reference/constrain_.html),etc.) que ajudam a interpolação de valores numéricos em intervalos. O wrapper do Processing.py irá invocar a função Processing se o número e tipo de argumentos na chamada de função corresponder à assinatura, e invocar o Python embutido [map()](https://docs.python.org/2/library/functions.html#map) de outra forma.

* <b>`set()`</b>. Esta função Processing [define a cor de um único pixel na tela ou desenha uma](https://processing.org/reference/set_.html) imagem. Em Python, [`set()`](https://docs.python.org/2/library/functions.html#func-set) cria um novo objeto set ou converte um iterável em um conjunto. Mais uma vez, função wrapper de Processing.py invoca tanto a função Processing ou a função Python com base na assinatura dos argumentos passados na chamada original.

Processing.py torna disponíveis  as funções do núcleo de Processing definindo atributos do objeto `__builtins__` do Jython. Se você estiver interessado nos detalhes técnicos, [os built-ins são atribuídos no core.py](https://github.com/jdf/processing.py/blob/master/runtime/src/jycessing/core.py) e as funções de "wrapper" são implementados em [PAppletJythonDriver.java](https://github.com/jdf/processing.py/blob/master/runtime/src/jycessing/PAppletJythonDriver.java).

### Listas e arrays

Para tornar as coisas mais fáceis para programadores iniciantes, Processing Java normal inclui uma série de funções para manipular arrays facilmente,  tais como `split()`, `splitTokens`, `append`, `arrayCopy`, `reverse`, etc.). Para fins de compatibilidade, Processing.py suporta estas funções, embora na maioria dos casos, você deve querer usar a estruturas de Python em seu lugar.

Se você acabar usando essas funções, esteja ciente de que elas retornam objetos array de Python e não listas. (Jython representa internamente arrays Java como objetos do tipo array do módulo Python [array](https://docs.python.org/2/library/array.html). Por exemplo, considere as seguinte duas linhas de código:

    print type(split("a,b,c,d", ",")) # usando o built-in do Processing
    print type("a,b,c,d".split(",")) # usando o método de string de Python

Na maioria das situações, arrays e listas são intercambiáveis, de modo que você pode até não notar. Mas arrays e listas têm funcionalidades sutilmente diferente, que pode causar erros em seu programa se você não tiver cuidado. Por exemplo, o seguinte código levanta um TypeError:

    x = split("a,b,c,d", ",")
    x.append(20)
   
... uma vez que split() retorna um array estritamente-tipado de objetos String do Java, e você não pode acrescentar um número inteiro a um tal array. Do mesmo modo, as listas e os arrays não permitem comparação elemento a elemento, tal como ilustrado pelo seguinte exemplo:

    x = split("a,b,c,d", ",")
    y = ["a", "b", "c", "d"]
    print x == y # prints False

Sempre fique atento aos tipos de suas variáveis e verifique se você sabe aquilo com o qual está trabalhando. Além das funções de Processing mencionadas acima, pode haver bibliotecas de terceiros que você usa no seu sketch Processing.py que retornam arrays também. Felizmente, há uma solução fácil: use a função buit-in de Python list() para converter os arrays em lista. Por exemplo:

    x = list(split("a,b,c,d", ","))
    y = ["a", "b", "c", "d"]
    print x == y # prints True

Note, no entanto, que a maior parte das funções de Processing Java que normalmente aceita um array como parâmetro ficará feliz em aceitar listas Python simples em seu lugar, embora ainda vá retornar um array. Assim, por exemplo:

    print shorten([1, 2, 3, 4]) # prints array('i', [1, 2, 3])

## Armadilhas para programadores Java/Processing

Por diversas razões a imprentação no Processing.py de algumas funções de Processing difere um pouco da implempementação no Processing Java padrão . Na maior parte das vezes, esses difereção serão invisíveis e as funções devem "simplesmente funcionar" como o esperado. Incluidas abaixo estão algumas peculiaridades que podem surgir:

* Como observado na seção anterior, Processing.py suporta muitas funções de strings e de manipulação de array do Processing  Java normal. Mas é quase sempre uma melhor ideia usar no seu lugar os tipos built-in de Python e seus métodos. (O [Tutorial de Python](http://turing.com.br/pydoc/2.7/tutorial/) é um bom lugar para começar, se você quiser saber mais sobre listas, strings e outras estruturas de dados em Python.

* O Processing.py não tem a função `loadTable()`. Use o módulo [csv](https://docs.python.org/2/library/csv.html) da biblioteca padrão do Python em seu lugar. Da mesma forma, use o módulo [json](https://docs.python.org/2/library/json.html) da biblioteca padrão do Python para o carregar, manipular e salvar os dados JSON (em vez de, por exemplo, loadJSONObject() do Procssing Java normal), e [ElementTree](https://docs.python.org/2/library/xml.etree.elementtree.html) para dados XML (em vez de `loadXML()`).

* O Processing.py não permite a "notação web" para especificar cores. Em vez disso, coloque a notação dentro de um string literal para passar à função relevante. (Por exemplo, `fill(#0000FF)` é um erro de sintaxe, mas `fill("#0000FF")` funciona muito bem).

## Usando bibliotecas Processing 

A maior parte das bibliotecas Processing funciona de primeira com o Processing.py. No modo Python do IDE Processing, você pode procurar e adicionar bibliotecas ao seu *sketch* usando o painel "Add Tool...", exatamente como se faz com o Processing normal. Processing.py acrescenta uma automaticamente ao seu *sketch* uma variável global this que você pode passar para bibliotecas de terceiros que precisam de uma referência ao *sketch* sendo executado.

Algumas bibliotecas Processing querem que você defina funções no seu *sketch* com nomes e assinaturas específicos como callbacks ou tratadores de eventos. Neste momento, estas bibliotecas não vão funcionar no Processing.py a menos que suporte específico tenha sido acrescentado. Neste momento existe suporte completo ou parcial para [Serial](https://processing.org/reference/libraries/serial/index.html), [Video](https://processing.org/reference/libraries/video/index.html), [Net](https://processing.org/reference/libraries/net/index.html) e [oscP5](http://www.sojamo.de/libraries/oscp5/). Se houver uma biblioteca que você gostaria de usar que ainda não funciona, [reporte o problema](https://github.com/jdf/processing.py/issues).

## Leituras adicionais

* O [Processing.py FAQ](https://github.com/jdf/processing.py#faq) (perguntas frequentes, em inglês) no repositório Github contém mais dicas e truques de como suar as bibliotecas Processing no Processing.py.

* O [Jython FAQ](https://wiki.python.org/jython/JythonFaq) (também em inglês) tem mais respostas aprofundadas para dúvidas sobre a compatibilidade entre Python, Jython e Java
