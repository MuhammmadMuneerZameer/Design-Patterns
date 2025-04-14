class AppConfig:
    _instance = None

    def __new__(cls):  # Corrected method name here
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            # Initialize default settings
            cls._instance.volume = 50
            cls._instance.screen_resolution = "1920x1080"
            cls._instance.difficulty_level = "Normal"
        return cls._instance

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
sett1 = AppConfig()
set2 = AppConfig()

sett1.setDifficulty("Legends")
set2.setVolume(33)

sett1.displaySettings()
set2.displaySettings()

print("Same instance?", sett1 is set2)  # Output: True
