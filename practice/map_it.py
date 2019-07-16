#! python3
# maplt.py - Launches a map in the browser using an address from he
# command line or clipboard.
# usage: python map_it.py 870 Valencia St,San Francisco,CA 94110

import webbrowser, sys, pyperclip

if len(sys.argv) > 1 :
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)