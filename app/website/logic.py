class Shot():
    def __init__(self, startDistance, startLie, finishDistance, finishLie, baseline):
        self.startDistance = startDistance
        self.startLie = startLie
        self.finishDistance = finishDistance
        self.finishLie = finishLie
        self.baseline = baseline
    
    def lookupShot(self, df, code, lookupColumn):
        return df.loc[df.shotcode == code, lookupColumn].values[0]

    def calcShotValue(self, df): 
        if self.finishDistance == str(0):
            return round(self.lookupShot(df, str(self.startDistance) + self.startLie, self.baseline) - 1,2)

        return round(self.lookupShot(df, str(self.startDistance) + self.startLie, self.baseline) - self.lookupShot(df, str(self.finishDistance) + self.finishLie, self.baseline) - 1,2)
  
    def shotNotValid(self):
        return any([
            self.startDistance == '' or self.finishDistance == '',
            int(self.startDistance) > 119 and self.startLie == 'g',
            int(self.finishDistance) > 119 and self.finishLie == 'g',
            self.startLie == 'h',
            self.finishLie == 'h' and self.finishDistance != str(0),
        ])
    

    
