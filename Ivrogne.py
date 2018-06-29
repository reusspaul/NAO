# -*- coding:Latin-1 -*-
#
# ===========
# | Ivrogne |
# ===========
#
# Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
# Type "copyright", "credits" or "license()" for more information.
#
from tkinter import *
from random import randrange
#
# Données et initialisations.
#
homothetie=0.5
largeur=1500.0*homothetie
hauteur=800.0*homothetie
delta_x=4.0
delta_t=0
delta_x0=delta_x
epaisseur=int(delta_x/2.0+0.5)
graine=0
np=0
longitudep=0
palette=['white','yellow','purple','cyan','brown','green','red','blue','pink','orange']
numero_couleur=-1
#
# Choix du pas delta_x.
#
def pas01():
	global delta_x,delta_x0,epaisseur
	delta_x=1.0
	delta_x0=delta_x
	epaisseur=int(delta_x/2.0+0.5)
	pas_de_calcul.configure(text="Pas en espace : "+str(delta_x)+".     Pas en temps : " +str(delta_t)+".")
#
def pas02():
	global delta_x,delta_x0,epaisseur
	delta_x=2.0
	delta_x0=delta_x
	epaisseur=int(delta_x/2.0+0.5)
	pas_de_calcul.configure(text="Pas en espace : "+str(delta_x)+".     Pas en temps : " +str(delta_t)+".")
#
def pas04():
	global delta_x,delta_x0,epaisseur
	delta_x=4.0
	delta_x0=delta_x
	epaisseur=int(delta_x/2.0+0.5)
	pas_de_calcul.configure(text="Pas en espace : "+str(delta_x)+".     Pas en temps : " +str(delta_t)+".")
#
def pas08():
	global delta_x,delta_x0,epaisseur
	delta_x=8.0
	delta_x0=delta_x
	epaisseur=int(delta_x/2.0+0.5)
	pas_de_calcul.configure(text="Pas en espace : "+str(delta_x)+".     Pas en temps : " +str(delta_t)+".")
#
# Sous-programme de lecture du pas delta_x.
#
def lecture(event):
	global entree,delta_x,chaine2,delta_x0,epaisseur,delta_t
	#
	delta_x=eval(entree.get())
	chaine2.configure(text=" Valeur que vous avez donnée pour delta_x = "+str(delta_x))
	pas_de_calcul.configure(text="Pas en espace : "+str(delta_x)+".     Pas en temps : " +str(delta_t)+".")
	epaisseur=int(delta_x/2.0+0.5)
	delta_x0=delta_x
#
# Programme de lecture du pas delta_x.
#
def pas_autre():
	global entree,chaine2,delta_x,delta_x0,epaisseur
	#
	fenetre2=Tk()
	fenetre2.title("Lecture de delta_x")
	chaine1=Label(fenetre2,text="     Entrer ci-dessous la valeur du pas delta_x !      ",font="Arial 16")
	chaine1.pack()
	entree=Entry(fenetre2)
	entree.bind("<Return>",lecture)
	entree.pack()
	chaine2=Label(fenetre2)
	chaine2.pack()
#
#
# Dessins.
# ========
#
# Déplacement de l'ivrogne.
#
def deplacement():
	global x1,y1,x2,y2,np,epaisseur,graine,numero_couleur,couleur,nombre_parcours,pas_de_calcul,delta_x,delta_t
	fin=0
	deplace=randrange(4)
	if deplace==0:
		x2=x1+delta_x
		y2=y1
		if x2>largeur:
			fin=1
	if deplace==1:
		x2=x1
		y2=y1+delta_x
		if y2>hauteur:
			fin=1
	if deplace==2:
		x2=x1-delta_x
		y2=y1
		if x2<0.0:
			fin=1
	if deplace==3:
		x2=x1
		y2=y1-delta_x
		if y2<0.0:
			fin=1
	np=np+1
	canevas.create_line(x1,hauteur-y1,x2,hauteur-y2,fill=couleur,width=epaisseur)
	pas_de_calcul.configure(text="Pas en espace : "+str(delta_x)+".     Pas en temps : " +str(delta_t)+".")
	nombre_parcours.configure(text="Nombre de parcours :  "+str(np))
	x1=x2
	y1=y2
	if fin<1:
		fenetre.after(delta_t,deplacement)	
#
# Elaboration de la figure.
#
def dessin():
	"Dessin de la figure"
	global x1,y1,x2,y2,np,graine,numero_couleur,couleur,nombre_parcours,delta_x,delta_t
	numero_couleur=numero_couleur+1
	if numero_couleur>9:
		numero_couleur=0
	couleur=palette[numero_couleur]
	np=0
	x1=0.5*largeur
	y1=0.5*hauteur
	deplacement()
	graine=graine+1
	numero_dessin.configure(text="Dessin numéro "+str(graine))
#
# Dessin nouveau après effacement du précédent.
#
def dessinn():
	"Effacement du précédent et nouveau dessin"
	global delta_x,delta_x0,delta_t
	canevas.create_line(0,0.5*hauteur,largeur,0.5*hauteur,width=hauteur,fill="black")
	delta_x=delta_x0
	delta_t=0
	dessin()
#
# Dessin à superposer au précédent.
#
def dessins():
	"Dessin à superposer au précédent"
	global delta_x,delta_x0,delta_t
	delta_x=delta_x0
	delta_t=0
	dessin()
#
# Dessin ralenti.
#
def dessinr():
	"Effacement du précédent et nouveau dessin en ralenti"
	global delta_x,delta_x0,delta_t
	canevas.create_line(0,0.5*hauteur,largeur,0.5*hauteur,width=hauteur,fill="black")
	delta_x=delta_x0
	delta_t=10
	dessin()
#
# Dessin ralenti et zoom.
#
def dessinz():
	"Effacement du précédent et nouveau dessin en ralenti et en zoom"
	global delta_x,delta_x0,delta_t
	canevas.create_line(0,0.5*hauteur,largeur,0.5*hauteur,width=hauteur,fill="black")
	delta_x=5.0*delta_x0
	if delta_x0<5.0:
		delta_x=25.0
	delta_t=50
	dessin()
#
#
# Programme principal.
# ====================
#
#
fenetre=Tk()
fenetre.title("Cheminement de l'ivrogne")
#
# Fenêtre destinée à accueillir le dessin.
#
canevas=Canvas(fenetre,bg="black",width=largeur,height=hauteur)
canevas.grid(row=2,column=0,columnspan=2)
#
# Lecture.
#
# Boutons en bas.
#
fra1=Frame(fenetre)
fra1.grid(row=4,column=0,sticky=W,padx=50)
Button(fra1, text="Effacer et recommencer",font="Arial 10 italic",fg="green",command=dessinn).pack(side=LEFT)
Button(fra1, text="Recommencer et superposer",font="Arial 10 italic",fg="blue",command=dessins).pack(side=LEFT)
Button(fra1, text="Effacer et faire un ralenti",font="Arial 10 italic",fg="brown",command=dessinr).pack(side=LEFT)
Button(fra1, text="Effacer et faire un zoom",font="Arial 10 italic",fg="black",command=dessinz).pack(side=LEFT)
fra2=Frame(fenetre)
fra2.grid(row=4,column=1,sticky=E,padx=50)
Button(fra2, text="Arrêter le programme",font="Arial 10 italic",fg="red",command=fenetre.quit).pack(side=LEFT)
#
# Choix du delta_x.
#
fra3=Frame(fenetre)
fra3.grid(row=2,column=3,sticky=W,pady=50)
Button(fra3,text="Pas = 1",font="Arial 10",fg="purple",command=pas01).pack(side=TOP,pady=5)
Button(fra3,text="Pas = 2",font="Arial 10",fg="purple",command=pas02).pack(side=TOP,pady=5)
Button(fra3,text="Pas = 4",font="Arial 10 italic",fg="purple",command=pas04).pack(side=TOP,pady=5)
Button(fra3,text="Pas = 8",font="Arial 10",fg="purple",command=pas08).pack(side=TOP,pady=5)
Button(fra3,text="Autre pas",font="Arial 10",fg="purple",command=pas_autre).pack(side=TOP,pady=5)
#
# Inscriptions au-dessus et au dessous du dessin.
#
pas_de_calcul=Label(fenetre,text="Pas en espace : "+str(delta_x)+".     Pas en temps : "+str(delta_t)+".")
pas_de_calcul.grid(row=1,column=0)
numero_dessin=Label(fenetre,text="Dessin numéro "+str(graine))
numero_dessin.grid(row=1,column=1)
nombre_parcours=Label(fenetre,text="Nombre de parcours :  "+str(np))
nombre_parcours.grid(row=3,column=1)
#
# Lancement du programme de l'ivrogne.
#
fenetre.mainloop()
#