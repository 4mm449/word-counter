#!/usr/bin/env python
#input("THIS IS AN EARLY BUILD OF THIS PROGRAM. FEATURES ARE LIMITED.\nHERE ARE SOME THINGS YOU CAN AND CANNOT DO IN THIS EARLY BUILD: \n1.YOU CANNOT PASTE TEXT FROM THE CLIPBOARD :( \n2.YOU CAN HOWEVER TYPE IN TEXT AND THE PROGRAM WILL WORK AS INTENDED. \nPress Enter (Return) to Continue...")
banner_text = '''

'##:::::'##::'#######::'########::'########::::::::::::'######:::'#######::'##::::'##:'##::: ##:'########:'########:'########::
 ##:'##: ##:'##.... ##: ##.... ##: ##.... ##::::::::::'##... ##:'##.... ##: ##:::: ##: ###:: ##:... ##..:: ##.....:: ##.... ##:
 ##: ##: ##: ##:::: ##: ##:::: ##: ##:::: ##:::::::::: ##:::..:: ##:::: ##: ##:::: ##: ####: ##:::: ##:::: ##::::::: ##:::: ##:
 ##: ##: ##: ##:::: ##: ########:: ##:::: ##:'#######: ##::::::: ##:::: ##: ##:::: ##: ## ## ##:::: ##:::: ######::: ########::
 ##: ##: ##: ##:::: ##: ##.. ##::: ##:::: ##:........: ##::::::: ##:::: ##: ##:::: ##: ##. ####:::: ##:::: ##...:::: ##.. ##:::
 ##: ##: ##: ##:::: ##: ##::. ##:: ##:::: ##:::::::::: ##::: ##: ##:::: ##: ##:::: ##: ##:. ###:::: ##:::: ##::::::: ##::. ##::
. ###. ###::. #######:: ##:::. ##: ########:::::::::::. ######::. #######::. #######:: ##::. ##:::: ##:::: ########: ##:::. ##:
:...::...::::.......:::..:::::..::........:::::::::::::......::::.......::::.......:::..::::..:::::..:::::........::..:::::..::

WORD-COUNTER V1.0
CODED BY AMMAAR> github.com/4mm449/word-counter
'''
print(banner_text)
input("Press Enter (Return) to Get Started...")
words = input("ENTER WORDS TO COUNT\n")

calculate_words = words.split()

length = str(len(calculate_words))


print("There are "+length+" word(s) in your input")

input("Press Enter (Return) to Exit...")
