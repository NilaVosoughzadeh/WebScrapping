import requests
from bs4 import BeautifulSoup

url = "https://tv.filmnet.ir"
response = requests.get(url)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text,'html.parser')

movies = soup.find_all("h4",attrs={"class":"css-stgv2v eg0dt7k0"})

index = 1
for movie in movies:
    print(f"{index}) {movie.text}")
    index += 1