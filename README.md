# crackmeup-bot
A twitter bot that tweets and tweets back jokes utilising the [crackmeup-api](https://github.com/bholagabbar/crackmeup-api)

## Tweeting to the bot

* Tweet to [@crackmeupbot](https://twitter.com/thedankjokebot), mention your category from
  * Blond
  * Dark
  * Dirty
  * Men
  * Women
  * Gross
  * Chuck Norris
  * Yo Mama
  * Random
* Make sure you add #crackmeup in your tweet. A dank joke should be tweeted back to you in a jiffy!

Example (it was formerly #crackmeupbro, nm):
> @crackmeupbot #crackmeup with a blond joke!
![image](http://shreyanssheth.com/img/crackmeup-mp.PNG)

## Setup

1. Get your Twitter App API credentials from [dev.twitter.com](https://dev.twitter.com)
2. Add the corresponding keys/credentials in the `.py` scripts
3. run `python tweet_bot.py && python reply_bot.py &&` or build and run with [Docker](https://docker.com) using `sudo docker build -t crackmeup-bot && docker run crackmeup-bot`
