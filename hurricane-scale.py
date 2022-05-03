"""
-------------------------------------------------------------------------------
Name:		hurricane-scale.py
Author:		Montane.X
Created:	            05/02/2022
------------------------------------------------------------------------------
"""
from tabulate import tabulate

print("\nThe Saffir-Simpson Hurricane Scale\n")
hurricane_scale = [
    [1, "Very Dangerous - Some damage expected"],
    [2, "Extremely Dangerous - Extensive damage expected"],
    [3, "Major - Devastating damage expected"],
    [4, "Major - Catastrophic damage expected"],
    [5, "Major - Catastrophic damage expected"],
]
print(tabulate(hurricane_scale, headers=["Category", "Classification"]))
# Table of hurricane classes in tabular form through the use of the tabulate function

speed = float(input("\nEnter sustained wind speed expected in your area: "))
unit = int(input("Choose speed unit of measure(1 - kt, 2 - mph, 3 - km/h): "))
# Input statements for both speed and unit of measure


def convert():
    if unit == 1:
        return speed * 1.852
    elif unit == 2:
        return speed * 1.609
    elif unit == 3:
        return speed


while unit > 3:
    print("Wrong input, try again!\n")
    unit = int(input("Choose speed unit of measure(1 - kt, 2 - mph, 3 - km/h): "))

# Function that converts the speed input into the according unit of measurement


speed = convert()


def category():
    if speed >= 64 and speed <= 82 and unit == 1:
        print("\nCategory 1 - Very Dangerous - Some damage expected.")
    elif speed >= 83 and speed <= 95 and unit == 1:
        print("\nCategory 2 - Extremely Dangerous - Extensive damage expected.")
    elif speed >= 96 and speed <= 112 and unit == 1:
        print("\nCategory 3 - Major - Devastating damage expected.")
    elif speed >= 113 and speed <= 136 and unit == 1:
        print("\nCategory 4 - Major - Catastrophic damage expected.")
    elif speed > 136 and unit == 1:
        print("\nCategory 5 - Major - Catastrophic damage expected.")
    elif speed >= 74 and speed <= 95 and unit == 2:
        print("\nCategory 1 - Very Dangerous - Some damage expected.")
    elif speed >= 96 and speed <= 110 and unit == 2:
        print("\nCategory 2 - Extremely Dangerous - Extensive damage expected.")
    elif speed >= 111 and speed <= 129 and unit == 2:
        print("\nCategory 3 - Major - Devastating damage expected.")
    elif speed >= 130 and speed <= 156 and unit == 2:
        print("\nCategory 4 - Major - Catastrophic damage expected.")
    elif speed > 156 and unit == 2:
        print("\nCategory 5 - Major - Catastrophic damage expected.")
    elif speed >= 119 and speed <= 153 and unit == 3:
        print("\nCategory 1 - Very Dangerous - Some damage expected.")
    elif speed >= 154 and speed <= 177 and unit == 3:
        print("\nCategory 2 - Extremely Dangerous - Extensive damage expected.")
    elif speed >= 178 and speed <= 208 and unit == 3:
        print("\nCategory 3 - Major - Devastating damage expected.")
    elif speed >= 209 and speed <= 251 and unit == 3:
        print("\nCategory 4 - Major - Catastrophic damage expected.")
    elif speed > 251 and unit == 3:
        print("\nCategory 5 - Major - Catastrophic damage expected.")
    else:
        print("\nNon-threatening wind speed.")


# Function that displays the hurricane category corresponding to the speed

category()
