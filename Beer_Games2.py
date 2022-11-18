import importlib
from math import atan2
from typing import cast
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.cache import Cache
import random
import os
import pandas as pd


global t1Name,t2Name,t3Name,t4Name, team1score,team2score,team3score,team4score, x, scores, y
global sorty


x = 1

y = 4

team1score = 0
team2score = 0
team3score = 0
team4score = 0

t1Name = ""
t2Name = ""
t3Name = ""
t4Name = ""

scores = {}



class ping(Screen):
    
    winner = ObjectProperty(None) #WinnerLabel
    second = ObjectProperty(None) #2nd label
    r1loser= ObjectProperty(None) #loser 1 input
    r2loser= ObjectProperty(None) #loser 2 input

    r2= ObjectProperty(None) #round 2 team (right)
    r1= ObjectProperty(None) #round 1 team (left)
    rLeft = ObjectProperty(None)
    rRight = ObjectProperty(None)

    team1L= ObjectProperty(None) #Team 1 label
    team2L= ObjectProperty(None) #Team 2 label
    team4L= ObjectProperty(None) #Team 3 label
    team3L= ObjectProperty(None) #Team 4 label

    lB2= ObjectProperty(None) #loser 2 for 3 or 4 label
    lB1 = ObjectProperty(None) #loser 1 for 3 or 4 labbel
    l2ndL= ObjectProperty(None) #2nd Loser label
    l22ndL = ObjectProperty(None)

    t1 = ObjectProperty(None) #team one input
    t2 = ObjectProperty(None) #team 2 input
    t3 = ObjectProperty(None) #team 3 input
    t4 = ObjectProperty(None) #team4 input


    def start(self):  #should only run once
        global x, sound 

        sound = SoundLoader.load('PumpIt.mp3')

        
        if sound:
            sound.volume = 1
            sound.play()  


        
  


        if x > 0:
            randAgain = [scores["t1Name"][0],scores["t2Name"][0],scores["t3Name"][0],scores["t4Name"][0]] 
            random.shuffle(randAgain)


            self.team1L.text = randAgain[0]
            self.team2L.text = randAgain[1]
            self.team3L.text = randAgain[2]
            self.team4L.text = randAgain[3]

            x -= 1


    def roundOne(self):

        round1ScoLEFT = [self.t1.text,self.t3.text]
        round1ScoLEFT.sort() #from lowest to highest

        round1ScoRIGHT = [self.t4.text,self.t2.text]
        round1ScoRIGHT.sort() #from lowest to highest


        if round1ScoLEFT[0] == self.t1.text:
            self.rLeft.text = self.team1L.text #winner bracket
            self.lb1.text = self.team3L.text #loser bracker

        elif round1ScoLEFT[0] == self.t3.text:
            self.rLeft.text = self.team3L.text
            self.lb1.text = self.team1L.text #loser bracker
        ######################################################
        if round1ScoRIGHT[0] == self.t2.text:
            self.rRight.text = self.team2L.text #winner bracket
            self.lb2.text = self.team4L.text #loser bracker

        elif round1ScoRIGHT[0] == self.t4.text:
            self.rRight.text = self.team4L.text
            self.lb2.text = self.team2L.text #loser bracker




    def roundTwo(self):

        round2ScoTOP = [self.r1.text,self.r2.text]
        round2ScoTOP.sort() #from lowest to highest

        if round2ScoTOP[0] == self.r1.text:
            self.winner.text = self.rRight.text
            self.second.text = self.rLeft.text

        elif round2ScoTOP[0] == self.r2.text:
            self.winner.text = self.rLeft.text
            self.second.text = self.rRight.text

    def roundTree(self):
        
        round2ScoBottom = [self.r2loser.text,self.r1loser.text]
        round2ScoBottom.sort() #from lowest to highest

        if round2ScoBottom[0] == self.r1loser.text: 
            self.l2ndL.text = self.lb2.text
            self.l22ndL.text = self.lb1.text

        elif round2ScoBottom[0] == self.r2loser.text:  
            self.l2ndL.text = self.lb1.text
            self.l22ndL.text = self.lb2.text

    def update(self):

        sound.stop()


        getNames = [scores.get("t1Name")[0], scores.get("t2Name")[0],scores.get("t3Name")[0],scores.get("t4Name")[0]]
        

        
        
        for s in getNames:
            if s == self.winner.text: #Specific to the first place

                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 100 

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 100 

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 100 

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 100

                    scores.get("t4Name")[1] = addthis


            elif s == self.second.text: #specific to second place
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 70

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 70

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 70

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 70

                    scores.get("t4Name")[1] = addthis


            elif s == self.l2ndL.text: #Specific to 3rd
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 55

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 55

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 55

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 55

                    scores.get("t4Name")[1] = addthis


            elif s == self.l22ndL.text: #Specific to 4th
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 20

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 20

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 20

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 20

                    scores.get("t4Name")[1] = addthis


class pyramid(Screen):

    newSco = ObjectProperty(None)
    newSco2 = ObjectProperty(None)
    newSco3 = ObjectProperty(None)
    newSco4 = ObjectProperty(None)

    winner = ObjectProperty(None) #WinnerLabel
    second = ObjectProperty(None) #2nd label
    r1loser= ObjectProperty(None) #loser 1 input
    r2loser= ObjectProperty(None) #loser 2 input

    r2= ObjectProperty(None) #round 2 team (right)
    r1= ObjectProperty(None) #round 1 team (left)
    rLeft = ObjectProperty(None)
    rRight = ObjectProperty(None)

    team1L= ObjectProperty(None) #Team 1 label
    team2L= ObjectProperty(None) #Team 2 label
    team4L= ObjectProperty(None) #Team 3 label
    team3L= ObjectProperty(None) #Team 4 label

    lB2= ObjectProperty(None) #loser 2 for 3 or 4 label
    lB1 = ObjectProperty(None) #loser 1 for 3 or 4 labbel
    l2ndL= ObjectProperty(None) #2nd Loser label
    l22ndL = ObjectProperty(None)

    t1 = ObjectProperty(None) #team one input
    t2 = ObjectProperty(None) #team 2 input
    t3 = ObjectProperty(None) #team 3 input
    t4 = ObjectProperty(None) #team4 input




    def showScore(self):

        global sound

        sound = SoundLoader.load('Collapse.mp3')
        
        if sound:
            sound.volume = 1
            sound.play()

        s1 = " ".join(str(x) for x in scores.get("t1Name"))
        s2 = " ".join(str(x) for x in scores.get("t2Name"))
        s3 = " ".join(str(x) for x in scores.get("t3Name"))
        s4 = " ".join(str(x) for x in scores.get("t4Name"))

        self.newSco.text = s1 
        self.newSco2.text = s2 
        self.newSco3.text = s3 
        self.newSco4.text = s4 

    def start(self):
        global x        



        randAgain = [scores["t1Name"][0],scores["t2Name"][0],scores["t3Name"][0],scores["t4Name"][0]] 
        random.shuffle(randAgain)


        self.team1L.text = randAgain[0]
        self.team2L.text = randAgain[1]
        self.team3L.text = randAgain[2]
        self.team4L.text = randAgain[3]




    def roundOne(self):

        round1ScoLEFT = [self.t1.text,self.t3.text]
        round1ScoLEFT.sort() #from lowest to highest

        round1ScoRIGHT = [self.t4.text,self.t2.text]
        round1ScoRIGHT.sort() #from lowest to highest


        if round1ScoLEFT[0] == self.t1.text:
            self.rLeft.text = self.team1L.text #winner bracket
            self.lb1.text = self.team3L.text #loser bracker

        elif round1ScoLEFT[0] == self.t3.text:
            self.rLeft.text = self.team3L.text
            self.lb1.text = self.team1L.text #loser bracker
        ######################################################
        if round1ScoRIGHT[0] == self.t2.text:
            self.rRight.text = self.team2L.text #winner bracket
            self.lb2.text = self.team4L.text #loser bracker

        elif round1ScoRIGHT[0] == self.t4.text:
            self.rRight.text = self.team4L.text
            self.lb2.text = self.team2L.text #loser bracker




    def roundTwo(self):

        round2ScoTOP = [self.r1.text,self.r2.text]
        round2ScoTOP.sort() #from lowest to highest

        if round2ScoTOP[0] == self.r1.text:
            self.winner.text = self.rRight.text
            self.second.text = self.rLeft.text

        elif round2ScoTOP[0] == self.r2.text:
            self.winner.text = self.rLeft.text
            self.second.text = self.rRight.text

    def roundTree(self):
        
        round2ScoBottom = [self.r2loser.text,self.r1loser.text]
        round2ScoBottom.sort() #from lowest to highest

        if round2ScoBottom[0] == self.r1loser.text: 
            self.l2ndL.text = self.lb2.text
            self.l22ndL.text = self.lb1.text

        elif round2ScoBottom[0] == self.r2loser.text:  
            self.l2ndL.text = self.lb1.text
            self.l22ndL.text = self.lb2.text

    def update(self):


        getNames = [scores.get("t1Name")[0], scores.get("t2Name")[0],scores.get("t3Name")[0],scores.get("t4Name")[0]]
        
        sound.stop()
        
        
        for s in getNames:
            if s == self.winner.text: #Specific to the first place

                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 100 

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 100 

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 100 

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 100

                    scores.get("t4Name")[1] = addthis


            elif s == self.second.text: #specific to second place
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 70

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 70

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 70

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 70

                    scores.get("t4Name")[1] = addthis


            elif s == self.l2ndL.text: #Specific to 3rd
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 55

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 55

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 55

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 55

                    scores.get("t4Name")[1] = addthis


            elif s == self.l22ndL.text: #Specific to 4th
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 20

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 20

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 20

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 20

                    scores.get("t4Name")[1] = addthis


class target(Screen):

    newSco = ObjectProperty(None)
    newSco2 = ObjectProperty(None)
    newSco3 = ObjectProperty(None)
    newSco4 = ObjectProperty(None)


    bonus1 = ObjectProperty(None)
    bonus2 = ObjectProperty(None)
    bonus3 = ObjectProperty(None)
    bonus4 = ObjectProperty(None)




    def showScore(self):
        global sound


        sound = SoundLoader.load('Start Bottom.mp3')
        
        if sound:
            sound.volume = 1
            sound.play()

        s1 = scores["t1Name"][0]
        s2 = scores["t2Name"][0]
        s3 = scores["t3Name"][0]
        s4 = scores["t4Name"][0]

        self.newSco.text = s1 
        self.newSco2.text = s2 
        self.newSco3.text = s3 
        self.newSco4.text = s4 





    def update(self):


        getNames = [scores.get("t1Name")[0], scores.get("t2Name")[0],scores.get("t3Name")[0],scores.get("t4Name")[0]]
        
        sound.stop()
        
        
        for s in getNames:
            if s == self.newSco.text: #Specific to the first place

                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 100 
                    addthis += int(self.bonus1.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 100 
                    addthis += int(self.bonus1.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 100 
                    addthis += int(self.bonus1.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 100
                    addthis += int(self.bonus1.text)

                    scores.get("t4Name")[1] = addthis


            elif s == self.newSco2.text: #specific to second place
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t4Name")[1] = addthis


            elif s == self.newSco3.text: #Specific to 3rd
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t4Name")[1] = addthis


            elif s == self.newSco4.text: #Specific to 4th
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t4Name")[1] = addthis


class tricks(Screen):

    newSco = ObjectProperty(None)
    newSco2 = ObjectProperty(None)
    newSco3 = ObjectProperty(None)
    newSco4 = ObjectProperty(None)

    winner = ObjectProperty(None) #WinnerLabel
    second = ObjectProperty(None) #2nd label
    r1loser= ObjectProperty(None) #loser 1 input
    r2loser= ObjectProperty(None) #loser 2 input

    r2= ObjectProperty(None) #round 2 team (right)
    r1= ObjectProperty(None) #round 1 team (left)
    rLeft = ObjectProperty(None)
    rRight = ObjectProperty(None)

    team1L= ObjectProperty(None) #Team 1 label
    team2L= ObjectProperty(None) #Team 2 label
    team4L= ObjectProperty(None) #Team 3 label
    team3L= ObjectProperty(None) #Team 4 label

    lB2= ObjectProperty(None) #loser 2 for 3 or 4 label
    lB1 = ObjectProperty(None) #loser 1 for 3 or 4 labbel
    l2ndL= ObjectProperty(None) #2nd Loser label
    l22ndL = ObjectProperty(None)

    t1 = ObjectProperty(None) #team one input
    t2 = ObjectProperty(None) #team 2 input
    t3 = ObjectProperty(None) #team 3 input
    t4 = ObjectProperty(None) #team4 input

    bonus1 = ObjectProperty(None)
    bonus2 = ObjectProperty(None)
    bonus3 = ObjectProperty(None)
    bonus4 = ObjectProperty(None)




    def showScore(self):
        global sound 
        sound = SoundLoader.load('Remember Name.mp3')
        
        if sound:
            sound.volume = 1
            sound.play()
        
        s1 = " ".join(str(x) for x in scores.get("t1Name"))
        s2 = " ".join(str(x) for x in scores.get("t2Name"))
        s3 = " ".join(str(x) for x in scores.get("t3Name"))
        s4 = " ".join(str(x) for x in scores.get("t4Name"))

        self.newSco.text = s1 
        self.newSco2.text = s2 
        self.newSco3.text = s3 
        self.newSco4.text = s4 

    def start(self):
        global x        


        randAgain = [scores["t1Name"][0],scores["t2Name"][0],scores["t3Name"][0],scores["t4Name"][0]] 
        random.shuffle(randAgain)


        self.team1L.text = randAgain[0]
        self.team2L.text = randAgain[1]
        self.team3L.text = randAgain[2]
        self.team4L.text = randAgain[3]



    def roundOne(self):

        round1ScoLEFT = [self.t1.text,self.t3.text]
        round1ScoLEFT.sort() #from lowest to highest

        round1ScoRIGHT = [self.t4.text,self.t2.text]
        round1ScoRIGHT.sort() #from lowest to highest


        if round1ScoLEFT[0] == self.t1.text:
            self.rLeft.text = self.team1L.text #winner bracket
            self.lb1.text = self.team3L.text #loser bracker

        elif round1ScoLEFT[0] == self.t3.text:
            self.rLeft.text = self.team3L.text
            self.lb1.text = self.team1L.text #loser bracker
        ######################################################
        if round1ScoRIGHT[0] == self.t2.text:
            self.rRight.text = self.team2L.text #winner bracket
            self.lb2.text = self.team4L.text #loser bracker

        elif round1ScoRIGHT[0] == self.t4.text:
            self.rRight.text = self.team4L.text
            self.lb2.text = self.team2L.text #loser bracker




    def roundTwo(self):

        round2ScoTOP = [self.r1.text,self.r2.text]
        round2ScoTOP.sort() #from lowest to highest

        if round2ScoTOP[0] == self.r1.text:
            self.winner.text = self.rRight.text
            self.second.text = self.rLeft.text

        elif round2ScoTOP[0] == self.r2.text:
            self.winner.text = self.rLeft.text
            self.second.text = self.rRight.text

    def roundTree(self):
        
        round2ScoBottom = [self.r2loser.text,self.r1loser.text]
        round2ScoBottom.sort() #from lowest to highest

        if round2ScoBottom[0] == self.r1loser.text: 
            self.l2ndL.text = self.lb2.text
            self.l22ndL.text = self.lb1.text

        elif round2ScoBottom[0] == self.r2loser.text:  
            self.l2ndL.text = self.lb1.text
            self.l22ndL.text = self.lb2.text

    def update(self):


        getNames = [scores.get("t1Name")[0], scores.get("t2Name")[0],scores.get("t3Name")[0],scores.get("t4Name")[0]]
        

        sound.stop()
        
        
        for s in getNames:
            if s == self.winner.text: #Specific to the first place

                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 100 
                    addthis += int(self.bonus1.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 100 
                    addthis += int(self.bonus1.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 100 
                    addthis += int(self.bonus1.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 100
                    addthis += int(self.bonus1.text)

                    scores.get("t4Name")[1] = addthis


            elif s == self.second.text: #specific to second place
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 70
                    addthis += int(self.bonus2.text)

                    scores.get("t4Name")[1] = addthis


            elif s == self.l2ndL.text: #Specific to 3rd
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 55
                    addthis += int(self.bonus3.text)

                    scores.get("t4Name")[1] = addthis


            elif s == self.l22ndL.text: #Specific to 4th
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 20
                    addthis += int(self.bonus4.text)

                    scores.get("t4Name")[1] = addthis


class cans(Screen):

    newSco = ObjectProperty(None)
    newSco2 = ObjectProperty(None)
    newSco3 = ObjectProperty(None)
    newSco4 = ObjectProperty(None)

    winner = ObjectProperty(None) #WinnerLabel
    second = ObjectProperty(None) #2nd label
    r1loser= ObjectProperty(None) #loser 1 input
    r2loser= ObjectProperty(None) #loser 2 input

    r2= ObjectProperty(None) #round 2 team (right)
    r1= ObjectProperty(None) #round 1 team (left)
    rLeft = ObjectProperty(None)
    rRight = ObjectProperty(None)

    team1L= ObjectProperty(None) #Team 1 label
    team2L= ObjectProperty(None) #Team 2 label
    team4L= ObjectProperty(None) #Team 3 label
    team3L= ObjectProperty(None) #Team 4 label

    lB2= ObjectProperty(None) #loser 2 for 3 or 4 label
    lB1 = ObjectProperty(None) #loser 1 for 3 or 4 labbel
    l2ndL= ObjectProperty(None) #2nd Loser label
    l22ndL = ObjectProperty(None)

    t1 = ObjectProperty(None) #team one input
    t2 = ObjectProperty(None) #team 2 input
    t3 = ObjectProperty(None) #team 3 input
    t4 = ObjectProperty(None) #team4 input




    def showScore(self):
        global sound
        sound = SoundLoader.load('The Final.mp3')
        
        if sound:
            sound.volume = 1
            sound.play()         
        
        s1 = " ".join(str(x) for x in scores.get("t1Name"))
        s2 = " ".join(str(x) for x in scores.get("t2Name"))
        s3 = " ".join(str(x) for x in scores.get("t3Name"))
        s4 = " ".join(str(x) for x in scores.get("t4Name"))

        self.newSco.text = s1 
        self.newSco2.text = s2 
        self.newSco3.text = s3 
        self.newSco4.text = s4 

    def start(self):
        global x        


        randAgain = [scores["t1Name"][0],scores["t2Name"][0],scores["t3Name"][0],scores["t4Name"][0]] 
        random.shuffle(randAgain)


        self.team1L.text = randAgain[0]
        self.team2L.text = randAgain[1]
        self.team3L.text = randAgain[2]
        self.team4L.text = randAgain[3]



    def roundOne(self):

        round1ScoLEFT = [self.t1.text,self.t3.text]
        round1ScoLEFT.sort() #from lowest to highest

        round1ScoRIGHT = [self.t4.text,self.t2.text]
        round1ScoRIGHT.sort() #from lowest to highest


        if round1ScoLEFT[0] == self.t1.text:
            self.rLeft.text = self.team1L.text #winner bracket
            self.lb1.text = self.team3L.text #loser bracker

        elif round1ScoLEFT[0] == self.t3.text:
            self.rLeft.text = self.team3L.text
            self.lb1.text = self.team1L.text #loser bracker
        ######################################################
        if round1ScoRIGHT[0] == self.t2.text:
            self.rRight.text = self.team2L.text #winner bracket
            self.lb2.text = self.team4L.text #loser bracker

        elif round1ScoRIGHT[0] == self.t4.text:
            self.rRight.text = self.team4L.text
            self.lb2.text = self.team2L.text #loser bracker




    def roundTwo(self):


    

        round2ScoTOP = [self.r1.text,self.r2.text]
        round2ScoTOP.sort() #from lowest to highest

        if round2ScoTOP[0] == self.r1.text:
            self.winner.text = self.rRight.text
            self.second.text = self.rLeft.text

        elif round2ScoTOP[0] == self.r2.text:
            self.winner.text = self.rLeft.text
            self.second.text = self.rRight.text

    def roundTree(self):
        
        round2ScoBottom = [self.r2loser.text,self.r1loser.text]
        round2ScoBottom.sort() #from lowest to highest

        if round2ScoBottom[0] == self.r1loser.text: 
            self.l2ndL.text = self.lb2.text
            self.l22ndL.text = self.lb1.text

        elif round2ScoBottom[0] == self.r2loser.text:  
            self.l2ndL.text = self.lb1.text
            self.l22ndL.text = self.lb2.text


    def update(self):

        sound.stop()

        getNames = [scores.get("t1Name")[0], scores.get("t2Name")[0],scores.get("t3Name")[0],scores.get("t4Name")[0]]
        

        
        
        for s in getNames:
            if s == self.winner.text: #Specific to the first place

                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 100 

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 100 

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 100 

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 100

                    scores.get("t4Name")[1] = addthis


            elif s == self.second.text: #specific to second place
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 70

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 70

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 70

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 70

                    scores.get("t4Name")[1] = addthis


            elif s == self.l2ndL.text: #Specific to 3rd
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 55

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 55

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 55

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 55

                    scores.get("t4Name")[1] = addthis


            elif s == self.l22ndL.text: #Specific to 4th
                if s == scores.get("t1Name")[0]: 

                    addthis = scores.get("t1Name")[1]
                    addthis += 20

                    scores.get("t1Name")[1] = addthis

                elif s == scores.get("t2Name")[0]: 
                    
                    addthis = scores.get("t2Name")[1]
                    addthis += 20

                    scores.get("t2Name")[1] = addthis

                elif s == scores.get("t3Name")[0]: 
                    
                    addthis = scores.get("t3Name")[1]
                    addthis += 20

                    scores.get("t3Name")[1] = addthis

                elif s == scores.get("t4Name")[0]: 
                    
                    addthis = scores.get("t4Name")[1]
                    addthis += 20

                    scores.get("t4Name")[1] = addthis


class finals(Screen):
    winner = ObjectProperty(None)
    second = ObjectProperty(None)
    third = ObjectProperty(None)
    fourth = ObjectProperty(None)

    global y,sorty 


    def update(self):
        global y,sorty 


        global sound2

        sound2 = SoundLoader.load('All I Do Is Win.mp3')
        

        s1 = " ".join(str(x) for x in scores.get("t1Name"))
        s2 = " ".join(str(x) for x in scores.get("t2Name"))
        s3 = " ".join(str(x) for x in scores.get("t3Name"))
        s4 = " ".join(str(x) for x in scores.get("t4Name"))

        getNames = [scores.get("t1Name")[0], scores.get("t2Name")[0],scores.get("t3Name")[0],scores.get("t4Name")[0]]


        sorty = [scores.get("t1Name")[1], scores.get("t2Name")[1],scores.get("t3Name")[1],scores.get("t4Name")[1]]
        sorty.sort()


        if y == 4:
            if sorty[0] == scores.get("t1Name")[1]:
                self.fourth.text = s1 
                
                y -= 1
                #sorty.sort()

            elif sorty[0] == scores.get("t2Name")[1]:
                self.fourth.text = s2 
                
                y -= 1
                #sorty.sort()


            elif sorty[0] == scores.get("t3Name")[1]:
                self.fourth.text = s3 
               
                y -= 1
                #sorty.sort()


            elif sorty[0] == scores.get("t4Name")[1]:
                self.fourth.text = s4
                
                y -= 1
                #sorty.sort()


        elif y == 3:
            if sorty[1] == scores.get("t1Name")[1]:
                self.third.text = s1 
                
                y -= 1
                #sorty.sort()


            elif sorty[1] == scores.get("t2Name")[1]:
                self.third.text = s2 
                
                y -= 1
                #sorty.sort()


            elif sorty[1] == scores.get("t3Name")[1]:
                self.third.text = s3 
                
                y -= 1
                #sorty.sort()


            elif sorty[1] == scores.get("t4Name")[1]:
                self.third.text = s4
                
                y -= 1
                #sorty.sort()


        elif y == 2:


           
            
            sound2.volume = 3
            sound2.play()


            if sorty[2] == scores.get("t1Name")[1]:
                self.second.text = s1 
                
                #sorty.sort()


            elif sorty[2] == scores.get("t2Name")[1]:
                self.second.text = s2 
                
                #sorty.sort()


            elif sorty[2] == scores.get("t3Name")[1]:
                self.second.text = s3 
               
                #sorty.sort()


            elif sorty[2] == scores.get("t4Name")[1]:
                self.second.text = s4
                
                #sorty.sort()



            if sorty[3] == scores.get("t1Name")[1]:
                self.winner.text = s1 
               
                #sorty.sort()


            elif sorty[3] == scores.get("t2Name")[1]:
                self.winner.text = s2 
                
                #sorty.sort()


            elif sorty[3] == scores.get("t3Name")[1]:
                self.winner.text = s3 
                
                #sorty.sort()


            elif sorty[3] == scores.get("t4Name")[1]:
                self.winner.text = s4
                
               


           









class mainpage(Screen):

    t1 = ObjectProperty(None)
    t2 = ObjectProperty(None)
    t3 = ObjectProperty(None)
    t4 = ObjectProperty(None)    

    global sound
    

    sound = SoundLoader.load('Ghostbusters.mp3')
    
    if sound:
        sound.volume = 1
        sound.play()

    
    def add_names(self):
        global t1Name,t2Name,t3Name,t4Name, team1score,team2score,team3score,team4score
        
        t1Name = self.t1.text
        t2Name = self.t2.text
        t3Name = self.t3.text
        t4Name = self.t4.text

        scores.update({"t1Name":[t1Name,team1score],"t2Name":[t2Name,team2score],"t3Name":[t3Name,team3score],"t4Name":[t4Name,team4score] })

        sound.stop()






class Manager(ScreenManager):
    ... #transitions










##################

kv = Builder.load_file("beerGAMES.kv")
sm = Manager()

switch = [mainpage(name = "ready"), ping(name = "ping"),pyramid(name = "pyramid"),target(name="target"),tricks(name="tricks"),cans(name="cans"),finals(name="finals")]

for screen in switch:
    sm.add_widget(screen)
    
    

sm.current = "ready"       

class BeerLympics2App(App):
    def build(self):
        return sm



if __name__ == '__main__':
    BeerLympics2App().run()  