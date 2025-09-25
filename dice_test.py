
# py -m pip install keyboard

import time
import os
# To use any `random` functions, we must first `import random`:
import random

dice_num_1_path = r"/workspaces/skole_dice_test/dice_side_num_1_ASCII.txt"
dice_num_2_path = r"/workspaces/skole_dice_test/dice_side_num_2_ASCII.txt"
dice_num_3_path = r"/workspaces/skole_dice_test/dice_side_num_3_ASCII.txt"
dice_num_4_path = r"/workspaces/skole_dice_test/dice_side_num_4_ASCII.txt"
dice_num_5_path = r"/workspaces/skole_dice_test/dice_side_num_5_ASCII.txt"
dice_num_6_path = r"/workspaces/skole_dice_test/dice_side_num_6_ASCII.txt"


toss_frame_6_path = r"/workspaces/skole_dice_test/toss_frames/toss_frame_6_ASCII.txt"
toss_frame_5_path = r"/workspaces/skole_dice_test/toss_frames/toss_frame_5_ASCII.txt"
toss_frame_4_path = r"/workspaces/skole_dice_test/toss_frames/toss_frame_4_ASCII.txt"
toss_frame_3_path = r"/workspaces/skole_dice_test/toss_frames/toss_frame_3_ASCII.txt"
toss_frame_2_path = r"/workspaces/skole_dice_test/toss_frames/toss_frame_2_ASCII.txt"
toss_frame_1_path = r"/workspaces/skole_dice_test/toss_frames/toss_frame_1_ASCII.txt"

start_text_ASCII = r"/workspaces/skole_dice_test/start_text_ASCII.txt"
reroll_text_ASCII = r"/workspaces/skole_dice_test/reroll_text_ASCII.txt"

git_dice_num_1_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/dice_side_num_1_ASCII.txt"
git_dice_num_2_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/dice_side_num_2_ASCII.txt"
git_dice_num_3_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/dice_side_num_3_ASCII.txt"
git_dice_num_4_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/dice_side_num_4_ASCII.txt"
git_dice_num_5_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/dice_side_num_5_ASCII.txt"
git_dice_num_6_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/dice_side_num_6_ASCII.txt"

git_toss_frame_6_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/toss_frames/toss_frame_6_ASCII.txt"
git_toss_frame_5_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/toss_frames/toss_frame_5_ASCII.txt"
git_toss_frame_4_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/toss_frames/toss_frame_4_ASCII.txt"
git_toss_frame_3_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/toss_frames/toss_frame_3_ASCII.txt"
git_toss_frame_2_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/toss_frames/toss_frame_2_ASCII.txt"
git_toss_frame_1_path = r"/Users/wilton/Documents/GitHub/skole_dice_test/toss_frames/toss_frame_1_ASCII.txt"

git_start_text_ASCII = r"/Users/wilton/Documents/GitHub/skole_dice_test/start_text_ASCII.txt"
git_reroll_text_ASCII = r"/Users/wilton/Documents/GitHub/skole_dice_test/reroll_text_ASCII.txt"
curnet_num = int(1)


git_dice_num_frames = [
    git_dice_num_1_path,
    git_dice_num_2_path,
    git_dice_num_3_path,
    git_dice_num_4_path,
    git_dice_num_5_path,
    git_dice_num_6_path,
]
dice_num_frames = [
    dice_num_1_path,
    dice_num_2_path,
    dice_num_3_path,
    dice_num_4_path,
    dice_num_5_path,
    dice_num_6_path,
]

git_toss_anim_frames = [
    git_toss_frame_1_path,
    git_toss_frame_2_path,
    git_toss_frame_3_path,
    git_toss_frame_4_path,
    git_toss_frame_5_path,
    git_toss_frame_6_path
]

toss_anim_frames = [
    toss_frame_1_path,
    toss_frame_2_path,
    toss_frame_3_path,
    toss_frame_4_path,
    toss_frame_5_path,
    toss_frame_6_path
]


start_up = bool(True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")  # clear screen
def roll_num():
        dice_roll = random.randint(0, 5)
        print(f"Dice roll: {dice_roll}")
        return dice_roll
def roll(roll_num, Speed,):
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")  # clear screen
    #try:
        #for frame in toss_anim_frames:
            #os.system("cls" if os.name == "nt" else "clear")  # clear screen
            #with open(frame, "r", encoding="utf-8") as f:
                #os.system("cls" if os.name == "nt" else "clear")  # clear screen
                #print(f.read())
            #time.sleep(Speed)  # delay between frames
            
        #if frame == toss_anim_frames[5]:
            #os.system("cls" if os.name == "nt" else "clear")  # clear screen
            #with open(dice_num_frames[roll_num], "r", encoding="utf-8") as f:
                #print(f.read())         
           # time.sleep(2)  # delay between frames
           # roll_number = str(roll_num + 1)
            #print("you rolled a ", roll_number)
           # print(input("Press Enter to roll again..."))
           # return
    try:
        for frame in git_toss_anim_frames:
            clear_screen()
            with open(frame, "r", encoding="utf-8") as f:
                print(f.read())
            time.sleep(Speed)  # delay between frames
        if frame == git_toss_anim_frames[5]:
            clear_screen()
            with open(git_dice_num_frames[roll_num], "r", encoding="utf-8") as f:
                print(f.read())
            time.sleep(2)  # delay between frames
            roll_number = str(roll_num + 1)
            print("you rolled a ", roll_number)
            print(input("Press Enter to roll again..."))
            return
    except:
        print("An error occurred. Please try again.")
        return

while True:
    try:
        if start_up == False:
            roll(roll_num(), 0.3)
        elif start_up == True:
            start_up = False
            os.system("cls" if os.name == "nt" else "clear")  # clear screen
            #try:
                #with open(start_text_ASCII, "r", encoding="utf-8") as f:
                    #print(f.read())
                    #print(input())
                    #time.sleep(1)  # delay between frames
            with open(git_start_text_ASCII, "r", encoding="utf-8") as f:
                print(f.read())
                print(input())
                time.sleep(1)  # delay between frames
            os.system("cls" if os.name == "nt" else "clear")  # clear screen
            roll(roll_num(), 0.3)
            start_up = bool(False)
        
    except:
        print("An error occurred. Please try again.")
        #test 4 