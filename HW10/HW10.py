import requests
import random
page = random.randint(1, 7438)
pageSize = 1
url = f'https://api.disneyapi.dev/character?pageSize={pageSize}&page={page}'
response = requests.get(url)
imageUrl = None
sour = None
if response.ok:
    as_json = response.json()
    data = as_json["data"]
    name = data["name"]
    print(f"Name - {name}")
    fil = data["films"]
    print(f"Films - {fil}")
    sfil = data['shortFilms']
    print(f"Short Films - {sfil}")
    tvs = data['tvShows']
    print(f"TV shows - {tvs}")
    vgames = data['videoGames']
    print(f"Video games - {vgames}")
    try:
        imageUrl = data['imageUrl']
        print(f"Image (url) - {imageUrl}")
    except Exception:
        print('Cant get image url')
    try:
        sour = data['sourceUrl']
        print(f"Source (url) - {sour}")
    except Exception:
        print("Cant get Source url")

else:
    print('Щось пішло не так...')
    print(f'{response.status_code=}')