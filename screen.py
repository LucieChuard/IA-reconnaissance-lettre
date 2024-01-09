import matplotlib.pyplot as plt
import random
import data

test=random.randint(1,40000)
#exemple d'image à afficher sur matplotlib / peut être changé
img_index=test
img=data.image_train[img_index]
print("image label : " + str(chr(data.label_train[img_index]+96)))

#img.reshape() + 1 arg, ici 28,28 donc entre parenthèses
plt.imshow(img.reshape((28,28)))

plt.show()