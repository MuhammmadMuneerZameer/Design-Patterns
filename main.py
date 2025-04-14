class GameSettingsManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameSettingsManager, cls).__new__(cls)
            # Initialize default settings
            cls._instance.volume = 50
            cls._instance.screen_resolution = "1920x1080"
            cls._instance.difficulty_level = "Normal"
        return cls._instance

    def set_volume(self, value):
        self.volume = value

    def set_resolution(self, resolution):
        self.screen_resolution = resolution

    def set_difficulty(self, level):
        self.difficulty_level = level

    def display_settings(self):
        print("Volume:", self.volume)
        print("Resolution:", self.screen_resolution)
        print("Difficulty:", self.difficulty_level)


# Usage example:
settings1 = GameSettingsManager()
settings2 = GameSettingsManager()

settings1.set_volume(40)
settings2.set_difficulty("Legends")

# Both objects point to the same instance
settings1.display_settings()
settings2.display_settings()

print("Same instance?", settings1 is settings2)  # Output: True
