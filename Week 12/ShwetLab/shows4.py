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

def get_episodes_of_season(season_id: int) -> list[dict]:
    """
    Get the episodes of a given season of a show
    season_id is the id (not the number!) of the season
    """
    url = BASE_URL + f"seasons/{season_id}/episodes"
    response = requests.get(url)
    status = response.status_code
    if status == 200:
        data = response.json()
        return data
    else:
        return None

def format_episode_name(episode: dict) -> str:
    """
    Format the episode name
    """
    if episode['season']:
        formatted_string = f"S{episode['season']}E"
    else:
        formatted_string = "S?E"
    if episode['number']:
        formatted_string += f'{episode["number"]} '
    else:
        formatted_string += '? '
    if episode['name']:
        formatted_string += f"{episode['name']} (rating: "
    else:
        formatted_string += "? (rating: "
    if episode['rating']:
        rating = episode['rating']['average']
        formatted_string += f"{rating})"
    else:
        formatted_string += "?)"
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
        season = int(input("Select a season:"))
        id = results[season-1]['id']
        results = get_episodes_of_season(id)
        n = 1
        for result in results:
            print(f"{n}. {format_episode_name(result)}")
            n += 1

if __name__ == '__main__':
    main()