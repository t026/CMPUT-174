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
    return requests.get(BASE_URL + "search/shows", params={'q':query}).json()

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    names = ['name', 'premiered', 'ended', 'genres']
    values = ['?', '?', '?', '?']
    for i in range(len(names)):
        if i == 1 or i == 2:
            if show[names[i]]:
                year = show[names[i]].split("-")
                year = year[0]
                values[i] = year
        elif show[names[i]]:
            values[i] = show[names[i]]
    name = values[0]
    premiered = values[1]
    ended = values[2]
    genres = values[3]
    genrestring = ''
    for i in genres:
        genrestring += f"{i}, "
    genrestring = genrestring[0:-2]
    returnstring = f"{name} ({premiered} - {ended}, {genrestring})"
    return returnstring

def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    return requests.get(BASE_URL + f"shows/{show_id}/seasons").json()

def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    names = ['number', 'premiereDate', 'endDate', 'episodeOrder']
    values = ['?', '?', '?', '?']
    for i in range(len(names)):
        if i == 1 or i == 2:
            if season[names[i]]:
                year = season[names[i]].split("-")
                year = year[0]
                values[i] = year
        elif season[names[i]]:
            values[i] = season[names[i]]
    number = values[0]
    premiereDate = values[1]
    endDate = values[2]
    episodeOrder = values[3]
    returnstring = f"Season {number} ({premiereDate} - {endDate}), {episodeOrder} episodes"
    return returnstring

def get_episodes_of_season(season_id: int) -> list[dict]:
    """
    Get the episodes of a given season of a show
    season_id is the id (not the number!) of the season
    """
    return requests.get(BASE_URL + f"seasons/{season_id}/episodes").json()

def format_episode_name(episode: dict) -> str:
    """
    Format the episode name
    """
    names = ['season', 'number', 'name', 'rating']
    values = ['?', '?', '?', '?']
    for i in range(len(names)):
        if episode[names[i]]:
            values[i] = episode[names[i]]
    season = values[0]
    number = values[1]
    name = values[2]
    rating = values[3]['average']
    returnstring = f"S{season}E{number} {name} (rating: {rating})"
    return returnstring

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
        seasonresults = get_seasons(id)
        o = 1
        for result in seasonresults:
            print(f"{o}. {format_season_name(result)}")
            o += 1
        season = int(input("Select a season:"))
        id = seasonresults[season-1]['id']
        episoderesults = get_episodes_of_season(id)
        p = 1
        for result in episoderesults:
            print(f"{p}. {format_episode_name(result)}")
            p += 1
        

if __name__ == '__main__':
    main()