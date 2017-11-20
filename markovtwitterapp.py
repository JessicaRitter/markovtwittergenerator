from flask import Flask, render_template, request
import jinja2
import markov_twitter

app = Flask(__name__)

@app.route('/')
def show_main():
    return render_template("home.html")

@app.route('/markovtwitter', methods=['GET'])
def show_tweet():
    username = request.args.get('screenname')

    tweets = markov_twitter.get_tweets(username)
    text_string = markov_twitter.create_tweet_file(tweets)
    chains = markov_twitter.make_chains(text_string)
    markovtweet = markov_twitter.make_text(chains).decode('utf-8')
    
    return render_template("tweets.html", markovtweet=markovtweet, chains=chains,
                            username=username)    


if __name__ == '__main__':
    app.run()