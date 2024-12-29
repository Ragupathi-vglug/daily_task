from pytube import YouTube
url=YouTube("https://youtu.be/OAFgzShfyvw?si=S4Ef-ovw4TNO6-cK")
link=url.streams.get_highest_resolution()
print("downloading...")
link.download(filename="ragu")
print("Downloaded successfully")