import time
import sys
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlRequest
from urllib.request import urlretrieve as urlRetrieve

# this could be changed to any url according to user's liking
page_url = 'https://old.reddit.com/r/witcher'

try:
    urlClient = urlRequest(page_url)
except Exception:
    # for loop is used instead of time.sleep(5) to make the countdown timer
    for i in range(5):
        # most of the time the error is a 429 error. best solution is to try again after few seconds
        msg = str('Error occurred. Retrying in ' + str(5-i) + ' secs.')
        # \r is used to move cursor back to the beginning of the line so that it won't print on a new line
        sys.stdout.write('\r' + msg)
        time.sleep(1)
    # trying for the second time. this could be improved using a loop. will check later
    try:
        urlClient = urlRequest(page_url)
    except Exception:
        # if error is still there then display a message and terminate the process
        sys.stdout.write('\nRetrying failed. Please check your internet connection and run again.')
        exit()

# parsing the html
page_soup = soup(urlClient.read(), "html.parser")
# close the open internet connection
urlClient.close()

# getting image urls to img_urls list
img_urls = []
containers = page_soup.findAll("div", {"data-type": "link"})
for container in containers:
    urls = container["data-url"]
    # finding urls with .jpg at the end because some reddit posts may not have image on them thus causing an error
    if urls.find(".jpg") != -1:
        img_urls.append(urls)

# downloading the image
for i in range (len(img_urls)):
    file_name = str(i) + '.jpg'
    urlRetrieve(img_urls[i], file_name)
