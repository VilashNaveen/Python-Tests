#! python3
# Multiclipboard program
# save things copied in clipboard
# mcb.py copy/paste/del (keyword)
import sys, shelve,pyperclip

mcbshelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshelf[sys.argv[2]] = pyperclip.paste()
# elif len(sys.argv)==3 and sys.argv[1].lower=='del' and sys.argv[2] in mcbshelf:
#    del
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshelf.keys())))
    elif sys.argv[1] in mcbshelf:
        pyperclip.copy(mcbshelf[sys.argv[1]])
mcbshelf.close()
