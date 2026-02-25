import pyautogui
from PIL import Image
import time
import random

IMAGE_PATH = "catn.jpeg"
SCALE_FACTOR = 0.4
LINE_SPACING = 1


def draw_hatching():
    try:

        img = Image.open(IMAGE_PATH).convert('L')
    except FileNotFoundError:
        print("Image introuvable.")
        return

    if SCALE_FACTOR != 1:
        new_size = (int(img.width * SCALE_FACTOR), int(img.height * SCALE_FACTOR))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    width, height = img.size
    
    print("Positionnez la souris en haut à gauche de Paint...")
    time.sleep(5)
    
    start_x, start_y = pyautogui.position()
    
    pyautogui.PAUSE = 0.0000 

    for y in range(0, height, LINE_SPACING):
        is_drawing = False
        print(f"Processing line {y}/{height} ({y/height*100:.2f}%)")
        for x in range(width):
      
            pixel = img.getpixel((x, y))
            chance_de_cliquer = (255 - pixel) / 255
            
            if  not is_drawing and random.random() < chance_de_cliquer:
                pyautogui.moveTo(start_x + x, start_y + y)
                pyautogui.mouseDown()
                is_drawing = True
            elif is_drawing and random.random() < chance_de_cliquer:
                pyautogui.moveTo(start_x + x, start_y + y)
            elif is_drawing and random.random() > chance_de_cliquer:
                pyautogui.mouseUp()
                is_drawing = False
        
        if is_drawing:
            pyautogui.mouseUp()


    print("Hachures terminées !")

if __name__ == "__main__":
    draw_hatching()

