from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/disease-detection')
def disese_detection():
    return render_template("disease.html")


@app.route('/crop-planning')
def crop_planning():
    return render_template("crop.html")


crop_recommendation_model = pickle.load(
    open('Models/model.pkl', 'rb'))


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    # api_key = config.weather_api_key
    api_key = "6ee1dc7bb1bc5a8a16ba813050149c05"
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="

    complete_url = base_url + city_name + "&appid=" + api_key
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None


@ app.route('/crop-recommend')
def crop_recommend():
    title = 'Kisan++ - Crop Recommendation'
    return render_template('crop.html', title=title)


@ app.route('/crop-predict', methods=['POST'])
def crop_prediction():
    title = 'Kisan++ - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        city = request.form.get("city")

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]
            print("Final Prediction", final_prediction)
            return render_template('crop-result.html', prediction=final_prediction, title=title)
        else:
            return render_template('try_again.html', title=title)


if __name__ == "__main__":
    app.run()
