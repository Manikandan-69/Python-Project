"""
Steps to follow:
1) Install the request and beautifulsoup module to access link and get html conetent respectively.
2)First we access the link by using request.get()
3)fetch all the contents in the page by using .content function in bs
4)Find the key values to get the lines using .find  or .find_all function
5)using loop to traverse to each line and get the required details
"""
import requests
from bs4 import BeautifulSoup as bs

github_profile='https://github.com/Manikandan-69?tab=repositories'
req=requests.get(github_profile) 

"""
200 OK → Request was successful.
301 Moved Permanently → The URL has been redirected (e.g., from HTTP to HTTPS).
403 Forbidden → Access is denied (GitHub might block scrapers).
404 Not Found → The page does not exist.
429 Too Many Requests → You've hit GitHub's rate limit.
500 Internal Server Error → The server has an issue
"""
scraper=bs(req.content,'html.parser')
repo_name=scraper.find_all('a',itemprop="name codeRepository")

"""
<a href="/Manikandan-69/Python-Project" itemprop="name codeRepository">
        Python-Project</a>

"""
"""
It fetch only the public repo name not private
"""
for repo in repo_name:
    print(repo.text.strip())