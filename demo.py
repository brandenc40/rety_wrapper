from retry_wrapper import *

from random import randint
import credentials

# setup for alert email on failure
email_to = credentials.gmail_login['email']
subject = 'It was not 4'
body = 'Your script did not return the value 4 after 2 attempts'
email_from = credentials.gmail_login['email']


# retry with failure email
@retry(max_retries=2, sec_delay_btwn_retries=2, email_on_fail=email_to, email_subject=subject,
       email_body=body, email_from=email_from)
def is_it_four_email():
    """Does the random number generated equal 4?"""
    x = randint(0, 6)
    assert x == 4, 'This doesn\'t equal 4!!'
    return x


# retry without failure email
@retry(max_retries=2, sec_delay_btwn_retries=2)
def is_it_four_no_email():
    """Does the random number generated equal 4?"""
    x = randint(0, 6)
    assert x == 4, 'This doesn\'t equal 4!!'
    return x


is_it_four_no_email()


is_it_four_email()

