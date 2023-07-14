import pyperclip
import keyboard

smallify = pyperclip.paste()

#ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ

now_small = ""
for ltr in smallify.lower():
    if ltr == 'a':
        now_small += 'ᵃ'
    elif ltr == 'b':
        now_small += 'ᵇ'
    elif ltr == 'c':
        now_small += 'ᶜ'
    elif ltr == 'd':
        now_small += 'ᵈ'
    elif ltr == 'e':
        now_small += 'ᵉ'
    elif ltr == 'f':
        now_small += 'ᶠ'
    elif ltr == 'g':
        now_small += 'ᵍ'
    elif ltr == 'h':
        now_small += 'ʰ'
    elif ltr == 'i':
        now_small += 'ᶤ'
    elif ltr == 'j':
        now_small += 'ʲ'
    elif ltr == 'k':
        now_small += 'ᵏ'
    elif ltr == 'l':
        now_small += 'ˡ'
    elif ltr == 'm':
        now_small += 'ᵐ'
    elif ltr == 'n':
        now_small += 'ⁿ'
    elif ltr == 'o':
        now_small += 'ᵒ'
    elif ltr == 'p':
        now_small += 'ᵖ'
    elif ltr == 'q':
        now_small += 'ᵟ'
    elif ltr == 'r':
        now_small += 'ʳ'
    elif ltr == 's':
        now_small += 'ˢ'
    elif ltr == 't':
        now_small += 'ᵗ'
    elif ltr == 'u':
        now_small += 'ᵘ'
    elif ltr == 'v':
        now_small += 'ᵛ'
    elif ltr == 'w':
        now_small += 'ʷ'
    elif ltr == 'x':
        now_small += 'ˣ'
    elif ltr == 'y':
        now_small += 'ʸ'
    elif ltr == 'z':
        now_small += 'ᶻ'
    elif ltr == "!":
        now_small += '!'
    elif ltr == "?":
        now_small += '?'
    elif ltr == " ":
        now_small += ' '
    elif ltr == "'":
        now_small += "'"
    elif ltr == ",":
        now_small += ','
    elif ltr == '.':
        now_small += '.'
    elif ltr == '0':
        now_small += '⁰'
    elif ltr == '1':
        now_small += '¹'
    elif ltr == '2':
        now_small += '²'
    elif ltr == '3':
        now_small += '³'
    elif ltr == '4':
        now_small += '⁴'
    elif ltr == "5":
        now_small += '⁵'
    elif ltr == "6":
        now_small += '⁶'
    elif ltr == "7":
        now_small += '⁷'
    elif ltr == "8":
        now_small += "⁸"
    elif ltr == "9":
        now_small += '⁹'
    else:
        continue

pyperclip.copy(now_small)
keyboard.press_and_release('ctrl+v')


#Compact version from reddit

#import pyperclip

#smallify = pyperclip.paste()

#smallify = smallify.lower()

#now_small = smallify.translate({97 + i: c for i, c in enumerate("ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ")})

#pyperclip.copy(now_small)
#print(now_small)