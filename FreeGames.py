import requests
import pandas as pd

def save(url):
    jsonF = open('db.json','w+')
    r= requests.get(url)
    jsonF.write(r.text)
    df = pd.read_json('db.json')
    df.to_csv (r'OpenWithLibreOffice.csv', index = None)
    
    
    
def todos():
    url = ' https://www.freetogame.com/api/games'
    seVienenCositas = 'https://www.freetogame.com/api/comingsoon'

    save(url)



def custom():
    try:
        plataforma = str(input('''
╔══════════════════════════════════╗
║ introduzca la plataforma deseada ║
╠══════════════════════════════════╣
║ pc[default]                      ║
║ browser                          ║
║ all                              ║
╚══════════════════════════════════╝

> '''))
        if plataforma == '':
            plataforma = 'pc'
    except ValueError:
        plataforma = 'pc'
        print('\ndebido a un fallo, se escogera la opcion por defecto(pc)') 
    
    
    tags = '''
╔══════════════════════════════════════════════════════════════════════════╗
║                                categorias                                ║
╠══════════════════════════════════════════════════════════════════════════╣
║ all[default]                                                             ║
║ all      mmorpg       shooter      strategy     moba       racing        ║
║ sports   social       sandbox      open-world   survival   pvp           ║
║ pve      pixel        voxel        zombie       tank       turn-based    ║
║ space    third-Person sailing      top-down     permadeath first-person  ║
║ mmofps   3d           2d           sci-fi       low-spec   battle-royale ║
║ anime    fantasy      fighting     action-rpg   flight                   ║
║ military martial-arts mmorts       horror       tower-defense            ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
'''

    print(tags+'\n')
    try:
        tag = str(input('''

╔══════════════════════════════════════════════════════════════════════════╗
║ Elija las categorias.Puedes escoger más de una, separalas con un espacio ║
╚══════════════════════════════════════════════════════════════════════════╝

> '''))
        if not tag == 'all' and tag != '':
            tagFull = '&category='+tag
        else:
            tagFull = ''

    except ValueError:
        tagFull = ''
        print('\ndebido a un fallo, se escogerá la opción por defecto(pc)') 


    try:
        ordenar = str(input('''
                            
╔═════════════════════════════════════╗
║ ¿como desea ordenar los resultados? ║
╠═════════════════════════════════════╣
║ popularidad [default]               ║
║ fecha de salida                     ║
║ alfabeticamente                     ║
║ relevancia                          ║
╚═════════════════════════════════════╝

> '''))
        if ordenar == 'popularidad':
           ordenar = 'popularity'
           
        elif ordenar == 'fecha de salida':
            ordenar = 'release-date'
            
        elif ordenar == 'alfabeticamente':
            ordenar = 'alphabetical'
        elif ordenar == 'relevance':
            ordenar = 'relevancia'
        else:
            ordenar = 'popularity'
    except ValueError:
        ordenar = 'popularity'
        print('\ndebido a un fallo, se escogerá la opción por defecto(popularidad)') 


    url= 'https://www.freetogame.com/api/games?platform='+plataforma+'&sort-by='+ordenar + tagFull
    
    #seVienenCositas = 'https://www.freetogame.com/api/comingsoon'

    r= requests.get(url)
    save(url)


def bannerDef():
    try:   

        banner = int(input('''
                        
    ╔════════════════════════════╗
    ║       Juegos Gratis        ║
    ╠════════════════════════════╣
    ║ [1]todos los juegos gratis ║
    ║ [2]búsqueda personalizada  ║
    ╚════════════════════════════╝

    > '''))
        if banner == 1:
            todos()
        elif banner == 2:
            custom()
        else:
            print('introduzca una respuesta valida')
            bannerDef()
    except ValueError:
        print('Introduzca una opción válida')
        bannerDef()
bannerDef()