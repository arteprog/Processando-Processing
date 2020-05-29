## Material para conversão da referência do Processing em Português 

### [UTFPR, 2005 (Prof. Luiz Ernesto Merkle)](http://www.dainf.ct.utfpr.edu.br/~merkle/processing/reference/ptBR/index.html) --> [Wiki-tradução em Processando Processing](https://github.com/arteprog/Processando-Processing/wiki)

Os arquivos .md do(a) Wiki podem ser clonados usando a URL **https://github.com/arteprog/Processando-Processing.wiki.git**

#### Roadmap (tentativa de)

1. Identificar páginas 'deprecadas' da ptBR v1 ('nossas'), termos que não existem mais na atual Processing 3 (enV3)
   - comparando páginas 'nossas' vs enV3
2. Identificar páginas que estão faltando, coisas que tem no Processing 3 e que precisam ser traduzidas
   - comparando páginas enV3 vs 'nossas'
3. Baixar as imagens da referência atual do Processing 3 em enV3
4. Identificar páginas a revisar / revisadas da wiki
5. Melhorar os índices
   - 3 colunas
   - indicar páginas deprecadas
   - indicar páginas que falta traduzir
   - indicar páginas a revisar/revisadas
6. ...
6. Profit! Quer dizer, pronto pra galera traduzir tudo
   
#### dados
- `enV3` aquivos do site atual em inglês - está sem imagens... :(
- `ptBR` arquivos baixados do site original
    - html
    - imagens
- `r1` html - primeira limpeza, remove cabeçalhos todos
- `r2` ~markdown~ - primeira conversão, movi os .md pro repositório-wiki já, ficou a pasta e uns indices...
 
#### `cleanup_scripts`
- scripts pra converter o HTML original simplificado (ptBR -> r1)
  - `modify_html_index_first_cleanup.py` 4 arquivos index__ 
  - `modify_html_files_first_cleanup.py` todos os outros
- scripts pra converter o HTML simplifcado em markdown (r1 -> r2)
  - `modify2md_indez.py`4 arquivos index__
  - `moidfy2md_files.py` todos os outros
