# ---- ---- ---- ---- ---- {RiddleMeThis} ---- ---- ---- ---- ---- #
# Copyright (C) [2023] [Jordy Kennes]

# Well well well, look at you being nosey and peaking at the code.
# The code is explains using these comment lines to provide aid for the curious.
# Hope you enjoy reading the code and playing the game.

class Main():

    """Class 'Main' runs the application from start to finish."""

    def __init__(self):

        """This function is used to enable the parameter 'self' to have global variables within the class.
        It will also be called as soon as the main class is called."""

        # Print an introduction message:
        welcome_message = ("\n\n\n\n"\
                "\t\t[]---------------------------------------------------------------------------------[]\n"\
                "\t\t|- RRRRR   II DDDDD   DDDDD   LL    EEEEE   M   MM EEEEE   TTTTTT HH   HH II  SSSS -|\n"\
                "\t\t|- RR  RR  II DD  DD  DD  DD  LL    EE      MM MMM EE        TT   HH   HH II SS    -|\n"\
                "\t\t|- RR  RR  II DD   DD DD   DD LL    EEEE    MMMMMM EEEE      TT   HH   HH II SSS   -|\n"\
                "\t\t|- RRRRR   II DD   DD DD   DD LL    EE      M M MM EE        TT   HHHHHHH II  SSS  -|\n"\
                "\t\t|- RR RR   II DD   DD DD   DD LL    EE      M   MM EE        TT   HH   HH II   SSS -|\n"\
                "\t\t|- RR  RR  II DD  DD  DD  DD  LL    EE      M   MM EE        TT   HH   HH II    SS -|\n"\
                "\t\t|- RR   RR II DDDDD   DDDDD   LLLLL EEEEE   M   MM EEEEE     TT   HH   HH II SSSS  -|\n"\
                "\t\t[]---------------------------------------------------------------------------------[]\n"\
                "\n\n")
        print(welcome_message)
        keep_terminal_open = input(str(""))

Main()