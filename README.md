# Earn the Fanatic Badge on Stack Overflow

A Python script deployed to Heroku that performs automatic logins on stackoverflow.com on a regular basis, so that you can earn the **Fanatic** badge, effortlessly.

[Fanatic Badge](https://stackoverflow.com/help/badges/83/fanatic)
> Visit the site each day for 100 consecutive days. (Days are counted in UTC.).

Moreover, you get notified, via email, if the script goes wrong and you haven’t logged into Stack Overflow for at least _twelve hours_.

ℹ️ To count as a visit, besides the login, the script also accesses your profile page: https://meta.stackoverflow.com/a/298532.

## Step-by-step guide

You may follow the step-by-step guide [here](https://medium.com/coders-do-read/earn-the-fanatic-badge-on-stack-overflow-828d2c46930).

And the second part, with additional improvements, [here](https://medium.com/coders-do-read/fanatic-badge-on-stack-overflow-part-two-email-notification-820f5394f8f0).

Alternatively, you can follow the (less detailed) quick start below.

## Quick start

1. Make sure you have the following dependencies:

    - Python 3.6+ (along with pip)

    - Chrome installed (or another browser of choice, though you will have to edit the script)

    - Python packages (use `pip install` to get): `selenium`, `sendgrid`, `webdriver_manager`, `requests_oauthlib`, `apscheduler`, `requests`, `python_http_client`

2. Edit `.env` to include your email, password, and display name.

    - WARNING: don't push this to a public repository!

3. Run `python3 stack_overflow_page.py` to see the script work.

4. If you want to be notified by email when things go wrong, [sign up for sendgrid](https://signup.sendgrid.com/) to get an API key, and add that to `env_vars.txt` as well. This can take some work to set up successfully.

5. To schedule the script on Heroku, sign up for an account on Heroku and follow the instructions in the full step-by-step guide on Medium. Or press the _Deploy to Heroku_ button below.

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alexsomai/stackoverflow-fanatic-badge/tree/master)

Once deployed, set the following Config Vars in Heroku app Settings:

* **Mandatory** (basic login script variables):
  * `STACK_OVERFLOW_EMAIL`
  * `STACK_OVERFLOW_PASSWORD`
  * `STACK_OVERFLOW_DISPLAY_NAME`

* **Optional**:
  * Sendgrid, for sending email when things go wrong:
    * `SENDGRID_API_KEY`
  * Stack Exchange API, to get an email after a period of inactivity:    
    * `STACK_EXCHANGE_CLIENT_ID`
    * `STACK_EXCHANGE_KEY`
    * `STACK_EXCHANGE_ACCESS_TOKEN`


## Troubleshooting

The script can trigger a CAPTCHA from StackOverflow. A human has to resolve this.

StackOverflow sometimes changes their UI, so that the old CSS identifiers don't match anymore. This can cause one of lines in `stack_overflow_page.py` starting with `driver.find_element_by_` to fail. To debug this in Chrome, look for the correct identifier to use instead using the "inspect element" feature in developer tools (Ctrl+Shift+C).

Emails sent by sendgrid can go to spam. If you get errors when sending mail with sendgrid, make sure that you have an account which includes an API key, a verified email address, and that you have set up a verified sender to send mail. Note that sendgrid requires the dependency `python-http-client`.
