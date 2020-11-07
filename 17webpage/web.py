import requests
from bs4 import BeautifulSoup
url = 'https://www.elespectador.com'
print("###### Titles of website " +url +"#####")
r = requests.get(url)
r_html = r.text
soup = BeautifulSoup(r_html,features='lxml')
for story_heading in soup.find_all(class_="Card_CustomLabel"):
    if story_heading.title:
        #print(story_heading.title)
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        #print(story_heading)
        print(story_heading.contents[0].strip())
        
user = input("Tell me the github user you want to see the repos: ")
url = 'https://github.com/'+user+'?tab=repositories'
r=requests.get(url)
soup = BeautifulSoup(r.text, features='lxml')
for repos in soup.find_all(class_='wb-break-all'):
    print(repos.a.text.replace("\n", " ").strip())
