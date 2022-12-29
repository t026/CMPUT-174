def display_header(string:str)-> None:
    '''Prints the header'''
    print(f"+{'-'*len(string)}+")
    print(f"|{string}|")
    print(f"+{'-'*len(string)}+")
def main():
    display_header("Math is Fun-Ends")
main()