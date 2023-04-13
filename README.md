# fanatic-badge-browserless
Get stackoverflow's fanatic badge automatically

## How to deploy

1. Create a free account at browserless.io. This will allow you to have a cloud instance for Chrome WebDriver, which can be used to automate workflow you normally do manually. For example logging in stackoverflow.com everyday to get the fanatic badge :smirk:
2. Install git, cron, python3 (I tested this script for version 3.8, it should also work with a newer one) and python3-pip on a Linux machine which is always online, like an Ubuntu VPS. This step can be achieved using a cloud provider (usually requires money) or using your own device (RaspberryPI maybe?).
3. Git clone this repo and `cd` into it
4. Create a python virtual environment and install the required libraries with `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
5. Edit `.env.example` with your browserless.io token and stackoverflow.com credentials then save a copy of it and rename it as `.env`
6. Launch the script with `python3 main.py`. You should automate this to proc the command every 6h or 12h [using a crontab](https://crontab.guru/examples.html).
7. Wait 100 days... :hourglass:
8. Profit! :chart_with_upwards_trend:

## Notes
browserless.io has a free tier for 1000 monthly sessions (just 1 current per time), it should be more than enough to get the 100 required consecutives logins.
If you don't have a linux machine online and you don't want to spend money for this, check out https://www.pythonanywhere.com. There's a free tier to run 1 python script and they have selenium library available, it should work for this use case.