import numpy as np
import matplotlib.pyplot as plt




def displayRayPath(f=1,L=np.pi):
	"""
	Cette fonction simule le dispositif optique suivant : 
	
	Miroir <--- L/2---> Lentille <---L/2---> Miroir
	
	f: distance focale de la lentille 
	On affiche la trajectoire partant du centre du premier miroir avec une pente de 1. 
	"""
	# Merci à Gonzague de Carpentier pour l'écriture de ce code 


	L = L / 2
	# Attention aux conventions, le L utilisé après dans le code correspond à la distance entre la lentille et un miroir et non à la distance entre les deux miroirs. 
	N = 500 #Nombre de rebonds sur le premier miroir. 
	a = 0 #ordonnée initiale
	b = 1 # pente initiale
	
	n = 1000
	xm = np.linspace(-L, 0, n)
	xp = np.linspace(0, L, n)
	
	for i in range(N):
		plt.plot(xm, a + b*(xm + L))
		a = a + b * L
		b = b - a / f
		plt.plot(xp, a + b*xp)
		a = a + b * L
		b = - b
		plt.plot(xp, a + b*(xp - L))
		a = a - b * L
		b = b + a / f
		plt.plot(xm, a + b*xm)
		a = a - b * L
		b = - b
	
	plt.plot(xm, a + b*(xm + L))
	a = a + b * L
	b = b - a / f
	plt.plot(xp, a + b*xp)
	a = a + b * L
	b = - b
	plt.plot(xp, a + b*(xp - L))
	a = a - b * L
	b = b + a / f
	
	plt.show()


displayRayPath(L=3)
