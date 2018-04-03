__author__ = 'Crisly'

from Constants import *
from Ant import *
import tkinter  #library in which the GUI development
import random  #Of the random library was imported to build the boxes should be located where the lumps
from tkinter import *

x = 0
y = 0
steps=0


def writeFile(nameAnt, sugarClod, poisonClod, sizeMatrix, wineClod):
    """
    the method write file manager is writing a file and save the data entered in the settings file of the game
    :param nameAnt: name entered in the entry
    :param sugarClod: sugarClod count entered in the entry
    :param poisonClod: poisonClod count entered in the entry
    :param sizeMatrix: large sizeMatrix entered in the entry
    :param wineClod:  wineClod count entered in the entry
    """
    file = open("Settings.txt", "w")

    nameAntInt = "nameAnt" + "," + nameAnt
    nameAntStr = str(nameAntInt)
    file.write(nameAntStr + "\n")

    sugarClodInt = "sugarClod" + "," + sugarClod
    sugarClodStr = str(sugarClodInt)
    file.write(sugarClodStr + "\n")

    poisonClodInt = "poisonClod" + "," + poisonClod
    poisonClodStr = str(poisonClodInt)
    file.write(poisonClodStr + "\n")

    wineClodInt = "wineClod" + "," + wineClod
    wineClodStr = str(wineClodInt)
    file.write(wineClodStr + "\n")

    sizeMatrixInt = "sizeMatrix" + "," + sizeMatrix
    sizeMatrixStr = str(sizeMatrixInt)
    file.write(sizeMatrixStr + "\n")

    file.close()


def display(window):
    """
    shows the main window
    :param window: main window
    """
    window.deiconify()


def hide(window):
    """
    hides the main window
    """
    window.withdraw()


def run(f):
    """
    the main window performs other functions

    """
    window.after(200, f)


def leave(window):
    """
    destroys the main window
    :param window: main window
    """
    window.destroy()


def loadingFile():
    """
    load the file with the last saved data, makes a split method that puts you located in the file lists the position
    as 0 and 1 at position 1 are all values ​​suggar, poison, wine Clod and the size of the matrix, equals the globals
     variables to change the value of the same
    """

    global wineCount
    global poisonCount
    global sugarCount
    global nameAntFile
    global sizeMatrixGlobals
    global antInstance

    file = open("Settings.txt", "r")

    dataLines = file.readlines()

    for line in dataLines:

        info = line.split(",")

        if info[0] == "wineClod":
            wineCount = int(info[1])

        if info[0] == "poisonClod":
            poisonCount = int(info[1])

        if info[0] == "sugarClod":
            sugarCount = int(info[1])

        if info[0] == "sizeMatrix":
            sizeMatrixGlobals = int(info[1])

        if info[0] == "nameAnt":
            nameAntFile = info[1]
            antInstance = Ant(info[1])

    file.close()


def close():
    """
    destroys the main window
    :param window: main window

    """
    window.destroy()


def logWindow():
    """
    creates the window and makes the random matrix, then recognizes the image at each position and places,
    to finally go to the settings window method
    """
    close()
    createWindows()
    recognizeImage()
    windowSettings()


def crearLabel(i, j, name):
    """
    recognizes the image, created for use with photoimage and creates a label at position i = row j = column column called in.
    :param i: row
    :param name: name's image
    """
    global window
    photoAnt = tkinter.PhotoImage(file=name)
    label = tkinter.Label(window, image=photoAnt)
    label.img = photoAnt
    label.grid(row=i, column=j)


def windowSettings():
    """
    Window settings so that you can show
    window.bind_all('<Key>', keypress) helps the program receives keyboard commands
    """
    global window
    window.grid()
    window.resizable(0, 0)
    window.bind_all('<Key>', keypress)
    window.mainloop()


def createWindows():
    """
    creates the window and all windomws label's necessary to show the updated information while playing ant will

    """
    global window
    global antInstance
    variable = ""
    global healthVar
    global levelDrunkVar
    global stateVar

    window = tkinter.Tk()
    window.title("Ant's Game")
    nameLabel = tkinter.Label(window, text="Ant's name: \n"
                                           "" + antInstance.getName(), width=15)

    healthInt = antInstance.getHealthAnt()
    healthString = str(healthInt)
    healthVar = StringVar()
    healthVar.set("Health: "+healthString)
    healthLabel = tkinter.Label(window, textvariable= healthVar, width=13)


    levelDrunkInt = antInstance.getlevelDrunk()
    levelDrunkString = str(levelDrunkInt)
    levelDrunkVar = StringVar()
    levelDrunkVar.set("Level Drunk: "+levelDrunkString)
    levelDrunkLabel = tkinter.Label(window, textvariable= levelDrunkVar, width=13)



    stateVar = StringVar()
    estado= antInstance.getstate()
    stateVar.set("Status: "+ estado)
    statusLabel = tkinter.Label(window, textvariable=stateVar, width=13)




    nameLabel.grid(row=0, column=0)
    healthLabel.grid(row=2, column=0)
    levelDrunkLabel.grid(row=3, column=0)
    statusLabel.grid(row=4, column=0)


def informationSettings():
    """
creates the menu cascade settings with the respective labels for the information in the entry, both are located
in columns and respective rows to avoid Confucianism, written on the size of the matrix information should be greater
than 7 if less not generates eventOnclick who is set to take the text and send write

    """

    global entryName, entrySizeMatrix, entryPoisonClod, entryWineClod, entrySugarClod, window, settings, \
        sizeMatrixGlobals, poisonCount
    global nameAntFile

    import tkinter

    createWindows()

    menubar = tkinter.Menu(window)
    filemenu = tkinter.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Settings", command=lambda: run(display(settings)) or run(hide(window)))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)

    menubar.add_cascade(label="Game", menu=filemenu)

    settings = tkinter.Tk()

    settings.title("Settings")
    settings.geometry("300x350+500+500")
    settings.withdraw()
    settings.resizable(0, 0)

    v = tkinter.IntVar()

    # Labels
    label = tkinter.Label(settings, text="Size of the gird")

    name = tkinter.Label(settings, text="Entry ant's name")
    sugarClod = tkinter.Label(settings, text="Sugar Clod")
    wineClod = tkinter.Label(settings, text=" Wine Clod")
    poisonClod = tkinter.Label(settings, text="Poison Clod")
    sizeMatrix = tkinter.Label(settings, text="Size Matrix")

    #text box empty

    entryName = tkinter.Entry(settings)
    entryName.insert(0, nameAntFile)

    entrySugarClod = tkinter.Entry(settings)
    entrySugarClod.insert(0, sugarCount)

    entryWineClod = tkinter.Entry(settings)
    entryWineClod.insert(0, wineCount)

    entryPoisonClod = tkinter.Entry(settings)
    entryPoisonClod.insert(0, poisonCount)

    entrySizeMatrix = tkinter.Entry(settings)
    entrySizeMatrix.insert(0, sizeMatrixGlobals)


    #location label

    label.grid(row=0, column=1)
    name.grid(row=5, column=1)
    sugarClod.grid(row=7, column=1)
    wineClod.grid(row=9, column=1)
    poisonClod.grid(row=11, column=1)
    sizeMatrix.grid(row=13, column=1)



    #location the text box

    entrySugarClod.grid(row=7, column=2)
    entryWineClod.grid(row=9, column=2)
    entryPoisonClod.grid(row=11, column=2)
    entrySizeMatrix.grid(row=13, column=2)
    entryName.grid(row=5, column=2)


    #Buttons to accept that is to be playing after save to return to prinpal window, this also cancels the one
    # which does nothing and returns to the main window is created


    accept = tkinter.Button(settings, text="Accept", width=11, background="brown", command=lambda: run(display(window))
    or run(hide(settings)))

    save = tkinter.Button(settings, text="Save", width=11, command=saveOnclick, background="brown")

    cancel = tkinter.Button(settings, text="Cancel", width=11, background="brown", command=lambda: run(display(window))
    or run(hide(settings)))


    #location botton
    accept.grid(row=15, column=1)
    cancel.grid(row=15, column=2)
    save.grid(row=16, column=1)

    window.config(menu=menubar)


def saveOnclick():
    """
onclick method in the data entered in the entry through getEntryName are captured and verifies that the array size is
correct to write the file with the new data entered, if you can not write less value to 7 then notify you to re-enter a
number on the entrySizeMatrix

    """
    global menssage, menssage1
    import tkinter


    nameAnt = entryName.get()
    sizeMatrix = entrySizeMatrix.get()
    poisonClod = entryPoisonClod.get()
    sugarClod = entrySugarClod.get()
    wineClod = entryWineClod.get()

    sizeMatrixInt = int(sizeMatrix)
    validacion = False

    if sizeMatrixInt < 7:
        menssage = tkinter.Label(settings, text="Enter the size of the largest array back to 7", justify="right")
        menssage.config(bg='pink', font=('times', 9, 'italic'))
        menssage.grid(row=19, column=1)
        validacion = True


    elif sizeMatrixInt >= 7:
        if validacion == True:
            writeFile(nameAnt, sugarClod, poisonClod, sizeMatrix, wineClod)
            menssage.destroy()
            menssage1 = tkinter.Label(settings, text="correct Information", justify="right")
            menssage1.config(bg='pink', font=('times', 9, 'italic'))
            menssage1.grid(row=19, column=1)
        else:
            writeFile(nameAnt, sugarClod, poisonClod, sizeMatrix, wineClod)
            menssage1 = tkinter.Label(settings, text="correct Information", justify="right")
            menssage1.config(bg='pink', font=('times', 9, 'italic'))
            menssage1.grid(row=19, column=1)





def updateMatrixUI():
    """
    Method who updates the last and actual position in the UI Matrix
    """
    global antInstance

    #Get the last and actual position
    travel = antInstance.getTravel()
    actual = travel[len(travel) - 1]
    anterior = travel[len(travel) - 2]

    #refresh the last position with the traveled image
    crearLabel(anterior[0], anterior[1] + 1, "travel.gif")

    #select the image for the actual position
    fotoName = "Hormiga.gif"
    if Matrix[actual[0]][actual[1]] == 5:
        fotoName = "ClodSuggar.gif"
    if Matrix[actual[0]][actual[1]] == 6:
        fotoName = "ClodWine.gif"
    if Matrix[actual[0]][actual[1]] == 7:
        fotoName = "ClodPoison.gif"

    #refresh the actual position with the selected image
    crearLabel(actual[0], actual[1] + 1, fotoName)

    #set the ant's id in the logical matrix
    Matrix[actual[0]][actual[1]] = 1


def recognizeImage():
    """
traverses the array checking the number that exists in each of her and placed the image, if there were no pink remains
 in number, note that to advance one frame will be put light blue marking the route

    """
    #global sizeMatrixGlobals
    i = 0
    while i < len(Matrix):
        j = 0
        while j < len(Matrix[i]):
            fotoName = ""
            if Matrix[i][j] == 1:
                fotoName = "Hormiga.gif"
            elif Matrix[i][j] == 2:
                fotoName = "ANTHIll.gif"
            else:
                fotoName = "roseBox.gif"

            crearLabel(i, j + 1, fotoName)
            j += 1
        i += 1


def startFinallyMatrix():
    """
    defines the default start position and end position in the last 0

    """
    Matrix[0][0] = ANT
    Matrix[len(Matrix) - 1][len(Matrix) - 1] = ANTHILL


def calcRandom(idClod, countClod):
    """
    makes a random number of times that brings countClod and updates the array, this will continue
    while updateMatrix == True

    :param idClod: number for description Ant
    :param countClod: amount of the user clod Stand
    """
    i = 0
    while i < countClod:

        line = random.randint(0, len(Matrix) - 1)
        column = random.randint(0, len(Matrix) - 1)
        if updateMatrix(idClod, line, column) == True:
            i += 1


def updateMatrix(idClod, line, column):
    """
verifies that the initial and final position are not occupied, if you are looking for but returns False and the the
line and column position in the matrix and places the cold returning True to the number of times they appear in the
 matrix cold

    :param idClod: id the cold to be placed in the position found by the random
    :param line:line number found by the random
    :param column:column number found by the random
    :return: True if the replacement was successful and increasing the number of times to place the id in the matrix
            False was already occupied back do random
    """
    if line == 0 and column == 0 or line == len(Matrix) - 1 and column == len(Matrix) - 1:
        return False

    else:
        if Matrix[line][column] == 0:
            Matrix[line][column] = idClod
            return True
        else:
            return False




def createMatrix(size):
    """
receives the size of the matrix
while j(small list) sizeMatrix: then creates an empty row which is then inserted into
the matrix which will be inserting row in matrix while not exceeding the size
    :param size: size the matrix
    """

    i = 0
    while i < size:
        j = 0
        row = []
        while j < size:
            row.append(0)
            j += 1
        Matrix.append(row)
        i += 1


def printMatrix():
    """
    print the matrix

    """

    i = 0
    while i < len(Matrix):
        print(Matrix[i])
        i += 1


def moveAnt(keyboardAddress):
    """
ant will move according to the coordinates that indicate, if you want to move and the matrix is x = 0 y = 0 then the
box does not point in the journey as a double, then you must wait for another address indicated
    :param keyboardAddress: Keyboard events pc
    """
    global x
    global y
    global Matrix
    global healthVar
    global steps

    if keyboardAddress == "Right":

        if y == len(Matrix[x]) - 1:
            print("Ant can not move")

        else:
            Matrix[x][y] = 3
            y += 1
            idCasilla = Matrix[x][y]
            if idCasilla != 0:
                antInstance.box(idCasilla)
                newhealth = str(antInstance.getHealthAnt())
                healthVar.set("Health:"+newhealth)

                newLevelDrunk =str(antInstance.getlevelDrunk())
                levelDrunkVar.set("Level Drunk:"+ newLevelDrunk)

                newState = antInstance.getstate()
                stateVar.set("State:"+ newState)
            else:
                antInstance.box(idCasilla)

            steps+=1
            row = [x, y]
            antInstance.addTravel(row)



    if keyboardAddress == "Left":
        if y == 0:
            print("Ant can not move")

        else:
            Matrix[x][y] = 3
            y -= 1
            idCasilla = Matrix[x][y]
            if idCasilla != 0:
                antInstance.box(idCasilla)
                newhealth = str(antInstance.getHealthAnt())
                healthVar.set("Health:"+newhealth)

                newLevelDrunk =str(antInstance.getlevelDrunk())
                levelDrunkVar.set("Level Drunk:"+ newLevelDrunk)

                newState = antInstance.getstate()
                stateVar.set("State:"+ newState)
            else:
                antInstance.box(idCasilla)

            steps+=1
            row = [x, y]
            antInstance.addTravel(row)

    if keyboardAddress == "Down":

        if x == len(Matrix) - 1:
            print("Ant can not move")

        else:
            Matrix[x][y] = 3
            x += 1
            idCasilla = Matrix[x][y]
            if idCasilla != 0:
                antInstance.box(idCasilla)
                newhealth = str(antInstance.getHealthAnt())
                healthVar.set("Health:"+newhealth)

                newLevelDrunk =str(antInstance.getlevelDrunk())
                levelDrunkVar.set("Level Drunk:"+ newLevelDrunk)

                newState = antInstance.getstate()
                stateVar.set("State:"+ newState)
            if idCasilla==0:
                antInstance.box(idCasilla)

            steps+=1
            row = [x, y]
            antInstance.addTravel(row)

    if keyboardAddress == "Up":

        if x == 0:
            print("Ant can not climb")

        else:
            Matrix[x][y] = 3
            x -= 1
            idCasilla = Matrix[x][y]
            if idCasilla != 0:
                antInstance.box(idCasilla)
                newhealth = str(antInstance.getHealthAnt())
                healthVar.set("Health: "+newhealth)

                newLevelDrunk =str(antInstance.getlevelDrunk())
                levelDrunkVar.set("Level Drunk: "+ newLevelDrunk)

                newState = antInstance.getstate()
                stateVar.set("State: "+ newState)
            else:
                antInstance.box(idCasilla)

            steps+=1
            row = [x, y]
            antInstance.addTravel(row)


def keypress(event):
    """
    declado recognizes events and will send to moveAnt method in which the position should be the first image
    :param event: takes an event
    """
    keyboardAddress = ""
    import winsound

    if event.keysym == 'Left':
        keyboardAddress = "Left"
        moveAnt(keyboardAddress)
        updateMatrixUI()
        printMatrix()
        print("the journey of the ant was", antInstance.getTravel())
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

    if event.keysym == 'Down':
        keyboardAddress = "Down"
        moveAnt(keyboardAddress)
        updateMatrixUI()
        printMatrix()
        print("the journey of the ant was", antInstance.getTravel())
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

    if event.keysym == 'Right':
        keyboardAddress = "Right"
        moveAnt(keyboardAddress)
        updateMatrixUI()
        printMatrix()
        print("the journey of the ant was", antInstance.getTravel())
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)

    if event.keysym == 'Up':
        keyboardAddress = "Up"
        moveAnt(keyboardAddress)
        updateMatrixUI()
        printMatrix()
        print("the journey of the ant was", antInstance.getTravel())
        winsound.PlaySound("sound.wav", winsound.SND_FILENAME)


def event(args):
    pass


def startMatrix():
    """
    call the methods necessary to initiate matrix

    """
    loadingFile()

    loadingFile()
    createMatrix(sizeMatrixGlobals)
    startFinallyMatrix()
    calcRandom(CLOD_WINE, wineCount)
    calcRandom(CLOD_POISON, poisonCount)
    calcRandom(CLOD_SUGGAR, sugarCount)
    printMatrix()
    informationSettings()
    recognizeImage()
    windowSettings()
    keypress(event)
    recognizeImage()


startMatrix()