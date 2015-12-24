import requests
from bs4 import BeautifulSoup

URL= "https://www.google.co.in/search?q=best+inspirational+quotes&client=safari&rls=en&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiRwq7J6fPJAhVHUY4KHfeIBRQQ_AUIBygB&biw=1280&bih=689"

r= requests.get(URL)

print(r.status_code)
value= r.text

output_file= open("data.txt", "w")
output_file.write(value)

#print(value)
