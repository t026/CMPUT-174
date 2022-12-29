oldEpisodeFormat = input("Enter the name of the episode in the inital format:")
'''using the split function with separator _ to split the string into an array where the first item is season
the second item is the episode, the third item is the title.'''
oldEpisodeFormatList = oldEpisodeFormat.split("_")
#takes the last 2 for season and episode to get rid of the S and the E
season =  oldEpisodeFormatList[0][1:]
episode = oldEpisodeFormatList[1][1:]
title = oldEpisodeFormatList[2]
#uses an f string to print it out.
print(f"Season {season}, Episode {episode}: {title} (The Simpsons)")
