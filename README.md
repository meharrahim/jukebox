# Jukebox
This project is to import youtube links from a slack channel and sort and play according to the votes of the users
## Functionality
### Browser app functionalities
  * Sign In
    * via username & password
    * via email & password
    * via email or username & password
  * Sign Up
  * Log Out
  * List the youtube videos from the specified slack channel
  * Vote video
  * Play list (sorted according to the votes)
### Slack bot functionalities
  * Post video link to private channal where jukebox bot is added.
  * User can add multiple links at the same time
  * User can also add youtube links in between text 
      e.g.: Please add \<youtube link\>

## Installation
### Clone the project
```
git clone https://github.com/meharrahim/jukebox.git
cd jukebox
```

### Install dependencies & activate virtualenv
```
pip install pipenv
pipenv install
pipenv shell
```
### Install required packages from requirements.txt
`pip install -r requirements.txt`

### Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```

### Create slack app and tunnel the local network to get public url using ngrok
Follow every steps in the awesome tutorial below

[Slackbot installation tutorial]( https://medium.com/freehunch/how-to-build-a-slack-bot-with-python-using-slack-events-api-django-under-20-minute-code-included-269c3a9bf64e)

The app credentials should be added to .env file inside root folder

### Add bot to channel
Create a private channel and add the app to the channel by an invite.
Workspace event to be subscribed is **message.groups**

### Run the project
Run the project in one terminal
`python manage.py runserver 0.0.0.0:8000`

In another terminal tunnel the localhost to get a public url
`./ngrok http 8000`

## Screenshots
![Screenshot3](https://github.com/meharrahim/jukebox/blob/master/screenshots/slack_msg1.png)
![Screenshot4](https://github.com/meharrahim/jukebox/blob/master/screenshots/slack_msg2.png)
![Screenshot5](https://github.com/meharrahim/jukebox/blob/master/screenshots/slack_msg3.png)
![Screenshot1]( https://github.com/meharrahim/jukebox/blob/master/screenshots/home_page.png )
![Screenshot7](https://github.com/meharrahim/jukebox/blob/master/screenshots/votepage.png)
![Screenshot6](https://github.com/meharrahim/jukebox/blob/master/screenshots/voted.png)
![Screenshot2](https://github.com/meharrahim/jukebox/blob/master/screenshots/playlist.png)
 
