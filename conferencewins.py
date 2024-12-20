import time
import networkx as nx
from scraper import get_team_record
import json

json_file = '2010seasonScrapedNodes.json'
with open(json_file, 'r') as file:
    json_2005 = json.load(file)

node_dict = []
edge_dict = []

wins_dict = {
    "ACC": 0,
    "Big 12": 0,
    "Big East": 0,
    "Big Ten": 0,
    "Sun Belt": 0,
    "CUSA": 0,
    "Ind": 0,
    "MAC": 0,
    "MWC": 0,
    "Pac-10": 0,
    "SEC": 0,
    "WAC": 0
}

team_dict = {
    "ACC": 0,
    "Big 12": 0,
    "Big East": 0,
    "Big Ten": 0,
    "Sun Belt": 0,
    "CUSA": 0,
    "Ind": 0,
    "MAC": 0,
    "MWC": 0,
    "Pac-10": 0,
    "SEC": 0,
    "WAC": 0
}

for node in json_2005["nodes"]:
    
    wins = node["wins"]
    conference = node["value"]

    wins_dict[conference] += wins

    print(f"This is the conference name: {conference}")
    print(f" {node["id"]} won {wins} games")
    print(wins_dict)

    
 
with open('conference_wins2010.json', 'w') as json_file:
    json.dump(wins_dict, json_file, indent=4)

print("Conference wins have been saved to conference_teams2005.json.")