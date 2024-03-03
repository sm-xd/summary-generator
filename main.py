from downloader import *
from youtube import *

def main():
    yt = YouTube( 
    str(input("Enter the URL of the video you want to download: \n>> "))) 
    download(yt)
    summary()


if __name__ == "__main__":
    main()