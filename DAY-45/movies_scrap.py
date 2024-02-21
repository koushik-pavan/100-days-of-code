import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
content = response.content.decode("utf-8")

soup = BeautifulSoup(content, "html.parser")
all_movies = soup.find_all('h3', class_ = "title")
titles = []
for i in all_movies:
    titles.append(f"{i.text}\n")
titles.reverse()

with open(r"C:\Users\koush\PycharmProjects\days100code\DAY-45\movies.txt", "w") as f:
    f.writelines(titles)
