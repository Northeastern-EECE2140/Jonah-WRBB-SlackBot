import os
import logging
from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from spinbot import SpinBot

def get_message(channel):
    """
    Craft the SpinBot, call spinitron and send the message to the channel
    """

    SpinitronBot = SpinBot(channel)

    pass


def message(payload):
    """
    Parse the message event, and if the activation string is in the text, 
    call the get_message function.
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if the activation phrase was in the text of the message.
    # If so, execute the code to flip a coin.
    if "!song" in text.lower():
        # Since the activation phrase was met, get the channel ID that the event
        # was executed on
        channel_id = event.get("channel")

        # Execute the flip_coin function and send the results of
        # flipping a coin to the channel
        return get_message(channel_id)
