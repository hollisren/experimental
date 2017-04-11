#! /usr/bin/env python3

import datetime
import logging
import RPi.GPIO as GPIO
import database


class MotionSensorClass():
    """
    """

    def __init__(self):
        return

class LEDClass():
    """
    """
    def __init__(self):
        """
        """
        print("LEDClass Init")
        self.POWER_PIN = 23
        self.state = False
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.POWER_PIN, GPIO.OUT)
        GPIO.output(self.POWER_PIN, self.state)
        return

    def toggle(self):
        """
        """
        self.state = not self.state
        print("LED Toggle {}".format(self.state))
        GPIO.output(self.POWER_PIN, self.state)
        return

class LCDClass():
    """
    """
    def __init__(self):
        return

class PushButtonClass():
    """
    """
    def __init__(self):
        return
    
class RasPiHardware():
    """
    """

    def __init__(self):
        self.LED = LEDClass()
        return

    def __del__(self):
        print("RasPiHardware Destructor")
        GPIO.cleanup()
        return