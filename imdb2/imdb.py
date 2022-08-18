import requests
from bs4 import BeautifulSoup

"""Datayı çekeceğin sitenin urlsini belirliyoruz."""
url="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
"""url ye request atıyoruz."""
r=requests.get(url).content
"""İçeriği parse ediyoruz."""
soup=BeautifulSoup(r,"html.parser")
"""Kullanıcıdan rating için değer istiyoruz."""
a=float(input("Lütfen izlemek istediğiniz filmin ratingini giriniz:"))
"""parse edilen sayfadan alınacak verileri seçiyoruz"""
movies=soup.find_all("td",{"class":"titleColumn"})
ratings=soup.find_all("td",{"class","ratingColumn imdbRating"})

for movie,rating in zip(movies,ratings):
    movie=movie.text
    rating=rating.text

    movie=movie.strip()
    movive=movie.replace("\n"," ")

    rating=rating.strip()
    rating=rating.replace("\n"," ")
    
    if(float(rating)>=a):
        print("************************************************\n")
        print("Film Adı:"+movie,"Filmin Ratingi:"+rating)