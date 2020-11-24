import numpy as  np
from Glove import Golve_embedding
from tensorflow.keras.models import load_model

class NamedEntityRecognition:
    def __init__(self,model_path,glove_model_path,):
        self.id_pos = {0: '$', 1: ',', 2: '.', 3: ':', 4: ';', 5: 'CC', 6: 'CD', 7: 'DT', 8: 'EX', 9: 'FW', 10: 'IN', 11: 'JJ', 12: 'JJR', 13: 'JJS', 14: 'LRB', 15: 'MD', 16: 'NN', 17: 'NNP', 18: 'NNPS', 19: 'NNS', 20: 'PDT', 21: 'POS', 22: 'PRP', 23: 'PRP$', 24: 'RB', 25: 'RBR', 26: 'RBS', 27: 'RP', 28: 'RRB', 29: 'TO', 30: 'UH', 31: 'VB', 32: 'VBD', 33: 'VBG', 34: 'VBN', 35: 'VBP', 36: 'VBZ', 37: 'WDT', 38: 'WP', 39: 'WP$', 40: 'WRB', 41: '``'}
        self.id_label = {0: 'B-art', 1: 'B-eve', 2: 'B-geo', 3: 'B-gpe', 4: 'B-nat', 5: 'B-org', 6: 'B-per', 7: 'B-tim', 8: 'I-art', 9: 'I-eve', 10: 'I-geo', 11: 'I-gpe', 12: 'I-nat', 13: 'I-org', 14: 'I-per', 15: 'I-tim', 16: 'O'}
        try:
            self.model = load_model(model_path)
            print("MODEL LOAD COMPLETE")
        except Exception as e:
            print('MODEL LOADING ERROR!!!')
            print(e)
        try:
            self.glove = Golve_embedding(glove_model_path,25)
            print("GLOVE MODEL LOAD COMPLETE")
        except Exception as e:
            print('GLOVE MODEL LOADING ERROR!!!')
            print(e)
    def model_predict_to_labels(self,vec,word):
        pos_pred = vec[:42]
        label_pred = vec[42:]
        return (word,self.id_pos[np.argmax(pos_pred)],self.id_label[np.argmax(label_pred)])
    def get_entities(self,text):
        text = text.replace('"','')
        text  = '.....'+text+'.....'
        text_tokens = self.glove.tokenizer(text)
        text_vectors = self.glove.fetch_all(text_tokens)
        entities=[]
        for i in range(text_vectors.shape[0]-9):
            entities.append(self.model_predict_to_labels(self.model.predict(np.array([text_vectors[i:i+10,:]]))[0],text_tokens[i+5]))
        return entities
