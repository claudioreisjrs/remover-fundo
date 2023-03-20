from rembg import remove
from PIL import Image
#carrega foto com fundo
foto = Image.open("fotocomfundo.jpeg")
#salva foto sem fundo
saida = remove(foto).save("fotosemfundo.png")