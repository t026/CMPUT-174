'''
Lab 9 Version 3
Name: Tanishq
Description: Asks the user for a show and returns information about the seasons of that show
'''
import requests, pprint  #imports pprint to debug print lists of dictionaries

# Uncomment two lines below if you get status code 429 (rate limit exceeded)
# import requests_cache
# requests_cache.install_cache('cmput174_cache')

BASE_URL = "https://api.tvmaze.com/"

def get_shows(query: str) -> list[dict]:
    """
    Search for TV shows using the TV Maze API.
    If the show is not found, return None
    """
    response = requests.get(BASE_URL + 'search/shows', params = {'q':query})  #adds the endpoint to the base url and passes a parameter with 'q' as the key and the query as the value
    if response.status_code == 200:  #checks if the status code is allowed
        return response.json()

def format_show_name(show: dict) -> str:
    """
    Format the show name.
    """
    mydict = {'name' : '?', 'premiered' : '?', 'ended' : '?', 'genres' : '?'}  #uses a dictionary to store the values.
    for i in mydict:
        if show[i]:
            if i == 'premiered' or i == 'ended':
                mydict[i] = show[i].split("-")[0]  #only stores the year 
            else:
                mydict[i] = show[i]
    genres = mydict['genres']
    if genres != "?":  #separates a list of genres into a sentence.
        genres = ''
        for i in range(len(mydict['genres'])):
            genres += mydict['genres'][i]
            if i != len(mydict['genres']) - 1:
                genres += ", "  #adds a comma if it is not the last one.
    return f"{mydict['name']} ({mydict['premiered']} - {mydict['ended']}, {genres})"

def get_seasons(show_id: int) -> list[dict]:
    """
    Get the seasons for a given show_id
    """
    response = requests.get(BASE_URL + f"shows/{show_id}/seasons")  
    if response.status_code == 200:  #checks if status is valid.
        return response.json()  #returns a list of dictionaries if valid, returns None if not.

def format_season_name(season: dict) -> str:
    """
    Format the season name
    """
    mydict = {'number' : "?", 'premiereDate' : "?", 'endDate' : "?", 'episodeOrder' : "?"}  #stores the data in a dictionary.
    for i in mydict:
        if season[i]:
            if i == 'premiereDate' or i == 'endDate':
                mydict[i] = season[i].split("-")[0]
            else:
                mydict[i] = season[i]
    return f"Season {mydict['number']} ({mydict['premiereDate']} - {mydict['endDate']}), {mydict['episodeOrder']} episodes"

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
            print(f"{n}. {format_show_name(result['show'])}")
            n += 1 
        selection = int(input("Select a show:"))
        if selection > 0 and selection <= 10:
            seasons = get_seasons(results[selection-1]['show']['id'])
            count = 1
            for season in seasons:
                print(f"{count}. {format_season_name(season)}")
                count += 1
        else:
            print("Not a valid show")
if __name__ == '__main__':
    main()

