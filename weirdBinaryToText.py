import re
import sys

mode = ""
bin_param = ""
text_param = ""
selected_lang = ""
weird_param = ""
lang_dict = {"EN": ["Zero", "One"], "DE": ["Null", "Eins"], "FR": ["Zéro", "Un"], "ES": ["Cero", "Uno"]}
helptext = ""  # TODO: Write a Help / Man Page


def bin_to_weird(convert_param, lang):
    return convert_param.replace("0", lang[0]).replace("1", lang[1])


def weird_to_bin(convert_param, lang):
    return convert_param.replace(lang[0], "0").replace(lang[1], "1")


def text_to_bin(convert_param):
    output = ""
    for i in convert_param:
        output += format(ord(i), "08b") + " "
    return output


def bin_to_text(convert_param):
    output = ""
    temp = ""
    j = 1
    for i in convert_param:
        if i.isnumeric() and j <= 8:
            temp += i
        else:
            output += chr(int(temp, 2))
            j = 0
            temp = ""
    output += chr(int(temp, 2))
    return "'" + output + "'"


script = sys.argv.pop(0)
while sys.argv:
    arg = sys.argv.pop(0)
    if re.search(r'^(-b)$', arg):
        bin_param = sys.argv.pop(0)
    elif re.search(r'^(-w)$', arg):
        weird_param = sys.argv.pop(0)
    elif re.search(r'^(-t)$', arg):
        text_param = sys.argv.pop(0)
    elif re.search(r'^(-l)$', arg):
        selected_lang = lang_dict[sys.argv.pop(0)]

    elif re.search(r'^(-bw)$', arg):
        mode = "bw"
    elif re.search(r'^(-wb)$', arg):
        mode = "wb"
    elif re.search(r'^(-tb)$', arg):
        mode = "tb"
    elif re.search(r'^(-bt)$', arg):
        mode = "bt"
    elif re.search(r'^(-wt)$', arg):
        mode = "wt"
    elif re.search(r'^(-tw)$', arg):
        mode = "tw"

    elif re.search(r'^(-h)$', arg):
        print(help_text)

if mode == "bw":
    print(bin_to_weird(bin_param, selected_lang))
elif mode == "wb":
    print(weird_to_bin(weird_param, selected_lang))
elif mode == "tb":
    print(text_to_bin(text_param))
elif mode == "bt":
    print(bin_to_text(bin_param))
elif mode == "wt":
    print(bin_to_text(weird_to_bin(weird_param, selected_lang)))
elif mode == "tw":
    print(bin_to_weird(text_to_bin(text_param), selected_lang))
else:
    print("You have to give an argument. e.g.:\n\n'python example.py -b 001011010 0100100110 -l EN -bttb'")
