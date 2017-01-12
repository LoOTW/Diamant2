#RTLF DA-42


"""    Copyright (c) 2016, BRUNEAU Loïc
    All rights reserved.

    Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
    * Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.  """


import matplotlib.pyplot as plt
from tkinter import *
import tkinter
import tkinter.filedialog
import getpass
import os
import numpy as np
from matplotlib.widgets import Cursor

def maint():        #fenêtre de choix entre les modes maintenance et dépannage
    largeur=30
    global maintenance
    fenetre=Tk()                #boutons radio (un seul peut être coché à la fois)
    fenetre.title(" ")
    var = StringVar()
    c1 = Radiobutton(fenetre, text="Maintenance", variable=var, value=0, width=largeur)
    c2 = Radiobutton(fenetre, text="Dépannage", variable=var, value=1,width=largeur)
    OK=Button(fenetre, text='OK', command=fenetre.destroy)
    c1.pack()
    c2.pack()
    OK.pack()
    c1.select()
    mainloop()
    maintenance=var.get() #-> pour récupérer la valeur associée au bouton
        
def choixcourbes():     #fenêtre de choix des courbes à afficher lorsque l'on est en mode dépannage
    a=1
    b=40
    global wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3  #1 si case cochée, zéro sinon
    top = tkinter.Tk()      #top est le nom de la fenêtre
    top.title('Choix des courbes')
    OK=Button(top, text='OK', command=top.destroy)
    OK.pack(side=BOTTOM)
    # l = LabelFrame(fenetre, text="Titre de la frame", padx=20, pady=20)
    Frame5 = LabelFrame(top,text="Autres paramètres",borderwidth=2,relief=GROOVE)
    Frame5.pack(side=BOTTOM,padx=10,pady=10)
    Frame3b = Frame(top,borderwidth=0)#,relief=GROOVE)
    Frame3b.pack(side=BOTTOM,padx=10,pady=10)
    Frame4 = LabelFrame(Frame3b,text="Pression carburant",borderwidth=2,relief=GROOVE)
    Frame4.pack(side=RIGHT,padx=10,pady=10)
    Frame3 = LabelFrame(Frame3b,text="Hélice",borderwidth=2,relief=GROOVE)
    Frame3.pack(side=LEFT,padx=10,pady=10)
    Frame2 = LabelFrame(top,text="Moteur",borderwidth=2,relief=GROOVE)
    Frame2.pack(side=RIGHT,padx=10,pady=10)
    Frame1 = LabelFrame(top,text="Admission",borderwidth=2,relief=GROOVE)
    Frame1.pack(padx=10,pady=10)
    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()
    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()
    CheckVar9 = IntVar()
    CheckVar10 = IntVar()
    CheckVar11 = IntVar()
    CheckVar12 = IntVar()
    CheckVar13 = IntVar()
    CheckVar14 = IntVar()
    CheckVar15 = IntVar()
    CheckVar16 = IntVar()
    CheckVar17 = IntVar()
    CheckVar18 = IntVar()
    CheckVar19 = IntVar()
    CheckVar20 = IntVar()
    CheckVar21 = IntVar()
    CheckVar22 = IntVar()
    C1 = Checkbutton(Frame1, text = "WG_DC-A190", variable = CheckVar1, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C2 = Checkbutton(Frame2, text = "DisLoad-A334", variable = CheckVar2, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C3 = Checkbutton(Frame3, text = "Prop RPM-A306", variable = CheckVar3, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C4 = Checkbutton(Frame3, text = "Prop-DC-A313", variable = CheckVar4, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C5 = Checkbutton(Frame3, text = "PrSpdTar-A308", variable = CheckVar5, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C6 = Checkbutton(Frame1, text = "MAPTar-A181", variable = CheckVar6, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C7 = Checkbutton(Frame4, text = "PRail_DC-A204", variable = CheckVar7, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C8 = Checkbutton(Frame4, text = "PRaTar-A192", variable = CheckVar8, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C9 = Checkbutton(Frame4, text = "PRail-A131", variable = CheckVar9, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C10 = Checkbutton(Frame1, text = "MAP-A88", variable = CheckVar10, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C11 = Checkbutton(Frame2, text = "Engine Revs. RPM-A47", variable = CheckVar11, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C12 = Checkbutton(Frame5, text = "VBatt-A91", variable = CheckVar12, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C13 = Checkbutton(Frame5, text = "TAir-A93", variable = CheckVar13, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C14 = Checkbutton(Frame5, text = "TH2O-A92", variable = CheckVar14, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C15 = Checkbutton(Frame5, text = "TOil-A94", variable = CheckVar15, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C16 = Checkbutton(Frame5, text = "POil-A97", variable = CheckVar16, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C17 = Checkbutton(Frame5, text = "TGear-A267", variable = CheckVar17, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C18 = Checkbutton(Frame5, text = "PBaro-A99", variable = CheckVar18, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C19 = Checkbutton(Frame5, text = "TECU-A96", variable = CheckVar19, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C20 = Checkbutton(Frame4, text = "FCh-A246", variable = CheckVar20, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C21 = Checkbutton(Frame2, text = "Load-A87", variable = CheckVar21, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    C22 = Checkbutton(Frame5, text = "Altitude", variable = CheckVar22, \
                    onvalue = 1, offvalue = 0, height=a, \
                    width = b)
    
    C1.pack();C6.pack();C10.pack();
    C2.pack();C11.pack();C21.pack();
    C3.pack();C4.pack();C5.pack();
    C7.pack();C8.pack();C9.pack();C20.pack();
    C13.pack();C14.pack();C15.pack();C17.pack();C19.pack();C16.pack();C18.pack();C22.pack();C12.pack();
    
    
    top.mainloop()
    e=(CheckVar1.get(),CheckVar2.get(),CheckVar3.get(),CheckVar4.get(),CheckVar5.get(),CheckVar6.get(),CheckVar7.get(),CheckVar8.get(),CheckVar9.get(),CheckVar10.get(),CheckVar11.get(),CheckVar12.get(),CheckVar13.get(),CheckVar14.get(),CheckVar15.get(),CheckVar16.get(),CheckVar17.get(),CheckVar18.get(),CheckVar19.get(),CheckVar20.get(),CheckVar21.get(),CheckVar22.get())
    (wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3)=e

def ecu():      #fenêtre du choix des ECU
    largeur=30
    global ecu1
    fenetre=Tk()                #boutons radio (un seul peut être coché à la fois)
    fenetre.title("Choix de l'ECU")
    var = StringVar()
    ecua = Radiobutton(fenetre, text="ECU A", variable=var, value=0, width=largeur)
    ecub = Radiobutton(fenetre, text="ECU B", variable=var, value=1,width=largeur)
    OK=Button(fenetre, text='OK', command=fenetre.destroy)
    ecua.pack()
    ecub.pack()
    OK.pack()
    ecua.select()       #par défaut A est sélectionné
    mainloop()
    ecu1=var.get() #-> pour récupérer la valeur associée au bouton

def click():        #fonction exécutée une fois l'explorateur de fichier fermé
    global chemin
    user = getpass.getuser()
    file = tkinter.filedialog.askopenfilename(filetypes=[('text files', '.csv')],initialdir='C:/Users/%s' % user)
    directory = os.path.split(file)
    # print(directory)
    chemin=directory
    
def explo():            #lance l'explorateur de fichiers et stock l'adresse du fichier dans variable globale
    global gui
    gui = tkinter.Tk()
    user = getpass.getuser()
    button = tkinter.Button(gui, command=click())
    button.grid()
    gui.destroy()
    gui.mainloop()
    
def f():                #fermeture de la fenêtre et mode recommencer activé
    global recommencer
    recommencer=1
    fenetre2.destroy()
    
def apropos():
    about="Copyright (c) 2016, Loïc BRUNEAU\nAll rights reserved.\n"
    about+="Logiciel sous licence BSD\n\n"
    about+="Contact: loic.ds1@hotmail.fr\n\n"
    about+="Développé à l'ENAC Melun"
    fenetre2.destroy()
    fenetre3=Tk()                #boutons radio (un seul peut être coché à la fois)
    fenetre3.title("À propos")
    Label(fenetre3, text=about).pack()
    mainloop()
    
def rtlf():
    global maintenance
    global recommencer
    global fenetre2
    global gui
    tableau=[]                  #tableau des données qu'on affichera ensuite
    global wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3
    global chemin
    global ecu1
    
    explo()
    chemin=chemin[0]+'/'+chemin[1]          #l'adresse exacte du fichier avec le nom du fichier
    # fic=open('C:/Users/Loïc/Desktop/delog/RTLF#02-02-03295#0702#160208#093347.csv',"r")
    fic=open(chemin,"r")

    maint()
    
    n=0
    for line in fic:           #pour compter le nombre de lignes dans le fichier
        n+=1
    fic.close()
    # n=str(n-1)
    # afficher="fichier de "+n+" secondes"    #nombre de secondes dans le fichier pour choisir la plage horaire
    # print(afficher)
    # fenetre=Tk()                #afficher le texte dans une fenêtre   #à voir si c'est utile dans le cas où compilé en .exe
    # champ_label = Label(fenetre, text=afficher)
    # debut=StringVar()
    # fin=StringVar()
    # ligne_texte = Entry(fenetre, textvariable=var_texte, width=30)
    # ligne_texte.pack()
    # champ_label.pack()
    # mainloop()
    # try:
    #     debut=int(input("Temps de départ :"))
    # except BaseException:
    #     debut=0
    # try:
    #     fin=int(input("Temps de fin :"))
    # except BaseException:
    #     fin=int(n)
    # if fin>int(n) or debut<0 or fin-debut<1:            #pour afficher quelque chose quoi qu'on rentre comme valeur ou chaine de caractère
    #     debut=0
    #     fin=int(n)
    # debut=int(debut)
    # fic=open("C:/Users/Loïc/Desktop/delog/RTLF#02-02-03295#0702#160208#093347.csv","r")
             #penser à supprimer les '' de chaque str pour un meilleur affichage
    
    recommencer=1
    
    while str(recommencer)=='1':
        moteur=chemin[-28:-23]      #numéro de série du moteur
        nbheures=chemin[-22:-18]    #nombre d'heures de vol
        titre="Moteur "+moteur+"                                                                                                                     "+nbheures+"h"
        
        
        fic=open(chemin,"r")
        t=fic.readline()
        t=t.split(",") 

        ecu()
        
        try:
            if int(ecu1)==1:                    #ECU B sélectionnée
                iwg=t.index('WG_DC-B190')
                idisload=t.index('DisLoad-B334')    #c'est ici qu'il faut modifier les chaines de caractère si à l'avenir les NOMS des colonnes changent
                iproprpm=t.index('Prop RPM-B306')   #il faudrait alors efectuer ce changement à trois endroits: ici puis à deux reprises dans la fonction rtlf2()
                ipropdc=t.index('Prop-DC-B313')
                iprspd=t.index('PrSpdTar-B308')
                imaptar=t.index('MAPTar-B181')
                ipraildc=t.index('PRail_DC-B204')
                ipratar=t.index('PRaTar-B192')
                iprail=t.index('PRail-B131')
                imap=t.index('MAP-B88')
                iengine=t.index('Engine Revs. RPM-B47')
                ivbatt=t.index('VBatt-B91')
                itair=t.index('TAir-B93')
                ith2o=t.index('TH2O-B92')
                itoil=t.index('TOil-B94')
                ipoil=t.index('POil-B97')
                itgear=t.index('TGear-B267')
                ipbaro=t.index('PBaro-B99')
                itecu=t.index('TECU-B96')
                ifch=t.index('FCh-B246')
                iload=t.index('Load-B87')
                iecuact=t.index('ECU Act-B257')        
            else:                                       #ECU A sélectionée
                iwg=t.index('WG_DC-A190')
                idisload=t.index('DisLoad-A334')
                iproprpm=t.index('Prop RPM-A306')
                ipropdc=t.index('Prop-DC-A313')
                iprspd=t.index('PrSpdTar-A308')
                imaptar=t.index('MAPTar-A181')
                ipraildc=t.index('PRail_DC-A204')
                ipratar=t.index('PRaTar-A192')
                iprail=t.index('PRail-A131')
                imap=t.index('MAP-A88')
                iengine=t.index('Engine Revs. RPM-A47')
                ivbatt=t.index('VBatt-A91')
                itair=t.index('TAir-A93')
                ith2o=t.index('TH2O-A92')
                itoil=t.index('TOil-A94')
                ipoil=t.index('POil-A97')
                itgear=t.index('TGear-A267')
                ipbaro=t.index('PBaro-A99')
                itecu=t.index('TECU-A96')
                ifch=t.index('FCh-A246')
                iload=t.index('Load-A87')
                iecuact=t.index('ECU Act-A257')
            
            wg=[]
            disload=[]
            proprpm=[]
            propdc=[]
            prspd=[]
            maptar=[]
            praildc=[]
            pratar=[]
            prail=[]
            map=[]
            engine=[]
            vbatt=[]
            tair=[]
            th2o=[]
            toil=[]
            poil=[]
            tgear=[]
            pbaro=[]
            tecu=[]
            fch=[]
            load=[]
            alti=[]
            temps=[]
            ecuact=[]
            drail=[]
            dprop=[]
            dmap=[]
            
            # for i in range(debut):
            #     fic.readline()
            for i in range(n-1):#debut,fin):
                s=fic.readline()
                s=s.split(",")
        # WG 93-35              58
        # diload 84-48              36
        # prop rpm 95-37            58
        # prspd=pratar=wg=maptar=prail=praildc      58
        # load 68-16                                52
        # poil=toil=th2o=tgear 76-24                    52
        # engine 57-5                           52
        # map 70-18                 52
        # propdc 97-39                          58
        # tair 71-19                    52
        # vbatt 69-17                   52
        # pbaro=tecu 78-26                  52
        # fch 83-32                     51
                temps.append(i)
                wg.append(round(float(s[iwg]),2))             
                disload.append(round(float(s[idisload]),1))            
                proprpm.append(round(float(s[iproprpm]),2))         #Finalement niveau durée d'exécution c'est équivalent, autant garder ça
                propdc.append(round(float(s[ipropdc]),2))
                prspd.append(int(float(s[iprspd])))
                maptar.append(int(float(s[imaptar])))
                praildc.append(int(float(s[ipraildc])))
                pratar.append(int(float(s[ipratar])))
                prail.append(round(float(s[iprail]),1))
                map.append(int(float(s[imap])))
                engine.append(int(float(s[iengine])))
                vbatt.append(round(float(s[ivbatt]),1))
                tair.append(round(float(s[itair]),2))
                th2o.append(int(float(s[ith2o])))
                toil.append(int(float(s[itoil])))
                poil.append(round(float(s[ipoil]),1))
                tgear.append(int(float(s[itgear])))
                pbaro.append(int(float(s[ipbaro])))
                tecu.append(int(float(s[itecu])))
                fch.append(round(float(s[ifch]),2))
                load.append(round(float(s[iload]),1))
                alti.append(int(float(-(np.exp((np.log(abs(pbaro[-1]))-np.log(1013.25))/5.255)-1)*(288.15/0.0065)*3.5)))
                ecuact.append(190*float(s[iecuact]))
                drail.append(pratar[-1]-prail[-1])
                dprop.append(prspd[-1]-proprpm[-1])
                dmap.append(maptar[-1]-map[-1])
                # if (abs(alti[-1]-alti[-2])>1000 and i>debut+5):       #pour éviter les valeurs incohérentes
                #     alti[-1]=alti[-2]         #ne fonctionne pas, on s'en passera pour le moment
                if prspd[-1]==-1:                       #permet de retirer les lignes où tout est égal à -1, les courbes sont vachement mieux et problème de l'alti réglée?
                    for i in [temps,wg,disload,proprpm,propdc,prspd,maptar,praildc,pratar,prail,map,engine,vbatt,tair,th2o,toil,poil,tgear,pbaro,tecu,fch,load,alti,ecuact,drail,dprop,dmap]:
                        del i[-1]
            
            fic.close()
        
            if int(maintenance)==1:
                choixcourbes()
            else:
                (wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3)=(1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
                
            niveau=min(alti)
            for i in range(len(alti)):      #pour affiner la valeur de l'altitude, on considère 0m-> plus basse pression
                alti[i]=alti[i]-niveau
            k=(wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3)
            fig=plt.figure(figsize=(40,20))
            # ax = fig.add_subplot(111, axisbg='#FFFFFF')    #si on veut rajouter des barres horizontales et verticales autour du curseur, +voir ligne curseur
            tableau=[]
            tableau.append(temps)       #tableau des valeurs qu'on va afficher après
            courbes=['Temps']
            if k[0]:
                plt.plot(temps,wg,label='Waste Gate')
                tableau.append(wg)
                courbes.append('Waste Gate')                #titre à afficher pour le tableau de valeurs
            if k[5]:
                plt.plot(temps,maptar,label='Map Tar')
                tableau.append(maptar)
                courbes.append('Map Tar')
            if k[9]:
                plt.plot(temps,map,label='MAP')
                tableau.append(map)
                courbes.append('MAP')
            if int(maintenance)==0:
                tableau.append(dmap)
                courbes.append('Écart MAP')
            if k[1]:
                plt.plot(temps,disload,label='DisLoad')
                tableau.append(disload)
                courbes.append('DisLoad')
            if k[10]:
                plt.plot(temps,engine,label='Engine Revs. RPM-A47')
                tableau.append(engine)
                courbes.append('Engine Revs. RPM-A47')
            if k[20]:
                plt.plot(temps,load,label='Load-A87')
                tableau.append(load)
                courbes.append('Load-A87')
            if k[4]:
                plt.plot(temps,prspd,label='Prop Speed')
                tableau.append(prspd)
                courbes.append('Prop Speed')
            if k[2]:
                plt.plot(temps,proprpm,label='Prop RPM')
                tableau.append(proprpm)
                courbes.append('Prop RPM')
            if int(maintenance)==0:
                tableau.append(dprop)
                courbes.append('Écart PROP')
            if k[3]:
                plt.plot(temps,propdc,label='Prop DC')
                tableau.append(propdc)
                courbes.append('Prop DC')
            if k[6]:
                plt.plot(temps,praildc,label='Prail DC')
                tableau.append(praildc)
                courbes.append('Prail DC')
            if k[7]:
                plt.plot(temps,pratar,label='PraTar')
                tableau.append(pratar)
                courbes.append('PraTar')
            if k[8]:
                plt.plot(temps,prail,label='Prail')
                tableau.append(prail)
                courbes.append('Prail')
            if int(maintenance)==0:
                tableau.append(drail)
                courbes.append('Écart Rail')
            if k[19]:
                plt.plot(temps,fch,label='FCh-A246')
                tableau.append(fch)
                courbes.append('FCh-A246')
            if k[12]:
                plt.plot(temps,tair,label='TAir-A93')
                tableau.append(tair)
                courbes.append('TAir-A93')
            if k[13]:
                plt.plot(temps,th2o,label='TH2O-A92')
                tableau.append(th2o)
                courbes.append('TH2O-A92')
            if k[14]:
                plt.plot(temps,toil,label='TOil-A94')
                tableau.append(toil)
                courbes.append('TOil-A94')
            if k[16]:
                plt.plot(temps,tgear,label='TGear-A267')
                tableau.append(tgear)
                courbes.append('TGear-A267')
            if k[18]:
                plt.plot(temps,tecu,label='TECU-A96')
                tableau.append(tecu)
                courbes.append('TECU-A96')
            if k[15]:
                plt.plot(temps,poil,label='POil-A97')
                tableau.append(poil)
                courbes.append('POil-A97')
            if k[17]:
                plt.plot(temps,pbaro,label='PBaro-A99')
                tableau.append(pbaro)
                courbes.append('PBaro-A99')
            if k[21]:
                plt.plot(temps,alti,label="Allure de l'altitude")
                tableau.append(alti)
                courbes.append("Altitude")
            if k[11]:
                plt.plot(temps,vbatt,label='VBatt-A91')
                tableau.append(vbatt)
                courbes.append('VBatt-A91')
            plt.plot(temps,ecuact,'#798081',label=t[iecuact])    #hexa du gris, courbe pour voir si l'ECU selectionnée est active
            plt.legend()
            if ecu1=='0':
                titre+='                                                                                                                            ECU A'
            else:
                titre+='                                                                                                                            ECU B'
            plt.title(titre)       #immat du moteur+nombre d'heures de vol
            plt.show()
            l=''
            for i in courbes:
                c=len(i)
                c-=11
                c=-c
                c=c*' '
                l+=i+c
            # ppp=l+'\n'
            ppp=''
            temp=''
            for j in range(len(tableau[0])):
                temp=' '
                for i in range(len(tableau)):
                    b=len(str(tableau[i][j]))
                    b-=11
                    b=-b
                    b=b*' '
                    temp=temp+str(tableau[i][j])+b
                # print(str(temp)[1:-1])
                temp+='\n'
                ppp+=temp
            # print(ppp)
            root = Tk()
            root.title('Tableau de valeurs')
            Frame6 = Frame(root,borderwidth=0)#,relief=GROOVE)
            Frame6.pack(side=TOP,padx=10,pady=10)
            U=Text(Frame6, height=0, width=13*len(courbes))
            U.pack()
            U.insert(END,l)
            T = Text(root, height=400, width=13*len(courbes))
            T.pack()
            T.insert(END, ppp)
            mainloop()
            
            # print(courbes)
            # for i in range (len(tableau)):
            #     print(tableau[i])
        except BaseException:
            print('Le fichier est corrompu, il faut effectuer de nouvelles mesures')
        recommencer=0
        # recommencer=input("Recommencer? 1 si oui :")
        global fenetre2
        fenetre2=Tk()                #boutons radio (un seul peut être coché à la fois)
        fenetre2.title("")
        quitt=Button(fenetre2, text="Quitter", command=fenetre2.destroy)
        reco=Button(fenetre2, text='Recommencer', command=f)
        propos=Button(fenetre2, text='À propos',command=apropos)
        reco.pack()
        propos.pack()
        quitt.pack()
        mainloop()
    


def rtlf2():
    again=0
    global courbes,l
    global maintenance
    global recommencer
    global fenetre2
    global gui
    tableau=[]                  #tableau des données qu'on affichera ensuite
    global wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3
    global chemin
    global ecu1
    
    explo()
    chemin2=chemin
    chemin2=chemin2[0]+'/'+chemin2[1]          #l'adresse exacte du fichier avec le nom du fichier
    # fic=open('C:/Users/Loïc/Desktop/delog/RTLF#02-02-03295#0702#160208#093347.csv',"r")
    
    recommencer=1
    
    while str(recommencer)=='1':
    
        fic=open(chemin2,"r")
        
        
        if again==0:
            maint()
        
        n=0
        for line in fic:           #pour compter le nombre de lignes dans le fichier
            n+=1
        fic.close()
        
        
        
        
        moteur=chemin2[-28:-23]      #numéro de série du moteur
        nbheures=chemin2[-22:-18]    #nombre d'heures de vol
        titre="Moteur "+moteur+"                                                                                                                     "+nbheures+"h"
        
        
        fic=open(chemin2,"r")
        t=fic.readline()
        t=t.split(",") 
    
    

        ecu()
        
        ecu0=ecu1
        
        try:
            if int(ecu1)==1:                    #ECU B sélectionnée
                iwg=t.index('WG_DC-B190')
                idisload=t.index('DisLoad-B334')
                iproprpm=t.index('Prop RPM-B306')
                ipropdc=t.index('Prop-DC-B313')
                iprspd=t.index('PrSpdTar-B308')
                imaptar=t.index('MAPTar-B181')
                ipraildc=t.index('PRail_DC-B204')
                ipratar=t.index('PRaTar-B192')
                iprail=t.index('PRail-B131')
                imap=t.index('MAP-B88')
                iengine=t.index('Engine Revs. RPM-B47')
                ivbatt=t.index('VBatt-B91')
                itair=t.index('TAir-B93')
                ith2o=t.index('TH2O-B92')
                itoil=t.index('TOil-B94')
                ipoil=t.index('POil-B97')
                itgear=t.index('TGear-B267')
                ipbaro=t.index('PBaro-B99')
                itecu=t.index('TECU-B96')
                ifch=t.index('FCh-B246')
                iload=t.index('Load-B87')
                iecuact=t.index('ECU Act-B257')        
            else:                                       #ECU A sélectionée
                iwg=t.index('WG_DC-A190')
                idisload=t.index('DisLoad-A334')
                iproprpm=t.index('Prop RPM-A306')
                ipropdc=t.index('Prop-DC-A313')
                iprspd=t.index('PrSpdTar-A308')
                imaptar=t.index('MAPTar-A181')
                ipraildc=t.index('PRail_DC-A204')
                ipratar=t.index('PRaTar-A192')
                iprail=t.index('PRail-A131')
                imap=t.index('MAP-A88')
                iengine=t.index('Engine Revs. RPM-A47')
                ivbatt=t.index('VBatt-A91')
                itair=t.index('TAir-A93')
                ith2o=t.index('TH2O-A92')
                itoil=t.index('TOil-A94')
                ipoil=t.index('POil-A97')
                itgear=t.index('TGear-A267')
                ipbaro=t.index('PBaro-A99')
                itecu=t.index('TECU-A96')
                ifch=t.index('FCh-A246')
                iload=t.index('Load-A87')
                iecuact=t.index('ECU Act-A257')
            
            wg=[]
            disload=[]
            proprpm=[]
            propdc=[]
            prspd=[]
            maptar=[]
            praildc=[]
            pratar=[]
            prail=[]
            map=[]
            engine=[]
            vbatt=[]
            tair=[]
            th2o=[]
            toil=[]
            poil=[]
            tgear=[]
            pbaro=[]
            tecu=[]
            fch=[]
            load=[]
            alti=[]
            temps=[]
            ecuact=[]
            drail=[]
            dprop=[]
            dmap=[]
            
    
            for i in range(n-1):#debut,fin):
                s=fic.readline()
                s=s.split(",")
    
                temps.append(i)
                wg.append(round(float(s[iwg]),2))             
                disload.append(round(float(s[idisload]),1))            
                proprpm.append(round(float(s[iproprpm]),2))        
                propdc.append(round(float(s[ipropdc]),2))
                prspd.append(int(float(s[iprspd])))
                maptar.append(int(float(s[imaptar])))
                praildc.append(int(float(s[ipraildc])))
                pratar.append(int(float(s[ipratar])))
                prail.append(round(float(s[iprail]),1))
                map.append(int(float(s[imap])))
                engine.append(int(float(s[iengine])))
                vbatt.append(round(float(s[ivbatt]),1))
                tair.append(round(float(s[itair]),2))
                th2o.append(int(float(s[ith2o])))
                toil.append(int(float(s[itoil])))
                poil.append(round(float(s[ipoil]),1))
                tgear.append(int(float(s[itgear])))
                pbaro.append(int(float(s[ipbaro])))
                tecu.append(int(float(s[itecu])))
                fch.append(round(float(s[ifch]),2))
                load.append(round(float(s[iload]),1))
                alti.append(int(float(-(np.exp((np.log(abs(pbaro[-1]))-np.log(1013.25))/5.255)-1)*(288.15/0.0065)*3.5)))
                ecuact.append(190*float(s[iecuact]))
                drail.append(pratar[-1]-prail[-1])
                dprop.append(prspd[-1]-proprpm[-1])
                dmap.append(maptar[-1]-map[-1])
                # if (abs(alti[-1]-alti[-2])>1000 and i>debut+5):       #pour éviter les valeurs incohérentes
                #     alti[-1]=alti[-2]         #ne fonctionne pas, on s'en passera pour le moment
                if prspd[-1]==-1:                       #permet de retirer les lignes où tout est égal à -1, les courbes sont vachement mieux et problème de l'alti réglée?
                    for i in [temps,wg,disload,proprpm,propdc,prspd,maptar,praildc,pratar,prail,map,engine,vbatt,tair,th2o,toil,poil,tgear,pbaro,tecu,fch,load,alti,ecuact,drail,dprop,dmap]:
                        del i[-1]
            
            fic.close()    # fin du ctrl c
        
        except BaseException:
            print("Le fichier du moteur 1 semble corrompu, il faut effectuer de nouvelles mesures")
        
    
        try:
            if int(maintenance)==1:
                choixcourbes()
            else:
                (wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3)=(1,0,1,0,1,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0)
                
            niveau=min(alti)   #penser à le refaire pour l'autre liste
            for i in range(len(alti)):      #pour affiner la valeur de l'altitude, on considère 0m-> plus basse pression
                alti[i]=alti[i]-niveau
            
        except BaseException:
            print("Le fichier du moteur 1 semble corrompu, il faut effectuer de nouvelles mesures")
            
            
            
            
            
        #DEUXIEME MOTEUR
        
        
        
        
        
        
        
        if again==0:    
            explo()
            chemin=chemin[0]+'/'+chemin[1]          #l'adresse exacte du fichier avec le nom du fichier
        # fic=open('C:/Users/Loïc/Desktop/delog/RTLF#02-02-03295#0702#160208#093347.csv',"r")
        fic=open(chemin,"r")
        
        n=0
        for line in fic:           #pour compter le nombre de lignes dans le fichier
            n+=1
        fic.close()
        
        
        moteur=chemin[-28:-23]      #numéro de série du moteur
        nbheures=chemin[-22:-18]    #nombre d'heures de vol
        titre2="Moteur "+moteur+"                                                                                                                     "+nbheures+"h"
        
        
        fic=open(chemin,"r")
        t2=fic.readline()
        t2=t2.split(",") 
    
        ecu()
        
        # try:
        if int(ecu1)==1:                    #ECU B sélectionnée
            iiwg=t2.index('WG_DC-B190')
            iidisload=t2.index('DisLoad-B334')
            iiproprpm=t2.index('Prop RPM-B306')
            iipropdc=t2.index('Prop-DC-B313')
            iiprspd=t2.index('PrSpdTar-B308')
            iimaptar=t2.index('MAPTar-B181')
            iipraildc=t2.index('PRail_DC-B204')
            iipratar=t2.index('PRaTar-B192')
            iiprail=t2.index('PRail-B131')
            iimap=t2.index('MAP-B88')
            iiengine=t2.index('Engine Revs. RPM-B47')
            iivbatt=t2.index('VBatt-B91')
            iitair=t2.index('TAir-B93')
            iith2o=t2.index('TH2O-B92')
            iitoil=t2.index('TOil-B94')
            iipoil=t2.index('POil-B97')
            iitgear=t2.index('TGear-B267')
            iipbaro=t2.index('PBaro-B99')
            iitecu=t2.index('TECU-B96')
            iifch=t2.index('FCh-B246')
            iiload=t2.index('Load-B87')
            iiecuact=t2.index('ECU Act-B257')        
        else:                                       #ECU A sélectionée
            iiwg=t2.index('WG_DC-A190')
            iidisload=t2.index('DisLoad-A334')
            iiproprpm=t2.index('Prop RPM-A306')
            iipropdc=t2.index('Prop-DC-A313')
            iiprspd=t2.index('PrSpdTar-A308')
            iimaptar=t2.index('MAPTar-A181')
            iipraildc=t2.index('PRail_DC-A204')
            iipratar=t2.index('PRaTar-A192')
            iiprail=t2.index('PRail-A131')
            iimap=t2.index('MAP-A88')
            iiengine=t2.index('Engine Revs. RPM-A47')
            iivbatt=t2.index('VBatt-A91')
            iitair=t2.index('TAir-A93')
            iith2o=t2.index('TH2O-A92')
            iitoil=t2.index('TOil-A94')
            iipoil=t2.index('POil-A97')
            iitgear=t2.index('TGear-A267')
            iipbaro=t2.index('PBaro-A99')
            iitecu=t2.index('TECU-A96')
            iifch=t2.index('FCh-A246')
            iiload=t2.index('Load-A87')
            iiecuact=t2.index('ECU Act-A257')
        
        wgp=[]
        disloadp=[]
        proprpmp=[]
        propdcp=[]
        prspdp=[]
        maptarp=[]
        praildcp=[]
        pratarp=[]
        prailp=[]
        mapp=[]
        enginep=[]
        vbattp=[]
        tairp=[]
        th2op=[]
        toilp=[]
        poilp=[]
        tgearp=[]
        pbarop=[]
        tecup=[]
        fchp=[]
        loadp=[]
        altip=[]
        tempsp=[]
        ecuactp=[]
        drailp=[]
        dpropp=[]
        dmapp=[]
        

        for i in range(n-1):#debut,fin):
            s=fic.readline()
            s=s.split(",")

            tempsp.append(i)
            wgp.append(round(float(s[iiwg]),2))            
            disloadp.append(round(float(s[iidisload]),1)  )         
            proprpmp.append(round(float(s[iiproprpm]),2))
            propdcp.append(round(float(s[iipropdc]),2))
            prspdp.append(int(float(s[iiprspd])))
            maptarp.append(int(float(s[iimaptar])))
            praildcp.append(int(float(s[iipraildc])))
            pratarp.append(int(float(s[iipratar])))
            prailp.append(round(float(s[iiprail]),2))
            mapp.append(int(float(s[iimap])))
            enginep.append(int(float(s[iiengine])))
            vbattp.append(round(float(s[iivbatt]),1))
            tairp.append(round(float(s[iitair]),2))
            th2op.append(int(float(s[iith2o])))
            toilp.append(int(float(s[iitoil])))
            poilp.append(round(float(s[iipoil]),1))
            tgearp.append(int(float(s[iitgear])))
            pbarop.append(int(float(s[iipbaro])))
            tecup.append(int(float(s[iitecu])))
            fchp.append(round(float(s[iifch]),2))
            loadp.append(round(float(s[iiload]),1))
            altip.append(int(float(-(np.exp((np.log(abs(pbarop[-1]))-np.log(1013.25))/5.255)-1)*(288.15/0.0065)*3.5)))
            ecuactp.append(190*float(s[iiecuact]))
            drailp.append(pratarp[-1]-prailp[-1])
            dpropp.append(prspdp[-1]-proprpmp[-1])
            dmapp.append(maptarp[-1]-mapp[-1])
            # if (abs(alti[-1]-alti[-2])>1000 and i>debut+5):       #pour éviter les valeurs incohérentes
            #     alti[-1]=alti[-2]         #ne fonctionne pas, on s'en passera pour le moment
            if prspdp[-1]==-1:                       #permet de retirer les lignes où tout est égal à -1, les courbes sont vachement mieux et problème de l'alti réglée?
                for i in [tempsp,wgp,disloadp,proprpmp,propdcp,prspdp,maptarp,praildcp,pratarp,prailp,mapp,enginep,vbattp,tairp,th2op,toilp,poilp,tgearp,pbarop,tecup,fchp,loadp,altip,ecuactp,drailp,dpropp,dmapp]:
                    del i[-1]
        
        fic.close()
        
        niveau=min(altip)   
        for i in range(len(altip)):      #pour affiner la valeur de l'altitude, on considère 0m-> plus basse pression
            altip[i]=altip[i]-niveau
    
    
    
    
    
    
    
        
        k=(wg3,disload3,proprpm3,propdc3,prspd3,maptar3,praildc3,pratar3,prail3,map3,engine3,vbatt3,tair3,th2o3,toil3,poil3,tgear3,pbaro3,tecu3,fch3,load3,alti3)
        fig=plt.figure(figsize=(40,20))
        # ax = fig.add_subplot(111, axisbg='#FFFFFF')    #si on veut rajouter des barres horizontales et verticales autour du curseur, +voir ligne curseur
        tableau=[]
        tableau2=[]
        tableau.append(temps)
        tableau2.append(tempsp)       #tableau des valeurs qu'on va afficher après
        courbes=['Temps']
        courbes2=['Temps']
        
        plt.subplot(211)
        if k[0]:
            plt.plot(temps,wg,label='Waste Gate')
            tableau.append(wg)
            courbes.append('Waste Gate')                #titre à afficher pour le tableau de valeurs
        if k[5]:
            plt.plot(temps,maptar,label='Map Tar')
            tableau.append(maptar)
            courbes.append('Map Tar')
        if k[9]:
            plt.plot(temps,map,label='MAP')
            tableau.append(map)
            courbes.append('MAP')
        if int(maintenance)==0:
            tableau.append(dmap)
            courbes.append('Écart MAP')
        if k[1]:
            plt.plot(temps,disload,label='DisLoad')
            tableau.append(disload)
            courbes.append('DisLoad')
        if k[10]:
            plt.plot(temps,engine,label='Engine Revs. RPM-A47')
            tableau.append(engine)
            courbes.append('Engine Revs. RPM-A47')
        if k[20]:
            plt.plot(temps,load,label='Load-A87')
            tableau.append(load)
            courbes.append('Load-A87')
        if k[4]:
            plt.plot(temps,prspd,label='Prop Speed')
            tableau.append(prspd)
            courbes.append('Prop Speed')
        if k[2]:
            plt.plot(temps,proprpm,label='Prop RPM')
            tableau.append(proprpm)
            courbes.append('Prop RPM')
        if int(maintenance)==0:
            tableau.append(dprop)
            courbes.append('Écart PROP')
        if k[3]:
            plt.plot(temps,propdc,label='Prop DC')
            tableau.append(propdc)
            courbes.append('Prop DC')
        if k[6]:
            plt.plot(temps,praildc,label='Prail DC')
            tableau.append(praildc)
            courbes.append('Prail DC')
        if k[7]:
            plt.plot(temps,pratar,label='PraTar')
            tableau.append(pratar)
            courbes.append('PraTar')
        if k[8]:
            plt.plot(temps,prail,label='Prail')
            tableau.append(prail)
            courbes.append('Prail')
        if int(maintenance)==0:
            tableau.append(drail)
            courbes.append('Écart Rail')
        if k[19]:
            plt.plot(temps,fch,label='FCh-A246')
            tableau.append(fch)
            courbes.append('FCh-A246')
        if k[12]:
            plt.plot(temps,tair,label='TAir-A93')
            tableau.append(tair)
            courbes.append('TAir-A93')
        if k[13]:
            plt.plot(temps,th2o,label='TH2O-A92')
            tableau.append(th2o)
            courbes.append('TH2O-A92')
        if k[14]:
            plt.plot(temps,toil,label='TOil-A94')
            tableau.append(toil)
            courbes.append('TOil-A94')
        if k[16]:
            plt.plot(temps,tgear,label='TGear-A267')
            tableau.append(tgear)
            courbes.append('TGear-A267')
        if k[18]:
            plt.plot(temps,tecu,label='TECU-A96')
            tableau.append(tecu)
            courbes.append('TECU-A96')
        if k[15]:
            plt.plot(temps,poil,label='POil-A97')
            tableau.append(poil)
            courbes.append('POil-A97')
        if k[17]:
            plt.plot(temps,pbaro,label='PBaro-A99')
            tableau.append(pbaro)
            courbes.append('PBaro-A99')
        if k[21]:
            plt.plot(temps,alti,label="Allure de l'altitude")
            tableau.append(alti)
            courbes.append("Altitude")
        if k[11]:
            plt.plot(temps,vbatt,label='VBatt-A91')
            tableau.append(vbatt)
            courbes.append('VBatt-A91')
        plt.plot(temps,ecuact,'#798081',label=t[iecuact])    #hexa du gris, courbe pour voir si l'ECU selectionnée est active
        plt.legend()
        if ecu0=='0':
            titre+='                                                                                                                            ECU A'
        else:
            titre+='                                                                                                                            ECU B'
        plt.title(titre)       #immat du moteur+nombre d'heures de vol
        
        
        plt.subplot(212)
        
        
        if k[0]:
            plt.plot(tempsp,wgp,label='Waste Gate')
            tableau2.append(wgp)
            courbes2.append('Waste Gate')                #titre à afficher pour le tableau2 de valeurs
        if k[5]:
            plt.plot(tempsp,maptarp,label='Map Tar')
            tableau2.append(maptarp)
            courbes2.append('Map Tar')
        if k[9]:
            plt.plot(tempsp,mapp,label='MAP')
            tableau2.append(mapp)
            courbes2.append('MAP')
        if int(maintenance)==0:
            tableau2.append(dmapp)
            courbes2.append('Écart MAP')
        if k[1]:
            plt.plot(tempsp,disloadp,label='DisLoad')
            tableau2.append(disloadp)
            courbes2.append('DisLoad')
        if k[10]:
            plt.plot(tempsp,enginep,label='Engine Revs. RPM-A47')
            tableau2.append(enginep)
            courbes2.append('Engine Revs. RPM-A47')
        if k[20]:
            plt.plot(tempsp,loadp,label='Load-A87')
            tableau2.append(loadp)
            courbes2.append('Load-A87')
        if k[4]:
            plt.plot(tempsp,prspdp,label='Prop Speed')
            tableau2.append(prspdp)
            courbes2.append('Prop Speed')
        if k[2]:
            plt.plot(tempsp,proprpmp,label='Prop RPM')
            tableau2.append(proprpmp)
            courbes2.append('Prop RPM')
        if int(maintenance)==0:
            tableau2.append(dpropp)
            courbes2.append('Écart PROP')
        if k[3]:
            plt.plot(tempsp,propdcp,label='Prop DC')
            tableau2.append(propdcp)
            courbes2.append('Prop DC')
        if k[6]:
            plt.plot(tempsp,praildcp,label='Prail DC')
            tableau2.append(praildcp)
            courbes2.append('Prail DC')
        if k[7]:
            plt.plot(tempsp,pratarp,label='PraTar')
            tableau2.append(pratarp)
            courbes2.append('PraTar')
        if k[8]:
            plt.plot(tempsp,prailp,label='Prail')
            tableau2.append(prailp)
            courbes2.append('Prail')
        if int(maintenance)==0:
            tableau2.append(drailp)
            courbes2.append('Écart Rail')
        if k[19]:
            plt.plot(tempsp,fchp,label='FCh-A246')
            tableau2.append(fchp)
            courbes2.append('FCh-A246')
        if k[12]:
            plt.plot(tempsp,tairp,label='TAir-A93')
            tableau2.append(tairp)
            courbes2.append('TAir-A93')
        if k[13]:
            plt.plot(tempsp,th2op,label='TH2O-A92')
            tableau2.append(th2op)
            courbes2.append('TH2O-A92')
        if k[14]:
            plt.plot(tempsp,toilp,label='TOil-A94')
            tableau2.append(toilp)
            courbes2.append('TOil-A94')
        if k[16]:
            plt.plot(tempsp,tgearp,label='TGear-A267')
            tableau2.append(tgearp)
            courbes2.append('TGear-A267')
        if k[18]:
            plt.plot(tempsp,tecup,label='TECU-A96')
            tableau2.append(tecup)
            courbes2.append('TECU-A96')
        if k[15]:
            plt.plot(tempsp,poilp,label='POil-A97')
            tableau2.append(poilp)
            courbes2.append('POil-A97')
        if k[17]:
            plt.plot(tempsp,pbarop,label='PBaro-A99')
            tableau2.append(pbarop)
            courbes2.append('PBaro-A99')
        if k[21]:
            plt.plot(tempsp,altip,label="Allure de l'altitude")
            tableau2.append(altip)
            courbes2.append("Altitude")
        if k[11]:
            plt.plot(tempsp,vbattp,label='VBatt-A91')
            tableau2.append(vbattp)
            courbes2.append('VBatt-A91')
        plt.plot(tempsp,ecuactp,'#798081',label=t[iiecuact])    #hexa du gris, courbe pour voir si l'ECU selectionnée est active
        plt.legend()
        if ecu1=='0':
            titre2+='                                                                                                                            ECU A'
        else:
            titre2+='                                                                                                                            ECU B'
        plt.title(titre2)       #immat du moteur+nombre d'heures de vol
        
        
        plt.show()
        again+=1
        l=''
        for i in courbes:
            c=len(i)
            c-=11
            c=-c
            c=c*' '
            l+=i+c
        # ppp=l+'\n'
        ppp=''
        temp=''
        for j in range(len(tableau[0])):
            temp=' '
            for i in range(len(tableau)):
                b=len(str(tableau[i][j]))
                b-=11
                b=-b
                b=b*' '
                temp=temp+str(tableau[i][j])+b
            # print(str(temp)[1:-1])
            temp+='\n'
            ppp+=temp
            
        l2=''
        for i in courbes2:
            c2=len(i)
            c2-=11
            c2=-c2
            c2=c2*' '
            l2+=i+c2
        # ppp=l+'\n'
        ppp2=''
        temp2=''
        for j in range(len(tableau2[0])):
            temp2=' '
            for i in range(len(tableau2)):
                b2=len(str(tableau2[i][j]))
                b2-=11
                b2=-b2
                b2=b2*' '
                temp2=temp2+str(tableau2[i][j])+b2
            # print(str(temp)[1:-1])
            temp2+='\n'
            ppp2+=temp2
        
        
        
        
        root = Tk()
        root.title('Tableau de valeurs 1')
        Frame6 = Frame(root,borderwidth=0)#,relief=GROOVE)
        Frame6.pack(side=TOP,padx=10,pady=10)
        U=Text(Frame6, height=0, width=13*len(courbes))
        U.pack()
        U.insert(END,l)
        T = Text(root, height=400, width=13*len(courbes))
        T.pack()
        T.insert(END, ppp)
        mainloop()
        
        root = Tk()
        root.title('Tableau de valeurs 2')
        Frame6 = Frame(root,borderwidth=0)#,relief=GROOVE)
        Frame6.pack(side=TOP,padx=10,pady=10)
        U=Text(Frame6, height=0, width=13*len(courbes2))
        U.pack()
        U.insert(END,l)
        T = Text(root, height=400, width=13*len(courbes2))
        T.pack()
        T.insert(END, ppp2)
        mainloop()
        # 
        # print(courbes)
        # for i in range (len(tableau)):
        #     print(tableau[i])
        # except BaseException:
        #     print('Le fichier du moteur 2 semble corrompu, il faut effectuer de nouvelles mesures')
        recommencer=0
        # recommencer=input("Recommencer? 1 si oui :")
        global fenetre2
        fenetre2=Tk()                #boutons radio (un seul peut être coché à la fois)
        fenetre2.title("")
        quitt=Button(fenetre2, text="Quitter", command=fenetre2.destroy)
        reco=Button(fenetre2, text='Recommencer', command=f)
        propos=Button(fenetre2, text='À propos',command=apropos)
        # valeurs1=Button(fenetre2, text="Afficher le 1er tableau", command=h(ppp))
        # valeurs2=Button(fenetre2, text="Afficher le 2ème tableau", command=h(ppp2))
        # valeurs1.pack()
        # valeurs2.pack()
        reco.pack()
        propos.pack()
        quitt.pack()
        mainloop()
    
    
    
    

largeur=60

global nbdemoteurs
fenetre=Tk()                #boutons radio (un seul peut être coché à la fois)
fenetre.title("Choix du nombre de moteurs")
var = StringVar()
c1 = Radiobutton(fenetre, text="Un moteur", variable=var, value=0, width=largeur)
c2 = Radiobutton(fenetre, text="Deux moteurs", variable=var, value=1,width=largeur)
OK=Button(fenetre, text='OK', command=fenetre.destroy)
c1.pack()
c2.pack()
OK.pack()
c1.select()
mainloop()
nbdemoteurs=var.get() #-> pour récupérer la valeur associée au bouton    

if str(nbdemoteurs)=='1':
    rtlf2()
else:
    rtlf()


