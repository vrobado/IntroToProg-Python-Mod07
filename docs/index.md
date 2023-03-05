# Assignment 07: Pickling and Error Handling
**Name**: Victoria O’Laughlin

**Date**: March 1, 2023

**Course**: IT FDN 110 A

===================================================================================================
## Introduction

This week’s learning was focused on pickling and error handling. I am a test engineer and do quite a bit of error handling in my automation testing, but I’ve never taken a formal Python class before (I’ve learned everything I know on the job, aside from this class) and it was nice to gain a better understanding of it via my own research and the course videos. Pickling was a new concept to me, but after some research and practice, it all made sense.

## Thought process while watching course videos and writing my script:

1. This week, the script was focused on giving a demo of pickling and a demo of error handling. As I mentioned in the introduction, I’m familiar with the latter but needed to invest some extra effort to understand pickling. 
2. While I don’t include it in my script, in my practice, I learned to appreciate using PASS as a placeholder for when a function is defined but I don’t have the code in it yet. This helps me stay organized. 
3. Professor Root suggested doing as many try-except blocks that you can think of in a script, as this is beneficial for testing (my job!). I will certainly take that advice and apply it at work.
4. I always find it useful to familiarize myself with Python’s builtins.py file. These functions help me understand what’s already available in my toolkit. See Figure 1.0 for an example of hitting command+b to enter the file with all these functions. 
5. I spent a bit of time making my script look nice because this script has two demos in one and I wanted to make sure they were clearly separated. See Figure 1.1 for an example of what I mean.
6. Making a Github webpage was the next step after my script. I was happy to practice this because I always encounter markdown language in my job and I haven’t taken the time to understand it.

## Summary

These simple demos made me feel more confident in my ability to display my code’s output how I want it to. It was fun to play around with different try-except or raise exceptions. While I don’t see myself using pickling much in my current work, it’s good to know the option for writing to a binary file is actually not too tricky - I’m sure it would be handy to know one day. 

### Figure 1.0: builtins.py - I used isnumeric in my script
![Figure 1.0](https://github.com/vrobado/IntroToProg-Python-Mod07/blob/main/Screen%20Shot%202023-03-04%20at%209.14.02%20PM.png "Figure 1.0: builtins.py - I used isnumeric in my script")

### Figure 1.1: Separating the demos using the print function to display the message"
![Figure 1.1](https://github.com/vrobado/IntroToProg-Python-Mod07/blob/main/Screen%20Shot%202023-03-04%20at%209.44.48%20PM.png "Figure 1.1: Separating the demos using the print function to display the message")


### Example of a try-catch with manually raised errors
```
# -------------------------------------- #
# Title: Listing 13
# Description: A try-catch with manually raised errors
# ChangeLog: (Who, When, What)
# VOLaughlin,3.1.2023,Created Script
# -------------------------------------- #

try:
  new_file_name = input("Enter the name of the file you watn to make: ")
  if new_file_name.isnumeric()"
    raise Exception("Do not use numbers for the file's name")
  except Exception as e:
    print("There was a non-specific error!")
    print("Built-in Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```
