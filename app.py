from flask import Flask,jsonify
import requests
from bs4 import BeautifulSoup



app = Flask(__name__)

@app.route('/<string:ap>')
def hello(ap: str):

    URL = 'https://www.aviationweather.gov/metar/data?ids={}&format=decoded&hours=0&taf=off&layout=on'.format(ap)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,"html.parser")
    #result = soup.find(id="awc_main_content_wrap")
    result_final = soup.find_all('td')


    date = soup.find('strong').text
    airport = result_final[1].text
    temp = result_final[5].text
    dewpoint = result_final[7].text
    altimeter = result_final[9].text
    wind = result_final[11].text
    visibility = result_final[13].text
    ceiling = result_final[15].text
    clouds = result_final[17].text

    metars = {
        'airport': airport,
        'date': date,
        'temp': temp,
        'dewpoint':dewpoint,
        'altimeter': altimeter,
        'wind': wind,
        'visibility': visibility,
        'ceiling':ceiling,
        'clouds':clouds
        
    }




    
    return jsonify(metars= metars)



if __name__ == '__main__':
    app.run(debug=True)