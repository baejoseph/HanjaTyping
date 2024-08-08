# Screen dimensions
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Parameters
PASS_MARK = 8
MAX_MISTAKE = 5
SUPER_FAST_THRESHOLD = 0.35
FAST_THRESHOLD = 0.55
NOT_SHOW_NAME_TIME = 3000
TRANSITION_TIME = 2500

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
AMBER = (255, 191, 0)
RED = (255, 0, 0)
GRAY = (120,120,120)
LIGHT_GRAY = (220,220,220)
COMBOCOLOR1 = (255, 165, 0)
COMBOCOLOR2 = (255, 69, 0)

# Grade-level information
indices = [(0, 49), (50, 99), (100, 149), (150, 224), (225, 347), (348, 447), (448, 547), (548, 796), (797, 1046), (1047, 1546), (1547, 1863), (1864, 2401), (2402, 3546)]

GENS = [
    {"grade": "8",
  "indices": indices[0],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "7II",
  "indices": indices[1],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "7",
  "indices": indices[2],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "6II",
  "indices": indices[3],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "6",
  "indices": indices[4],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "5II",
  "indices": indices[5],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "5",
  "indices": indices[6],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "4II",
  "indices": indices[7],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "4",
  "indices": indices[8],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "3II",
  "indices": indices[9],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "3",
  "indices": indices[10],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "2",
  "indices": indices[11],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
    {"grade": "1",
  "indices": indices[12],
  "bg": "Rock Garden.jpg",
  "music":"Main.mp3"},
]


# Font
FONTPATH = "assets/font1.otf"

REWARD_MAP = {
            1: 100,
            2: 150,
            3: 200,
            4: 250,
            5: 300,
            6: 400,
            7: 500,
            8: 600,
            9: 800,
            10: 1000,
            11: 1200,
            12: 1400,
            13: 1600,
            14: 1800,
            15: 2000,
            16: 2200,
            17: 2400,
            18: 2600,
            19: 2800,
            20: 3000,
        }