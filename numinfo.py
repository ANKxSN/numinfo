#!/bin/usr/python

''' Hello guys I'm ANKxSN 
Here I maka a simple phone number information tool.

        --------------------------------
        REQUIREMENT FOR THIS TOOL

       - python programming 
       - phonenumbers module

        --------------------------------


This tool is created by ANKxSN.
And this is my second project


'''

# import system
import os
# clear the screen
os.system("clear")
print()
print("\033[0;31m\033[1m_______________________________________________________\033[0m")
name = ("\033[0;35m\033[1mCREATED BY ANKxSN")

tool_detail = ("\033[0;35m\033[1mSIMPLE PHONE NUMBER INFO TOOL\033[0m")
print()
print(name.center(60))
print()
print()
print(tool_detail.center(65))
print("\033[0;31m\033[1m_______________________________________________________\033[0m")

print()
print()

import phonenumbers
from phonenumbers import timezone,geocoder,carrier
# Taking number from user
num = input("\033[0;31m\033[1m -> \033[0m\033[0;32m\033[1m Enter With + : \033[0m")
# Give a new name
phone = phonenumbers.parse(num)
# from timezone module
Timezone = timezone.time_zones_for_number(phone)
# from geocoder module
geo = geocoder.description_for_number(phone,"en")
# from carrier module
carr = carrier.name_for_number(phone,"en")

# Print all module

print(phone)
print(Timezone)
print(geo)
print(carr)



