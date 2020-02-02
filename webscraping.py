import bs4 as bs
import urllib.request
import pandas as pd

sauce = urllib.request.urlopen('https://en.wikipedia.org/wiki/List_of_most-streamed_songs_on_Spotify')
soup = bs.BeautifulSoup(sauce,'lxml')
table = soup.find('table')
table_rows = table.find_all('tr')

l = []
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    l.append(row)

df = pd.DataFrame(l,columns = ["Song","artist","album","streams_in_mil","date"])
print(df)    
    
