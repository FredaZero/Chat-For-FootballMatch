# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType, SlotSet
from actions.football import WinLoseRecord, get_league_ID
import aiofiles
from .config import ALLOWED_FOOTBALL_TEAMS
class ActionWinLoseRecord(Action):

    def name(self) -> Text:
        return "action_get_football_match_record"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("football_team")
        league_ID = tracker.get_slot("league_ID")
        season = tracker.get_slot("season")
        league_ID = int(league_ID)
        season = int(season)
        text = WinLoseRecord(name, league_ID, season)
        


        dispatcher.utter_message(text)

        return []


class ActionAskForLeagueID(Action):

    def name(self) -> Text:
        return "action_ask_for_ID"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        
        # season = tracker.get_slot('season')
        league_name = tracker.get_slot('league_name')

        # Implement the logic to get the league_ID based on season and league_name
        # For example:
        league_ID = None
        league_ID = await get_league_ID(league_name)

        if league_ID:
            dispatcher.utter_message(text=f"The league ID for {league_name} is {league_ID}.")
            return [SlotSet("league_ID", league_ID)]
        else:
            dispatcher.utter_message(text=f"Sorry, I couldn't find the league ID for {league_name}.")
            return [SlotSet("league_ID", None)]

class validate_simple_football_form(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_football_form"
    
    async def validate_league_ID(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'league_ID' value"""

        if int(slot_value) >= 1170 or int(slot_value) <=0:
            dispatcher.utter_message(text="The league ID is invalid.")
            return {"league_ID": None}
        dispatcher.utter_message(text=f"Got it! You want to the league with ID {int(slot_value)}")
        return {"league_ID": int(slot_value)}
    
    async def validate_season(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'season' value"""

        if int(slot_value) >= 2025 or int(slot_value) <=2007:
            dispatcher.utter_message(text="The season is invalid.")
            return {"season": None}
        dispatcher.utter_message(text=f"Ok! you are looking at season {int(slot_value)}")
        return {"season": int(slot_value)}
    
    async def validate_football_team(
            self,
            slot_value: Any,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate 'football_team' value"""

        if slot_value.lower() not in ALLOWED_FOOTBALL_TEAMS:
            dispatcher.utter_message(text="The football team is invalid.")
            return {"football_team": None}
        dispatcher.utter_message(text=f"Got it! You want to check the record of team {slot_value}")
        return {"football_team": slot_value}
    
class ActionResetSlots(Action):

    def name(self) -> Text:
        return "action_reset_slots"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
        
        
        return [SlotSet("league_ID", None),
                SlotSet("season", None),
                SlotSet("football_team", None),
                SlotSet("league_name", None)]
        