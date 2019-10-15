from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as url_request
from urllib.request import urlretrieve as url_retrieve
import re

# getting user inputs
url_input = input("Enter the  URL: http://www.reddit.com/r/")
page_url = 'https://old.reddit.com/r/' + str(url_input)
number_of_attempts = input("Enter the number of retry attempts: ")

for i in range(int(number_of_attempts)):
    try:
        url_client = url_request(page_url)
        if url_client != -1:
            break
    except Exception:
        print("Error occurred. Retrying")

# parsing the html
page_soup = soup(url_client.read(), "html.parser")
# close the open internet connection
url_client.close()

# getting image urls to img_urls list
img_urls = []
post_urls = []
post_names = []
file_types = []

containers = page_soup.findAll("div", {"data-type": "link"})
name_containers = page_soup.findAll("a", {"data-event-action": "title"})

# finding image urls
for container in containers:
    urls = container["data-url"]
    # finding urls with .jpg at the end because some reddit posts may not have image on them thus causing an error
    if urls.find(".jpg") != -1:
        img_urls.append(urls)
        post_urls.append(container["data-permalink"])
        file_types.append(".jpg")
    if urls.find(".png") != -1:
        img_urls.append(urls)
        post_urls.append(container["data-permalink"])
        file_types.append(".png")

# finding image names
for each_url in post_urls:
    for each_name in name_containers:
        if each_url == each_name["href"]:
            # removing special characters and setting the length of file names
            name = re.sub('[^A-Za-z0-9 ]+', '', each_name.text)
            name = name[:250]
            post_names.append(name)
            break

# print the number of images detected
print(len(img_urls), "images have been detected")

# downloading the image
for i in range (len(img_urls)):
    file_name = str(post_names[i]) + str(file_types[i])
    url_retrieve(img_urls[i], file_name)
