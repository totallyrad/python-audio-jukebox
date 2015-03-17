#!/usr/bin/env python

from time import sleep
import os
import RPi.GPIO as GPIO

#setup buttons as inputs
GPIO.setmode(GPIO.BCM)
#sSets up GPIO pins
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.IN)
GPIO.setup(25, GPIO.IN)

#sets "playing" to false
#this lets us stop the player
#on a press if the sound is playing  

playing=0

#runs the indented code forever
#"while" tells the program to keep 
#doing something until the second 
#part is false. I made it "True" so 
#it will loop forever

while True:
        #if a sounds is not playing do this
        if ( playing == 0):
                #if someone pressons button one play ska
                if ( GPIO.input(23) == False ):
                        os.system('sudo mpg321 -Z /Music/Ska/* ')
                        #set 'playing' value to 'true'
                        playing = 1
                #if someone pushes button 2 play Pop Punk
                if ( GPIO.input(24) == False ):
                        os.system('sudo mpg321 -Z /Music/PopPunk/* ')
                        #set 'playing' value to 'true'
                        playing = 1
                #if soeone pushed button 3 play Covers
                if ( GPIO.input(25) == False ):
                        os.system('sudo mpg321 -Z /Music/PunkCovers/* ')
                        #set 'playing' value to 'true'
                        playing = 1

        #if a sound is not playing do this
        else:
                #if either button is pressed and a sound is playing STOP IT!
                if( GPIO.input(23) == False or GPIO.input(24) == False or GPIO.input(25) == False):
                        #stops the sound
                        os.system('sudo pkill -SIGKILL mpg321 #force exit')
                        #sets my "playing" variable to false
                        playing=0
        #waits half of a second before starting over again 
        #at the top of my while loop 
        sleep(0.5);
