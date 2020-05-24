# versão incial para limpar os HTML da referência - não funciona nos index____.html

import os
from bs4 import BeautifulSoup

base = '/home/villares/Documentos/GitHub/Processando-Processing/merkle_p5'
folder = os.path.join(base, 'ptBR')   # your directory
out_folder = os.path.join(base, 'r1')
if not os.path.isdir(out_folder):
    os.mkdir(out_folder)

file_names = [f for f in os.listdir(folder)
         if f.endswith('.html') and not f.startswith('index')]

for file_name in file_names[:]:
    print(file_name)
    with open(os.path.join(folder, file_name), encoding='cp1252') as f:  # unicode deu pau
        soup = BeautifulSoup(f, "html.parser")
#         for img in soup.find_all('img'):
#             img.decompose()
        tables = soup.find_all('table')
        t6 = tables[5]
        it = t6.find_all('table')
        it = it or (t6,)  # as vezes não tem uma tabela dentro (no index.html, por exemplo)
        with open(os.path.join(out_folder, file_name), "w") as g:
            g.write(str(it[0]))
