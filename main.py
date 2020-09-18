import requests
from bs4 import BeautifulSoup
from dateutil import parser
from textstat.textstat import textstat

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'referrer': 'https://google.com'
}

def parse_page(url):
    r = requests.get(url, headers = headers)
    html = r.text.strip()

    # Allows you to search for different classes and ids
    soup = BeautifulSoup(html, 'lxml')

    # Header Content
    header = soup.find(class_ = 'entry-header')
    read_time = extract_read_time(header)
    title = extract_title(header)

    author = extract_author(header)
    categories = extract_categories(header)

    date = extract_date(header)
    dt = parser.parse(date)
    month = dt.strftime("%B")
    weekday = dt.strftime("%A")

    # Body Content
    content = soup.find(class_ = 'entry-content')
    word_count = len(content.text.split())
    reading_level = textstat.flesch_kincaid_grade(content.text)

    links = content.find_all("a")
    link_count = len(links)

    images = content.find_all("img")
    image_count = len(images)

    page_data = {
        'reading_time': read_time,
        'title': title,
        'date': date,
        'month': month,
        'weekday': weekday,
        'author': author,
        'categories': categories,
        'word_count': word_count,
        'reading_level': reading_level,
        'link_count': link_count,
        'image_count': image_count
    }

    return page_data

def extract_read_time(header):
    html_str = header.find(class_ = 'read-time')
    time_str = html_str.contents[0].strip().lower().split()[0]
    time_int = int(time_str)
    return time_int

def extract_title(header):
    html_str = header.find(class_ = 'post-meta-title')
    title_str = html_str.contents[0].strip()
    return title_str

def extract_date(header):
    html_str = header.find(class_ = 'single-post-date')
    date_str = html_str.contents[0].strip()
    return date_str

def extract_author(header):
    html_str = header.find(class_ = 'author-name')
    author_str = html_str.find('a').contents[0].strip()
    return author_str

def extract_categories(header):
    html_str = header.find(class_ = 'single-post-cat')
    categories = html_str.findAll('a')
    cat_names = []
    for cat_link in categories:
        cat_name = cat_link.contents[0].strip().lower()
        cat_names.append(cat_name)
    return cat_names

url = 'https://blog.frame.io/2020/02/03/color-spaces-101/'
wmn_exp = parse_page(url)

print(wmn_exp)