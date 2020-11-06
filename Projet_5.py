# -*- coding: utf-8 -*-
"""
name: Annuaire
Description: Permet de communiquer avec une base de donnée
Version: 1.0
author: Mans léo
"""

"""_________________________IMPORTATIONS___________________________________"""

import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import os
from PIL import *
from PIL import Image, ImageDraw,ImageFont,ImageTk
from random import randint

"""_________________________FONCTIONS__________________________________"""

def verif1():
    cur.execute('SELECT * FROM ANNUAIRE')
    conn.commit()
    liste = cur.fetchall()
    if len(liste)==0:
        supp['state'] = DISABLED
        modif['state'] = DISABLED
        recherche_but['state'] = DISABLED
    else:
        supp['state'] = NORMAL
        modif['state'] = NORMAL
        recherche_but['state'] = NORMAL
def verif2():
        try:
            for c in menu_entry.winfo_children():
                c.destroy()
            menu_entry.destroy()
            bouton_supprimer.destroy()
        except:
                return
            
def verif3():
        try:
            label_choixx.destroy()
            bouton_supprimer.destroy()
            label_choixsup.destroy()
        except:
            return     
        
def verif4():
        try:
            for c in menu_entry4.winfo_children():
                c.destroy()
            menu_entry4.destroy()
            bouton_supprimer.destroy()
        except:
                return
def convert(liste:list):
    liste_nom=[]
    liste_prenom=[]
    liste_tel=[]
    liste_mail=[]
    liste_qual=[]
    liste_id=[]
    for i in range(len(liste)):
        liste_id.append(liste[i][0]);
        liste_nom.append(liste[i][1]);
        liste_prenom.append(liste[i][2]);
        liste_tel.append(liste[i][3]);
        liste_mail.append(liste[i][4]);
        liste_qual.append(liste[i][5]);
    myNliste=[]
    for i in range(len(liste_id)):
        myNliste.append(str(liste_id[i])+" | "+str(liste_nom[i])+" | "+str(liste_prenom[i])+" | "+str(liste_tel[i])+" | "+str(liste_mail[i])+" | "+str(liste_qual[i]))
    return myNliste

"""________________________________________"""

def ajouter():
    global nom_e
    global prenom_e
    global tel_e
    global tel_e2
    global email_e
    global qualite_e
    global fenetre2
    fenetre2=Toplevel(fenetre1)
    fenetre2.title("Ajouter")
    fenetre2.geometry("800x400")
    fenetre2.config(background="Black")
    canvas_effect=Canvas(fenetre2,height=50,width=776,bg="black",relief="groove").place(x=11,y=5)                  
    my_label2 =Label(fenetre2,text="AJOUTER",font=("Courrier",20),bg="black",foreground ="White").place(x=350,y=15)    

    my_label_N =Label(fenetre2,text="Nom :",font=("Courrier",20),bg="black",foreground ="White").place(x=40,y=100)
    nom_e=Entry(fenetre2,bg="#4B4B57",font=("Courrier",20))
    nom_e.place(x=270,y=100)                
    my_label8_P =Label(fenetre2,text="Prenom :",font=("Courrier",20),bg="black",foreground ="White").place(x=40,y=150)
    prenom_e=Entry(fenetre2,bg="#4B4B57",font=("Courrier",20))
    prenom_e.place(x=270,y=150)                                
    my_label2_T =Label(fenetre2,text="Telephone :  +",font=("Courrier",20),bg="black",foreground ="White").place(x=40,y=200)
    tel_e2=Entry(fenetre2,bg="#4B4B57",font=("Courrier",20))
    tel_e2.place(x=220,y=200)
    tel_e=Entry(fenetre2,bg="#4B4B57",font=("Courrier",20))
    tel_e.place(x=270,y=200)               
    my_label2_E =Label(fenetre2,text="Email :",font=("Courrier",20),bg="black",foreground ="White").place(x=40,y=250)
    email_e=Entry(fenetre2,bg="#4B4B57",font=("Courrier",20))
    email_e.place(x=270,y=250)             
    my_label2_Q =Label(fenetre2,text="Qualiter :",font=("Courrier",20),bg="black",foreground ="White").place(x=40,y=300)
    qualite_e=Entry(fenetre2,bg="#4B4B57",font=("Courrier",20))
    qualite_e.place(x=270,y=300)
    but_val=Button(fenetre2,text="Valider",font=("Courrier",20),image=pixelVirtual,width=250,height=40,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=ajjouter_bdd)
    but_val.place(x=300,y=345)
    
"""________________________________________"""    
    
def supprimer(): 
    global var_choix 
    global fenetre3   
    global choix_annu
    global choix_infor
    global mylist2
    fenetre3=Toplevel(fenetre1)
    fenetre3.title("Supprimer")
    fenetre3.geometry("1000x600")
    fenetre3.config(background="BLACK")
    canvas_effect=Canvas(fenetre3,height=50,width=976,bg="BLACK",relief="groove").place(x=11,y=5)
    my_label2 =Label(fenetre3,text="SUPPRIMER",font=("Courrier",20),bg="BLACK",foreground ="White")
    my_label2.place(x=450,y=15)
                     
                     
    label_quest=Label(fenetre3,text="Quel methode voulez vous utilisez ? ",font=("Courrier",15),bg="BLACK",foreground ="White")      
    label_quest.place(x=5,y=70)
    
    var_choix = IntVar()
    choix_infor = Radiobutton(fenetre3,variable=var_choix,value=0,bg="BLACK",foreground ="white",command=radio_modif)
    my_label2 =Label(fenetre3,text="Saisir une infomation du contact",font=("Courrier",13),bg="BLACK",foreground ="White")
    my_label2.place(x=30,y=120)
    choix_annu = Radiobutton(fenetre3,variable=var_choix,value=1,bg="BLACK",foreground ="Blue",command=radio_modif)
    my_label3 =Label(fenetre3,text="Parcourir l'annuaire",font=("Courrier",13),bg="BLACK",foreground ="White")
    my_label3.place(x=30,y=150)

                             
    choix_infor.place(x=10,y=120)
    choix_annu.place(x=10,y=150)
    cur.execute('SELECT * FROM ANNUAIRE')
    conn.commit()
    liste = cur.fetchall()
    scroll3y=Scrollbar(fenetre3,width=20)
    scroll3y.pack( side = RIGHT, fill = Y ,padx=5)
    mylist2 = Listbox(fenetre3,font=("Courrier",15), yscrollcommand =scroll3y.set,height=10,width=50,bg="#80808C")
    for i in range(len(liste)):
            mylist2.insert(END,liste[i])
    mylist2.place(x=400,y=70);       
    
"""________________________________________"""       

def radio_modif():

    if var_choix.get()==0:
        suppchoix1(fenetre3)
    else:
        suppchoix2()
 
"""________________________________________"""

def recherche_sup():
     global resultTXT
     global liste_result
     global myIDlist
     cur.execute('SELECT * FROM ANNUAIRE')
     conn.commit()
     liste_2=[id_e2.get(),nom_e2.get(),prenom_e2.get(),tel_e2.get(),mail_e2.get()]
     
     liste_result=[]
     liste = cur.fetchall()
     compteur_result=0
     var3=str(liste_2[var_choix2.get()])
     for i in range(len(liste)):
            var2=str(liste[i][var_choix2.get()])
            if var2==var3:
                compteur_result=compteur_result+1
                liste_result.append(liste[i])
     if compteur_result==0:
         warn_supp=messagebox.showerror("ERREUR","Aucun contact n'a été trouvé.")
     if compteur_result==1:
         resultTXT=convert(liste_result)
         quest_supp=messagebox.askyesno("Valider","""Etes vous sûr de bien Supprimer ce contact ? \n
                                """+str(resultTXT))
         if quest_supp==True:
            cur.execute("DELETE FROM ANNUAIRE WHERE id=?",(liste_result[0][0],))
            conn.commit()
         else:
            return
     if compteur_result>1:
        global selected_item
        global fenetre_choix
        selected_item = StringVar()
        fenetre_choix=Toplevel(fenetre3)
        fenetre_choix.title("Supprimer")
        fenetre_choix.geometry("800x400")
        fenetre_choix.config(background="BLACK")
        scroll2y=Scrollbar(fenetre_choix,width=20)
        scroll2y.pack( side = RIGHT, fill = Y ,padx=5)
        myIDlist = Listbox(fenetre_choix,font=("Courrier",15), yscrollcommand =scroll2y.set,height=8,width=40,bg="#80808C")
        for i in range(len(liste_result)):
            myIDlist.insert(END,liste_result[i])
        myIDlist.place(x=175,y=10);   
        scroll2y.config( command = myIDlist.yview )
        label_choixx=Label(fenetre_choix,text=" Ligne Choisie :   ",font=("Courrier",17),fg="white",background="BLACK")
        label_choixx.place(x=50,y=215)
        label_choixsup=Label(fenetre_choix,textvariable=selected_item,font=("Courrier",17),fg="white",background="BLACK")
        label_choixsup.place(x=200,y=215)
        bouton_supprimer=Button(fenetre_choix,text="Valider",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=supprimerchoix)
        bouton_supprimer.place(x=175,y=300)
        
        myIDlist.bind("<<ListboxSelect>>", get_listeboxx)
        
"""________________________________________"""        

def get_listeboxx(event):
    global supre
    e=myIDlist.curselection()[0]
    supre=myIDlist.get(e)
    selected_item.set(supre)
    
"""________________________________________"""    
    
def supprimerchoix():
         quest_supp=messagebox.askyesno("Valider","""Etes vous sûr de bien Supprimer ce contact ? \n
                                """+str(selected_item.get()))
         if quest_supp==True:
            cur.execute("DELETE FROM ANNUAIRE WHERE id=?",(supre[0],))
            conn.commit()
            fenetre_choix.destroy()
            fenetre3.destroy()
            uptate()

             
         else:
            return   
        
"""________________________________________"""        
        
def suppchoix1(fen):
        global var_choix2
        global menu_entry
        global choix_id
        global choix_nom
        global choix_prenom
        global choix_tel
        global choix_mail
        global bouton_supprimer
        verif3()
        menu_entry=Canvas(fen,height=250,width=345,bg="#42424D",relief="sunken",borderwidth=0)
        menu_entry.place(x=5,y=315) 
        
        var_choix2 = IntVar()
        choix_id = Radiobutton(menu_entry,variable=var_choix2,value=0,bg="#42424D",foreground ="Blue",command=entry_sup)
        choix_id.place(x=5,y=10)
        my_label2 =Label(menu_entry,text="ID :",font=("Courrier",12),bg="#42424D",foreground ="White").place(x=25,y=10)
                 
                         
        choix_nom = Radiobutton(menu_entry,variable=var_choix2,value=1,bg="#42424D",foreground ="BLUE",command=entry_sup)
        choix_nom.place(x=5,y=60)
        my_label3 =Label(menu_entry,text="NOM :",font=("Courrier",12),bg="#42424D",foreground ="White")
        my_label3.place(x=25,y=60)
        
                         
        choix_prenom = Radiobutton(menu_entry,variable=var_choix2,value=2,bg="#42424D",foreground ="BLUE",command=entry_sup)
        choix_prenom.place(x=5,y=110)         
        my_label4 =Label(menu_entry,text="PRENOM :",font=("Courrier",12),bg="#42424D",foreground ="White").place(x=25,y=110)
    
        
        choix_tel = Radiobutton(menu_entry,variable=var_choix2,value=3,bg="#42424D",foreground ="BLUE",command=entry_sup)
        choix_tel.place(x=5,y=160)
        my_label5 =Label(menu_entry,text="TELEPHONE :",font=("Courrier",12),bg="#42424D",foreground ="White").place(x=25,y=160)
    
        
        choix_mail = Radiobutton(menu_entry,variable=var_choix2,value=4,bg="#42424D",foreground ="BLUE",command=entry_sup)
        choix_mail.place(x=5,y=210)
        my_label6 =Label(menu_entry,text="EMAIL :",font=("Courrier",12),bg="#42424D",foreground ="White").place(x=25,y=210)
        bouton_supprimer=Button(fenetre3,text="Valider",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=recherche_sup)
        bouton_supprimer.place(x=550,y=500) 
        choix_infor["state"]=DISABLED
        choix_annu["state"]=NORMAL
        
"""________________________________________"""

def suppchoix2():
            verif2()
            global bouton_supprimer
            global selected_item2
            global label_choixx
            global label_choixsup
            global mylist2
            selected_item2=StringVar()

            choix_infor["state"]=NORMAL
            choix_annu["state"]=DISABLED
            label_choixx=Label(fenetre3,text=" Ligne Choisie :   ",font=("Courrier",17),fg="white",background="BLACK")
            label_choixx.place(x=50,y=400)
            label_choixsup=Label(fenetre3,textvariable=selected_item2,font=("Courrier",17),fg="white",background="BLACK")
            label_choixsup.place(x=250,y=400)
            bouton_supprimer=Button(fenetre3,text="Valider",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=supprimerchoix2)
            bouton_supprimer.place(x=550,y=500)
            mylist2.bind("<<ListboxSelect>>", get_listeboxx2)
            
"""________________________________________"""            
            
def get_listeboxx2(event):
    global supre2
    e2=mylist2.curselection()[0]
    supre2=mylist2.get(e2)
    selected_item2.set(supre2) 
    
"""________________________________________"""    
    
def supprimerchoix2():
         quest_supp=messagebox.askyesno("Valider","""Etes vous sûr de bien Supprimer ce contact ? \n
                                """+str(selected_item2.get()))
         if quest_supp==True:
            cur.execute("DELETE FROM ANNUAIRE WHERE id=?",(supre2[0],))
            conn.commit()
            fenetre3.destroy()
            uptate()
         else:
            return  

"""________________________________________"""
            
def entry_sup():
    global id_e2
    global nom_e2
    global prenom_e2
    global tel_e2
    global mail_e2

    id_e2=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    id_e2.place(x=140,y=10)
    nom_e2=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    nom_e2.place(x=140,y=60)
    prenom_e2=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    prenom_e2.place(x=140,y=110)
    tel_e2=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    tel_e2.place(x=140,y=160)   
    mail_e2=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    mail_e2.place(x=140,y=210)
    if var_choix2.get()==0:
        id_e2["state"]=NORMAL
        nom_e2["state"]=DISABLED
        prenom_e2["state"]=DISABLED
        tel_e2["state"]=DISABLED
        mail_e2["state"]=DISABLED
        
        choix_id["state"]=DISABLED
        choix_nom["state"]=NORMAL
        choix_prenom["state"]=NORMAL
        choix_tel["state"]=NORMAL
        choix_mail["state"]=NORMAL
        
    elif var_choix2.get()==1:
        id_e2["state"]=DISABLED
        nom_e2["state"]=NORMAL
        prenom_e2["state"]=DISABLED
        tel_e2["state"]=DISABLED
        mail_e2["state"]=DISABLED
        
        choix_id["state"]=NORMAL
        choix_nom["state"]=DISABLED
        choix_prenom["state"]=NORMAL
        choix_tel["state"]=NORMAL
        choix_mail["state"]=NORMAL
    elif var_choix2.get()==2:
        id_e2["state"]=DISABLED
        nom_e2["state"]=DISABLED
        prenom_e2["state"]=NORMAL
        tel_e2["state"]=DISABLED
        mail_e2["state"]=DISABLED

        choix_id["state"]=NORMAL
        choix_nom["state"]=NORMAL
        choix_prenom["state"]=DISABLED
        choix_tel["state"]=NORMAL
        choix_mail["state"]=NORMAL
    elif var_choix2.get()==3:
        id_e2["state"]=DISABLED
        nom_e2["state"]=DISABLED
        prenom_e2["state"]=DISABLED
        tel_e2["state"]=NORMAL
        mail_e2["state"]=DISABLED
        
        choix_id["state"]=NORMAL
        choix_nom["state"]=NORMAL
        choix_prenom["state"]=NORMAL
        choix_tel["state"]=DISABLED
        choix_mail["state"]=NORMAL
    else:
        id_e2["state"]=DISABLED
        nom_e2["state"]=DISABLED
        prenom_e2["state"]=DISABLED
        tel_e2["state"]=DISABLED
        mail_e2["state"]=NORMAL
        
        choix_id["state"]=NORMAL
        choix_nom["state"]=NORMAL
        choix_prenom["state"]=NORMAL
        choix_tel["state"]=NORMAL
        choix_mail["state"]=DISABLED
        
"""________________________________________"""
        
def modifier():
    global fenetre4
    global var_choix
    global choix_infor
    global choix_annu
    global myIDlist
    fenetre4=Toplevel(fenetre1)
    fenetre4.title("Modifier")
    fenetre4.geometry("1000x600")
    fenetre4.config(background="BLACK")
    canvas_effect=Canvas(fenetre4,height=50,width=776,bg="BLACK",relief="groove").place(x=11,y=5)
    my_label2 =Label(fenetre4,text="MODIFIER",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=350,y=15)
    label_quest=Label(fenetre4,text="Quel methode voulez vous utilisez ? ",font=("Courrier",15),bg="BLACK",foreground ="White")      
    label_quest.place(x=5,y=70)
    
    var_choix = IntVar()
    choix_infor = Radiobutton(fenetre4,variable=var_choix,value=0,bg="BLACK",foreground ="Blue",command=radio_modif2)
    my_label2 =Label(fenetre4,text="Saisir une infomation du contact",font=("Courrier",13),bg="BLACK",foreground ="White")
    my_label2.place(x=30,y=120)
    choix_annu = Radiobutton(fenetre4,variable=var_choix,value=1,bg="BLACK",foreground ="Blue",command=radio_modif2)
    my_label3 =Label(fenetre4,text="Parcourir l'annuaire",font=("Courrier",13),bg="BLACK",foreground ="White")
    my_label3.place(x=30,y=150)

                             
    choix_infor.place(x=10,y=120)
    choix_annu.place(x=10,y=150)
    cur.execute('SELECT * FROM ANNUAIRE')
    conn.commit()
    liste = cur.fetchall()
    scroll4y=Scrollbar(fenetre4,width=20)
    scroll4y.pack( side = RIGHT, fill = Y ,padx=5)
    myIDlist = Listbox(fenetre4,font=("Courrier",15), yscrollcommand =scroll4y.set,height=10,width=50,bg="#80808C")
    for i in range(len(liste)):
            myIDlist.insert(END,liste[i])
    myIDlist.place(x=400,y=70);   

"""________________________________________"""       

def radio_modif2():

    if var_choix.get()==0:
        modifchoix1(fenetre4)
    else:
        modifchoix2()
 
"""________________________________________"""
    
def modifchoix1(fen):
        global var_choix4
        global menu_entry4
        global choix_id4
        global choix_nom4
        global choix_prenom4
        global choix_tel4
        global choix_mail4
        global bouton_supprimer
        verif3()
        menu_entry4=Canvas(fen,height=250,width=345,bg="#42424D",relief="sunken",borderwidth=0)
        menu_entry4.place(x=5,y=315) 
        
        var_choix4 = IntVar()
        choix_id4 = Radiobutton(menu_entry4,text="ID :",font=("Courrier",12),variable=var_choix4,value=0,bg="#42424D",foreground ="white",command=entry_modif)
        choix_id4.place(x=5,y=10)                 
                         
        choix_nom4 = Radiobutton(menu_entry4,text="NOM :",font=("Courrier",12),variable=var_choix4,value=1,bg="#42424D",foreground ="white",command=entry_modif)
        choix_nom4.place(x=5,y=60)
        
                         
        choix_prenom4 = Radiobutton(menu_entry4,variable=var_choix4,text="PRENOM :",font=("Courrier",12),value=2,bg="#42424D",foreground ="white",command=entry_modif)
        choix_prenom4.place(x=5,y=110)             
        
        choix_tel4 = Radiobutton(menu_entry4,variable=var_choix4,text="TELEPHONE :",font=("Courrier",12),value=3,bg="#42424D",foreground ="white",command=entry_modif)
        choix_tel4.place(x=5,y=160)
        choix_mail4 = Radiobutton(menu_entry4,variable=var_choix4,text="EMAIL :",font=("Courrier",12),value=4,bg="#42424D",foreground ="white",command=entry_modif)
        choix_mail4.place(x=5,y=210)

        bouton_supprimer=Button(fenetre4,text="Valider",font=("Courrier",20),image=pixelVirtual,width=250,height=40,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=recherche_modif)
        bouton_supprimer.place(x=550,y=400) 
        choix_infor["state"]=DISABLED
        choix_annu["state"]=NORMAL
"""________________________________________"""
            
def entry_modif():
    global id_e4
    global nom_e4
    global prenom_e4
    global tel_e4
    global mail_e4

    id_e4=Entry(menu_entry4,bg="#4B4B57",font=("Courrier",12))
    id_e4.place(x=140,y=10)
    nom_e4=Entry(menu_entry4,bg="#4B4B57",font=("Courrier",12))
    nom_e4.place(x=140,y=60)
    prenom_e4=Entry(menu_entry4,bg="#4B4B57",font=("Courrier",12))
    prenom_e4.place(x=140,y=110)
    tel_e4=Entry(menu_entry4,bg="#4B4B57",font=("Courrier",12))
    tel_e4.place(x=140,y=160)   
    mail_e4=Entry(menu_entry4,bg="#4B4B57",font=("Courrier",12))
    mail_e4.place(x=140,y=210)
    if var_choix4.get()==0:
        id_e4["state"]=NORMAL
        nom_e4["state"]=DISABLED
        prenom_e4["state"]=DISABLED
        tel_e4["state"]=DISABLED
        mail_e4["state"]=DISABLED
        
        choix_id4["state"]=DISABLED
        choix_nom4["state"]=NORMAL
        choix_prenom4["state"]=NORMAL
        choix_tel4["state"]=NORMAL
        choix_mail4["state"]=NORMAL
        
    elif var_choix4.get()==1:
        id_e4["state"]=DISABLED
        nom_e4["state"]=NORMAL
        prenom_e4["state"]=DISABLED
        tel_e4["state"]=DISABLED
        mail_e4["state"]=DISABLED
        
        choix_id4["state"]=NORMAL
        choix_nom4["state"]=DISABLED
        choix_prenom4["state"]=NORMAL
        choix_tel4["state"]=NORMAL
        choix_mail4["state"]=NORMAL
    elif var_choix4.get()==2:
        id_e4["state"]=DISABLED
        nom_e4["state"]=DISABLED
        prenom_e4["state"]=NORMAL
        tel_e4["state"]=DISABLED
        mail_e4["state"]=DISABLED

        choix_id4["state"]=NORMAL
        choix_nom4["state"]=NORMAL
        choix_prenom4["state"]=DISABLED
        choix_tel4["state"]=NORMAL
        choix_mail4["state"]=NORMAL
    elif var_choix4.get()==3:
        id_e4["state"]=DISABLED
        nom_e4["state"]=DISABLED
        prenom_e4["state"]=DISABLED
        tel_e4["state"]=NORMAL
        mail_e4["state"]=DISABLED
        
        choix_id4["state"]=NORMAL
        choix_nom4["state"]=NORMAL
        choix_prenom4["state"]=NORMAL
        choix_tel4["state"]=DISABLED
        choix_mail4["state"]=NORMAL
    else:
        id_e4["state"]=DISABLED
        nom_e4["state"]=DISABLED
        prenom_e4["state"]=DISABLED
        tel_e4["state"]=DISABLED
        mail_e4["state"]=NORMAL
        
        choix_id4["state"]=NORMAL
        choix_nom4["state"]=NORMAL
        choix_prenom4["state"]=NORMAL
        choix_tel4["state"]=NORMAL
        choix_mail4["state"]=DISABLED        

"""________________________________________"""

def modifchoix2():
            verif4()
            global bouton_supprimer
            global selected_item3
            global label_choixx
            global label_choixsup
            selected_item3=StringVar()
            bouton_supprimer=Button(fenetre4,text="Valider",font=("Courrier",20),image=pixelVirtual,width=250,height=40,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=modificaton_menu)
            bouton_supprimer.place(x=550,y=500) 
            choix_infor["state"]=NORMAL
            choix_annu["state"]=DISABLED
            label_choixx=Label(fenetre4,text=" Ligne Choisie :   ",font=("Courrier",17),fg="white",background="BLACK")
            label_choixx.place(x=50,y=400)
            label_choixsup=Label(fenetre4,textvariable=selected_item3,font=("Courrier",17),fg="white",background="BLACK")
            label_choixsup.place(x=250,y=400)
            myIDlist.bind("<<ListboxSelect>>", get_listeboxx3)
            
"""________________________________________"""
            
def modificaton_menu():
    global fenetre6
    global nom_e2
    global prenom_e2
    global tel_e22
    global tel_e2
    global email_e2
    global qualite_e2
    fenetre6=Toplevel(fenetre4)
    fenetre6.title("Modifier")
    fenetre6.geometry("800x600")
    fenetre6.config(background="BLACK")
    canvas_effect=Canvas(fenetre6,height=50,width=776,bg='BLACK',relief="groove").place(x=11,y=5)                  
    my_label2 =Label(fenetre6,text="MODIFIER",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=350,y=15)    
    phrase =Label(fenetre6,text="Saissisez les informations à modifier :",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=40,y=100)

    my_label_N =Label(fenetre6,text="Nom :",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=40,y=200)
    nom_e2=Entry(fenetre6,bg="#4B4B57",font=("Courrier",20))
    nom_e2.place(x=270,y=200)                
    my_label8_P =Label(fenetre6,text="Prenom :",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=40,y=250)
    prenom_e2=Entry(fenetre6,bg="#4B4B57",font=("Courrier",20))
    prenom_e2.place(x=270,y=250)                                
    my_label2_T =Label(fenetre6,text="Telephone :  +",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=40,y=300)
    tel_e22=Entry(fenetre6,bg="#4B4B57",font=("Courrier",20))
    tel_e22.place(x=220,y=300)
    tel_e2=Entry(fenetre6,bg="#4B4B57",font=("Courrier",20))
    tel_e2.place(x=270,y=300)               
    my_label2_E =Label(fenetre6,text="Email :",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=40,y=350)
    email_e2=Entry(fenetre6,bg="#4B4B57",font=("Courrier",20))
    email_e2.place(x=270,y=350)             
    my_label2_Q =Label(fenetre6,text="Qualiter :",font=("Courrier",20),bg="BLACK",foreground ="White").place(x=40,y=400)
    qualite_e2=Entry(fenetre6,bg="#4B4B57",font=("Courrier",20))
    qualite_e2.place(x=270,y=400)
    but_val=Button(fenetre6,text="Valider",font=("Courrier",20),image=pixelVirtual,width=250,height=40,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=modificaton_bdd)
    but_val.place(x=300,y=500)
"""________________________________________"""
def recherche_modif():
     global resultTXT
     global liste_result
     global myIDlist
     global compteur_result
     cur.execute('SELECT * FROM ANNUAIRE')
     conn.commit()
     liste_2=[id_e4.get(),nom_e4.get(),prenom_e4.get(),tel_e4.get(),mail_e4.get()]
     
     liste_result=[]
     liste = cur.fetchall()
     compteur_result=0
     var3=str(liste_2[var_choix4.get()])
     for i in range(len(liste)):
            var2=str(liste[i][var_choix4.get()])
            if var2==var3:
                compteur_result=compteur_result+1
                liste_result.append(liste[i])
     if compteur_result==0:
         warn_supp=messagebox.showerror("ERREUR","Aucun contact n'a été trouvé.")
     if compteur_result==1:
         print(liste_result)
         modificaton_menu()
     
     if compteur_result>1:
        global selected_item3
        global myIDlist
        global fenetre_choix
        selected_item3 = StringVar()
        fenetre_choix=Toplevel(fenetre4)
        fenetre_choix.title("Modifier")
        fenetre_choix.geometry("800x400")
        fenetre_choix.config(background="BLACK")
        scroll2y=Scrollbar(fenetre_choix,width=20)
        scroll2y.pack( side = RIGHT, fill = Y ,padx=5)
        myIDlist = Listbox(fenetre_choix,font=("Courrier",15), yscrollcommand =scroll2y.set,height=8,width=40,bg="#80808C")
        for i in range(len(liste_result)):
            myIDlist.insert(END,liste_result[i])
        myIDlist.place(x=175,y=10);   
        scroll2y.config( command = myIDlist.yview )
        label_choixx=Label(fenetre_choix,text=" Ligne Choisie :   ",font=("Courrier",17),fg="white",background="black")
        label_choixx.place(x=50,y=215)
        label_choixsup=Label(fenetre_choix,textvariable=selected_item3,font=("Courrier",17),fg="white",background="BLACK")
        label_choixsup.place(x=200,y=215)
        bouton_supprimer=Button(fenetre_choix,text="Valider",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=modificaton_menu)
        bouton_supprimer.place(x=175,y=300)
        
        myIDlist.bind("<<ListboxSelect>>", get_listeboxx3)
def compteur_exist():
    try :
        print(compteur_result)
        return True
    except NameError :
        return False
"""________________________________________"""
def modificaton_bdd():
    if compteur_exist()!=False:
        if compteur_result==1:
            modificat=liste_result[0]
        else:
            modificat=supre3
    else:
     modificat=supre3
     if nom_e2.get()!="":
        modif=(nom_e2.get(),modificat[0],)
        cur.execute('UPDATE ANNUAIRE SET Nom = ? WHERE id = ?', modif)
        uptate()
        fenetre6.destroy()
    if prenom_e2.get()!="":
        modif=(prenom_e2.get(),modificat[0],)
        cur.execute('UPDATE ANNUAIRE SET Prénom = ? WHERE id = ?', modif)
        uptate()
        fenetre6.destroy()
    if email_e2.get()!="":
        modif=(email_e2.get(),modificat[0],)
        cur.execute('UPDATE ANNUAIRE SET email = ? WHERE id = ?', modif)
        uptate()
        fenetre6.destroy()
    if qualite_e2.get()!="":
        modif=(qualite_e2.get(),modificat[0],)
        cur.execute('UPDATE ANNUAIRE SET qualité = ? WHERE id = ?', modif)
        uptate()
        fenetre6.destroy()
    if tel_e2.get()!="" :
        modif=(tel_e22.get()+tel_e2.get(),modificat[0],)
        cur.execute('UPDATE ANNUAIRE SET telephone = ? WHERE id = ?', modif)
        uptate()
        fenetre6.destroy()
    return
    
    
"""________________________________________"""            
            
def get_listeboxx3(event):
    global supre3
    e3=myIDlist.curselection()[0]
    supre3=myIDlist.get(e3)
    selected_item3.set(supre3) 
    
"""________________________________________"""

def rechercher():
        global menu_entry
        global var_choix3
        global choix_id2
        global choix_nom2
        global choix_prenom2
        global choix_tel2
        global choix_mail2
        global mylist3
        global scroll4y
        global fenetre5
        var_choix3=IntVar()
        fenetre5=Toplevel(fenetre1)
        fenetre5.title("Rechercher")
        fenetre5.geometry("1000x600")
        fenetre5.config(background="black")
        canvas_effect=Canvas(fenetre5,height=50,width=975,bg="black",relief="groove").place(x=11,y=5)
        my_label2 =Label(fenetre5,text="RECHERCHER",font=("Courrier",20),bg="black",foreground ="White").place(x=350,y=15)
        menu_entry=Canvas(fenetre5,height=250,width=345,bg="#42424D",relief="sunken",borderwidth=0)
        menu_entry.place(x=100,y=325) 
        
        var_choix2 = IntVar()
        choix_id2 = Radiobutton(menu_entry,text="ID :",font=("Courrier",12),variable=var_choix3,value=0,bg="#42424D",foreground ="white",command=entry_rech)
        choix_id2.place(x=5,y=10)                 
                         
        choix_nom2 = Radiobutton(menu_entry,text="NOM :",font=("Courrier",12),variable=var_choix3,value=1,bg="#42424D",foreground ="white",command=entry_rech)
        choix_nom2.place(x=5,y=60)
        
                         
        choix_prenom2 = Radiobutton(menu_entry,variable=var_choix3,text="PRENOM :",font=("Courrier",12),value=2,bg="#42424D",foreground ="white",command=entry_rech)
        choix_prenom2.place(x=5,y=110)             
        
        choix_tel2 = Radiobutton(menu_entry,variable=var_choix3,text="TELEPHONE :",font=("Courrier",12),value=3,bg="#42424D",foreground ="white",command=entry_rech)
        choix_tel2.place(x=5,y=160)    
        
        choix_mail2 = Radiobutton(menu_entry,variable=var_choix3,text="EMAIL :",font=("Courrier",12),value=4,bg="#42424D",foreground ="white",command=entry_rech)
        choix_mail2.place(x=5,y=210)
        
        but_sup=Button(fenetre5,text="Rechercher",font=("Courrier",20),image=pixelVirtual,width=250,height=40,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=recherche)
        but_sup.place(x=550,y=400) 
        
        cur.execute('SELECT * FROM ANNUAIRE')
        conn.commit()
        liste = cur.fetchall()
        scroll4y=Scrollbar(fenetre5,width=20)
        scroll4y.pack( side = RIGHT, fill = Y ,padx=5)
        mylist3 = Listbox(fenetre5,font=("Courrier",15), yscrollcommand =scroll4y.set,height=10,width=50,bg="#80808C")
        for i in range(len(liste)):
                mylist3.insert(END,liste[i])
        mylist3.place(x=100,y=70);   
"""________________________________________"""
            
def entry_rech():
    global id_e3
    global nom_e3
    global prenom_e3
    global tel_e3
    global mail_e3

    id_e3=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    id_e3.place(x=140,y=10)
    nom_e3=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    nom_e3.place(x=140,y=60)
    prenom_e3=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    prenom_e3.place(x=140,y=110)
    tel_e3=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    tel_e3.place(x=140,y=160)   
    mail_e3=Entry(menu_entry,bg="#4B4B57",font=("Courrier",12))
    mail_e3.place(x=140,y=210)
    if var_choix3.get()==0:
        id_e3["state"]=NORMAL
        nom_e3["state"]=DISABLED
        prenom_e3["state"]=DISABLED
        tel_e3["state"]=DISABLED
        mail_e3["state"]=DISABLED
        
        choix_id2["state"]=DISABLED
        choix_nom2["state"]=NORMAL
        choix_prenom2["state"]=NORMAL
        choix_tel2["state"]=NORMAL
        choix_mail2["state"]=NORMAL
        
    elif var_choix3.get()==1:
        id_e3["state"]=DISABLED
        nom_e3["state"]=NORMAL
        prenom_e3["state"]=DISABLED
        tel_e3["state"]=DISABLED
        mail_e3["state"]=DISABLED
        
        choix_id2["state"]=NORMAL
        choix_nom2["state"]=DISABLED
        choix_prenom2["state"]=NORMAL
        choix_tel2["state"]=NORMAL
        choix_mail2["state"]=NORMAL
    elif var_choix3.get()==2:
        id_e3["state"]=DISABLED
        nom_e3["state"]=DISABLED
        prenom_e3["state"]=NORMAL
        tel_e3["state"]=DISABLED
        mail_e3["state"]=DISABLED

        choix_id2["state"]=NORMAL
        choix_nom2["state"]=NORMAL
        choix_prenom2["state"]=DISABLED
        choix_tel2["state"]=NORMAL
        choix_mail2["state"]=NORMAL
    elif var_choix3.get()==3:
        id_e3["state"]=DISABLED
        nom_e3["state"]=DISABLED
        prenom_e3["state"]=DISABLED
        tel_e3["state"]=NORMAL
        mail_e3["state"]=DISABLED
        
        choix_id2["state"]=NORMAL
        choix_nom2["state"]=NORMAL
        choix_prenom2["state"]=NORMAL
        choix_tel2["state"]=DISABLED
        choix_mail2["state"]=NORMAL
    else:
        id_e3["state"]=DISABLED
        nom_e3["state"]=DISABLED
        prenom_e3["state"]=DISABLED
        tel_e3["state"]=DISABLED
        mail_e3["state"]=NORMAL
        
        choix_id2["state"]=NORMAL
        choix_nom2["state"]=NORMAL
        choix_prenom2["state"]=NORMAL
        choix_tel2["state"]=NORMAL
        choix_mail2["state"]=DISABLED
        
"""________________________________________"""
def recherche():
    mylist3.destroy()
    scroll4y.destroy()
    if var_choix3.get()==0:
        cur.execute('SELECT id,Nom,Prénom,telephone FROM ANNUAIRE WHERE id = ? ',(id_e3.get(),))
        conn.commit()
        liste_rec = cur.fetchall()
        createlisteRecherche(liste_rec)
    elif var_choix3.get()==1:
        cur.execute('SELECT Nom,Prénom,telephone FROM ANNUAIRE WHERE nom = ? ',(nom_e3.get(),))
        conn.commit()
        liste_rec = cur.fetchall()
        createlisteRecherche(liste_rec)
    elif var_choix3.get()==2:
        cur.execute('SELECT Nom,Prénom,telephone FROM ANNUAIRE WHERE prenom = ? ',(prenom_e3.get(),))
        conn.commit()
        liste_rec = cur.fetchall()
        createlisteRecherche(liste_rec)
    elif var_choix3.get()==3:
        cur.execute('SELECT Nom,Prénom,telephone FROM ANNUAIRE WHERE telephone = ? ',(tel_e3.get(),))
        conn.commit()
        liste_rec = cur.fetchall()
        createlisteRecherche(liste_rec)

    else: 
        cur.execute('SELECT Nom,Prénom,email FROM ANNUAIRE WHERE email = ? ',(mail_e3.get(),))
        conn.commit()
        liste_rec = cur.fetchall()
        createlisteRecherche(liste_rec)
def createlisteRecherche(liste):
    if len(liste)==0:
        
        warn_rec=messagebox.showerror("ERREUR","Aucun contact n'a été trouvé.")
        cur.execute('SELECT * FROM ANNUAIRE')
        conn.commit()
        liste = cur.fetchall()
        scroll4y=Scrollbar(fenetre5,width=20)
        scroll4y.pack( side = RIGHT, fill = Y ,padx=5)
        mylist3 = Listbox(fenetre5,font=("Courrier",15), yscrollcommand =scroll4y.set,height=10,width=50,bg="#80808C")
        for i in range(len(liste)):
                mylist3.insert(END,liste[i])
        mylist3.place(x=100,y=70);   
    else:
        scroll4y=Scrollbar(fenetre5,width=20)
        scroll4y.pack( side = RIGHT, fill = Y ,padx=5)
        mylist3 = Listbox(fenetre5,font=("Courrier",15), yscrollcommand =scroll4y.set,height=10,width=50,bg="#80808C")
        for i in range(len(liste)):
            mylist3.insert(END,liste[i])
        mylist3.place(x=100,y=70);   
"""________________________________________"""
    
def ajjouter_bdd():
    nom=nom_e.get()
    prenom=prenom_e.get()
    telephone=tel_e2.get()+tel_e.get()
    email=email_e.get()
    qualité=qualite_e.get()
    info_ajj=(nom,prenom,telephone,email,qualité)
    if nom=="" and prenom=="":
        warn_ajj=messagebox.showerror("ERREUR","L'identiter de la personne est incorrect.")
    else:
        quest_ajj=messagebox.askyesno("Valider","""Etes vous sûr de bien ajouter ces informations ? \n
                                """+str(info_ajj))
        if quest_ajj==True:
            cur.execute("INSERT INTO ANNUAIRE(Nom,Prénom,telephone,email,qualité) VALUES(?,?,?,?,?)",info_ajj)
            conn.commit()
            fenetre2.destroy()
            uptate()
        else:
            return
"""________________________________________"""
def quitter():
    cur.close()
    conn.close()
    fenetre1.destroy()
"""________________________________________"""
def uptate():
    scroll1y.destroy()
    myIDlist.destroy()
    createTab(fenetre1,410,158)
    verif1()
    
    
"""__________________________________________________"""
def createTab(fen,Xp,Yp):
    global myIDlist
    global scroll1y
    global myNliste
    scroll1y=Scrollbar(fen,width=20)
    scroll1y.pack( side = RIGHT, fill = Y ,padx=5)
    cur.execute('SELECT * FROM ANNUAIRE')
    conn.commit()
    liste = cur.fetchall()
    liste_nom=[]
    liste_prenom=[]
    liste_tel=[]
    liste_mail=[]
    liste_qual=[]
    liste_id=[]
    for i in range(len(liste)):
        liste_id.append(liste[i][0]);
        liste_nom.append(liste[i][1]);
        liste_prenom.append(liste[i][2]);
        liste_tel.append(liste[i][3]);
        liste_mail.append(liste[i][4]);
        liste_qual.append(liste[i][5]);
    myNliste=[]
    for i in range(len(liste_id)):
        myNliste.append(str(liste_id[i])+" | "+str(liste_nom[i])+" | "+str(liste_prenom[i])+" | "+str(liste_tel[i])+" | "+str(liste_mail[i])+" | "+str(liste_qual[i]))
    myIDlist = Listbox(fen,font=("Courrier",15), yscrollcommand =scroll1y.set,height=20,width=77,bg="#80808C")
    for i in range(len(liste_id)):
        myIDlist.insert(END,myNliste[i])
    myIDlist.place(x=Xp,y=Yp);   
    scroll1y.config( command = myIDlist.yview )

"""____________________INITIALISATION DE LA BASE DE DONNEES____________________________________"""

conn = sqlite3.connect('base_donnée.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS ANNUAIRE(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, Nom TEXT, Prénom TXT, telephone TXT, email TXT, qualité TXT)")

"""________________________________________________________________________________"""
fenetre1=Tk()
pixelVirtual =PhotoImage(width=1, height=1) 
fenetre1.title("Annuaire")
fenetre1.geometry("1300x670")
fenetre1.config(background="Black")
canvas_effect=Canvas(fenetre1,height=100,width=1250,bg="black",relief="groove").place(x=11,y=5)                             
fenetre1.iconbitmap('annuaire.ico')
tableau=Canvas(fenetre1,height=480,width=850,bg="#80808C",relief="sunken",borderwidth=7)
tableau.place(x=400,y=150)

createTab(fenetre1,410,158)
my_label2 =Label(fenetre1,text="ANNUAIRE",font=("Courrier",40),bg="black",foreground ="white").place(x=580,y=20)
update_b=Button(fenetre1,text="Update",font=("Courrier",10),image=pixelVirtual, width=300,height=20,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=uptate)
update_b.place(x=555,y=118)
ajj=Button(fenetre1,text="Ajouter une valeur",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=ajouter)
ajj.place(x=10,y=150)
supp=Button(fenetre1,text="Supprimer une valeur",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=supprimer)
supp.place(x=10,y=250)
modif=Button(fenetre1,text="Modifier une valeur",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=modifier)
modif.place(x=10,y=350)
recherche_but=Button(fenetre1,text="Rechercher une valeur",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=rechercher)
recherche_but.place(x=10,y=450)
quitt=Button(fenetre1,text="Fermer le logiciel",font=("Courrier",20),image=pixelVirtual,width=300,height=50,compound="c",borderwidth=2,bg="#616172",fg="black",relief="groove",command=quitter)
quitt.place(x=10,y=550)
verif1()

"""________________________________________________________________________________"""




fenetre1.mainloop()