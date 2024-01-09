import tkinter
from PIL import Image, ImageDraw

class ScreenDraw:
    def __init__(self, root):
        self.i=0
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


    def paint(self, event):
        x1,y1=(event.x-self.step), (event.y-self.step)
        #récupération des coordonnées initiales
        x2,y2=(event.x+self.step),(event.y+self.step)
        #coordonnées fin de mouvement
        
        self.canvas.create_oval(x1,y1,x2,y2, fill="white", width=2)
        self.draw.line([x1,y1,x2,y2], fill="white", width=2)

    def reset(self,event):

        folder="letters"
        self.image.save(f"{folder}/letter{self.i}.png")
        self.i+=1


