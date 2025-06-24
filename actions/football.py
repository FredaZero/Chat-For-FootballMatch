import requests
import json
import os
import aiohttp

# league = 39
# season = 2021

headers = {
    'x-rapidapi-key': '61b347bbf471e7a85eb18f112f8292f2',
    'x-rapidapi-host': 'v3.football.api-sports.io'
    }

def GetFootballTeamID(name, league, season):
   
    url = f"https://v3.football.api-sports.io/teams?league={league}&season={season}"
    response = requests.request("GET", url, headers=headers)
    teams_info = json.loads(response.text)
    # print(teams_info["response"])
   
    teams_dict = dict()
    for team in teams_info['response']:
        key = team['team']['name']
        value = team["team"]["id"]
        teams_dict[key] = value
       
    try: 
        ID = teams_dict[name]
    except KeyError:
        print("Not record of this team.")
        ID = None
    print(f"The Team ID is {ID}")
    return ID


async def get_league_ID(league_name: str) -> str:
    if league_name is not None:
        url = "https://v3.football.api-sports.io/leagues"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    leagues_info = await response.json()
                    league_ID = None
                    for league in leagues_info["response"]:
                        if league_name.lower() == league['league']['name'].lower():
                            league_ID = league['league']['id']
                    return league_ID
                else:
                    return None


def WinLoseRecord(name,league, season):
    team = GetFootballTeamID(name, league, season)
    if team is None:
        text_message = "Not record of this team."
        return text_message

    URL = f"https://v3.football.api-sports.io/teams/statistics?season={season}&league={league}&team={team}"
    res = requests.request("GET", URL, headers=headers)
    data = json.loads(res.text)

    if data['response']['fixtures']['played']['total'] == 0:
        text_message = "They have not played any game in this season"
        return text_message
    
    text_message = "Their record is {} wins, {} loss and {} draws." .format(
        data['response']['fixtures']['wins']['total'],
        data['response']['fixtures']['loses']['total'],
        data['response']['fixtures']['draws']['total']
    )
    print(text_message)
    return text_message
    

if __name__ == '__main__':
    WinLoseRecord('Manchester United', 39, 2021)