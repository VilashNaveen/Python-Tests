# program to match phone numbers and emails in a text
import re

import pyperclip
phoneNum=re.compile(r'''(
            ((\+94\s\d\d)|(\d){3})
            (\s|-)?
            (\d){3}(\s|-)?
            (\d){4})''',re.VERBOSE)

eMail=re.compile(r'''(
            (\w+(\d+)?(\.|_)?\w+(\d+)?)
            @(\w+\.\w+))''',re.VERBOSE)

text=pyperclip.paste()
matches=[]
for groups in phoneNum.findall(text):
    print(groups[0])