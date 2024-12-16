import requests
import bs4

print("mvm | inroads | bmw | tara")
carPrice = input("Enter car name : ").lower()

url = f"https://karnameh.com/car-price/{carPrice}"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text , 'html.parser')
prices = soup.find_all('p', attrs={"class": "MuiTypography-root MuiTypography-body1 muirtl-22intj"})

for price in prices:
    print(f"Current {carPrice} Price : {price.text}")