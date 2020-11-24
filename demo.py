import numpy as np
from model import NamedEntityRecognition

model = NamedEntityRecognition(model_path='saved_model\\Model',glove_model_path='Glove_db\\glove25d.db')
text = "London is a very important city in Europe. Many Europeans say it is probably the most beautiful city in Europe. People can go to this place in order to see the monuments as the Tower Bridge, Buckingham Palace… But also they would discover this cosmopolitan place with all of nationalities that are represented in this town. Finally they would enjoy the arts, the music, sports, and the languages that are spoken."

print(model.get_entities(text))