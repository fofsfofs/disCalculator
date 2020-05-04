# disCalculator

Since we are students, we are pretty lazy. Thus, we created the bot to be able to take in a submitted picture by the user which outputs a picture of the solved problem as an image. The bot is able to solve (find roots), simplify, expand, differentiate, and integrate equations - all from just being given a picture! It first displays the received image through LaTeX so users are able to check if your image has been properly converted, then it instantly displays an image to the solution to your problem!

This discord bot was made by [Farhan](https://github.com/fofsfofs), [Shoeb](https://github.com/Dhruvooo), [Erio](https://github.com/mrerioh), and [Sanjeev](https://github.com/sanjeev2001) for TOHacks 2020

## Accessing the bot

An invite link to the bot can be found at: https://mrerioh.github.io/discalculatorsite/

## How it works

We used a multitude of technologies for the creation of our bot including the Python programming language, Discord Developer Platform, and the Mathpix, Pillow, and Wolfram|Alpha APIs. The Discord Developer Platform was used to create and host the app within Discords servers. Integration of Discord was done through syncing the discord API through our scripts. The Mathpix API was integrated to display images by converting them from an image to LaTeX which was aided by Pillow (also known as PIL) which helps to manipulate the file through saving it in a suitable format. The Wolfram|Alpha API is used by querying the converted LaTeX text alongside a keyword given by the user.

## How to use the bot

Simply type ``` .code ``` followed by your command and paste an image. To see all the commands, type ``` .help ```

Here is an example of how to use the bot:
 
<p align="center">
  <img src="/ezgif-3-a7849cefa6b7.gif">
</p>
