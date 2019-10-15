# scraddit
Reddit scrapper written in Python that downloads images from given subreddits

**Caution: Work in progress**

This module depends on **BeautifulSoup** and **requests**

## How to setup and run
- Install **BeautifulSoup** package ('pip install bs4')
- Change *page_url* in *reddit-scrapper.py* to the link of the subreddit you want to scrap
- Download and run *reddit-scrapper.py* ('python yourlocation\reddit-scrapper.py')

## Version changes
**v1.0 (2019/09/01)**

Download images from subreddits that does not need age verification or any other type of authentication based on cookies. The issue with age verification is that it redirects to a different page instead of directly loading the subreddit.

**v1.1 (2019/10/15)**

File name is as same as the post name now.
Program asks for the subreddit URL now. (don't have to change it in the code)
User can now input the number of retry attempts needed when establishing the connection. (at least 10 is recommended)

## Future updates
What my plans are for this project as of now (Last updated: 2019/09/01)
- [ ] Fix the issue with pages that have age verification
- [ ] Need to add support for gifs and videos
