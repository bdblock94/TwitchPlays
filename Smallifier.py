import pyperclip


smallify = pyperclip.paste()

#ᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖᵠʳˢᵗᵘᵛʷˣʸᶻ

now_small = ""
for ltr in smallify:
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
        now_small += 'ᶦ'
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
        now_small += 'ᵠ'
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
    elif ltr == ".":
        now_small += '!'
    elif ltr == "?":
        now_small += '?'
    elif ltr == " ":
        now_small += ' '
    elif ltr == "'":
        now_small += "'"
    elif ltr == ",":
        now_small += ','
    else:
        continue

pyperclip.copy(now_small)