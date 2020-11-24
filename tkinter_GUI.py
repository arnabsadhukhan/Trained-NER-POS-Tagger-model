import numpy as np
import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext 
from model import NamedEntityRecognition

model = NamedEntityRecognition(model_path='saved_model\\Model',glove_model_path='Glove_db\\glove25d.db')


def recognize_text():
  text = text_area.get("1.0", tk.END)
  text_area2.delete('1.0',tk.END)
  text_area2.insert(tk.INSERT, 'Converting Wait...')
  result = model.get_entities(text)
  text_area2.delete('1.0',tk.END)
  for (word,pos,entity) in result:
    if entity!='O':
      text_area2.insert(tk.INSERT, word+'-'+entity[2:].upper(),entity[2:])
      text_area2.insert(tk.INSERT, ' ')
    else:
      text_area2.insert(tk.INSERT, word)
      text_area2.insert(tk.INSERT,pos,'pos')
      text_area2.insert(tk.INSERT, ' ')
  text_area2.tag_config('art',background='blue',foreground='white')
  text_area2.tag_config('geo',background='green',foreground='white')
  text_area2.tag_config('eve',background='blue',foreground='white')
  text_area2.tag_config('gpe',background='green',foreground='white')
  text_area2.tag_config('nat',background='blue',foreground='white')
  text_area2.tag_config('org',background='green',foreground='white')
  text_area2.tag_config('per',background='blue',foreground='white')
  text_area2.tag_config('tim',background='blue',foreground='white')
  text_area2.tag_config('pos',background='lightblue',foreground='white')


win = tk.Tk() 
win.geometry('900x500')
win.title("Named Entiry Recognition") 
ttk.Label(win,  text = "Input Text", font = ("Times New Roman", 15),  background = 'green',  foreground = "white").grid(column = 0, row = 0) 

text_area = scrolledtext.ScrolledText(win,  wrap = tk.WORD,  width = 72,  height = 8,  font = ("Courier", 15)) 
text_area.grid(row=1,column = 0, pady = 25, padx = 10) 

button = tk.Button(win, text ="Recognize", command = recognize_text)
button.grid(row=2,column = 0)
text_area.focus() 

text_area2 = scrolledtext.ScrolledText(win,  wrap = tk.WORD,  width = 72,  height = 8,  font = ("Courier", 15)) 
text_area2.grid(row=3,column = 0, pady = 25, padx = 10) 

win.mainloop() 