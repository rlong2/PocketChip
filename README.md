# PocketChip Random Album Picker

Tired of picking items at random? This repository details how to build a python app on a Pocket C.H.I.P. that ingests a CSV of vinyl records and displays them at random for you to spin at your leisure. The keyboard can be used to pick songs out of a certain genre.

![Pocket CHIP handheld device](https://cdn.shopify.com/s/files/1/0046/2612/0774/files/akrales_160719_1147_A_0139_large.jpg?v=1537278482)
## Requirements
- A [Pocket C.H.I.P.](https://shop.pocketchip.co/pages/about) I believe this company is now insolvent, but there may be devices floating around.
- A CSV file of records. Here is a snippet of how I have my fields arranged in Google Sheets, which was then exported to a CSV:
	![](SpreadsheetSnippet.png)

The csv included in this repo is not a complete version. It was generated with `shuf -n 10 vinyl.csv `

## Files
- /`usr/share/pocket-home/config.json` - contains shell commands, paths to icons, the python app, and the csv.
- `/home/chip/random_album.py` - the python program. Note that the python file must be written in `python2`. The CHIP does not support `python3`.
- `/home/chip/vinyl.csv` - the list of vinyl records. 

## End Result
Pocket C.H.I.P. app selection:
![](PocketChipAppSelection.png)

'Random Album' app running:
![](PocketChipAppRunning.png)

