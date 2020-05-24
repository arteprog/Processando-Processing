# versão para os index

import os
from bs4 import BeautifulSoup

base = '/home/villares/Documentos/GitHub/Processando-Processing/merkle_p5'
folder = os.path.join(base, 'ptBR')   # your directory
out_folder = os.path.join(base, 'r1')
if not os.path.isdir(out_folder):
    os.mkdir(out_folder)

file_names = [f for f in os.listdir(folder)
         if f.startswith('index')]  # filtro, só os 4 arquivos com index

for file_name in file_names[:]:
    print(file_name)
    with open(os.path.join(folder, file_name), encoding='cp1252') as f: # unicode
        soup = BeautifulSoup(f, "html.parser")
#         for img in soup.find_all('img'):
#             img.decompose()

        #  tou perdendo as imagens dos temas aqui :(
        tables = soup.find_all('table')
        t7 = tables[6].find_all('table')[1:]
        
        with open(os.path.join(out_folder, file_name), "w") as g:
            for t in t7:
                g.write(str(t))
