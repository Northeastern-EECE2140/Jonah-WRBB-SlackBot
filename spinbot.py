import SpinPapiClient

# Create the SpinBot Class
class SpinBot:

    # The constructor for the class. It takes the channel name as the a 
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel

    # Get the current song from Spinitron, then send a  
    # crafted slack payload with the song as a message.
    def _get_song(self):
        pass
    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        pass