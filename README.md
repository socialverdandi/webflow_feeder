# How To Use

## Update Config file
when there premier leargue start the new season please update it in [config.py](config.py)

## Update football team name
to display football team name, this file need to be update. However the English need also need to matched with the one in the api.
so first run this scirpt to get the english name first

```
python displayTeamName.py
```

then use this name to update the one it [thaiTeamName.py](thaiTeamName.py)

## run the script

this as the main script to feed the data into webflow
but first we need to tell the scirpt the range of date we want it to get the data
open [main.py](main.py)
and update this line

```
resp =  get_mathes_data('2021-02-25', '2021-03-05')
```
it is in this format
```
resp =  get_mathes_data(from_date, to date)
```
starting getting the match data 'from_date' to 'to_date'