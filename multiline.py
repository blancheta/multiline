
text = "Bonjour je m appelle Alexandre et ce texte doit être divisé en plusieurs ligne"
# text = "Bonjour je m'appelle"
char_by_line = 30

text_split = text.split(" ")
final_text = ""
linecount = 0

for textsplit in text_split:
    if linecount + len(textsplit) >= char_by_line:
        print("== RESET LINECOUNT ==")
        final_text += "\r\n"
        final_text += textsplit
        linecount = len(textsplit)
    else:
        if final_text is not "":
            textsplit = " " + textsplit

        final_text += textsplit
        linecount += len(textsplit)
print(final_text)
