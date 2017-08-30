color_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
               "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4",
               "azure2": "#e0eeee", "beige": "#f5f5dc", "black": "#000000"}
# print(STATE_NAMES)

color = input("Enter color name: ?")
while color != "":
    if color in color_NAMES:
        print(color, "is", color_NAMES[color])
    else:
        print("Invalid short state")
    color = input("Enter color name: ")
