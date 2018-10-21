import io
import os
from google.oauth2 import service_account

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

from kivy.config import Config

from returnLocation import returnLocationTime
from create_event import creat_event
import requests


Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: True
    ToggleButton:
        text: 'Start / Stop'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()
''')


credentials = service_account.Credentials.from_service_account_file("credential-vision.json")
# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=credentials)


def image_process(file_name):
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    result = []
    title = ""
    max_area = 0
    for text in texts:
        s = text.description
        vertices = ([(vertex.x, vertex.y) for vertex in text.bounding_poly.vertices])
        area = abs((vertices[0][0]-vertices[2][0])*(vertices[0][0]-vertices[1][0]))
        if area > max_area:
            max_area = area
            title = s.replace("\n", " ")
        s = s.replace("\n", " ")
        result += (s.split(" "))

    return result, title


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        file_name = "IMG_"+timestr+".png"
        camera.export_to_png(file_name)
        print("Captured")
        texts, title = image_process(file_name)

        location, times = returnLocationTime(texts)

        url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'

        params = dict(
            input=location,
            inputtype="textquery",
            fields="formatted_address,name,opening_hours,rating",
            locationbias="circle:2000@42.447548,-76.482721",
            key="AIzaSyATjqU9jorOGXwqWkpzTloRWBpNjiiW_YE"
        )

        resp = requests.get(url=url, params=params)
        data = resp.json()
        try:
            location = data["candidates"][0]["name"]
        except:
            location = ""

        date = (str(times).split(" "))[0]
        date = "2018"+date[4:]
        start_time = (str(times).split(" "))[1]
        print("location:", location)
        print("date:", date)
        print("time:", start_time)
        print("title:", title)

        start_time = start_time[:8]
        end_time = str(int(start_time[:2])+1)+start_time[2:]
        creat_event(title, location, date, start_time, end_time)



class SmartPoster(App):

    def build(self):
        return CameraClick()


SmartPoster().run()
