import requests
import re

def extract_url(url):
    response = requests.get(url)
    html_content=response.text

    url_pattern = r"https?://[^s] \.(png|jpg|jpeg|icon|svg|bmp|gif)"
    urls = re.findall(url_pattern, html_content)
    
    # eindigt met .png .jpg .jpeg .icon .svg .bmp .gif


def main():
    url = "https://www.duoparty.be/"
    urls = extract_url(url)
    print("extracted urls")
    for url in urls:
        print(url)