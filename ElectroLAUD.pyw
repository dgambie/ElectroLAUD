import os
from tkinter import * #import pour l'interface graphique
from tkinter.messagebox import * #pour les fenetres de dialog
#from tkinter import filedialog # pour l'explorateur
#from tkinter import ttk



def Quitter () : #Fonction pour quitter le programme
    '''
    Fonction pour Quitter l'application
'''
    fenetre.destroy()

def About():
    '''
    Fonction pour le à propos
'''
    showinfo("À propos", "Aide à la lecure des résistances\nVersion 1.0\nLaudren Electronique - DG - 2019") #Fonction pour le APROPOS
    
def Calcul_resistance (sign1,sign2,sign3,multi,bypass = ''):
    global valeurResistance
    
    if sign1 == -1 :
        sign1 = ''
    if sign2 == -1 :
        sign2 = ''
    if sign3 == -1 :
        sign3 = ''
        
    res = str(sign1) + str (sign2) + str (sign3)
    res = int (res) * multi
    res = round(res,2)
    decimal = res %1
    print(decimal)
    
    if decimal == 0.0 :
        print ('OK')
        res = int (res)
        
    if res >= 100000000 :
        res = res / 1000000
        decimal = res%1
        if decimal == 0.0:
            res = int(res)
        res = str(res) + ' M'
        #res = res[:5]
    
    elif res >= 10000000 :
        res = res / 1000000
        decimal = res%1
        if decimal == 0.0:
            res = int(res)
        res = str(res) + ' M'
        #res = res[:5]
        
    elif res >= 1000000 :
        res = res / 1000000
        res = str(res) + ' M'
        #res = res[:4]
        
    elif res >= 100000 :
        res = res / 1000
        decimal = res%1
        if decimal == 0.0:
            res = int(res)
        res = str(res) + ' k'
        #res = res[:6]
        
    elif res >= 10000 :
        res = res / 1000
        decimal = res%1
        if decimal == 0.0:
            res = int(res)
        res = str(res) + ' k'
        #res = res[:5]
        
    elif res >= 1000 :
        res = res / 1000
        res = str(res) + ' k'
        #res = res[:4]
    
    else :
        res = str(res)
        #res = res[:4]
        res = res + ' '
    
    #res = str(res)
    #bypass permet d'afficher directement la valeur sans calcul   
    if bypass != '':
        valeurResistance.set(bypass + 'Ohms')
    else :
        valeurResistance.set (res + 'Ohms')



def Nombre_bande (fenetre,nbBande) :
    
    if nbBande == 1 :
        print ('5 bandes')
        Actualiser_trad(fenetre,0)

    else :
        Actualiser_trad(fenetre,1)
        print ('4 bandes')
        print (nbBande)
    

def Menu_app (nbBande,fenetre):
    #Création des menus defaut
    menuPrincipal = Menu()
    ssMenuResistance = Menu()
    ssMenuApropos = Menu()
           
    ssMenuResistance.add_checkbutton(label = '5 Bandes', variable = nbBande, command = lambda : Nombre_bande(fenetre,nbBande.get()))
    ssMenuApropos.add_command(label = 'Ajout Remarques',command = Ajout_remarque)
    ssMenuApropos.add_command(label = 'Aide', command = Aide)
    ssMenuApropos.add_command(label = 'A propos', command = About)
    menuPrincipal.add_cascade(label = 'Résistance trad',menu = ssMenuResistance)
    #menuPrincipal.add_command(label = 'Resistance trad',command = lambda : Actualiser_trad(0,fenetre))
    menuPrincipal.add_command(label = 'Resistance CMS',command = lambda : Actualiser_CMS(fenetre))
    #menuPrincipal.add_command(label = 'Ajout Remarque', command = Ajout_remarque)
    #menuPrincipal.add_command(label = 'A propos',command = About)
    menuPrincipal.add_command(label = 'Quitter',command = Quitter)
    menuPrincipal.add_cascade(label = '?', menu = ssMenuApropos)

    fenetre.config(menu = menuPrincipal)

  
def Aide ():
    os.startfile("aide.pdf") 

def Ajout_remarque():
    #création d'une fenetre secondaire
    global fenetre_remarque
    fenetre_remarque = Toplevel()
    fenetre_remarque.title('Ajout / consultation des remarques')
    fenetre_remarque.focus_set()

    
    
    #Label
    lblRemarques = Label(fenetre_remarque,text='Remarques :', justify = 'left')
    lblRemarques.grid(column = 0, row = 0, sticky = 'sw')
    
    #input pour les remarques
    #varRemarque = StringVar()
    #varRemarque.set(Lecture_Ecriture_Remarque(''))
    strRmarque = Lecture_Ecriture_Remarque('')
    print (strRmarque)
    txtRemarque = Text(fenetre_remarque, width = 50,wrap='word')
    txtRemarque.insert(END,strRmarque)
    txtRemarque.grid(column = 0, row = 1, columnspan = 2)
    
    #Bouton OK et Annuler
    btnOk_remarque = Button (fenetre_remarque, text = 'OK', justify = 'right', command = lambda : Lecture_Ecriture_Remarque(txtRemarque.get('1.0','end'), mode = 'ecriture'))
    btnAnnuler_remarque = Button (fenetre_remarque,text = 'Annuler', justify = 'left', command = fenetre_remarque.destroy)
    btnOk_remarque.grid(column = 0, row = 2, sticky = 'se', padx = 5)
    btnAnnuler_remarque.grid(column = 1, row = 2, sticky = 'sw', padx = 5)

def Lecture_Ecriture_Remarque(text,mode = 'lecture'):
    if mode == 'lecture':
        with open("remarques.txt", "r") as fichier:
            return fichier.read()
    if mode == 'ecriture':
        with open("remarques.txt", "w") as fichier:
            print ('ecriture de : ',text)
            fichier.write(text)
            fenetre_remarque.destroy()
    

def Actualiser_CMS(fenetre):
    global logo
    global resistance_CMS
    #global nbBande
     
    
    #Effacement de la fenetre
    for element in fenetre.winfo_children():
        if (isinstance(element,Menu)) != True:
            element.destroy()
    
            
    ###############Création des frames################
    frmLogo = Frame(fenetre,bd = 2, relief = 'groove')
    frmHeader = Frame (fenetre)
    frmBody = Frame (fenetre)
    frmFooter = Frame (fenetre)

    #Header :
    logo = PhotoImage (file = 'logo.png')
    lLogo = logo.width()
    hLogo = logo.height()
    canLogo = Canvas(frmLogo, width = lLogo, height = hLogo)
    canLogo.create_image(0,0,anchor = 'nw', image = logo)
    canLogo.grid(column = 0, row = 0)
    
    
    resistance_CMS = PhotoImage (file = 'resistance_CMS.png')
    lResistance_CMS = resistance_CMS.width()
    hResistance_CMS = resistance_CMS.height()
    canResistance_CMS = Canvas(frmHeader, width = lResistance_CMS, height = hResistance_CMS)
    canResistance_CMS.create_image(0,0,anchor = 'nw',image = resistance_CMS)
    canResistance_CMS.grid(column = 0, row = 1)
    
        #Affichage des frames
    frmLogo.grid(column = 0, row = 0)
    frmHeader.grid(column = 0, row = 1)
    frmBody.grid(column = 0, row = 2)
    frmFooter.grid(column=0,row = 3)

    #Variable de calacul de resistance
    valeurResistance.set("A calculer")
    police = ('Helvetica',14,'bold')
    lblValeurResistance = Label(frmHeader,textvariable = valeurResistance, font = police)
    lblValeurResistance.grid(column = 0, row = 2, columnspan = 1)
    
    #EntryBox
    entryResitance = StringVar()
    eSaisi = Entry(frmBody,width = 20, textvariable = entryResitance, justify = 'center')
    eSaisi.grid(column = 0, row = 1)
    
    #Bouton OK
    bntOKresistance = Button(frmBody,text="CALCULER", command = lambda : Decode_resistance_CMS(entryResitance.get()))
    bntOKresistance.grid(column=1,row=1)
    
def Decode_resistance_CMS(codeResistance):
    presenceCaractere = False
    #codeEIA = False
    typeCode = ''
    #liCodeResistance = []
    resistance = 0
    chiffreSignificatif = ''
    exposant = ''
    print(codeResistance)
    
    #Parcours de la chaine pour verifier la precence d un caractere
    for caractere in codeResistance:
        print ('Caractere {}, type : {}'.format(caractere,type(caractere)))
        try :
            caratere = int(caractere)
            print ('apres conversion : {} est : {}'.format(caractere,type(caractere)))
        except:
            print('conversion impossible')
            presenceCaractere = True
 
    #Si presence d un caracter, est ce le R ?     
    if presenceCaractere == True:
        print('Presence lettre')
        codeResistance = codeResistance.upper()
        print (codeResistance)
        if codeResistance.find('R') > -1:
            typeCode = 'codeVirgule'
        else :
            typeCode = 'codeEIA'
        
    #sinon que des entier
    else:
        print ('que des entiers')
        typeCode = 'codeEntier'
        
     ##################################################Code entier#########################
    if typeCode == 'codeEntier' :
        print('##############CODE ENTIER##############')
        i = 0
        
        #Chiffre significatif
        while (i < len(codeResistance)-1):
            print ('chiffre : {}, type : {} , i : {}'.format(codeResistance[i],type(codeResistance[i]),i))
            chiffreSignificatif = chiffreSignificatif + codeResistance[i]
            i = i+1
        print ('chiffre significatifs : ',chiffreSignificatif)
        
        #Exposant
        exposant = codeResistance[len(codeResistance)-1]
        print ('Exposant : ',exposant)

        #Conversion des chiffres significatifs et de l'exposant
        chiffreSignificatif = int (chiffreSignificatif)
        exposant = int (exposant)
        
        #Calcul de la resistance
        resistance = chiffreSignificatif * (10**exposant)
        print('La resistance est de : ', resistance)
        exposant = 10**exposant
        Calcul_resistance(chiffreSignificatif,-1,-1,exposant)
        
        
    ############################################Code Virgule#################################
    if typeCode == 'codeVirgule' :
        print('##############CODE VIRGULE##############')
        i = 0
        codeResistance = codeResistance.upper()
        positionR = codeResistance.find('R')
        codeResistance = codeResistance.replace('R',',')
        if positionR == 0:
         codeResistance = '0'+codeResistance
       
        print ('La resitance est egale a : ',codeResistance)
        Calcul_resistance(1,1,1,1,bypass = codeResistance)





    #######################################Code EIA96#####################################
    if typeCode == 'codeEIA':
        dictEIA = {'01':100,'02':102,'03':105,'04':107,'05':110,'06':113,'07':115,'08':118,'09':121,'10':124,'11':127,'12':130,
                   '13':133,'14':137,'15':140,'16':143,'17':147,'18':150,'19':154,'20':158,'21':162,'22':165,'23':169,'24':174,
                   '25':178,'26':182,'27':187,'28':191,'29':196,'30':200,'31':205,'32':210,'33':215,'34':221,'35':226,'36':232,
                   '37':237,'38':243,'39':249,'40':255,'41':261,'42':267,'43':274,'44':280,'45':287,'46':294,'47':301,'48':309,
                   '49':316,'50':324,'51':332,'52':340,'53':348,'54':357,'55':365,'56':374,'57':383,'58':392,'59':402,'60':412,
                   '61':422,'62':432,'63':442,'64':453,'65':464,'66':475,'67':487,'68':499,'69':511,'70':523,'71':536,'72':549,
                   '73':562,'74':576,'75':590,'76':604,'77':619,'78':634,'79':649,'80':665,'81':681,'82':698,'83':715,'84':732,
                   '85':750,'86':768,'87':787,'88':806,'89':825,'90':845,'91':866,'92':887,'93':909,'94':931,'95':953,'96':976}
        
        dictEIA_exposant = {'Y':-2,'X':-1,'A':0,'B':1,'C':2,'D':3,'E':4,'F':5}
        if len(codeResistance) != 3:
            typeCode = ''
        else :
            #print ('chiffre s : ', codeResistance[0:2])
            chiffreSignificatif = dictEIA[codeResistance[0:2]]
            exposant = dictEIA_exposant[codeResistance[2]]
            exposant = 10**exposant
            print ('Chiffre significatifs : {}, Exposant : {}'.format(chiffreSignificatif,exposant))
            Calcul_resistance(chiffreSignificatif,-1,-1,exposant)

    #####################################Pas de code######################################
    if typeCode == '' :
        print ('pas de code associé')
        Calcul_resistance(1,1,1,1,bypass = '... ')
        showerror('Erreur code','Aucune correspondance de code\nVérifiez la saisie')


def Actualiser_trad (fenetre,nbBande):
    global logo
    global resistance
    
        
    #Effacement de la fenetre
    for element in fenetre.winfo_children():
        if (isinstance(element,Menu)) == True:
            pass
        else:
            element.destroy()

            
    #################################Création des variables Pour les cases à cocher##########################
    #Chiffre significateur
    sign1 = IntVar ()
    sign2 = IntVar ()
    sign3 = IntVar ()
    sign1.set(-1)
    sign2.set(-1)
    sign3.set(-1)

    #Multiplicateur
    multi = DoubleVar ()
    multi.set(1)
    #Tolérance
    tol = IntVar ()
    #Coeff Température
    coef = IntVar ()
    #Valeur de la résistances
    #valeurResistance = StringVar()
    valeurResistance.set("A calculer")

    #Création d'une frame pour le choix du nombre de bande
    #frmNbBande = Frame(frmHeader)
    #frmNbBande.grid(column = 1, row = 1)
    
    
    ###############Création des frames################
    frmLogo = Frame(fenetre,bd = 2, relief = 'groove')
    frmHeader = Frame (fenetre)
    frmBody = Frame (fenetre)
    frmFooter = Frame (fenetre)

    #Header :
    logo = PhotoImage (file = 'logo.png')
    lLogo = logo.width()
    hLogo = logo.height()
    canLogo = Canvas(frmLogo, width = lLogo, height = hLogo)
    canLogo.create_image(0,0,anchor = 'nw', image = logo)
    canLogo.grid(column = 0, row = 0)


    if nbBande == 0 :
        resistance = PhotoImage (file = 'resistance5.png')
    else :
        resistance = PhotoImage (file = 'resistance4.png')
        
    lResistance = resistance.width()
    hResistance = resistance.height()
    canResistance = Canvas(frmHeader, width = lResistance, height = hResistance)
    canResistance.create_image(0,0,anchor = 'nw',image = resistance)
    canResistance.grid(column = 0, row = 1)

    #Affichage des frames
    frmLogo.grid(column=0,row=0)
    frmHeader.grid(column = 0, row = 1)
    frmBody.grid(column = 0, row = 2)
    frmFooter.grid(column=0,row = 3)


    #################Création des cases à cocher############################
    ###Chiffre significatif###
    #1er
    chkbSign0_0 = Radiobutton(frmBody, variable = sign1, value = 0 , text = '0',bg = 'black', fg = 'white',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign1_0 = Radiobutton(frmBody, variable = sign1, value = 1, text = '1',bg = 'brown',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign2_0 = Radiobutton(frmBody, variable = sign1, value = 2, text = '2',bg = 'red',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign3_0 = Radiobutton(frmBody, variable = sign1, value = 3, text = '3',bg = 'orange',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign4_0 = Radiobutton(frmBody, variable = sign1, value = 4, text = '4',bg = 'yellow',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign5_0 = Radiobutton(frmBody, variable = sign1, value = 5, text = '5',bg = 'green',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign6_0 = Radiobutton(frmBody, variable = sign1, value = 6, text = '6',bg = 'SkyBlue1', fg = 'black',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign7_0 = Radiobutton(frmBody, variable = sign1, value = 7, text = '7',bg = 'purple',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign8_0 = Radiobutton(frmBody, variable = sign1, value = 8, text = '8',bg = 'grey',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign9_0 = Radiobutton(frmBody, variable = sign1, value = 9, text = '9',bg = 'white',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    #2eme
    chkbSign0_1 = Radiobutton(frmBody, variable = sign2, value = 0, text = '0',bg = 'black', fg = 'white',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign1_1 = Radiobutton(frmBody, variable = sign2, value = 1, text = '1',bg = 'brown',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign2_1 = Radiobutton(frmBody, variable = sign2, value = 2, text = '2',bg = 'red',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign3_1 = Radiobutton(frmBody, variable = sign2, value = 3, text = '3',bg = 'orange',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign4_1 = Radiobutton(frmBody, variable = sign2, value = 4, text = '4',bg = 'yellow',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign5_1 = Radiobutton(frmBody, variable = sign2, value = 5, text = '5',bg = 'green',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign6_1 = Radiobutton(frmBody, variable = sign2, value = 6, text = '6',bg = 'SkyBlue1', fg = 'black',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign7_1 = Radiobutton(frmBody, variable = sign2, value = 7, text = '7',bg = 'purple',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign8_1 = Radiobutton(frmBody, variable = sign2, value = 8, text = '8',bg = 'grey',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign9_1 = Radiobutton(frmBody, variable = sign2, value = 9, text = '9',bg = 'white',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    #3eme
    chkbSign0_2 = Radiobutton(frmBody, variable = sign3, value = 0, text = '0',bg = 'black', fg = 'white',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign1_2 = Radiobutton(frmBody, variable = sign3, value = 1, text = '1',bg = 'brown',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign2_2 = Radiobutton(frmBody, variable = sign3, value = 2, text = '2',bg = 'red',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign3_2 = Radiobutton(frmBody, variable = sign3, value = 3, text = '3',bg = 'orange',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign4_2 = Radiobutton(frmBody, variable = sign3, value = 4, text = '4',bg = 'yellow',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign5_2 = Radiobutton(frmBody, variable = sign3, value = 5, text = '5',bg = 'green',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign6_2 = Radiobutton(frmBody, variable = sign3, value = 6, text = '6',bg = 'SkyBlue1', fg = 'black',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign7_2 = Radiobutton(frmBody, variable = sign3, value = 7, text = '7',bg = 'purple',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign8_2 = Radiobutton(frmBody, variable = sign3, value = 8, text = '8',bg = 'grey',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbSign9_2 = Radiobutton(frmBody, variable = sign3, value = 9, text = '9',bg = 'white',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))

    #####Multiplicateur######
    chkbMulti0= Radiobutton(frmBody, variable = multi, value = 0.01, text = 'X0.01',bg = 'silver',width = 5,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()) )
    chkbMulti1= Radiobutton(frmBody, variable = multi, value = 0.1, text = 'X0.1',bg = 'gold',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti2= Radiobutton(frmBody, variable = multi, value = 10, text = 'X10',bg = 'brown',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti3= Radiobutton(frmBody, variable = multi, value = 100, text = 'X100',bg = 'red',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti4= Radiobutton(frmBody, variable = multi, value = 1000, text = 'X1k',bg = 'orange',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti5= Radiobutton(frmBody, variable = multi, value = 10000, text = 'X10k',bg = 'yellow',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti6= Radiobutton(frmBody, variable = multi, value = 100000, text = 'X100k',bg = 'green',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti7= Radiobutton(frmBody, variable = multi, value = 1000000, text = 'X1M',bg = 'SkyBlue1',fg = 'black',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbMulti8= Radiobutton(frmBody, variable = multi, value = 10000000, text = 'X10',bg = 'purple',width = 5,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))

    ###########Tolérance############
    chkbTol0 = Radiobutton(frmBody, variable = tol, value = 10, text = '+/-10%', bg = 'silver',width = 8,anchor = 'w' ,command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbTol1 = Radiobutton(frmBody, variable = tol, value = 5, text = '+/-5%', bg = 'gold',width = 8,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbTol2 = Radiobutton(frmBody, variable = tol, value = 1, text = '+/-1%', bg = 'brown',width = 8,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbTol3 = Radiobutton(frmBody, variable = tol, value = 2, text = '+/-2%', bg = 'red',width = 8,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbTol4 = Radiobutton(frmBody, variable = tol, value = 0.5, text = '+/-0.5%', bg = 'green',width = 8,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbTol5 = Radiobutton(frmBody, variable = tol, value = 0.25, text = '+/-0.25%', bg = 'SkyBlue1',fg = 'black',width = 8,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbTol6 = Radiobutton(frmBody, variable = tol, value = 0.1, text = '+/-0.1%', bg = 'purple',width = 8,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))

    #Coeff
    chkbCoef0 = Radiobutton(frmBody, variable = coef, value = 200, text = "200 ppm", bg = 'black',fg = 'white',width = 7,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbCoef1 = Radiobutton(frmBody, variable = coef, value = 100, text = "100 ppm", bg = 'brown',width = 7,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbCoef2 = Radiobutton(frmBody, variable = coef, value = 50, text = "50 ppm", bg = 'red',width = 7,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbCoef3 = Radiobutton(frmBody, variable = coef, value = 15, text = "15 ppm", bg = 'orange',width = 7,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))
    chkbCoef4 = Radiobutton(frmBody, variable = coef, value = 25, text = "25 ppm", bg = 'yellow',width = 7,anchor = 'w',command = lambda : Calcul_resistance (sign1.get(),sign2.get(),sign3.get(),multi.get()))

    #choix nombre de bandes
    #chkbNbBande0 = Radiobutton (frmNbBande, variable = nbBande,value = 4, text = '4 Bandes', command = lambda : InversionBool(nbBande.get(),resistance5Anneaux))
    #chkbNbBande1 = Radiobutton (frmNbBande, variable = nbBande,value = 5, text = '5/6 Bandes', command = lambda : InversionBool(nbBande.get(),resistance5Anneaux))

    ###########Création du Label###########
    police = ('Helvetica',14,'bold')
    lblValeur = Label(frmHeader,textvariable = valeurResistance, font = police)
    lblValeur.grid(column = 0, row = 2)


    ##########################Placement des checkbox

    #Variable de placement
    colSign = 0
    rowSign = 5
    colMulti = 2
    rowMulti = 3
    colTol = 3
    rowTol = 3
    colCoef = 5
    rowCoef = 5
    spanResistance = 4
    spanLogo = 4



    if nbBande == 0 :
        #Debug
        spanLogo = 6
        spanResistance = 6
        colMulti = 3
        colTol = 4


    #####Chiffres significatif###
    #1er
    chkbSign0_0.grid(column = colSign,row = 2)
    chkbSign1_0.grid(column = colSign,row = 3)
    chkbSign2_0.grid(column = colSign,row = 4)
    chkbSign3_0.grid(column = colSign,row = 5)
    chkbSign4_0.grid(column = colSign,row = 6)
    chkbSign5_0.grid(column = colSign,row = 7)
    chkbSign6_0.grid(column = colSign,row = 8)
    chkbSign7_0.grid(column = colSign,row = 9)
    chkbSign8_0.grid(column = colSign,row = 10)
    chkbSign9_0.grid(column = colSign,row = 11)
    #2eme
    chkbSign0_1.grid(column = colSign + 1,row = 2)
    chkbSign1_1.grid(column = colSign + 1,row = 3)
    chkbSign2_1.grid(column = colSign + 1,row = 4)
    chkbSign3_1.grid(column = colSign + 1,row = 5)
    chkbSign4_1.grid(column = colSign + 1,row = 6)
    chkbSign5_1.grid(column = colSign + 1,row = 7)
    chkbSign6_1.grid(column = colSign + 1,row = 8)
    chkbSign7_1.grid(column = colSign + 1,row = 9)
    chkbSign8_1.grid(column = colSign + 1,row = 10)
    chkbSign9_1.grid(column = colSign + 1,row = 11)
    #3eme
    if nbBande == 0 :
        chkbSign0_2.grid(column = colSign + 2,row = 2)
        chkbSign1_2.grid(column = colSign + 2,row = 3)
        chkbSign2_2.grid(column = colSign + 2,row = 4)
        chkbSign3_2.grid(column = colSign + 2,row = 5)
        chkbSign4_2.grid(column = colSign + 2,row = 6)
        chkbSign5_2.grid(column = colSign + 2,row = 7)
        chkbSign6_2.grid(column = colSign + 2,row = 8)
        chkbSign7_2.grid(column = colSign + 2,row = 9)
        chkbSign8_2.grid(column = colSign + 2,row = 10)
        chkbSign9_2.grid(column = colSign + 2,row = 11)

    ##Multiplicateur
    chkbMulti0.grid(column = colMulti, row = 0)
    chkbMulti1.grid(column = colMulti, row = 1)
    chkbMulti2.grid(column = colMulti, row = 3)
    chkbMulti3.grid(column = colMulti, row = 4)
    chkbMulti4.grid(column = colMulti, row = 5)
    chkbMulti5.grid(column = colMulti, row = 6)
    chkbMulti6.grid(column = colMulti, row = 7)
    chkbMulti7.grid(column = colMulti, row = 8)
    chkbMulti8.grid(column = colMulti, row = 9)

    ##Tolérance##
    chkbTol0.grid (column = colTol, row = 0)
    chkbTol1.grid (column = colTol, row = 1)
    chkbTol2.grid (column = colTol, row = 3)
    chkbTol3.grid (column = colTol, row = 4)
    chkbTol4.grid (column = colTol, row = 7)
    chkbTol5.grid (column = colTol, row = 8)
    chkbTol6.grid (column = colTol, row = 9)
    #Coeff
    if nbBande == 0 :
        chkbCoef0.grid (column = colCoef, row = 2)
        chkbCoef1.grid (column = colCoef, row = 3)
        chkbCoef2.grid (column = colCoef, row = 4)
        chkbCoef3.grid (column = colCoef, row = 5)
        chkbCoef4.grid (column = colCoef, row = 6)
            
        
        
        
        
##########################################################################################
fenetre = Tk()
#fenetre.geometry("805x400")
fenetre.title("ElectroLaud")
fenetre.iconbitmap('icone.ico')
nbBande = IntVar()
nbBande.set(0)

#Variable pour la valeur de la résistances:
valeurResistance = StringVar()
#Image (fenetre,nbBande)
Menu_app(nbBande,fenetre)
Actualiser_trad (fenetre,nbBande)
fenetre.mainloop()