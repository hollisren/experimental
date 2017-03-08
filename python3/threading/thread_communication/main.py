#! /usr/bin/env python3
"""
File: template_executable.py
Author: YOUR NAME GOES HERE

This is an example template of how a python program should be structured.
It is a good starting point for any new coders.

You should change this comment to reflect what will be in the file
"""

# Imports go here
import queue
import time
import threading

import task1

# Classes or functions go here

# Program starts running from here
if __name__ == "__main__":
    """
    Instantiate classes and call functions from here
    """

    print("Thread Communication")
    
    task1_inst = task1.Task1()
    task1_message = task1.Task1Message("Example Message")
    task1_queue = queue.Queue()

    task1_thread = threading.Thread(target=task1_inst.run,
                                    args=(task1_queue, ))
    task1_thread.start()

    time.sleep(5)

    task1_queue.put(task1_message)

    time.sleep(2)
    task1_inst.kill()
    task1_message.message = "Terminate Thread Message"
    task1_queue.put(task1_message)
    while (task1_thread.isAlive()):
        pass

    print("Program Terminate")
