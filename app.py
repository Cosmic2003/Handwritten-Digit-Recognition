import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
from keras.models import load_model


model = load_model('model.keras')

class DigitRecognizerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Handwritten Digit Recognizer")
        
        
        self.canvas = tk.Canvas(self, width=280, height=280, bg='white', cursor="cross")
        self.canvas.grid(row=0, column=0, pady=2, sticky=tk.W, columnspan=2)
        
        
        self.label = tk.Label(self, text="Draw a digit on the canvas", font=("Helvetica", 14))
        self.label.grid(row=1, column=0, columnspan=2)
        
        self.clear_button = tk.Button(self, text="Clear", command=self.clear_canvas)
        self.clear_button.grid(row=2, column=0)
        
        self.recognize_button = tk.Button(self, text="Recognize", command=self.predict_digit)
        self.recognize_button.grid(row=2, column=1)
        
        
        self.canvas.bind("<B1-Motion>", self.paint)
        self.drawing = False
        
        
        self.image = Image.new('L', (280, 280), 255)
        self.draw = ImageDraw.Draw(self.image)
        
    def clear_canvas(self):
        self.canvas.delete("all")
        self.image.paste(255, [0, 0, 280, 280])

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill='black', width=10)
        self.draw.ellipse([x1, y1, x2, y2], fill='black')
        
    def predict_digit(self):
        
        img_resized = self.image.resize((28, 28))
        img_resized = ImageOps.invert(img_resized)
        img_array = np.array(img_resized)
        img_array = img_array.reshape(1, 28, 28, 1)
        img_array = img_array.astype('float32')
        img_array /= 255.0 
        
        
        pred = model.predict(img_array)
        digit = np.argmax(pred)
        
        
        self.label.configure(text=f"Prediction: {digit}")

app = DigitRecognizerApp()
app.mainloop()