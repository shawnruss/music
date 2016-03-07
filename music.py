class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print(self.sounds[i % len(self.sounds)], end=" ")
        print()

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print("Be with you in a moment")
        print("Twoning, sproing, splang")
        
class Drummer(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super().__init__(["Bom Bom", "Kaboom", "Crash"])
    
    def count(self):
        for n in range (1, 5):
            print(n)
        #print(" duh ... what's next")
    
    def spontaneously_combust(self):
        print(".......... WHOOOMPA!!")
    
class Band():
    def __init__(self, drummer):
        self.musicians = []
        self.musicians.append(drummer)
    
    def hireMuso(self, muso):
        self.musicians.append(muso)
    
    def fireMuso(self, muso):
        self.musicians.remove(muso)
        
    def playSolos(self):
        self.musicians[0].count()
        for musician in self.musicians:
            musician.solo(6)
        
# find a drummer
theDrummer = Drummer()

# form the band
theBand = Band(theDrummer)

# hire the other musos
theBassist = Bassist()
theGuitarist = Guitarist()
theBand.hireMuso(theBassist)
theBand.hireMuso(theGuitarist)

# play the solos
theBand.playSolos()

# fire the musos, except for the drummer
theBand.fireMuso(theBassist)

# drummer combusts
theDrummer.spontaneously_combust()
