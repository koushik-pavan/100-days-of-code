from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text
article_text = []
article_link = []
article_score = []
soup = BeautifulSoup(yc_web_page, "html.parser")
content = soup.select('span.titleline a' )
for i in range(0, len(content),2):
    article_text.append(content[i].text)
    article_link.append(content[i]['href'])

upvotes = soup.select('span.score')
for i in range(0, len(upvotes)):
    article_score.append(int(upvotes[i].getText().split()[0]))

print(article_score)
largest_number = max(article_score)
largest_index = article_score.index(largest_number)
print(largest_index)
#print(article_text)
#print(article_link)
