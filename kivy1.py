import time

import kivy
kivy.require('2.3.1') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from pymongo import  mongo_client



#class MyApp(App):
client = mongo_client.MongoClient('mongodb://127.0.0.1:27017/')
#print(client)

db = client.enos
collection = db.collection

# Insert a document
collection.insert_many([{"name": "Courtney", "age": 26}, {"name": "Lisa", "age": 50}, {"name": "christen", "age": 25}])
#print(collection.insert_one({"name": "Alice", "age": 30}))
#print(collection.find())
#print("success")

#time.sleep(3)

client.close()

'''
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing='10', padding=10)
        TextInput(hint_text="Enter details", multiline=True, height=40, size_hint_x=10, size_hint_y=None)
        layout.add_widget(Label(text='Name', color='red', font_size=60))
        layout.add_widget(TextInput(hint_text="Enter details", multiline=True, height=40, size_hint_x=10, size_hint_y=None))
        layout.add_widget(Label(text='Gender', color='red', font_size=60))
        layout.add_widget(TextInput(hint_text="Enter details", multiline=True, height=40, size_hint_x=10, size_hint_y=None))
        #layout.add_widget(TextInput(hint_text="code", multiline=False, password=True, height=40, size_hint_x=10, size_hint_y=None))
        layout.add_widget(Button(text='Save', size_hint_y=None))

        return layout '''

if __name__ == '__main__':
    print(client)