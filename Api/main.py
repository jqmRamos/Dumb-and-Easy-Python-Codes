'''
import pokebase as pb
from fastapi import FastAPI

    charmander = pb.pokemon('charmander')
    chesto = pb.APIResource('berry', 'chesto')
    print(chesto.name)
    print(chesto.natural_gift_type.name)
    print(charmander.height)


    s1 = pb.SpriteResource('pokemon', 17)
    print(s1)
    print(s1.url)
    s2 = pb.SpriteResource('pokemon', 1, other=True, official_artwork=True)
    print(s2.path)
    #'/home/user/.cache/pokebase/sprite/pokemon/other-sprites/official-artwork/1.png'
    #>>> s3 = pb.SpriteResource('pokemon', 3, female=True, back=True)
    #>>> s3.img_data b'x89PNGrnx1anx00x00x00rIHDRx00x00x00 ... xca^x7fxbbd\*x00x00x00x00IENDxaeB`x82'


app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "hello world"}

'''
