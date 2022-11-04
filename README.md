# Jonah-WRBB-SlackBot
Final Project for EECE2140. A slack bot for WRBB

### Assignment 1: Project Proposal

1. *Who is on your team? If you are working with a partner, how will the labor be divided?*

I am the sole member of my team.

2. *An overview of the project similar in scope and length to the example projects listed below.*

The project is a slack bot for WRBB, our campus radio station. It will interface with Spinitron.com, our music logging servie. Users will be able to have the bot return information about the currently playing song. You will be able to request either the current song or the past 3. These will be translated to spotify urls for slack integration. The user may also request information on the currently playing DJ's name, real name, show title, show description, and episode information. This will also lead to a link to the current show playlist.

3. *A short description of the structure of your project. How many classes will you write? What the methods be for each class? (You can change this if it turns out a better structure would work better once you start writing code and you decide to refactor. Just try to come up with a reasonable one for the proposal.)*

There will be a class to make requests to the spinitron API. Additionally, there will be two classes dealing with the slack API, one to listen for the commands and one to write messages in response. Finally, there will be one class to convert the spinitron data into a format that slack can understand (likely a spotify url).

4. *What libraries and tools will you need to learn to use?*

- Requests for the spinitron API
- Slack API python library

5. Identify the highest-priority features, the medium-priority features, and the lowest-priority features for your project.

High priority:
- Interface with Slack API
- Interface with Spinitron API
- Return the current song

Medium priority:
- Return the past 3 songs

Low Priority:
- Return the current DJ's name, real name, show title, show description, and episode information
