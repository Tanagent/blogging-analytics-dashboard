import json
from collections import Counter

with open('data/articles.json', 'r') as f:
    articles_store = json.loads(f.read())

times = []
months = []
weekdays = []
authors = []
categories = []

for article in articles_store:

    # Average Reading Time
    times.append(article['reading_time'])
    average_time = sum(times) / float(len(times))
    average_time = round(average_time, 2)

    # Posts by Month
    months.append(article['month'])
    month_count = Counter(months)

    # Posts by Weekday
    weekdays.append(article['weekday'])
    weekday_count = Counter(weekdays)

    # Count by Category
    categories += article['categories']
    category_count = Counter(categories)

    # Count by Author
    authors.append(article['author'])
    author_count = Counter(authors)

stats = {
    'reading_time': average_time,
    'num_articles': len(articles_store)
}

with open('data/stats.json', 'w') as f:
    json.dump(stats, f)

with open('data/weekday.json', 'w') as f:
    json.dump(weekday_count, f)

with open('data/month.json', 'w') as f:
    json.dump(month_count, f)

with open('data/category.json', 'w') as f:
    json.dump(category_count, f)

with open('data/author.json', 'w') as f:
    json.dump(author_count, f)