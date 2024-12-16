print('Il programma prevede un file di istruzioni, uno di input e uno di output, importanti per l\'esecuzione del programma.')

from os import chdir as cd

#scelta path cartella
try:
    cd('C:\\Users\\user\\Desktop\\robot2_v6')
except FileNotFoundError:
    try:
        print('Il percorso del file di input non esiste, prova a inserirlo manualmente.')
        path=input('Percorso del file di input: ')
        cd(path)
    except FileNotFoundError:
        print('Il percorso inserito non è corretto.')
        esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
        exit()    

#input
try:
    with open('input robot2 v6.txt', 'r') as file:
        lista=file.read()
        lista=lista.replace('[','').replace(']','').replace('.','').replace('(','').replace(')','').replace(' ','')
        listac=lista.split(',')
except FileNotFoundError:
    print('Il file di input non esiste. Ricontrollare il percorso o il nome del file.')
    esci=input('Sviluppato da Baelish03.\nPremere Invio per uscire. ')
    exit()

#trasforma in interi
lista_coor=[]
try:
    for elem in listac:
        lista_coor.append(int(elem))
except ValueError:
    print('Nelle coordinate di input bisogna inserire numeri interi.')
    exit()

#output su txt e sistemazione
def esci():
    #rimuove f=1
    for i in range(lc.count('1')):
        lc.remove('1')
    #non separare f dal numero intero
    try:
        for j in range(lc.count('f')):
            k=lc.index('f')
            #str(int(, perchè se non c'è un intero va in errore
            lc[k]=lc[k]+str(int(lc[k+1]))
            lc.remove(lc[k+1])
    except ValueError:
        pass
    #nessuna gestione degli errori. il file di output viene creato automaticamente
    with open('output robot2 v6.txt', 'w') as file2:
        str_output=str(lc)
        str_output=str_output.replace("'","").replace("[","").replace("]","").replace(" ","")
        file2.write(str_output)
        print(str_output)
        esci=input('Il risultato è riportato anche nel file di output, da dove è più comodo copiarlo. \nSviluppato da Baelish03. Premere Invio per uscire. ')
    exit()




di=str(input('''
Direzione iniziale, digitare n/N per nord/alto,
                             s/S per sud/basso,
                             e/E per est/destra,
                             w/W per ovest/sinistra: '''))
while di!='n' and di!='N' and di!='s' and di!='S' and di!='e' and di!='E' and di!='w' and di!='W':
    print('Input non valido, ripetere inserimento.')
    di=str(input('Direzione iniziale (n/N,s/S,e/E,w/W): '))


if di.isupper()==True:
    di=di.lower()



#di volta in volta devo memorizzare i valori del punto strettamente precedente e chiamare in funzione quelli attuali

lc=[]
try:
    xprec=lista_coor[0]
    yprec=lista_coor[1]
except IndexError:
    print('Il file di input è vuoto.')
    esci=input('Sviluppato da Baelish03.\nPremere Invio per uscire. ')
    exit()
dprec=di

try:
    for r in range(1,int(len(lista_coor)/2)):
        xatt=lista_coor[2*r]
        yatt=lista_coor[2*r+1]

        if xatt>xprec:
            datt='e'
            if dprec=='n':
                lc=lc+['o','f',str(xatt-xprec)]
            if dprec=='s':
                lc=lc+['a','f',str(xatt-xprec)]
            if dprec=='e':
                lc=lc+['f',str(xatt-xprec)]
            if dprec=='w':
                lc=lc+['a','a','f',str(xatt-xprec)]

        if xatt<xprec:
            datt='w'
            if dprec=='n':
                lc=lc+['o','f',str(abs(xatt-xprec))]
            if dprec=='s':
                lc=lc+['a','f',str(abs(xatt-xprec))]
            if dprec=='e':
                lc=lc+['a','a','f',str(abs(xatt-xprec))]
            if dprec=='w':
                lc=lc+['f',str(abs(xatt-xprec))]

        if yatt>yprec:
            datt='n'
            if dprec=='n':
                lc=lc+['f',str(yatt-yprec)]
            if dprec=='s':
                lc=lc+['a','a','f',str(yatt-yprec)]
            if dprec=='e':
                lc=lc+['a','f',str(yatt-yprec)]
            if dprec=='w':
                lc=lc+['o','f',str(yatt-yprec)]

        if yatt<yprec:
            datt='s'
            if dprec=='n':
                lc=lc+['a','a','f',str(abs(yatt-yprec))]
            if dprec=='s':
                lc=lc+['f',str(abs(yatt-yprec))]
            if dprec=='e':
                lc=lc+['o','f',str(abs(yatt-yprec))]
            if dprec=='w':
                lc=lc+['a','f',str(abs(yatt-yprec))]
                
        dprec=datt
        xprec=xatt
        yprec=yatt
        
except TypeError:
    print('L\'input è incompleto: ogni punto dovrebbe avere un\'ascissa ed un\'ordinata.')
    esci=input('Sviluppato da Baelish03\nPremere Invio per uscire ')
    exit()  
    

#direzione finale, se c'è
df=str(input('''
Direzione finale, digitare n/N per nord/alto,
                           s/S per sud/basso,
                           e/E per est/destra,
                           w/W per ovest/sinistra,
                   premere Invio se l\'esercizio non la fornisce: '''))
while df!='n' and df!='N' and df!='s' and df!='S' and df!='e' and df!='E' and df!='w' and df!='W' and df!='':
    print('Input non valido, ripetere inserimento.')
    di=str(input('Direzione finale (n/N,s/S,e/E,w/W,Invio): '))

if df.isupper()==True:
    df=df.lower()
if df=='':
    esci()


if df=='e':
    if datt=='n':
        lc.append('o')
    if datt=='s':
        lc.append('a')
    if d20=='<':
        lc.append('a')
        lc.append('a')

if df=='w':
    if datt=='n':
        lc.append('a')
    if datt=='s':
        lc.append('o')
    if datt=='e':
        lc.append('a')
        lc.append('a')

if df=='n':
    if datt=='s':
        lc.append('a')
        lc.append('a')
    if datt=='e':
        lc.append('a')
    if datt=='w':
        lc.append('o')

if df=='s':
    if datt=='n':
        lc.append('a')
        lc.append('a')
    if datt=='e':
        lc.append('o')
    if datt=='w':
        lc.append('a')

#una volta finito il for i punti sono sicuramente finiti, perciò non serve creare un'eccezione di IndexError
esci()

#sviluppato da Emanuele Urso il 9/8/2020
#numero di passi, relativo alle 'f' aggiunto il 16/8/2020
#try+except agli input aggiunto il 19/08/2020
#input esterno il 2/8/2020
#rivoluzionato il 26/2/2023
