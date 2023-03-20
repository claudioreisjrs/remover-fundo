from rembg import remove
from PIL import Image
foto = Image.open("fotocomfundo.jpeg")
saida = remove(foto).save("fotosemfundo.png")