from pytube import YouTube

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        # Download the video as mp3

        
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")
list_id=[
"fyEAX7Cd3OE",
"mSe6iZF_UfE",
"fRyhqobl0sk",
"ZSRzCbpIxZo",
"O1x-hOOrl5E",
"AN_R4pR1hck",
"QJ5DOWPGxwg",
"7i5MRfWK-o8",
"LUjn3RpkcKY",
"k4QKLWRKDRA",
"X1ZDtVIQYrA",
"AMeGVJ1L2ks",
"v5ryZdpEHqM",
"N8NcQzMQN_U",
"4MS9N8qgi5o",
"Dkq3LD-4pmM",
"8wkyER6sv6I",
"sK0R0z9ts7g",
"YiE48jeMOwE"]

for elemt in list_id:
    link = "https://www.youtube.com/watch?v="+elemt
    Download(link)
