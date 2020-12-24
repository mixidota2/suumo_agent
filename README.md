# Suumo Agent
This is a project to analyse data from suumo, which is real estate agent service, to find my new room in Tokyo.  

## Requirements  
- python >= 3.6  
- Run `pip install -r requirements.txt` to install dependencies.  

## Features
- Automatically scrapes data from suumo
- Lists up all the apartments and screen them by some thresholds
- Some nice plots
- Access to the urls

## Get started
Simply run `streamlit run src/app.py` to launch a streamlit server locally.  
Then you can access to the dashboard, which shows some nice data including some plots and url to the suumo pages.  

## Notes
- Currently we support modes with only Shinjuku and Shibuya
- Apartments max fee is set to 95000 yen
- Apartments max distance from the station is set to 15min by walk

## ToDo
- Flexible choice for stations, max fees, and distances
- Some more nice plots
- Logics to filter apartments from images(You don't want a nasty toilet or ugly walls, do you?)
- Some nice recommendations
