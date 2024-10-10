import requests
from bs4 import BeautifulSoup 
import pandas as pd
city=input("Enter your city name:")
url="https://www.zomato.com/"+city+"/best-restaurants"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup=BeautifulSoup(response.text,"html.parser")
restaurants = soup.find_all('div', class_="jumbo-tracker")
data={"restaurant_Names":[],
      "restaurant_ratings":[]}
for i in restaurants:
    data["restaurant_Names"].append(i.select("h4")[0].get_text())
    data["restaurant_ratings"].append(i.select(".cILgox")[0].get_text())
pd.DataFrame(data).to_excel('Top 10 Restaurants in'+city+' According to Zomato.xlsx',sheet_name='Sheet1')
