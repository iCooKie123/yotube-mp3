
# importing packages
from pytube import YouTube
import os
def download(link):
    # url input from user
    yt = YouTube(
        str(link))
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = ""
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

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
    download(link)