import re
import sys

mode = ""
bin_param = ""
selected_lang = ""
trans_bin_param = ""
lang_dict = {"EN": ["Zero", "One"], "DE": ["Null", "Eins"], "FR": ["Zéro", "Un"], "ES": ["Cero", "Uno"]}


def bin_to_trans_bin(convert_param, lang):
    return convert_param.replace("0", lang[0]).replace("1", lang[1])


def trans_bin_to_bin(convert_param, lang):
    return convert_param.replace(lang[0], "0").replace(lang[1], "1")


def text_to_bin(convert_param):
    s = ""
    j=0
    for i in convert_param:
        s += format(ord(i), "08b")+" "
    return s


def bin_to_text(convert_param):
    return


def trans_bin_to_text(convert_param):
    return


def text_to_trans_bin(convert_param):
    return


script = sys.argv.pop(0)
while sys.argv:
    arg = sys.argv.pop(0)
    if re.search(r'^(-b)$', arg):
        bin_param = sys.argv.pop(0)
    elif re.search(r'^(-tb)$', arg):
        trans_bin_param = sys.argv.pop(0)
    elif re.search(r'^(-t)$', arg):
        txt_param = sys.argv.pop(0)
    elif re.search(r'^(-l)$', arg):
        selected_lang = lang_dict[sys.argv.pop(0)]

    elif re.search(r'^(-btb)$', arg):
        mode = "btb"
    elif re.search(r'^(-tbb)$', arg):
        mode = "tbb"
    elif re.search(r'^(-tTOb)$', arg):
        mode = "tb"
    elif re.search(r'^(-b>t)$', arg):
        mode = "bt"
    elif re.search(r'^(-tb>t)$', arg):
        mode = "tbt"
    elif re.search(r'^(-t>tb)$', arg):
        mode = "ttb"

    elif re.search(r'^(-h)$', arg):
        print("help")

if mode == "btb":
    print(bin_to_trans_bin(bin_param, selected_lang))
elif mode == "tbb":
    print(trans_bin_to_bin(trans_bin_param, selected_lang))
elif mode == "tb":
    print(text_to_bin(txt_param))
elif mode == "bt":
    print(trans_bin_to_bin(trans_bin_param, selected_lang))
elif mode == "tbt":
    print(trans_bin_to_bin(trans_bin_param, selected_lang))
elif mode == "ttb":
    print(trans_bin_to_bin(trans_bin_param, selected_lang))
else:
    print("You have to give an argument. e.g.:\n\n'python example.py -b 001011010 0100100110 -l EN -bttb'")
