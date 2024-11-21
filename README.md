# TimeToBeat-Py
A small script that returns a csv file with howlongtobeat average times to beat a game.

# Usage

I made this script for personal use and I don't plan to update this unless strictly necessary.

Requires Python 3.xx

Place this script in a folder with a list of games in .txt format. The games must be separated by commas.

The script will output a file named gamelist.csv and if the HLTB API fails to return an entry for a game, an exception will be raised and printed to console. 

Games will be written to the file as "GAME NAME, STORY AVG. TIME, STORY+EXTRAS AVG TIME". If the HLTB API fails to return an entry for a game, it will be written to the file as "GAME NAME, -, -"

# Credits
[ScrappyCocco](https://github.com/ScrappyCocco/HowLongToBeat-PythonAPI) - HowLongToBeat Python API
