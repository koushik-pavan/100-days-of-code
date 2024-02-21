import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

sender_mail = "koushikvaddadi@gmail.com"
receiver_mail = "koushikvaddadi@gmail.com"

target = 200
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
response = requests.get(url=url, headers=header)
data = response.text

soup = BeautifulSoup(data, "lxml")
#price = soup.find("span", class_="a-offscreen")
price_whole = soup.select_one("span.a-price-whole").getText()
price_fraction = soup.select_one("span.a-price-fraction").getText()
print(price_whole)
if price_whole and price_fraction:
    current_price = float(f"{price_whole}{price_fraction}")
else:
    current_price = None

msg = f"BUY IT NOW!!!The product you are looking for is at {current_price} which is less than {target} at {url} "

if current_price!=None and current_price<target:
    try:
        smtpobj = smtplib.SMTP(host="smtp.gmail.com", port=587)
        smtpobj.starttls()
        smtpobj.login("koushikvaddadi@gmail.com", "xevr lwyg anqv mnmc")
        smtpobj.sendmail(from_addr=sender_mail, to_addrs=receiver_mail, msg=msg)
        print("successful")
    except:
        print("unsuccessful")