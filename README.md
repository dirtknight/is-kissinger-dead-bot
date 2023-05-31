# is-kissinger-dead-bot
Discord bot reporting on if that rat bastard finally kicked the bucket

look I know the bot is shit but in my defense, I did this in an hour or so on a whim and I just can't bring myself to care enough to fix it

The bot requires a Discord guild ID and app token, plus a Twitter API token. Don't gotta pay Musk for the Twitter junk, it only reads.

Stick everything you need in a file named ".env" in the same directory as this bot. Specifically, you need these variables in there:

DIS_GUILD: Guild ID of the server you're trying to plug ikdb into

DIS_TOKEN: the API token you're using for this guy

TWI_BEARER: Twitter bearer token

TEST_CHANNEL: A Discord channel ID for somewhere for ikdb to barf info at so you can check it's actually working

The bot uses these modules:
[Tweepy](https://www.tweepy.org/) for the Twitter crap
[Disnake](https://docs.disnake.dev/en/stable/) for the Discord crap

I recommend running the thing as a separate user, with a systemd service handling keeping the thing alive.
There's an exampld .service file provided, ikdbot.service. Do with that what thou wilst.
