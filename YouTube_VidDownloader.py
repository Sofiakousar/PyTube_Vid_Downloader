# -*- coding: utf-8 -*-
from pytube import YouTube
from sys import argv
from os import path

link = argv[1]
yt = YouTube(link)

print("Title: ",yt.title)
print("Views: ",yt.views)
print("Length: ",yt.length ,"seconds")
print("YouTuber Name: ", yt.author)


yd = yt.streams.get_highest_resolution()

# download_path = 'Specified path'
download_path = 'C:/Users/mohdq/OneDrive/Desktop/YouTube Downloads'

# Add your path while EXECUTING 
# download_path = argv[2] if len(argv) > 2 else path.join(path.expanduser('~'), 'Downloads')

print("Downloading to: ",download_path)

try:
    yd.download(download_path)
    print("Download completed successfully!")
except Exception as e:
    print("Error: ",e)

# STEPS
    
# Imports required modules: pytube for YouTube video downloading, sys for command-line arguments, and os for path handling.
    
# Gets the video URL from the first command-line argument.
    
# Creates a YouTube object from the provided URL.
    
# Prints the video title, views, and length.
    
# Gets the highest resolution video stream available.
    
# Determines the download path from the second command-line argument or uses the user's Downloads folder as the default.
    
# Prints the download path.
    
# Downloads the video to the specified path using a try-except block to handle exceptions.
    
# Prints a success message if the download is successful or an error message if an exception occurs.