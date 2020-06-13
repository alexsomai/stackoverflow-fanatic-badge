# Earn the Fanatic Badge on Stack Overflow

A Python script deployed to Heroku that performs automatic logins on stackoverflow.com on a regular basis, so that you can earn the **Fanatic** badge, effortlessly.

[Fanatic Badge](https://stackoverflow.com/help/badges/83/fanatic)
> Visit the site each day for 100 consecutive days. (Days are counted in UTC.).

Moreover, you get notified, via email, if the script goes wrong and you haven’t logged into Stack Overflow for at least _twelve hours_.

## Step-by-step guide

You may follow the step-by-step guide [here](https://medium.com/coders-do-read/earn-the-fanatic-badge-on-stack-overflow-828d2c46930).

And the second part, with additional improvements, [here](https://medium.com/coders-do-read/fanatic-badge-on-stack-overflow-part-two-email-notification-820f5394f8f0).

Alternatively, you can follow the (less detailed) quick start below.

## Quick start

1. Make sure you have the following dependencies:

  - Python 3.6+ (along with pip)

  - Chrome installed (or another browser of choice, though you will have to edit the script)

  - Python packages (use `pip install` to get): `selenium`, `sendgrid`, `webdriver_manager`, `requests_oauthlib`, `apscheduler`

2. Edit `env_vars.txt` to include your email, password, and display name.

3. Run `source env_vars.txt` and then `python3 stack_overflow_page.py`.

## Troubleshooting

The script can trigger a CAPTCHA from StackOverflow. A human has to resolve this.
