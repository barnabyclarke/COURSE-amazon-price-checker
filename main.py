import requests
from bs4 import BeautifulSoup
import smtplib
# import lxml    # just need to import it and then not needed after

URL = "https://www.amazon.co.uk/PlayStation-9395003-5-Console/dp/B08H95Y452/ref=sr_1_1?keywords=ps5&qid=1666169340&" \
      "qu=eyJxc2MiOiI0LjM5IiwicXNhIjoiNi4xNyIsInFzcCI6IjYuMDkifQ%3D%3D&sprefix=ps%2Caps%2C52&sr=8-1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

password = "x"
my_gmail = "x"

response = requests.get(url=URL, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "lxml")
price = float(soup.find(class_="a-offscreen").get_text().strip("£"))
product_title = soup.find(id="productTitle").get_text().strip()

if price < 400:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs="x",
            msg=(f"Subject: Amazon Price Alert!\n\n"
                 f"{product_title} is now £{price}.\n"
                 f"{URL}").encode("utf-8")
        )
    print("Email sent")
