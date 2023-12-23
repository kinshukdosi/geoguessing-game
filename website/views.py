from flask import Blueprint, redirect, render_template, request
import random

views = Blueprint('views', __name__)

bearing = 0
coordinates = ""
imgsrc = ""
@views.route('/', methods=['GET', 'POST'])
def geoguess():
    global bearing
    global coordinates
    global imgsrc
    
    answer = 0
    result = ""
    dict = {
        "51.90085164360474, -2.05449667652761": 285,
        "51.905367372524125, -2.0598744141647347": 20,
        "51.90379881573086, -2.1148557115609115": 185,
        "51.91807051786763, -2.1084265596397134": 30,
        "51.90289151523852, -2.076461082877884": 30,
        "51.89745465456302, -2.098871681400098": 345, 
        "51.89378169502885, -2.0800451374206257": 295,
        "51.897452705241086, -2.0774155351780226": 215,
        "51.89140019702322, -2.044941206430609": 135,
        "51.92326682406667, -2.0886964369053307": 245,
        "51.906748053424025, -2.1150289099024397": 220,
        "51.90329636671142, -2.0973258624476583": 125,
        "51.91195303281294, -2.067969295850498": 83,
        "51.91063239182318, -2.0795770232157524": 20,
        "51.89731382310573, -2.1229642882349564": 340,
        "51.8790676534313, -2.107435997176357": 288,
        "51.90230968655359, -2.0511356618209615": 40,
    }
    if request.method == "GET":
        coordinates = random.choice(list(dict.keys()))
        bearing = dict[coordinates]
        size = 450
        key = ""
        imgsrc = f"https://maps.googleapis.com/maps/api/streetview?size={size}x{size}&location={coordinates}&fov=80&heading={bearing}&pitch=0&key={key}"

    
    if request.method == "POST":
        bearingguess = request.form.get('bearing')

        if int(bearingguess) >= (bearing - 15) and int(bearingguess) <= (bearing + 15) or int(bearingguess) == bearing:
            print(1, coordinates, bearing)
            result = "win"

        else:
            print(0, coordinates, bearing)
            result = "lose"
            answer = bearing
    return render_template('geo.html', imgsrc = imgsrc, result=result, answer = answer)