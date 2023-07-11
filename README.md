# Introduction to Visual Media Programming - FinalProject
김예서 20200365

![image](https://github.com/marivita126/VMP_FinalProject/assets/89694409/d026d690-5f53-44fa-b32c-a93161b26671)
Youtube Link:

## Introduction
For my final project for 'Introduction to Visual Media Programming', I made a simple game with a theme of a flowerpot falling down a building. The player's goal is to help and save the flowerpot, so it can land safely on the flowerbed on the floor. In this readme file, I will be going over the game and will be going through features I have implemented.

![image](https://github.com/marivita126/VMP_FinalProject/assets/89694409/0faca482-5ccd-4086-9d1a-81d668a758f5)

## Main Features
1. Player image(flowerpot's image) alters according to the current HP status
    - There are in total of 5 different flowerpot images. Which means the HP value is divded into 5 stages. The maximum HP is 100, and when it goes down to 80, the image changes. Again, once it goes down to 60, 40, 20, the image also changes.
3. HP Bar - Shows approximately how much HP is left. Located on the top left corner of the screen.
4. Items/Obstacles
    - There are items that increases HP, and obstacles that decreases HP. There is only one type of item, which is the fertilizer. It is colored yellow, for it to be more noticeable. Once the player collides with the fertizlier, HP increases by 20. On the other hand, there are two types of obstacles. Bird and trash. Bird decreases HP by 30 and trash decreases by 10. In addition, there are three images for trash obstacle, to make the game more interesting. 
5. Tracker - Shows how many meter is left until the flowerpot hits the ground.
    - Once again, the goal for the player is to help the flowerpot to land safely on the flowerbed. On the top right corner, it shows how many meters are left to the ground. So once the player hits 0m, game is cleared. 
6. Game over & Game Clear Screen
    - There is a screen for both circumstances; game over, game clear. Game over happens when the HP hits 0. Game clear happens when the meter tracker on the top right hits 0m.



## Minor Features
1. Sound FX
    - There is sound effect when the bird hits the player(flowerpot), and when the trash hits the player. Game clear and game over has its own sound effect as well.
2. Hit FX
    - There is a hit effect when any obstacle hits the player.
