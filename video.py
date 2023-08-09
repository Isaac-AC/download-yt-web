from pafy import new

url = input("Enter the url: ")

video = new(url)
dl = video.getbest()
dl.download()
