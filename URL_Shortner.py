import pyshorteners

url = input("Input Your Desire URL: ")

short_URL = pyshorteners.Shortener().tinyurl.short(url)

print("Short URL: ", short_URL)
