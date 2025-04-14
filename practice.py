class game:
    instancce=None
    def __new__(cls):
        if cls.instancce is None:
            cls.instancce = super(game, cls).__new__(cls)
            # Initialize default settings
            cls.instancce.volume = 50
            cls.instancce.screen_resolution = "1920x1080"
            cls.instancce.difficulty_level = "Normal"
        return cls.instancce
    def setVolume(self, value):
        self.volume = value
    def setResolution(self, resolution):
        self.screen_resolution = resolution
    def setDifficulty(self, level):
        self.difficulty_level = level
    def displaySettings(self):
        print("Volume:", self.volume)
        print("Resolution:", self.screen_resolution)
        print("Difficulty:", self.difficulty_level)
# Usage example:    
settings1=game()
setting2=game()
settings1.setVolume(33)
setting2.setDifficulty("Legends")
settings1.displaySettings()
setting2.displaySettings()
print("Same instance?", settings1 is setting2)  # Output: True 