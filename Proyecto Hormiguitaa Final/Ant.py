__author__ = 'Crisly'

from Constants import *
import random
from Globals import *

class Ant:

    """
    this is the method of Ant contrucctor object is responsible for receiving the parameter entered by the user
     required to develop skills in the game has a single set and get to change values ​​or to display them without
      modification.
    """


    def __init__(self, nameAnt):

        self.name = nameAnt
        self.travel = [[0,0]]
        self.heathAnt = 100
        self.levelDrunk = 0
        self.state = "Sobria"



    def setName(self, newName):
        self.name = newName

    def addTravel(self, newPosition):
        self.travel.append(newPosition)


    def setHealthAnt(self, newHealthAnt):
        self.health = newHealthAnt

    def setlevelDrunk(self, newlevelDrunk):
        self.levelDrunk = newlevelDrunk

    def setstate(self,newstate):
        self.state=newstate


    def getName(self):
        return self.name

    def getTravel(self):
        return self.travel

    def getHealthAnt(self):
        return self.heathAnt

    def getlevelDrunk(self):
        return self.levelDrunk

    def getstate(self):
        return self.state




    def box (self,idBox):

        """
        This method evaluates the check box matrix with constant number and begins to make its operation either increase or
        decrease health, Ant undergoes various changes

        :param self:
        :param idBox:number described in the constant and is set in the boxes, each lump changes the status, health level
         alchol
        """

        global poisonLevel


        if self.heathAnt >0 and self.levelDrunk <= 50:

            #ant while this sorbria

            if self.levelDrunk <= 0:
                print("*******He joined Ant Sober*******")
                self.state= "Sober"

                if idBox==0:
                    print("The box is empty, you can continue")

                print("level drunkenness",self.levelDrunk)
                print("The state of the ant is:",self.state)


                if idBox == CLOD_SUGGAR:
                    print("Consumed a sugar cube")
                    self.heathAnt+=10
                    print("Congratulations life has increased",self.heathAnt)

                elif idBox == CLOD_POISON:
                    print("oh a lump of poison, do NOT eat it")


                elif idBox == CLOD_WINE:
                    print("mmm A lump of wine.......... I'll eat mmm ")
                    self.heathAnt-=10
                    self.levelDrunk+=20
                    print("The health indicator decreases\n"
                          "the level of alcohol increases 20")



             # while the ant is drunk
            elif self.levelDrunk > 0:

                print("*******He joined Ant Drunk*******")
                self.state="Drunk"
                print("The status of the ant is: ",self.state)

                if idBox==0:
                    print(" Box is empty")
                    print(" Congratulations, decreases the level of drunkenness",self.levelDrunk)
                    print(" You can continue ")


                elif idBox == CLOD_SUGGAR:
                    print("mmm..... .A sugar cube.... I'll eat ")
                    self.heathAnt+=10
                    self.levelDrunk-=10
                    print("Congratulations sugar level increase:",self.heathAnt)
                    print("It will be well decreased the level of drunkenness:",self.levelDrunk)


                elif idBox == CLOD_POISON:
                    print("mmm..A clod of poison (status: Drunk)")
                    self.heathAnt-=50
                    print(" Oh no, the health indicator has dropped me: ",self.heathAnt)


                elif idBox == CLOD_WINE:
                    print("mm... A lump of wine, but I'll eat this drunk ")
                    self.levelDrunk+=20
                    self.heathAnt-=20
                    print(" Too bad! The level of intoxication increases\n"
                          "Oh nooo, my level of health is declining")



            # while this ant poison

            elif levelPoison>0:

                self.state= "Poisoned"
                print("******* He entered AntPoison *******")
                self.state="Poisoned"
                print(" The status of the ant is: ",self.state)

                if idBox==0:
                    print("box is empty")
                    self.heathAnt+=10
                    print("Congratulations, increases the level of health",self.heathAnt)
                    print("You can continue")


                elif idBox == CLOD_SUGGAR:
                    print("mmm.. a sugar cube, I'll eat poisoned me  ")
                    self.heathAnt+=20
                    print("oh good! My health increase",self.heathAnt)

        else:
            self.state= "Dead"
            print("************************************")
            print(" The Ant ",self.name," is Dead!!!")
            print("************************************")





    def hip(self):

            """
            ant moves randomly by this drunk

            """
            line=random.randint(0,len(Matrix)-1)
            column=random.randint(0,len(Matrix)-1)

            #genera la columna y la fila que debe seguir,este metodo es llamando cuando ebriedad este en 20 y
            # la salud baja a 10
            # si choca con la pared de la posicion donde esta se vuelve a general el random
