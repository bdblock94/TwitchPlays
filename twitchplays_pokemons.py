import concurrent.futures
import random
import keyboard
import pydirectinput
import pyautogui
import pyvjoy
import TwitchPlays_Connection
import pyautogui as pag
import pygetwindow as gw
from TwitchPlays_KeyCodes import *

##################### GAME VARIABLES #####################

# Replace this with your Twitch username. Must be all lowercase.
TWITCH_CHANNEL = 'viridianwave' 

# If streaming on Youtube, set this to False
STREAMING_ON_TWITCH = True

# If you're streaming on Youtube, replace this with your Youtube's Channel ID
# Find this by clicking your Youtube profile pic -> Settings -> Advanced Settings
YOUTUBE_CHANNEL_ID = "YOUTUBE_CHANNEL_ID_HERE" 

# If you're using an Unlisted stream to test on Youtube, replace "None" below with your stream's URL in quotes.
# Otherwise you can leave this as "None"
YOUTUBE_STREAM_URL = None

##################### MESSAGE QUEUE VARIABLES #####################

# MESSAGE_RATE controls how fast we process incoming Twitch Chat messages. It's the number of seconds it will take to handle all messages in the queue.
# This is used because Twitch delivers messages in "batches", rather than one at a time. So we process the messages over MESSAGE_RATE duration, rather than processing the entire batch at once.
# A smaller number means we go through the message queue faster, but we will run out of messages faster and activity might "stagnate" while waiting for a new batch. 
# A higher number means we go through the queue slower, and messages are more evenly spread out, but delay from the viewers' perspective is higher.
# You can set this to 0 to disable the queue and handle all messages immediately. However, then the wait before another "batch" of messages is more noticeable.
MESSAGE_RATE = 0.5
# MAX_QUEUE_LENGTH limits the number of commands that will be processed in a given "batch" of messages. 
# e.g. if you get a batch of 50 messages, you can choose to only process the first 10 of them and ignore the others.
# This is helpful for games where too many inputs at once can actually hinder the gameplay.
# Setting to ~50 is good for total chaos, ~5-10 is good for 2D platformers
MAX_QUEUE_LENGTH = 50
MAX_WORKERS = 100 # Maximum number of threads you can process at a time 

j = pyvjoy.VJoyDevice(1)
j2 = pyvjoy.VJoyDevice(2)

last_time = time.time()
message_queue = []
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS)
active_tasks = []
pyautogui.FAILSAFE = False
WINDOW_NAME = "Gameboy Advance - Pokemon - Firered Version (USA, Europe) (Rev 1)"
##########################################################

# Count down before starting, so you have time to load up the game
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

if STREAMING_ON_TWITCH:
    t = TwitchPlays_Connection.Twitch()
    t.twitch_connect(TWITCH_CHANNEL)
else:
    t = TwitchPlays_Connection.YouTube()
    t.youtube_connect(YOUTUBE_CHANNEL_ID, YOUTUBE_STREAM_URL)

def handle_message(message):
    try:
        msg = message['message'].lower()
        username = message['username'].lower()

        # Now that you have a chat message, this is where you add your game logic.
        # Use the "HoldKey(KEYCODE)" function to permanently press and hold down a key.
        # Use the "ReleaseKey(KEYCODE)" function to release a specific keyboard key.
        # Use the "HoldAndReleaseKey(KEYCODE, SECONDS)" function press down a key for X seconds, then release it.
        # Use the pydirectinput library to press or move the mouse

        # I've added some example videogame logic code below:

        ###################################
        # Example GTA V Code 
        ###################################

        if msg == "UP" or msg =="u": 
            j.set_button(1,1)
            time.sleep(.2)
            j.set_button(1,0)
            print("We go " + "up")

        if msg == "down" or msg =="d": 
            j.set_button(2,1)
            time.sleep(.2)
            j.set_button(2,0)
            print("We go " + "down")

        if msg == "left" or msg =="l": 
            j.set_button(3,1)
            time.sleep(.2)
            j.set_button(3,0)
            print("We go " + "left")

        if msg == "right" or msg =="r": 
            j.set_button(4,1)
            time.sleep(.2)
            j.set_button(4,0)
            print("We go " + "right")

        if msg == "longup" or msg =="lu": 
            j.set_button(1,1)
            time.sleep(.8)
            j.set_button(1,0)
            print("We go " + "upper")

        if msg == "longdown" or msg =="ld": 
            j.set_button(2,1)
            time.sleep(.8)
            j.set_button(2,0)
            print("We go " + "downer")

        if msg == "longleft" or msg =="ll": 
            j.set_button(3,1)
            time.sleep(.8)
            j.set_button(3,0)
            print("We go " + "lefter")

        if msg == "longright" or msg =="lr": 
            j.set_button(4,1)
            time.sleep(.8)
            j.set_button(4,0)
            print("We go " + "righter")

        if msg == "^": 
            j.set_button(1,1)
            time.sleep(.2)
            j.set_button(1,0)
            print("We go " + "up")

        if msg == "v": 
            j.set_button(2,1)
            time.sleep(.2)
            j.set_button(2,0)
            print("We go " + "down")

        if msg == "<": 
            j.set_button(3,1)
            time.sleep(.2)
            j.set_button(3,0)
            print("We go " + "left")

        if msg == ">": 
            j.set_button(4,1)
            time.sleep(.2)
            j.set_button(4,0)
            print("We go " + "right")

        if msg == "^^": 
            j.set_button(1,1)
            time.sleep(.8)
            j.set_button(1,0)
            print("We go " + "upper")

        if msg == "vv": 
            j.set_button(2,1)
            time.sleep(.8)
            j.set_button(2,0)
            print("We go " + "downer")

        if msg == "<<": 
            j.set_button(3,1)
            time.sleep(.8)
            j.set_button(3,0)
            print("We go " + "lefter")

        if msg == ">>": 
            j.set_button(4,1)
            time.sleep(.8)
            j.set_button(4,0)
            print("We go " + "righter")

        if msg == "a": 
            j.set_button(5,1)
            time.sleep(.2)
            j.set_button(5,0)
            print("We go " + "a")

        if msg == "b": 
            j.set_button(6,1)
            time.sleep(.2)
            j.set_button(6,0)
            print("We go " + "b")

        if msg == "select": 
            j.set_button(7,1)
            time.sleep(.2)
            j.set_button(7,0)
            print("We go " + "select")

        if msg == "start": 
            j.set_button(8,1)
            time.sleep(.2)
            j.set_button(8,0)
            print("We go " + "start")
        
        if msg == "save":
           if username == 'angrydemonnoises' or username == 'viridianwave' or username == 'amoop15' or username == 'krazykillzone' or username == 'beri':
                j2.set_button(1,1)
                time.sleep(.2)
                j2.set_button(1,0)
                print("We save")


        ####################################
        ####################################

    except Exception as e:
        print("Encountered exception: " + str(e))


while True:

    active_tasks = [t for t in active_tasks if not t.done()]

    #Check for new messages
    new_messages = t.twitch_receive_messages();
    if new_messages:
        message_queue += new_messages; # New messages are added to the back of the queue
        message_queue = message_queue[-MAX_QUEUE_LENGTH:] # Shorten the queue to only the most recent X messages

    messages_to_handle = []
    if not message_queue:
        # No messages in the queue
        last_time = time.time()
    else:
        # Determine how many messages we should handle now
        r = 1 if MESSAGE_RATE == 0 else (time.time() - last_time) / MESSAGE_RATE
        n = int(r * len(message_queue))
        if n > 0:
            # Pop the messages we want off the front of the queue
            messages_to_handle = message_queue[0:n]
            del message_queue[0:n]
            last_time = time.time();

    # If user presses Shift+Backspace, automatically end the program
    if keyboard.is_pressed('shift+backspace'):
        exit()

    if not messages_to_handle:
        continue
    else:
        for message in messages_to_handle:
            if len(active_tasks) <= MAX_WORKERS:
                active_tasks.append(thread_pool.submit(handle_message, message))
            else:
                print(f'WARNING: active tasks ({len(active_tasks)}) exceeds number of workers ({MAX_WORKERS}). ({len(message_queue)} messages in the queue)')
 
