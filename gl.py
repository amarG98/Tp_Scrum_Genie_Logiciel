import sys      #argument
import os       #commande de base
import os.path  #le path du program
import shutil   #pour suprimmer récursivement
import xml.etree.ElementTree as xmlElement #XML
from lxml import etree #XML

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
 # identifier l'auteur
def Auteur(Content,titre):
	titre2 = titre.split("Abstract",1)
	return titre2[0]
 # identifier les titres
def Titre(Content):
    title = Content.split("\n",1)
    titre = title[0]
    return titre

def Titre2(Content):
	title = Content.split("\n",1)
	titre = title[1]
	return titre
     # identifier la bib

def Bibliographie(normalContent):
    lowerContent = normalContent.lower()
    if " references" in lowerContent:
        indexFound = lowerContent.find("\nreferences\n")
    else:
        indexFound = lowerContent.find("references\n")
    if indexFound == -1 :
        return "bibliography not found"
    indexFound += len("references\n")
    normalContent = normalContent[indexFound:]
    indexFound = normalContent.find("\n\n");
    if indexFound == -1 :
        return "bibliography not found"

    if "[1]" in normalContent:
        contentOnLine = normalContent.replace(".\n","  ;  ").replace("\n"," ")
        contentOnLine = contentOnLine.replace(";", "\n")
        return contentOnLine
    elif "(2013)" in normalContent:
        normalContent = normalContent.replace("\n"," ")
        for i in range(1900,2020):
            if str(i) in normalContent:
                a = "("+str(i)+")"
                b = "("+str(i)+")\n"

                normalContent = normalContent.replace(a, b)
        return normalContent
    else:
        normalContent = normalContent.replace("\n"," ")
        for i in range(1900,2020):
            if str(i) in normalContent:
                a = str(i)+"."
                b = str(i)+".\n"


                normalContent = normalContent.replace(a, b)
        return normalContent
     # identifier l'introduction'

def Intro(Content):
	if "Introduction" in Content :
		debut = Content.split("Introduction\n",1)
		if "Mikolov" in Content:
			fin = "2 "
		else:
			fin = "2\n"
		a=debut[1].split(fin)
		a1=a[0]
		a = ''.join(a1)

		return a

	elif "INTRODUCTION" :
		debut = Content.split("INTRODUCTION\n",1)
		if "Naive" in Content:
			fin = "2."
		else :
			fin = "2\n"
		a=debut[1].split(fin)
		a1=a[0]
		a = ''.join(a1)

		return a

     # identifier la conclusion

def Conclusion(Content):
	if "Conclusion" in Content:
		debut = Content.split("Conclusion",1)
		if "Acknowledgments" in Content:
			fin= "Acknowledgments"
		elif "Acknowledgements" in Content:
			fin= "Acknowledgements"
		else:
			fin= "References\n"

		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a
	elif "CONCLUSION" :

		debut = Content.split("CONCLUSION",1)
		if "ACKNOWLEDGMENT" in Content:
			fin= "ACKNOWLEDGMENT"
		else:
			fin= "REFERENCES\n"

		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a
	else:
		return " "
     # identifier le corp

def Corpse(Content):
	if "Introduction" in Content:
		debut = Content.split("Introduction",1)

		if "Acknowledgments" in Content:
			fin = "Acknowledgments"
		else:
			fin = "References"
		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a
	elif "INTRODUCTION" in Content:
		debut = Content.split("INTRODUCTION",1)
		if "Acknowledgments" in Content:
			fin = "Acknowledgments"
		else:
			fin = "References"
		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a

     # identifier la disccussion

def Discuss(Content):
	if "Acknowledgments" in Content:
		debut = Content.split("Acknowledgments",1)
		fin="References"
		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a
	elif "Acknowledgements" in Content:
		debut = Content.split("Acknowledgements",1)
		fin="References"
		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a
	elif "ACKNOWLEDGMENT" in Content:
		debut = Content.split("ACKNOWLEDGMENT",1)
		fin="REFERENCES"
		a = debut[1].split(fin)
		a1 = a[0].split("\n")
		a = ''.join(a1)
		return a
	else :
		return " "



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
            dst.write("")
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
            #----------Auteurs------------

        dst.write("\n"+"Auteur : "+Auteur(txt,titre2))

        a2 = Resume(txt)
        dst.write("\n\n\nAbstract de l’auteur : ")
        for i in range(0,len(a2)) :  # ecriture du résumé dans le fichier de destination sur une seule ligne (troisieme ligne)
            dst.write(a2[i])

        #---------Intro--------------
        dst.write("\n"+"Introduction : "+Intro(txt))
        #---------Corps--------------
        dst.write("\n"+"Corps : "+Corpse(txt))
        #---------Conclusion--------------
        dst.write("\n"+"Conclusion : "+Conclusion(txt))
        #---------Discussion--------------
        dst.write("\n"+"Discussion : "+Discuss(txt))
        #----------Biblio-------------

        dst.write("\n"+"Biblio : "+Bibliographie(txt))
 # transfert vers le result

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
            pdfToTextCommand = "pdftotext {1}/{2} {1}/tmp/{3}.txt".format(os.getcwd(),directoryPath, newFileName, fileNameWithouExt)
            # Executer la commande de conversion
            os.system(pdfToTextCommand)


def createXmlFile(src,dst,title,rwt):

    filename = dst+rwt+".xml"
    titre = title.replace('.txt','').replace('_',' ')
    txt = src.read()

    root = xmlElement.Element("article")

    element0 = xmlElement.SubElement(root,"preamble").text = titre

    element1 = xmlElement.SubElement(root,"titre").text = Titre(txt)

    element2 = xmlElement.SubElement(root,"auteur").text = Auteur(txt, Titre2(txt))

    element3 = xmlElement.SubElement(root,"abstract").text = Resume(txt)

    element4 = xmlElement.SubElement(root,"introduction").text = Intro(txt)

    element5 = xmlElement.SubElement(root,"corps").text = Corpse(txt)

    element6 = xmlElement.SubElement(root,"conclusion").text = Conclusion(txt)

    element7 = xmlElement.SubElement(root,"discussion").text = Discuss(txt)

    element8 = xmlElement.SubElement(root,"biblio").text = Bibliographie(txt)


    tree= xmlElement.ElementTree(root)
    tree.write(filename)

def createFichierXml(arg) :
    tmp = "{}/result".format(arg)
    if os.path.exists(tmp):
        shutil.rmtree(tmp)
    os.mkdir(tmp)
    t = "{}/tmp".format(arg)
    for element in os.listdir(t):
        if element.endswith('.txt'):
            rwt = os.path.splitext(os.path.basename(element))[0]
            a = "{0}/result/".format(arg)
            s = "{0}/tmp/".format(arg)
            source = open(s+element,"r")
            createXmlFile(source,a,element,rwt)
            source.close()


print("*       PDF CONVERTER        *")
# S'assurer que notre programme reçois le bon nombre d'argument
# le premier argument est le nom de notre script python
# le deuxième argument est le répértoire content l'ensemble des fichiers pdf à convertir.
# le troisiéme argument est pour choisir le type de sortie soit txt soit XML

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
 if sys.argv[2] == '-t':
     # Début de la conversion
     print("Conversion pdf to txt")
     print ("Conversion des fichier du répértoire " + directory)
     pdf(directory)
     transfertToResult(directory)
     t = "{}/tmp".format(directory)
     shutil.rmtree(t)

#si en veux la conversion XML
if sys.argv[2] == '-x':
    # Début de la conversion
    print("Conversion pdf to xml")
    print ("Conversion des fichier du répértoire " + directory)
    pdf(directory)
    createFichierXml(directory)
    t = "{}/tmp".format(directory)
    shutil.rmtree(t)
