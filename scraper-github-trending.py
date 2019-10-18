import requests
from bs4 import BeautifulSoup
import csv

page = requests.get('https://github.com/trending')
soup = BeautifulSoup(page.text,'html.parser')
# print(soup)

repo = soup.find(class_="explore-pjax-container container-lg p-responsive pt-6")

file_name = "github_trending_today.csv"

f = csv.writer(open(file_name,'w',newline=''))

f.writerow(['Developer', 'Repo-name', 'no_of_stars'])   


repo_list = repo.find_all(class_='Box-row')


# print(len(repo_list))

for repo in repo_list:
    # full_repo_name = repo.find('a').split('/')
    #extract the developer name at index [0]
    developer = repo.find(class_='text-normal')
    #extract the repo name at index [1]
    # repo_name = full_repo_name[1].strip()

    stars = repo.find(class_='octicon octicon-star').parent.text.strip()
    print('developer',developer)
    # print('repo_name',repo_name)
    print('stars',stars)
    print('writing rows')

    f.writerow([developer,stars])