from ctypes import *
import random
import time
import yaml
import sys

MINUTES = 30

WORKOUTS = [
  'Archer Pushups 🏹 | 5x Each Side',
  'Diamond Pushups 💎 | 10x',
  'Pistol Squats 🔫 | 5x Each Side',
  'Clap Pushups 👏 | 10x',
  'Shrimp Squats 🍤 | 10x Each Side',
  'Plank 🌳 | 1m Hold',
  'Burpee 😰 | 10x',
]

def main():
  try: 
    global WORKOUTS
    global MINUTES
    config = yaml.safe_load(open("workouts.yml"))
    selected_workout = config['selectedWorkout']
    WORKOUTS = config[selected_workout]
    MINUTES = config['minutesBetweenWorkouts']
  except Exception as e:
    if e.args[0] == 2:
      windll.user32.MessageBoxW(0, f'No workouts.yml file found! Place config file in the same directory as this executable to set timer and customize your own exercises!', "Whoops!", 0)
    else:
      windll.user32.MessageBoxW(0, f'Something went wrong when loading the config file!\n\nPlease double check that the formatting is correct for your changes to take effect.', "Whoops!", 0)
  
  sleeptime = 60 * MINUTES 
  while(1):
    workout = random.choice(WORKOUTS)
    test = windll.user32.MessageBoxW(0, f'{workout} \n\nShow new workout in {MINUTES} minutes?', "Workout Time 💪", 4)
    if test == 7:
      sys.exit()
    time.sleep(sleeptime)

main()