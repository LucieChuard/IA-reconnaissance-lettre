import numpy
import matplotlib as plt
import neural_network
import cv2
import ecriture
import tkinter

multi_layer = neural_network.load()

if multi_layer is None:
    print("Entraînement du modèle...")
    neural_network.train()
    model = neural_network.load()


if __name__=="__main__":
        root=tkinter.Tk()
        app = ecriture.ScreenDraw(root)
        root.mainloop()


#i=0
#while i<4:
 #   letterToRead=cv2.resize("letters/letter{i}.png",(28,28))
  #  prediction=neural_network.multi_layer(letterToRead)
   # word=word+str(chr(prediction))
    #i=+1