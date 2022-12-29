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

if __name__ == '__main__':
    main()