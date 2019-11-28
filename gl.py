
import sys
import os
import os.path
import shutil


def Resume(Content):
    if "ABSTRACT" in Content :                                      # identifier le début du résumé
        debut = Content.split("ABSTRACT",1)

    if "Abstract" in Content :
        debut = Content.split("Abstract",1)

    fin="1"
    if "Keywords" in Content :                                      # identifier la fin du résumé
        fin="Keywords"

    elif "Index" in Content :
        fin="Index"
    try:
        debut
    except NameError:
        return "erreur"
    else:
        a1 = debut[1].split(fin)
        a2 = a1[0].split("\n")
        a = ''.join(a2)
        return a

def Auteur(Content,titre):
	titre2 = titre.split("Abstract",1)
	return titre2[0]

def Titre(Content):
    title = Content.split("\n",1)
    titre = title[0]
    return titre

def Titre2(Content):
	title = Content.split("\n",1)
	titre = title[1]
	return titre




def filtre(src,dst,element):
    #******nom du fichier d’origine******
        print(element)
        titre = element.replace('.txt','').replace('_',' ')
        dst.write("Nom du fichier d’origine : "+titre+"\n")
        txt = src.read()
        titre2 = titre
    #******Titre******
        for i in range(2000,2019) :
            if str(i) in titre :
                annee = str(i)
        try:
            annee
        except NameError:
            dst.write("titre not found")
        else:
            titre2 = titre.split(annee)[1]
        if "Rouge" in titre :
            titre1 = txt.split("ROUGE:")
            titre2 = titre1[1].split("\n")[0]
            dst.write("\n\n\nTitre du papier : "+  titre2 + "\n")
        elif "naive bayes" in titre:
            titre1 = txt.split("\n")
            titre2 = titre1[0]
            dst.write("\n\n\nTitre du papier  : "+  titre2 + "\n")
        else:
        	title = txt.split("\n",1)
        	dst.write("\n\n\nTitre du papier  : "+  title[0] + "\n")
    # on ecrit le titre du pdf dans le fichier de destination (deuxieme ligne)
    #******Résumé******   lecture du fichier dans une variable string
        a2 = Resume(txt)
        dst.write("\n\n\nAbstract de l’auteur : ")
        for i in range(0,len(a2)) :  # ecriture du résumé dans le fichier de destination sur une seule ligne (troisieme ligne)
            dst.write(a2[i])


def transfertToResult(arg):
    tmp = "{}/result".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    t = "{}/tmp".format(arg)
    for element in os.listdir(t):
        if element.endswith('.txt'):
            a = "{0}/result/".format(arg)
            s = "{0}/tmp/".format(arg)
            source = open(s+element,"r")
            destination = open(a+element, "w")
            filtre(source,destination,element)
            source.close()
            destination.close()


def pdf(directoryPath):


    tmp = "{}/tmp".format(directoryPath)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)

    # Créer un dossier temporaire à l'intérieur du dossier passé en paramètres
    os.mkdir(tmp)

    # Pour chaque fichier pdf ( se terminant par .pdf)
    for fileName in os.listdir(directoryPath):
        if fileName.endswith('.pdf'):

            fileNameWithouExt = os.path.splitext(fileName)[0]
            # Créer un nom de fichier qui est le même que le fichier pdf
            # en remplacent les espace par des underscore
            newFileName = fileName.replace(' ','_')

            # renommer le fichier
            os.rename("{0}/{1}".format(directoryPath,fileName), "{0}/{1}".format(directoryPath,newFileName))
            # créer la commande qui permet de faire la conversion
            pdfToTextCommand = "pdf2txt {1}/{2} >{1}/tmp/{3}.txt".format(os.getcwd(),directoryPath, newFileName, fileNameWithouExt)
            # Executer la commande de conversion
            os.system(pdfToTextCommand)





print("*       PDF CONVERTER        *")
# S'assurer que notre programme reçois le bon nombre d'argument
# le premier argument est le nom de notre script python
# le deuxième argument est le répértoire content l'ensemble des fichiers pdf à convertir.
# le troisiéme argument est pour choisir le type de sortie soit txt

if len(sys.argv) == 3:
 # Récupérer le répértoire courant ( cwd : current working directory )
 current = os.getcwd()
 directory = sys.argv[1]

 # Terminer le programme si l'argument passé en paramètre n'existe pas
 if not os.path.exists(directory):
     print(bcolors.FAIL + "L'argument passé en paramètre n'existe pas." + bcolors.ENDC)
     sys.exit(2)

 # Terminer le programme si le l'argument passé en n'est pas un dossier
 if not os.path.isdir(directory):
     print(bcolors.FAIL + "L'argument passé en paramètre n'est pas un dossier." + bcolors.ENDC)
     sys.exit(2)
 # Verifier si le type de sortie est égale a txt
 if sys.argv[2] == '-text':
     # Début de la conversion
     print("Conversion pdf to txt")
     print ("Conversion des fichier du répértoire " + directory)
     pdf(directory)
     transfertToResult(directory)
     t = "{}/tmp".format(directory)
