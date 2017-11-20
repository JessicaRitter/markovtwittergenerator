import os
import sys
from random import choice
import twitter



def get_tweets(username):
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    tweets = api.GetUserTimeline(screen_name=username, count=200)

    return tweets


def create_tweet_file(tweets):
    """Given a list of files, open them, read the text, and return one long
        string."""

    body = ""
    for tweet in tweets:
        text = tweet.text.encode("utf-8")
        body += text
    return body


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains."""

    chains = {}

    words = text_string.split("")


    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    key = choice(chains.keys())
    words = [key[0], key[1]]
    char_limit = 0

    while key in chains and char_limit <= 130:
        word = choice(chains[key])
        char_limit += len(word)
        words.append(word)
        key = (key[1], word)
    return " ".join(words)

def make_and_send_tweet(chains):
    # if you want to use this to make a mash up of two user's tweets make these adjustments:
    # have the method take two sets of chains
    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    # call twice and assign to variables, then concatenate them 
    chains = make_text(chains)
    status = api.PostUpdate(chains)
    return status

# tweets_dogs = get_tweets('Lin_Manuel')


# tweet_string = create_tweet_file(tweets_dogs)

# chains = make_chains(tweet_string)


# twitteroutput = make_and_send_tweet(chains)

