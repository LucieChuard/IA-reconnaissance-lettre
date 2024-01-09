import tkinter
from PIL import Image, ImageDraw
import neural_network
import cv2
import numpy as np

class ScreenDraw:
    def __init__(self, root):
        self.i=0
        self.word=""
        
        self.root=root
        self.root.title("Zone d'écriture")

        self.canvas=tkinter.Canvas(root, width=400, height=400, bg="black")
        self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        
        self.image=Image.new("RGB", (400,400), color="black")
        #créer une image de 400*400 sur fond noir en couleur RGB (voir pour laisser n&b)
        self.draw=ImageDraw.Draw(self.image)
        #cCréer l'objet ImageDraw pour dessiner sur l'image
        self.step=3

        self.canvas.bind("<B1-Motion>", self.paint)
        #mouvement bouton gauche pour dessiner (maintient clic) // fonction à définir
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        #relachement du bouton gauche pour stopper le bind précedent (arrêter de dessiner)

       # Chargement ou entraînement du modèle au démarrage
        self.multi_layer = neural_network.load()
        if self.multi_layer is None:
            print("Entraînement du modèle...")
            neural_network.train()
            # Recharge du modèle après l'entraînement
            self.multi_layer = neural_network.load()

    def paint(self, event):
        x1,y1=(event.x-self.step), (event.y-self.step)
        #récupération des coordonnées initiales
        x2,y2=(event.x+self.step),(event.y+self.step)
        #coordonnées fin de mouvement
        
        self.canvas.create_oval(x1,y1,x2,y2, fill="white", width=2)
        self.draw.line([x1,y1,x2,y2], fill="white", width=2)

    def reset(self, event):
        folder = "letters"
        self.image.save(f"{folder}/letter{self.i}.png")

        letter_to_read = cv2.imread(f"{folder}/letter{self.i}.png", cv2.IMREAD_GRAYSCALE)
        letter_to_read = cv2.resize(letter_to_read, (28, 28)).flatten()

        letter_to_read = np.full((1, 784), self.i)  # Utilisation de np.full pour créer un tableau répétant la valeur de self.i
        prediction = self.multi_layer.predict(letter_to_read)
        self.word = self.word + str(chr(prediction[0] + 96))

        print("Conversion complete!")
        print(self.word)
        self.i += 1
