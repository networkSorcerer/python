import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "안녕하세요. 플라스크 웹 입니다."

@app.route("/weather")
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    response = requests.get(url)
    # HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")
    output = ""

    for loc in soup.select("location"):
        output += f"<h3>{loc.select_one('city').string}</h3>"  # Corrected closing tag
        output += f"날씨 : {loc.select_one('wf').string}<br/>"
        output += f"최저/최고 기온 : {loc.select_one('tmn').string}/{loc.select_one('tmx').string}<br/><hr/>"  # Corrected and added .string for tmn and tmx

    return output

if __name__ == "__main__":
    app.run()
