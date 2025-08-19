import tkinter as tk


#bit of house keeping
myFont = "Rum Raisin"
bgColour = "#3b80c4"

#background colour is #3b80c4, just in case I delete it. 
#Disabled colour is #5887a7 for pressed buttons

#This initialised the program and switches between all the different screens
class start(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self,*args, **kwargs)
        self.attributes('-fullscreen', True)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        #Row configuration, I might change this when I start putting more in 
        container.grid_rowconfigure(0, weight = 20)
        container.grid_rowconfigure(0, weight =20)
        #Creates an array of frames to swap between and chooses a starting one
        self.frames = {}
        for F in (  StartPage, RoundOne, FirstBalanceRound1, FirstBalanceRound2, FirstBalanceRound3, FirstScoreBoard,
                    Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10,
                    Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18, Q19, Q20,
                    Q21, Q22, Q23, Q24, Q25,
                    RoundTwo, SecondBalanceRound1, SecondBalanceRound2, SecondBalanceRound3, SecondScoreBoard,
                    Q1b, Q2b, Q3b, Q4b, Q5b, Q6b, Q7b, Q8b, Q9b, Q10b,
                    Q11b, Q12b, Q13b, Q14b, Q15b, Q16b, Q17b, Q18b, Q19b, Q20b,
                    Q21b, Q22b, Q23b, Q24b, Q25b,
                    RoundThree,ThirdBalanceRound1, ThirdBalanceRound2, ThirdBalanceRound3, ThirdScoreBoard,
                    Q1c, Q2c, Q3c, Q4c, Q5c, Q6c, Q7c, Q8c, Q9c, Q10c,
                    Q11c, Q12c, Q13c, Q14c, Q15c, Q16c, Q17c, Q18c, Q19c, Q20c,
                    Q21c, Q22c, Q23c, Q24c, Q25c,
                    Finale,
                  ):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")
        self.showFrame(StartPage)


    #Method for swapping frames   
    def showFrame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    



#Starting menu
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        button = tk.Button(self, text = "DrunkPardy 3", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda:controller.showFrame(RoundOne), 
                           activebackground= bgColour)
                           
        button.pack()
        

            
          
#manages the score in the background for all the players           
class ScoreManager():
    def __init__(self, TeamName, TeamScore, TeamDrinks, CurrentScore):
        self.TeamName = TeamName
        self.TeamScore = TeamScore
        self.TeamDrinks = TeamDrinks
        self.CurrentScore = CurrentScore
        

    #Dynamically update the score for each question  
    def updateScore(self, score):
        self.CurrentScore = score 
    
    

    #Add the score and update the scoreboard
    def addScore(self, score):
        self.TeamScore += score
        ScoreBoard.TeamOneLabel["text"] =  TeamOne.TeamName +" = " + str(TeamOne.TeamScore) + " " + TeamOne.TeamName +" = " + str(TeamOne.TeamDrinks)
        ScoreBoard.TeamTwoLabel["text"] =  TeamTwo.TeamName +" = " + str(TeamTwo.TeamScore) + " " + TeamTwo.TeamName +" = " + str(TeamTwo.TeamDrinks)
        ScoreBoard.TeamThreeLabel["text"] =  TeamThree.TeamName +" = " + str(TeamThree.TeamScore) + " " + TeamThree.TeamName +" = " + str(TeamThree.TeamDrinks)
        ScoreBoard.TeamFourLabel["text"] =  TeamFour.TeamName +" = " + str(TeamFour.TeamScore) + " " + TeamFour.TeamName +" = " + str(TeamFour.TeamDrinks)
        
      
    def addDrinks(self):
        self.TeamDrinks += 1
        ScoreBoard.TeamOneLabel["text"] =  TeamOne.TeamName +" = " + str(TeamOne.TeamScore) + " " + TeamOne.TeamName +" = " + str(TeamOne.TeamDrinks)
        ScoreBoard.TeamTwoLabel["text"] =  TeamTwo.TeamName +" = " + str(TeamTwo.TeamScore) + " " + TeamTwo.TeamName +" = " + str(TeamTwo.TeamDrinks)
        ScoreBoard.TeamThreeLabel["text"] =  TeamThree.TeamName +" = " + str(TeamThree.TeamScore) + " " + TeamThree.TeamName +" = " + str(TeamThree.TeamDrinks)
        ScoreBoard.TeamFourLabel["text"] =  TeamFour.TeamName +" = " + str(TeamFour.TeamScore) + " " + TeamFour.TeamName +" = " + str(TeamFour.TeamDrinks)
    
    def minusPoints(self):
        self.TeamScore -= 100
        ScoreBoard.TeamOneLabel["text"] =  TeamOne.TeamName +" = " + str(TeamOne.TeamScore) + " " + TeamOne.TeamName +" = " + str(TeamOne.TeamDrinks)
        ScoreBoard.TeamTwoLabel["text"] =  TeamTwo.TeamName +" = " + str(TeamTwo.TeamScore) + " " + TeamTwo.TeamName +" = " + str(TeamTwo.TeamDrinks)
        ScoreBoard.TeamThreeLabel["text"] =  TeamThree.TeamName +" = " + str(TeamThree.TeamScore) + " " + TeamThree.TeamName +" = " + str(TeamThree.TeamDrinks)
        ScoreBoard.TeamFourLabel["text"] =  TeamFour.TeamName +" = " + str(TeamFour.TeamScore) + " " + TeamFour.TeamName +" = " + str(TeamFour.TeamDrinks)
    



    
#Imma put this hear, hopefully it stays put. 
#This is where you'll change names, and the score if the game crashes
#See I know how to properly use classes, I do it here.
TeamOne = ScoreManager("Peal Harbour Heroes", 0, 0, 0)  
TeamTwo = ScoreManager("Wedge Wench", 0, 0, 0)
TeamThree = ScoreManager("Ex-Yoko Bloko's", 0, 0, 0) 
TeamFour = ScoreManager("Team Four", 0, 0, 0)   

    
class ScoreBoard():
    def __init__(self) -> None:
        pass

    TeamOneLabel = tk.Label(text = TeamOne.TeamName +" Score = " + str(TeamOne.TeamScore) + " " + TeamOne.TeamName +" Drinks = " + str(TeamOne.TeamDrinks) )  
    TeamTwoLabel = tk.Label(text= TeamTwo.TeamName + " Score = "+ str(TeamTwo.TeamScore) + " " + TeamTwo.TeamName + " Drinks = " + str(TeamTwo.TeamDrinks)) 
    TeamThreeLabel = tk.Label(text= TeamThree.TeamName + " Score ="+ str(TeamThree.TeamScore) + " " + TeamThree.TeamName + " Drinks = " + str(TeamThree.TeamDrinks)) 
    TeamFourLabel = tk.Label(text= TeamFour.TeamName + " Score ="+ str(TeamFour.TeamScore) + " " + TeamFour.TeamName + " Drinks = " + str(TeamFour.TeamDrinks)) 

    TeamOneButton = tk.Button(text = TeamOne.TeamName + " add score", command = lambda: [TeamOne.addScore(TeamOne.CurrentScore)])
    TeamTwoButton = tk.Button(text = TeamTwo.TeamName + " add score", command = lambda: [TeamTwo.addScore(TeamTwo.CurrentScore)])
    TeamThreeButton = tk.Button(text = TeamThree.TeamName + " add score", command = lambda: [TeamThree.addScore(TeamThree.CurrentScore)])
    TeamFourButton = tk.Button(text = TeamFour.TeamName + " add score", command = lambda: [TeamFour.addScore(TeamFour.CurrentScore)])

    TeamOneDrinks = tk.Button(text = TeamOne.TeamName + " add drinks", command = lambda: [TeamOne.addDrinks()])
    TeamTwoDrinks = tk.Button(text = TeamTwo.TeamName +" add drinks", command = lambda: [TeamTwo.addDrinks()])
    TeamThreeDrinks = tk.Button(text = TeamThree.TeamName + " add drinks", command = lambda: [TeamThree.addDrinks()])
    TeamFourDrinks = tk.Button(text = TeamFour.TeamName + " add drinks", command = lambda: [TeamFour.addDrinks()])

    TeamOneMinus = tk.Button(text= "Minus points Team One", command = lambda: [TeamOne.minusPoints()])
    TeamTwoMinus = tk.Button(text = "Minus points Team Two", command = lambda: [TeamTwo.minusPoints()])
    TeamThreeMinus = tk.Button(text = "Minus points Team Three", command = lambda: [TeamThree.minusPoints()])
    TeamFourMinus = tk.Button(text = "Minus points Team Four", command = lambda: [TeamFour.minusPoints()])
        
#I'm gonna just jam this in its for me anyway  
    TeamOneLabel.grid(row = 1, column= 1)
    TeamTwoLabel.grid(row = 2, column =1)
    TeamThreeLabel.grid(row = 3, column =1)
    TeamFourLabel.grid(row = 4, column = 1)

    TeamOneButton.grid(row = 1, column = 2)
    TeamTwoButton.grid(row = 2, column = 2)
    TeamThreeButton.grid( row = 3, column = 2)
    TeamFourButton.grid(row = 4, column = 2)

    TeamOneDrinks.grid( row = 1, column = 3)
    TeamTwoDrinks.grid( row = 2, column = 3)
    TeamThreeDrinks.grid(row = 3, column = 3)
    TeamFourDrinks.grid(row = 4, column = 3)

    TeamOneMinus.grid(row = 1, column = 4)
    TeamTwoMinus.grid(row = 2, column = 4)
    TeamThreeMinus.grid(row = 3, column = 4)
    TeamFourMinus.grid(row = 4, column = 4)

  

#All of the first round data and stuff
class RoundOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg = bgColour)
        #Text button
        title = tk.Button(self, text = "FirstRound", 
                           font = (myFont, 50), bg= bgColour, 
                           bd = 0, command = lambda:controller.showFrame(FirstBalanceRound1), 
                           activebackground= bgColour,anchor = "center")
        title.grid(row =1, column =3)   

        

        #disable function for the buttons
        def disableButton(button):
            button["state"] = "disabled"
        
        #All of the questions for the first column including the top text, need to add link to the questions.
        C1Text = tk.Label(self, anchor = "center", text = "Hal9000 with down syndrome", font = (myFont, 30), wraplength= 150,
                          bg = bgColour)
        C1Text.grid(row = 2, column = 1)
        Q1Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q1Button),controller.showFrame(Q1), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q1Button.grid(row = 3, column = 1, padx = 85, pady = 10)

        Q2Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q2Button),controller.showFrame(Q2), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q2Button.grid(row = 4, column = 1, padx = 85, pady = 10)

        Q3Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q3Button),controller.showFrame(Q3), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q3Button.grid(row = 5, column = 1, padx = 85, pady = 10)

        Q4Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q4Button),controller.showFrame(Q4), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q4Button.grid(row = 6, column = 1, padx = 85, pady = 10)

        Q5Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q5Button),controller.showFrame(Q5), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500),TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q5Button.grid(row = 7, column = 1, padx = 85, pady = 10)


        #Row 2 questions, see above               
        C2Text = tk.Label(self, anchor = "center", text = "A place free of communism", font = (myFont, 30), wraplength= 170,
                          bg = bgColour)
        C2Text.grid(row = 2, column = 2)

        Q6Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q6Button),controller.showFrame(Q6), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q6Button.grid(row = 3, column = 2, padx = 85, pady = 10)

        Q7Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q7Button),controller.showFrame(Q7), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q7Button.grid(row = 4, column = 2, padx = 85, pady = 10)

        Q8Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q8Button),controller.showFrame(Q8), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q8Button.grid(row = 5, column = 2, padx = 85, pady = 10)

        Q9Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q9Button),controller.showFrame(Q9), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400),TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q9Button.grid(row = 6, column = 2, padx = 85, pady = 10)

        Q10Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q10Button),controller.showFrame(Q10), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500),TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q10Button.grid(row = 7, column = 2, padx = 85, pady = 10)
    

        C3Text = tk.Label(self, anchor = "center", text = "The C-Team", font = (myFont, 30), wraplength= 150,
                          bg = bgColour)
        C3Text.grid(row = 2, column = 3)

        Q11Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q11Button),controller.showFrame(Q11), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q11Button.grid(row = 3, column = 3, padx = 85, pady = 10)

        Q12Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q12Button),controller.showFrame(Q12), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q12Button.grid(row = 4, column = 3, padx = 85, pady = 10)

        Q13Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q13Button),controller.showFrame(Q13), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q13Button.grid(row = 5, column = 3, padx = 85, pady = 10)

        Q14Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q14Button),controller.showFrame(Q14), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400),TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q14Button.grid(row = 6, column = 3, padx = 85, pady = 10)

        Q15Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q15Button),controller.showFrame(Q15), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500),TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q15Button.grid(row = 7, column = 3, padx = 85, pady = 10)



        C4Text = tk.Label(self, anchor = "center", text = "Hopefully not Rohypnol", font = (myFont, 30), wraplength= 150,
                          bg = bgColour)
        C4Text.grid(row = 2, column = 4)

        Q16Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q16Button),controller.showFrame(Q16), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q16Button.grid(row = 3, column = 4, padx = 85, pady = 10)

        Q17Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q17Button),controller.showFrame(Q17), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q17Button.grid(row = 4, column = 4, padx = 85, pady = 10)

        Q18Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q18Button),controller.showFrame(Q18), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q18Button.grid(row = 5, column = 4, padx = 85, pady = 10)

        Q19Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q19Button),controller.showFrame(Q19), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400),TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q19Button.grid(row = 6, column = 4, padx = 85, pady = 10)

        Q20Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q20Button),controller.showFrame(Q20), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500),TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q20Button.grid(row = 7, column = 4, padx = 85, pady = 10)



        C5Text = tk.Label(self, anchor = "center", text = "What Michael Jackson was doing right before he died", font = (myFont, 20), wraplength= 150,
                          bg = bgColour)
        C5Text.grid(row = 2, column = 5)

        Q21Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q21Button),controller.showFrame(Q21), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q21Button.grid(row = 3, column = 5, padx = 85, pady = 10)

        Q22Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q22Button),controller.showFrame(Q22), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q22Button.grid(row = 4, column = 5, padx = 85, pady = 10)

        Q23Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q23Button),controller.showFrame(Q23), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q23Button.grid(row = 5, column = 5, padx = 85, pady = 10)

        Q24Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q24Button),controller.showFrame(Q24), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400),TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q24Button.grid(row = 6, column = 5, padx = 85, pady = 10)

        Q25Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q25Button),controller.showFrame(Q25), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q25Button.grid(row = 7, column = 5, padx = 85, pady = 10)
        
#I'm gonna basically copy paste this, I know I could make it simplier but I honestly dont care.
class Q1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 1", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
       
         
        
        def answered(button):
            button["text"] = "Alien"
            button["command"] = lambda:controller.showFrame(RoundOne)
         
class Q2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        image = tk.PhotoImage(file = "")
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Two", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Dune" 
            button["command"] = lambda:controller.showFrame(RoundOne)       
    
class Q3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Three", 
                           font = (myFont, 100), bg= bgColour, wraplength= 500,
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Charlie and the Chocolate Factory" 
            button["command"] = lambda:controller.showFrame(RoundOne)

class Q4(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Four", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Hatefull Eight" 
            button["command"] = lambda:controller.showFrame(RoundOne)  
        
class Q5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Five", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Buffy the Vampire slayer" 
            button["command"] = lambda:controller.showFrame(RoundOne)    

class Q6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is the name of the main theory for how the unviverse was created?", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The big band theory" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What three things are comets made from? ", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Dust, Ice and Rocks" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is the only planet not named after a god?", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Earth" 
            button["command"] = lambda:controller.showFrame(RoundOne)

class Q9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What colour is the hotest star?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Blue" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is the name for the most common stars found in the milkyway", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Red Dwarf stars" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question One", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Swamp thing" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Two", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Animal Man" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Three", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Ambush Bug" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Four", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "RagMan" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Five", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Cloak and Dagger" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Gin,\n Campari,\n Sweet red Vermouth", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Negronis" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Bourbon,\n Angrostura bitters,\n Sugar,\n Dash of water", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Old fashioned" 
            button["command"] = lambda:controller.showFrame(RoundOne)

class Q18(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "White rum,\n Sugar syrup,\n Lime juice", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Daiquiri" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q19(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Vodka,\n Ginger beer,\n Lime juice", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Moscow Mule" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q20(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "White rum,\n Orange Curacao,\n Dark rum,\n Lime juice,\n Orgeat syrup", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 500, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Mai Tai" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "BLANK tries to get the Ice King to remember who he really is. Its just a depressing episode", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Adventure Time" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Jimmy:\n BLANK befriends a bullied student named Jimmy. BLANK befriends Jimmy, who has been a victim of bullying. BLANK discovers Jimmy has taken his father's gun and gone to school for revenge", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Static Shock" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q23(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Are you happy now?:\n BLANK has trouble recalling his happiest memory, he takes a rope ties it and is left staring at it", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Spongebob Squarepants"
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q24(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Twisted Sister:\n After finding themselves far too tired after a full day of fighting crime, the girls decide to create a new sibling in order to assist them. The new girl is sent away by the sisters after making a mistake and then explodes", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "PowerPuff girls" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q25(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "The 9/11 Episode: \nThe firefighters saved the store, but BLANK was still frightened. He was shaken by the fire, and scared of the firefighters themselves. Seeing this, the firefighters invited BLANK to visit their station where they talk about 9/11", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Sesame Street" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class FirstBalanceRound1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "League or My Parents?:\n I hope you outlive your children\n ", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button),wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()

        def answered(button):
            button["text"] = "League" 
            button["command"] = lambda:controller.showFrame(FirstBalanceRound2)
            TeamOne.updateScore(100) 
            TeamTwo.updateScore(100) 
            TeamThree.updateScore(100) 
            TeamFour.updateScore(100) 

class FirstBalanceRound2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "League or My Parents?:\n You are a walking condom advertisement\n ", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        
        button.pack()
        def answered(button):
            button["text"] = "League" 
            button["command"] = lambda:controller.showFrame(FirstBalanceRound3)
            TeamOne.updateScore(300) 
            TeamTwo.updateScore(300) 
            TeamThree.updateScore(300) 
            TeamFour.updateScore(300)  

class FirstBalanceRound3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
       
        button = tk.Button(self, text = "League or my parents:\nThe best part of you ran down your mothers leg", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "Parents" 
            button["command"] = lambda:controller.showFrame(FirstScoreBoard)
            TeamOne.updateScore(500) 
            TeamTwo.updateScore(500) 
            TeamThree.updateScore(500) 
            TeamFour.updateScore(500)  


class FirstScoreBoard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button1 = tk.Button(self, text = "Next round", 
                            font = (myFont, 50), bg= bgColour, 
                            bd = 0, command = lambda: showScore1(TeamsScore1, button1), 
                            activebackground= bgColour)
        TeamsScore1 = tk.Label( self, text = "", font = (myFont, 50), wraplength= 1200, 
                                bg= bgColour)

        def showScore1(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n")
            button["command"] = lambda:showScore2(label, button)
        def showScore2(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n")
            button["command"] = lambda:showScore3(label, button)
        def showScore3(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n" +
                                TeamThree.TeamName + ": " + str(TeamThree.TeamScore) + "\n")
            button["command"] = lambda: controller.showFrame(RoundTwo)
        def showScore4(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n" +
                                TeamThree.TeamName + ": " + str(TeamThree.TeamScore) + "\n" +
                                TeamFour.TeamName + ": " + str(TeamFour.TeamScore)+ "\n")
            button["command"] = lambda:controller.showFrame(RoundTwo)
        TeamsScore1.grid(row = 2, column = 2, padx = 400)
        button1.grid(row = 0, column = 3, sticky = "w")
                     
        
#End of first balance round, begin round 2                

class RoundTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg = bgColour)
        #Text button
        title = tk.Button(self, text = "Second Round", 
                           font = (myFont, 50), bg= bgColour, 
                           bd = 0, command = lambda:controller.showFrame(SecondBalanceRound1),  
                           activebackground= bgColour,anchor = "center")
        title.grid(row =1, column =3)   

        

        #disable function for the buttons
        def disableButton(button):
            button["state"] = "disabled"
        
        #All of the questions for the first column including the top text, need to add link to the questions.
        C1Text = tk.Label(self, text = "Oopsies", font = (myFont, 50),
                          bg = bgColour)
        C1Text.grid(row = 2, column = 1)
        Q1Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q1Button),controller.showFrame(Q1b), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q1Button.grid(row = 3, column = 1, padx = 85, pady = 10)

        Q2Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q2Button),controller.showFrame(Q2b), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q2Button.grid(row = 4, column = 1, padx = 85, pady = 10)

        Q3Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q3Button),controller.showFrame(Q3b), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q3Button.grid(row = 5, column = 1, padx = 85, pady = 10)

        Q4Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q4Button),controller.showFrame(Q4b), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q4Button.grid(row = 6, column = 1, padx = 85, pady = 10)

        Q5Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q5Button),controller.showFrame(Q5b), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q5Button.grid(row = 7, column = 1, padx = 85, pady = 10)


        #Row 2 questions, see above               
        C2Text = tk.Label(self, text = "Topics only I care about", font = (myFont, 20), wraplength= 150, 
                          bg = bgColour)
        C2Text.grid(row = 2, column = 2)

        Q6Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q6Button),controller.showFrame(Q6b), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q6Button.grid(row = 3, column = 2, padx = 85, pady = 10)

        Q7Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q7Button),controller.showFrame(Q7b), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q7Button.grid(row = 4, column = 2, padx = 85, pady = 10)

        Q8Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q8Button),controller.showFrame(Q8b), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q8Button.grid(row = 5, column = 2, padx = 85, pady = 10)

        Q9Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q9Button),controller.showFrame(Q9b), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q9Button.grid(row = 6, column = 2, padx = 85, pady = 10)

        Q10Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q10Button),controller.showFrame(Q10b), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q10Button.grid(row = 7, column = 2, padx = 85, pady = 10)
    

        C3Text = tk.Label(self, text = "God has a weird sense of humour", font = (myFont, 20), wraplength= 150, 
                          bg = bgColour)
        C3Text.grid(row = 2, column = 3)

        Q11Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q11Button),controller.showFrame(Q11b), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q11Button.grid(row = 3, column = 3, padx = 85, pady = 10)

        Q12Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q12Button),controller.showFrame(Q12b), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q12Button.grid(row = 4, column = 3, padx = 85, pady = 10)

        Q13Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q13Button),controller.showFrame(Q13b), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q13Button.grid(row = 5, column = 3, padx = 85, pady = 10)

        Q14Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q14Button),controller.showFrame(Q14b), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q14Button.grid(row = 6, column = 3, padx = 85, pady = 10)

        Q15Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q15Button),controller.showFrame(Q15b), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q15Button.grid(row = 7, column = 3, padx = 85, pady = 10)



        C4Text = tk.Label(self, text = "Thats enough internet for today", font = (myFont, 20),wraplength= 150, 
                          bg = bgColour)
        C4Text.grid(row = 2, column = 4)

        Q16Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q16Button),controller.showFrame(Q16b), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q16Button.grid(row = 3, column = 4, padx = 85, pady = 10)

        Q17Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q17Button),controller.showFrame(Q17b), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q17Button.grid(row = 4, column = 4, padx = 85, pady = 10)

        Q18Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q18Button),controller.showFrame(Q18b), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q18Button.grid(row = 5, column = 4, padx = 85, pady = 10)

        Q19Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q19Button),controller.showFrame(Q19b), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q19Button.grid(row = 6, column = 4, padx = 85, pady = 10)

        Q20Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q20Button),controller.showFrame(Q20b), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q20Button.grid(row = 7, column = 4, padx = 85, pady = 10)



        C5Text = tk.Label(self, text = "Yo Ho, Yo Ho", font = (myFont, 40),
                          bg = bgColour)
        C5Text.grid(row = 2, column = 5)

        Q21Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q21Button),controller.showFrame(Q21b), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q21Button.grid(row = 3, column = 5, padx = 85, pady = 10)

        Q22Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q22Button),controller.showFrame(Q22b), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q22Button.grid(row = 4, column = 5, padx = 85, pady = 10)

        Q23Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q23Button),controller.showFrame(Q23b), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q23Button.grid(row = 5, column = 5, padx = 85, pady = 10)

        Q24Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q24Button),controller.showFrame(Q24b), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q24Button.grid(row = 6, column = 5, padx = 85, pady = 10)

        Q25Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q25Button),controller.showFrame(Q25b), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q25Button.grid(row = 7, column = 5, padx = 85, pady = 10)
        
#I'm gonna basically copy paste this, I know I could make it simplier but I honestly dont care.
class Q1b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "In 1666 a huge fire rampaged through this major city for 5 days, all caused by a baker", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "London, UK" 
            button["command"] = lambda:controller.showFrame(RoundTwo)
         
class Q2b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "in 1867 This country sold Alaska for 7.2 million dollars, now Alaska is one of the largest exporter of gold in the US", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Russia" 
            button["command"] = lambda:controller.showFrame(RoundTwo)       
    
class Q3b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "In 1453 while being besieged by the Turks, someone left one of the gates open, leading to the fall of this city", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Constantinople" 
            button["command"] = lambda:controller.showFrame(RoundTwo)

class Q4b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "In 1788 this army broke into 2 parts, split up and ended up massecring each other, the Turks arivied 2 days later to find 10,000 dead soldiers", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Austria" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  
        
class Q5b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This country invaded England in 1349 thinking the black plague was gods vengence, this lead to bringing the black plague back to their country", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Scotland" 
            button["command"] = lambda:controller.showFrame(RoundTwo)    

class Q6b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "The anouncement of this game was delayed due to the Queens death", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Legend of Zelda: Tears of the Kingdom" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q7b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This video game company was sued a mod was discovered enabling a sex mini game", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Rockstar, for GTA San Andres" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q8b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This video game would completely shut down and reboot the orginal xbox console, but the load times were so bad anyone no one noticed", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The Elderscrolls: Morrowind" 
            button["command"] = lambda:controller.showFrame(RoundTwo)

class Q9b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This video game was originally developed as an architecture tool", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The sims" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q10b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This video game holds the record for the longest cutscene at 71 minutes long", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Metal Gear Solid 4" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q11b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This native Australian Animal glows in the dark, and no one knows why", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Platipus" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q12b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "This Amphibious Austalian animal can climb trees", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Crocodile" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q13b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Roughly 10 times more people are killed by this farm animal than killed by sharks", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Cows" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q14b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "When this bird is bored, it will begin eating its friends", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Ducks" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q15b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "When this male insect mates, it's sexual organs explode, causing death", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Bees" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q16b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What if Jod was one of us", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "What if god came down one day and said its pronounced 'Jod'?" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q17b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Oi! Look at this fella..he's of the hairless variety! Rare and silky smooth to the touch, he actually likes when you rub his head! Look at his leg going!", 
                           font = (myFont, 90), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "If Steve Irwin had you in a headlock, what cool facts would he tell the audience" 
            button["command"] = lambda:controller.showFrame(RoundTwo)

class Q18b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Global epidemic crisis. It just started in Wuhan, China. It might take some time though, take a seat", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The Pope slapped a woman on day 1 of 2020, world war III is trending on day 2, what will happen on day 3?" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q19b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "People who have Only fans, what is stopping you from upgrading to an air conditioner?", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "I like talking into it and sounding like a robot" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q20b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text =  "all hogwarts students are required to take a sex ed course. the teacher? hagrid",
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "You take control of JK Rowings twitter account, what do you add to the HP lore?"
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q21b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What Pirate would light he's beard on fire to intimidate prisoners", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Blackbeard" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q22b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is the name of the traditional skull and bones?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Jolly Roger" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q23b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What female pirate set fire to her fathers house when learning she'd been cut off from her inheritance", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Anne Bonne" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q24b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What was the name of Anne Bonny's ship", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The sloop William" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q25b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What pirate Captain was never caught after stealing 85 million in gold", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1000,
                           activebackground= bgColour)
        
        button.pack()
         
        
        def answered(button):
            button["text"] = "Henry Avery" 
            button["command"] = lambda:controller.showFrame(RoundTwo)        
        
class SecondBalanceRound1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Fact or Fiction:\n After the kidnapping of his children, this historical figure travelled to multiple countries to retrieve his kin, murdering the culprit and cementing his legacy", 
                           font = (myFont, 70), bg= bgColour, wraplength= 1200,
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        

        button.pack()

        def answered(button):
            button["text"] = "Fiction, that is the plot of Spyro the dragon" 
            button["command"] = lambda:controller.showFrame(SecondBalanceRound2)
            TeamOne.updateScore(100) 
            TeamTwo.updateScore(100) 
            TeamThree.updateScore(100) 
            TeamFour.updateScore(100) 

class SecondBalanceRound2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Fact or Fiction:\n This historical figure sailed into an unkown Ocean, unaware of if he'll find land. He discovers a new land establishing a presence, after his death his sons saught after his betrayers to seek vengence, conquering this new land once and for all", 
                           font = (myFont, 50), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        
        button.pack()
        def answered(button):
            button["text"] = "Fact. That is Ragnar Lothbrok" 
            button["command"] = lambda:controller.showFrame(SecondBalanceRound3) 
            TeamOne.updateScore(300) 
            TeamTwo.updateScore(300) 
            TeamThree.updateScore(300) 
            TeamFour.updateScore(300) 

class SecondBalanceRound3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
       
        button = tk.Button(self, text = "Seiging this location for almost 2 months, using new invotive technology to persist in the attack. This historical location fell, leading to the fall of the entire empire", 
                           font = (myFont, 70), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "Fact. That is the fall of constantinople" 
            button["command"] = lambda:controller.showFrame(SecondScoreBoard) 
            TeamOne.updateScore(500) 
            TeamTwo.updateScore(500) 
            TeamThree.updateScore(500) 
            TeamFour.updateScore(500)
            

class SecondScoreBoard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button2 = tk.Button(self, text = "Next round", 
                            font = (myFont, 50), bg= bgColour, 
                            bd = 0, command = lambda: showScore1(TeamsScore2, button2), 
                            activebackground= bgColour)
        TeamsScore2 = tk.Label( self, text = "", font = (myFont, 50), wraplength= 1200, 
                                bg= bgColour)

        def showScore1(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n")
            button["command"] = lambda:showScore2(label, button)
        def showScore2(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n")
            button["command"] = lambda:showScore3(label, button)
        def showScore3(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n" +
                                TeamThree.TeamName + ": " + str(TeamThree.TeamScore) + "\n")
            button["command"] = lambda: controller.showFrame(RoundThree)
        def showScore4(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n" +
                                TeamThree.TeamName + ": " + str(TeamThree.TeamScore) + "\n" +
                                TeamFour.TeamName + ": " + str(TeamFour.TeamScore)+ "\n")
            button["command"] = lambda:controller.showFrame(RoundThree)
        TeamsScore2.grid(row = 2, column = 2, padx = 400)
        button2.grid(row = 0, column = 3, sticky = "w")

#End of round 2, begin round 4. ALSO I NEED TO CHANGE THE SCORE WHEN I CLICK ON THE BALANCE ROUNDS 

class RoundThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg = bgColour)
        #Text button
        title = tk.Button(self, text = "Third Round", 
                           font = (myFont, 50), bg= bgColour, 
                           bd = 0, command = lambda:controller.showFrame(ThirdBalanceRound1),  
                           activebackground= bgColour,anchor = "center")
        title.grid(row =1, column =3)   

        

        #disable function for the buttons
        def disableButton(button):
            button["state"] = "disabled"
        
        #All of the questions for the first column including the top text, need to add link to the questions.
        C1Text = tk.Label(self, text = "World dumpster diving", font = (myFont, 30), wraplength= 150, 
                          bg = bgColour)
        C1Text.grid(row = 2, column = 1)
        Q1Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q1Button),controller.showFrame(Q1c), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q1Button.grid(row = 3, column = 1, padx = 85, pady = 10)

        Q2Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q2Button),controller.showFrame(Q2c), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q2Button.grid(row = 4, column = 1, padx = 85, pady = 10)

        Q3Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q3Button),controller.showFrame(Q3c), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q3Button.grid(row = 5, column = 1, padx = 85, pady = 10)

        Q4Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q4Button),controller.showFrame(Q4c), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q4Button.grid(row = 6, column = 1, padx = 85, pady = 10)

        Q5Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q5Button),controller.showFrame(Q5c), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q5Button.grid(row = 7, column = 1, padx = 85, pady = 10)


        #Row 2 questions, see above               
        C2Text = tk.Label(self, text = "If god exists, he hates us", font = (myFont, 30), wraplength= 150, 
                          bg = bgColour)
        C2Text.grid(row = 2, column = 2)

        Q6Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q6Button),controller.showFrame(Q6c), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q6Button.grid(row = 3, column = 2, padx = 85, pady = 10)

        Q7Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q7Button),controller.showFrame(Q7c), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q7Button.grid(row = 4, column = 2, padx = 85, pady = 10)

        Q8Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q8Button),controller.showFrame(Q8c), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q8Button.grid(row = 5, column = 2, padx = 85, pady = 10)

        Q9Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q9Button),controller.showFrame(Q9c), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q9Button.grid(row = 6, column = 2, padx = 85, pady = 10)

        Q10Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q10Button),controller.showFrame(Q10c), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q10Button.grid(row = 7, column = 2, padx = 85, pady = 10)
    

        C3Text = tk.Label(self, text = "A thought with another thoughts hat on", font = (myFont, 20), wraplength= 150, 
                          bg = bgColour)
        C3Text.grid(row = 2, column = 3)

        Q11Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q11Button),controller.showFrame(Q11c), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q11Button.grid(row = 3, column = 3, padx = 85, pady = 10)

        Q12Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q12Button),controller.showFrame(Q12c), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q12Button.grid(row = 4, column = 3, padx = 85, pady = 10)

        Q13Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q13Button),controller.showFrame(Q13c), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q13Button.grid(row = 5, column = 3, padx = 85, pady = 10)

        Q14Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q14Button),controller.showFrame(Q14c), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q14Button.grid(row = 6, column = 3, padx = 85, pady = 10)

        Q15Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q15Button),controller.showFrame(Q15c), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q15Button.grid(row = 7, column = 3, padx = 85, pady = 10)



        C4Text = tk.Label(self, text = "Old timey devices", font = (myFont, 30), wraplength= 150,
                          bg = bgColour)
        C4Text.grid(row = 2, column = 4)

        Q16Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q16Button),controller.showFrame(Q16c), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q16Button.grid(row = 3, column = 4, padx = 85, pady = 10)

        Q17Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q17Button),controller.showFrame(Q17c), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q17Button.grid(row = 4, column = 4, padx = 85, pady = 10)

        Q18Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q18Button),controller.showFrame(Q18c), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q18Button.grid(row = 5, column = 4, padx = 85, pady = 10)

        Q19Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q19Button),controller.showFrame(Q19c), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q19Button.grid(row = 6, column = 4, padx = 85, pady = 10)

        Q20Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q20Button),controller.showFrame(Q20c), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q20Button.grid(row = 7, column = 4, padx = 85, pady = 10)



        C5Text = tk.Label(self, text = "Thats not a real job", font = (myFont, 30), wraplength= 150,
                          bg = bgColour)
        C5Text.grid(row = 2, column = 5)

        Q21Button = tk.Button(self, text = "100", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q21Button),controller.showFrame(Q21c), TeamOne.updateScore(100), TeamTwo.updateScore(100), TeamThree.updateScore(100), TeamFour.updateScore(100)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q21Button.grid(row = 3, column = 5, padx = 85, pady = 10)

        Q22Button = tk.Button(self, text = "200", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q22Button),controller.showFrame(Q22c), TeamOne.updateScore(200), TeamTwo.updateScore(200), TeamThree.updateScore(200), TeamFour.updateScore(200)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q22Button.grid(row = 4, column = 5, padx = 85, pady = 10)

        Q23Button = tk.Button(self, text = "300", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q23Button),controller.showFrame(Q23c), TeamOne.updateScore(300), TeamTwo.updateScore(300), TeamThree.updateScore(300),TeamFour.updateScore(300)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q23Button.grid(row = 5, column = 5, padx = 85, pady = 10)

        Q24Button = tk.Button(self, text = "400", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q24Button),controller.showFrame(Q24c), TeamOne.updateScore(400), TeamTwo.updateScore(400), TeamThree.updateScore(400), TeamFour.updateScore(400)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q24Button.grid(row = 6, column = 5, padx = 85, pady = 10)

        Q25Button = tk.Button(self, text = "500", font = (myFont, 30), 
                            activebackground = bgColour,state = "normal", 
                            command= lambda:[disableButton(Q25Button),controller.showFrame(Q25c), TeamOne.updateScore(500), TeamTwo.updateScore(500), TeamThree.updateScore(500), TeamFour.updateScore(500)],
                            width = 12, height = 1, bg= bgColour, relief = "ridge")
        Q25Button.grid(row = 7, column = 5, padx = 85, pady = 10)
        
#I'm gonna basically copy paste this, I know I could make it simplier but I honestly dont care.
class Q1c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "The only satisfaction I got here was knowing Reinhard Heydich died here", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Hospital" 
            button["command"] = lambda:controller.showFrame(RoundThree)
         
class Q2c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "The kids playing baseball were all terrible", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Park" 
            button["command"] = lambda:controller.showFrame(RoundThree)       
    
class Q3c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "I'd be weary bringing your family here, that Nick guys slept with my wife", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Church" 
            button["command"] = lambda:controller.showFrame(RoundThree)

class Q4c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "No games, No food, there's no fun here", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Laundromat" 
            button["command"] = lambda:controller.showFrame(RoundThree)  
        
class Q5c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Wanted to throw myself off the balcony so bad", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "A highschool" 
            button["command"] = lambda:controller.showFrame(RoundThree)    

class Q6c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Absiophilia", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Attraction to people with impaired mobility" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q7c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Acrotomophilia", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Attraction to amputees" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q8c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Autogynphelia", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Male attraction to oneself in female form" 
            button["command"] = lambda:controller.showFrame(RoundThree)

class Q9c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Nebulophilia", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Feeling aroused by fog" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q10c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Stygiophilia", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Feeling aroused by the thought of damnation or hellfire" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q11c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Armed to the death", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "A 17th century pirate that would carry 4 pistols and a knife in their teeth" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q12c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Butter them up", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "In ancient India, a religious act would involve throwing balls of butter at the statues of their gods" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q13c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Let the cat out of the bag", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "In the 18th century sellers would trick buyers by putting cats in bags, pretending they were valuables" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q14c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Mad as a hatter", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "In the 17th century Hatters would use mercury on hat felt, leading to mercury poisoning" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q15c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Skeleton in the closet", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Pre 1832 teachers would hide illegally obtained skeletons in closets during raids to avoid confistaction" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q16c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is this?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The first electric light" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q17c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is this?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The first popup toaster" 
            button["command"] = lambda:controller.showFrame(RoundThree)

class Q18c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is this?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The first Geiger counter" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q19c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is this?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The first parking meter" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q20c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is this?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "The first lie detector test" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q21c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is advertised", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Chupa Chups" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q22c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is advertised", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Insect Repellant" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q23c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is advertised", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200, 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Batteries" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q24c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is advertised", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button),wraplength= 1200,  
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Mouthwash" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q25c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "What is advertised", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Playstation" 
            button["command"] = lambda:controller.showFrame(RoundThree)        
        
class ThirdBalanceRound1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Have you been paying attention?\n Who was winning at the end of round 1?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button),wraplength= 1200,  
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "I'll write it down" 
            button["command"] = lambda:controller.showFrame(ThirdBalanceRound2) 
            TeamOne.updateScore(100) 
            TeamTwo.updateScore(100) 
            TeamThree.updateScore(100) 
            TeamFour.updateScore(100)

class ThirdBalanceRound2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Have you been paying attention?\n Who got the most points from the 'Shit only I care about section' ?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        
        button.pack()
        def answered(button):
            button["text"] = "I probably wasnt paying attention" 
            button["command"] = lambda:controller.showFrame(ThirdBalanceRound3)
            TeamOne.updateScore(300) 
            TeamTwo.updateScore(300) 
            TeamThree.updateScore(300) 
            TeamFour.updateScore(300)  

class ThirdBalanceRound3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
       
        button = tk.Button(self, text = "Have you been paying attention?\n Who has had the most to drink?", 
                           font = (myFont, 100), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), wraplength= 1200,
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "Answer 2" 
            button["command"] = lambda:controller.showFrame(ThirdScoreBoard)
            TeamOne.updateScore(500) 
            TeamTwo.updateScore(500) 
            TeamThree.updateScore(500) 
            TeamFour.updateScore(500) 
            

class ThirdScoreBoard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Next round", 
                            font = (myFont, 50), bg= bgColour, 
                            bd = 0, command = lambda: showScore1(TeamsScore, button), 
                            activebackground= bgColour)
        TeamsScore = tk.Label( self, text = "", font = (myFont, 50), wraplength= 1200, 
                                bg= bgColour)

        def showScore1(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n")
            button["command"] = lambda:showScore2(label, button)
        def showScore2(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n")
            button["command"] = lambda:showScore3(label, button)
        def showScore3(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n" +
                                TeamThree.TeamName + ": " + str(TeamThree.TeamScore) + "\n")
            button["command"] = lambda: controller.showFrame(Finale)
        def showScore4(label, button):
            label.config(text = "End of round One\n" + TeamOne.TeamName + ": " + str(TeamOne.TeamScore) + "\n" +
                                TeamTwo.TeamName + ": " + str(TeamTwo.TeamScore) + "\n" +
                                TeamThree.TeamName + ": " + str(TeamThree.TeamScore) + "\n" +
                                TeamFour.TeamName + ": " + str(TeamFour.TeamScore)+ "\n")
            button["command"] = lambda:controller.showFrame(Finale)
        TeamsScore.grid(row = 2, column = 2, padx = 300)
        button.grid(row = 0, column = 3, sticky = "w")

class Finale(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        TeamsScore = tk.Button( self, text = "Congrats", font = (myFont, 100), command = lambda: showWinner(TeamsScore), wraplength= 1200, 
                                bg= bgColour, bd = 0)
        def showWinner(button):
            if TeamOne.TeamScore > TeamTwo.TeamScore and TeamOne.TeamScore > TeamThree.TeamScore:
                button["text"] = "Congrate" + TeamOne.TeamName
            elif TeamTwo.TeamScore > TeamOne.TeamScore and TeamTwo.TeamScore > TeamThree.TeamScore:
                button["text"] = "Congrate" + TeamTwo.TeamName
            else:
                button["text"] = "Congrates\n" + TeamThree.TeamName + "!!"
        TeamsScore.pack()
        #Dunno what to put here yet
app = start()

app.mainloop()













