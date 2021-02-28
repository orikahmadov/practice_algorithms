import requests
from bs4 import BeautifulSoup
import smtplib
import os, imghdr
from email.message import EmailMessage

req =  requests.get("https://www.bbc.com/news").text
soup =  BeautifulSoup(req, features="lxml")
a_tags = [tag for tag in soup.find_all("a") ]
message = "Message"
paragraphs = [" ".join(p.text.split())  for p in soup.find_all("p", class_="gs-c-promo-summary gel-long-primer gs-u-mt nw-c-promo-summary")]
headlines = [" ".join(tag.text.split()) for tag in soup.find_all("h3", class_="gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text")]



EMAIL_ADDRESS  =  os.environ.get("EMAIL_ADDRESS")
PASSWORD  =  os.environ.get("PASSWORD")

with open("message_text.txt", "r", encoding="ascii", errors="ignore") as message:
    lines =  message.readlines()
    string =  " ".join(lines)
    test = "\n".join(lines)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        addresses = [EMAIL_ADDRESS]
        server.login(EMAIL_ADDRESS, PASSWORD)
        letter = EmailMessage()
        letter["Subject"] = "News"
        letter["FROM"] = EMAIL_ADDRESS
        letter["TO"] = addresses
        letter.set_content(string)
        with open("Screenshot (2).png", "rb") as f:
            file_data =  f.read()
            file_type =  imghdr.what(f.name)
            file_name =  f.name
            server.send_message(letter)



