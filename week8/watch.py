# python3 watch.py

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    

    if 'iframe' not in s or 'src' not in s:
        return None


    pattern = re.search(r"(https?)://(www\.)?(youtube\.com|youtu\.be).{18}", s)
    
    if pattern:
        url = re.sub(r"embed/", "", pattern.group())
        url = re.sub(r"youtube\.com", "youtu.be", url)
        url = re.sub(r"www\.", "", url)

        protocal = pattern.group(1)
        
        if protocal[-1] == 'p':
            protocal = protocal+'s'
            url = re.sub(r"http", protocal, url)        
        
        return(url)
    else:
        return None

if __name__ == "__main__":
    main()



def parse(s):

    pattern = re.search(
        r'<iframe[^>]*src="https?://(?:www\.)?(?:youtube\.com/embed/|youtu\.be/)([a-zA-Z0-9_-]{11})"',
        s
    )

    if pattern:
        return "https://youtu.be/" + pattern.group(1)

    return None