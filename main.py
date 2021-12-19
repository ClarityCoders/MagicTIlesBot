import cv2
import d3dshot
import keyboard
import time

"""
Before running this file you need to setup you locations on your screen!
Use screenshot to disk to find your game window then open that in paint.
Using that screen show find the X, Y location of each lane!

Have questions? https://discord.gg/cAWW5qq
Want to watch me use it on Magic Tiles 3? youtube.com/claritycoders
"""

d = d3dshot.create(capture_output="numpy")

# Get test screen shot
#d.screenshot_to_disk(file_name="Test.png", region=(0,40,580,1040))

# Define our locations
locations = [
    {
        'press': False,
        'loc': (763, 100),
        'key': 'a',
    },
    {
        'press': False,
        'loc': (763, 250),
        'key': 's'
    },
    {
        'press': False,
        'loc': (763, 400),
        'key': 'd'
    },
    {
        'press': False,
        'loc': (763, 550),
        'key': 'f'
    }
]

print('Starting in 3...')
time.sleep(3)
while True:
    start_time = time.time() 
    img = d.screenshot(region=(0,40,580,1040))

    for location in locations:
        value = sum(img[location['loc']])
        # if location['key'] == 'a':
        #     print(img[location['loc']])
        if value < 50 or img[location['loc']][0] == 0:
            keyboard.press(location['key'])
            #time.sleep(.1)
        else:
            keyboard.release(location['key'])

    if keyboard.is_pressed('q'):
        break
    #print("FPS: ", 1.0 / (time.time() - start_time))