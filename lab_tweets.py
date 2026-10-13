# Load master_2009.json through master_2018.json, analyze the tweets, and make a bar chart.
# Follow the linked course assignment in README.md.
'''Count catalog phrases in the 2009-2018 Trump tweet archive and plot them.'''
import json

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

REQUIRED = ['obama', 'trump', 'mexico', 'russia', 'fake news']
CHOSEN = ['wall', 'jobs', 'maga']
PHRASES = sorted(REQUIRED + CHOSEN)


def load_tweets():
    tweets = []
    for year in range(2009, 2019):
        with open(f'master_{year}.json', encoding='utf-8') as f:
            tweets.extend(json.load(f))
    return tweets


def message(tweet):
    if tweet.get('full_text') is not None:
        return tweet['full_text']
    return tweet.get('text') or ''


def count_phrases(tweets, phrases):
    counts = {}
    for phrase in phrases:
        counts[phrase] = 0
    for tweet in tweets:
        text = message(tweet).lower()
        for phrase in phrases:
            if phrase.lower() in text:
                counts[phrase] += 1
    return counts


def markdown_table(percents):
    lines = [
        '| phrase            | percent of tweets |',
        '| ----------------- | ----------------- |',
    ]
    for phrase in PHRASES:
        pct = f'{percents[phrase]:05.2f}'
        lines.append(f'| {phrase:>17} | {pct:<17} |')
    return '\n'.join(lines)


def main():
    tweets = load_tweets()
    total = len(tweets)
    print('Total tweets:', total)

    counts = count_phrases(tweets, PHRASES)
    for phrase in PHRASES:
        print(phrase, counts[phrase])

    percents = {}
    for phrase in PHRASES:
        percents[phrase] = 100 * counts[phrase] / total

    print()
    print(markdown_table(percents))

    values = [percents[p] for p in PHRASES]
    plt.figure(figsize=(8, 5))
    plt.barh(PHRASES, values)
    plt.xlabel('Percent of tweets')
    plt.ylabel('Phrase')
    plt.title('Catalog phrases in Trump tweets, 2009-2018')
    plt.tight_layout()
    plt.savefig('tweets.png')


if __name__ == '__main__':
    main()