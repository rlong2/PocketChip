# PocketChip Random Album Picker

This repository details how to build a python app on a Pocket C.H.I.P. that ingests a CSV of vinyl records and displays them at random. The keyboard can be used to pick songs out of a certain genre.

![Pocket CHIP handheld device](https://cdn.shopify.com/s/files/1/0046/2612/0774/files/akrales_160719_1147_A_0139_large.jpg?v=1537278482)
## Requirements
- A [Pocket C.H.I.P.](https://shop.pocketchip.co/pages/about) I believe this company is now insolvent, but there may be devices floating around.
- A CSV file of records. Here is a snippet of how I have my fields arranged in Google Sheets, which was then exported to a CSV:
	![](SpreadsheetSnippet.png)


## Files
- /`usr/share/pocket-home/config.json` - contains shell commands, paths to icons, the python app, and the csv.
- `/home/chip/random_album.py`
- `/home/chip/vinyl.csv`

## End Result
Pocket C.H.I.P. app selection:
![](PocketChipAppSelection.png)

'Random Album' app running:
![](PocketChipAppRunning.png)

