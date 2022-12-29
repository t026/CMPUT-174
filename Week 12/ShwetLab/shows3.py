import requests

# Uncomment two lines below if you get status code 429 (rate limit exceeded)
# import requests_cache
# requests_cache.install_cache('cmput174_cache')

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    url = BASE_URL + "search/shows"
    response = requests.get(url, params={'q':query})
    status = response.status_code
    if status == 200:
        data = response.json()
        return data
    else:
        return None

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    if show['name']:
        formatted_string = f"{show['name']} ("
    else:
        formatted_string = "? ("
    if show['premiered']:
        year = show['premiered'].split("-")
        year = year[0]
        formatted_string += f'{year} - '
    else:
        formatted_string += '? - '
    if show['ended']:
        year = show['ended'].split("-")
        year = year[0]
        formatted_string += f'{year}, '
    else:
        formatted_string += '?, '
    genres = ''
    if show['genres']:
        genrelist = show['genres']
        for i in range(len(genrelist)):
            genres += f"{genrelist[i]}, "
        genres = genres[0:-2]
        formatted_string += f"{genres})"
    return formatted_string

def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    url = BASE_URL + f"shows/{show_id}/seasons"
    response = requests.get(url)
    status = response.status_code
    if status == 200:
        data = response.json()
        return data
    else:
        return None

def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    if season['number']:
        formatted_string = f"Season {season['number']} ("
    else:
        formatted_string = "? ("
    if season['premiereDate']:
        year = season['premiereDate'].split("-")
        year = year[0]
        formatted_string += f'{year} - '
    else:
        formatted_string += '? - '
    if season['endDate']:
        year = season['endDate'].split("-")
        year = year[0]
        formatted_string += f'{year}, '
    else:
        formatted_string += '?, '
    genres = ''
    if season['episodeOrder']:
        formatted_string += f"{season['episodeOrder']} episodes"
    else:
        formatted_string += "? episodes"
    return formatted_string

def main():
    """
    Main function 
    """
    query = input("Search for a show: ")
    results = get_shows(query)
    if not results:
        print("No results found")
    else:
        n = 1
        print("Here are the results:")
        for result in results:
            show = result["show"]
            print(f"{n}. {format_show_name(show)}")
            n += 1 
        show = int(input("Select a show:"))
        id = results[show-1]['show']['id']
        results = get_seasons(id)
        n = 1
        for result in results:
            print(f"{n}. {format_season_name(result)}")
            n += 1

if __name__ == '__main__':
    main()