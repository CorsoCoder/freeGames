import requests
import pandas as pd

def save(url, csv_file='OpenWithLibreOffice.csv', guardar_csv=True):
    """
    Descarga datos JSON de la URL, convierte a DataFrame y opcionalmente guarda a CSV.
    """
    r = requests.get(url)
    r.raise_for_status()  # Para lanzar error si falla la petición

    data = r.json()  # directamente convierte JSON a lista/dict
    df = pd.DataFrame(data)

    if guardar_csv:
        df.to_csv(csv_file, index=False)
        print(f"Datos guardados en {csv_file}")

    return df  # Devuelve DataFrame para usarlo en memoria

# -----------------------

def todos():
    url = 'https://www.freetogame.com/api/games'
    df = save(url)
    print(df.head())  # ejemplo: muestra primeras filas

# -----------------------

def custom():
    # --- seleccionar plataforma ---
    plataforma = input('''
╔══════════════════════════════════╗
║ Introduzca la plataforma deseada ║
╠══════════════════════════════════╣
║ pc[default]                      ║
║ browser                          ║
║ all                              ║
╚══════════════════════════════════╝

> ''') or 'pc'

    # --- seleccionar categoría ---
    tags = '''
╔══════════════════════════════════════════════════════════════════════════╗
║                                Categorías                                ║
╠══════════════════════════════════════════════════════════════════════════╣
║ all[default]                                                             ║
║ mmorpg  shooter  strategy  moba  racing                                  ║
║ sports  social  sandbox  open-world  survival  pvp                       ║
║ pve  pixel  voxel  zombie  tank  turn-based                              ║
║ space  third-Person  sailing  top-down  permadeath  first-person         ║
║ mmofps  3d  2d  sci-fi  low-spec  battle-royale                          ║
║ anime  fantasy  fighting  action-rpg  flight                             ║
║ military  martial-arts  mmorts  horror  tower-defense                    ║
╚══════════════════════════════════════════════════════════════════════════╝
'''
    print(tags)
    tag_input = input("Elija las categorías (separadas por espacio) [all]: ") or 'all'
    tagFull = f"&category={tag_input}" if tag_input != 'all' else ''

    # --- seleccionar orden ---
    ordenar = input('''
╔═════════════════════════════════════╗
║ ¿Cómo desea ordenar los resultados? ║
╠═════════════════════════════════════╣
║ popularidad [default]               ║
║ fecha de salida                     ║
║ alfabeticamente                     ║
║ relevancia                          ║
╚═════════════════════════════════════╝

> ''').lower()

    mapping_orden = {
        'popularidad': 'popularity',
        'fecha de salida': 'release-date',
        'alfabeticamente': 'alphabetical',
        'relevancia': 'relevance'
    }
    ordenar = mapping_orden.get(ordenar, 'popularity')

    # --- construir URL y guardar ---
    url = f'https://www.freetogame.com/api/games?platform={plataforma}&sort-by={ordenar}{tagFull}'
    df = save(url)
    print(df.head())  # muestra primeras filas

# -----------------------

def bannerDef():
    while True:
        try:   
            banner = int(input('''
╔═════════════════════════════╗
║       Juegos Gratis         ║
╠═════════════════════════════╣
║ [1] Todos los juegos gratis ║
║ [2] Búsqueda personalizada  ║
╚═════════════════════════════╝

> '''))
            if banner == 1:
                todos()
                break
            elif banner == 2:
                custom()
                break
            else:
                print('Introduzca una respuesta válida')
        except ValueError:
            print('Introduzca una opción válida')

bannerDef()
