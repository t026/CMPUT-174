oldEpisodeFormat = input("Enter the name of the episode in the inital format:")
oldEpisodeFormatList = oldEpisodeFormat.split("_")
season =  oldEpisodeFormatList[0][1:]
episode = oldEpisodeFormatList[1][1:]
title = oldEpisodeFormatList[2]
print(f"Season {season}, Episode {episode}: {title} (The Simpsons)")


