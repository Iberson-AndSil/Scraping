from requests_html import HTMLSession
import os

s = HTMLSession()

evaluacion = True
id_carpeta = 0

while evaluacion == True:
    url = input('pega tu link: ')
    cur_dir = os.getcwd()
    outputfolder = cur_dir + f'/carpeta_{id_carpeta}'
    if not os.path.exists(outputfolder):
        os.mkdir(outputfolder)

    r = s.get(url)
    fotos = r.html.find('figure.showcase__item img')
    for foto in fotos:
        try:
            fotourl = foto.attrs['src']
            name = os.path.basename(fotourl)
            img_data = s.get(fotourl).content
            with open(os.path.join(outputfolder, name), 'wb') as f:
                f.write(img_data)
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    respuesta = input('deseas continuar? (y/n): ')
    id_carpeta = id_carpeta + 1
    if respuesta != 'y':
        evaluacion = False
    