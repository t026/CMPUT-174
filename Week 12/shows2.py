'''
Lab 9 Version 2
Name: Tanishq
Description: Implements a function that formats a dictionary to return a string with more details.
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
        return(response.json())

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

if __name__ == '__main__':
    main()