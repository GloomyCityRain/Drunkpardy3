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
TeamOne = ScoreManager("Team One", 0, 0, 0)  
TeamTwo = ScoreManager("Team Two", 0, 0, 0)
TeamThree = ScoreManager("Team Three", 0, 0, 0) 
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
        C1Text = tk.Label(self, text = "Question 1", font = (myFont, 50),
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
        C2Text = tk.Label(self, text = "Question 2", font = (myFont, 50),
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
    

        C3Text = tk.Label(self, text = "Question 3", font = (myFont, 50),
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



        C4Text = tk.Label(self, text = "Question 4", font = (myFont, 50),
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



        C5Text = tk.Label(self, text = "Question 5", font = (myFont, 50),
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
        
        button = tk.Button(self, text = "Question One", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerOne" 
            button["command"] = lambda:controller.showFrame(RoundOne)
         
class Q2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Two", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerTwo" 
            button["command"] = lambda:controller.showFrame(RoundOne)       
    
class Q3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Three", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerThree" 
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
            button["text"] = "AnswerFour" 
            button["command"] = lambda:controller.showFrame(RoundOne)  
        
class Q5(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Five", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerFive" 
            button["command"] = lambda:controller.showFrame(RoundOne)    

class Q6(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Six", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerSix" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q7(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Seven", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerSeven" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q8(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Eight", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerEight" 
            button["command"] = lambda:controller.showFrame(RoundOne)

class Q9(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Nine", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerNine" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q10(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 10", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 10" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q11(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 11", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 11" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q12(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 12", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerTen" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q13(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 13", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 13" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q14(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 14", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 14" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q15(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 15", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 15" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q16(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 16", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 16" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q17(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 17", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 17" 
            button["command"] = lambda:controller.showFrame(RoundOne)

class Q18(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 18", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 18" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q19(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 19", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 19" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q20(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 20", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 20" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q21(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 21", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 22" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q22(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 22", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 22" 
            button["command"] = lambda:controller.showFrame(RoundOne) 

class Q23(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 23", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 23" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q24(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 24", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 24" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class Q25(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 25", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 25" 
            button["command"] = lambda:controller.showFrame(RoundOne)  

class FirstBalanceRound1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 1", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()

        def answered(button):
            button["text"] = "Answer 1" 
            button["command"] = lambda:controller.showFrame(FirstBalanceRound2)
            TeamOne.updateScore(100) 
            TeamTwo.updateScore(100) 
            TeamThree.updateScore(100) 
            TeamFour.updateScore(100) 

class FirstBalanceRound2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 2", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()
        def answered(button):
            button["text"] = "Answer 2" 
            button["command"] = lambda:controller.showFrame(FirstBalanceRound3)
            TeamOne.updateScore(300) 
            TeamTwo.updateScore(300) 
            TeamThree.updateScore(300) 
            TeamFour.updateScore(300)  

class FirstBalanceRound3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
       
        button = tk.Button(self, text = "Question 3", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "Answer 2" 
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
        TeamsScore1 = tk.Label( self, text = "", font = (myFont, 100), 
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
            button["command"] = lambda: controller.showframe(RoundTwo)
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
        C1Text = tk.Label(self, text = "Question 7", font = (myFont, 50),
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
        C2Text = tk.Label(self, text = "Question 2", font = (myFont, 50),
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
    

        C3Text = tk.Label(self, text = "Question 3", font = (myFont, 50),
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



        C4Text = tk.Label(self, text = "Question 4", font = (myFont, 50),
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



        C5Text = tk.Label(self, text = "Question 5", font = (myFont, 50),
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
        
        button = tk.Button(self, text = "Question 1", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerOne" 
            button["command"] = lambda:controller.showFrame(RoundTwo)
         
class Q2b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Two", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerTwo" 
            button["command"] = lambda:controller.showFrame(RoundTwo)       
    
class Q3b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Three", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerThree" 
            button["command"] = lambda:controller.showFrame(RoundTwo)

class Q4b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Four", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerFour" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  
        
class Q5b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Five", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerFive" 
            button["command"] = lambda:controller.showFrame(RoundTwo)    

class Q6b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Six", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerSix" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q7b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Seven", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerSeven" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q8b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Eight", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerEight" 
            button["command"] = lambda:controller.showFrame(RoundTwo)

class Q9b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Nine", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerNine" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q10b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 10", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 10" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q11b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 11", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 11" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q12b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 12", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerTen" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q13b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 13", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 13" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q14b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 14", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 14" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q15b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 15", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 15" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q16b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 16", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 16" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q17b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 17", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 17" 
            button["command"] = lambda:controller.showFrame(RoundTwo)

class Q18b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 18", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 18" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q19b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 19", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 19" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q20b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 20", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 20" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q21b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 21", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 22" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q22b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 22", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 22" 
            button["command"] = lambda:controller.showFrame(RoundTwo) 

class Q23b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 23", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 23" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q24b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 24", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 24" 
            button["command"] = lambda:controller.showFrame(RoundTwo)  

class Q25b(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 25", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 25" 
            button["command"] = lambda:controller.showFrame(RoundTwo)        
        
class SecondBalanceRound1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 3", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        

        button.pack()

        def answered(button):
            button["text"] = "Answer 1" 
            button["command"] = lambda:controller.showFrame(SecondBalanceRound2)
            TeamOne.updateScore(100) 
            TeamTwo.updateScore(100) 
            TeamThree.updateScore(100) 
            TeamFour.updateScore(100) 

class SecondBalanceRound2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 4", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()
        def answered(button):
            button["text"] = "Answer 2" 
            button["command"] = lambda:controller.showFrame(SecondBalanceRound3) 
            TeamOne.updateScore(300) 
            TeamTwo.updateScore(300) 
            TeamThree.updateScore(300) 
            TeamFour.updateScore(300) 

class SecondBalanceRound3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
       
        button = tk.Button(self, text = "Question 6", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "Answer 2" 
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
        TeamsScore2 = tk.Label( self, text = "", font = (myFont, 100), 
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
            button["command"] = lambda: controller.showframe(RoundThree)
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
        C1Text = tk.Label(self, text = "Question 7", font = (myFont, 50),
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
        C2Text = tk.Label(self, text = "Question 2", font = (myFont, 50),
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
    

        C3Text = tk.Label(self, text = "Question 3", font = (myFont, 50),
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



        C4Text = tk.Label(self, text = "Question 4", font = (myFont, 50),
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



        C5Text = tk.Label(self, text = "Question 5", font = (myFont, 50),
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
        
        button = tk.Button(self, text = "Question 1c", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerOne" 
            button["command"] = lambda:controller.showFrame(RoundThree)
         
class Q2c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Twoc", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerTwo" 
            button["command"] = lambda:controller.showFrame(RoundThree)       
    
class Q3c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Threec", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerThree" 
            button["command"] = lambda:controller.showFrame(RoundThree)

class Q4c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Four", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerFour" 
            button["command"] = lambda:controller.showFrame(RoundThree)  
        
class Q5c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Five", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerFive" 
            button["command"] = lambda:controller.showFrame(RoundThree)    

class Q6c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Six", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerSix" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q7c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Seven", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerSeven" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q8c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Eight", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerEight" 
            button["command"] = lambda:controller.showFrame(RoundThree)

class Q9c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question Nine", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerNine" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q10c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 10", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 10" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q11c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 11", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 11" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q12c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 12", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "AnswerTen" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q13c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 13", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 13" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q14c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 14", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 14" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q15c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 15", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 15" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q16c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 16", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 16" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q17c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 17", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 17" 
            button["command"] = lambda:controller.showFrame(RoundThree)

class Q18c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 18", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 18" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q19c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 19", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 19" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q20c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 20", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 20" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q21c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 21", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 22" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q22c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 22", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 22" 
            button["command"] = lambda:controller.showFrame(RoundThree) 

class Q23c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 23", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 23" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q24c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 24", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 24" 
            button["command"] = lambda:controller.showFrame(RoundThree)  

class Q25c(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 25", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        button.pack()
         
        
        def answered(button):
            button["text"] = "Answer 25" 
            button["command"] = lambda:controller.showFrame(RoundThree)        
        
class ThirdBalanceRound1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 3", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()

        def answered(button):
            button["text"] = "Answer 1" 
            button["command"] = lambda:controller.showFrame(ThirdBalanceRound2) 
            TeamOne.updateScore(100) 
            TeamTwo.updateScore(100) 
            TeamThree.updateScore(100) 
            TeamFour.updateScore(100)

class ThirdBalanceRound2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
        
        button = tk.Button(self, text = "Question 4", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
                           activebackground= bgColour)
        
        button.pack()
        def answered(button):
            button["text"] = "Answer 2" 
            button["command"] = lambda:controller.showFrame(ThirdBalanceRound3)
            TeamOne.updateScore(300) 
            TeamTwo.updateScore(300) 
            TeamThree.updateScore(300) 
            TeamFour.updateScore(300)  

class ThirdBalanceRound3(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg = bgColour)
       
        button = tk.Button(self, text = "Question 6", 
                           font = (myFont, 200), bg= bgColour, 
                           bd = 0, command = lambda: answered(button), 
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
        TeamsScore = tk.Label( self, text = "", font = (myFont, 100), 
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
        #Dunno what to put here yet
app = start()

app.mainloop()













