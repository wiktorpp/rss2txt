import feedparser
import os


def is_empty_or_irrelevant(text):
    return not text or text.isspace() or len(text.strip()) <= 2


while True:
    print("")
    print("_________________________")
    print("  RSS to TXT DOWNLOADER  ")
    print("")
    feed_url = input(r"RSS feed url: ")
    feed = feedparser.parse(feed_url)

    # feed name to file name
    feed_title = feed.feed.title if feed.feed.title else "feed_output"
    output_file = f"{feed_title.replace(' ', '_').lower()}_output.txt"

    file_exists = os.path.isfile(output_file)

    with open(output_file, 'a', encoding='utf-8') as file:
        for entry in feed.entries[::-1]:
            if entry.description and not is_empty_or_irrelevant(entry.description and entry.summary):
                file.write(entry.published + '\n')
                print(entry.published)
                file.write(entry.title + '\n')
                print(entry.title)
                file.write(entry.link + '\n')
                print(entry.link)
                file.write(entry.description + '\n')
                print(entry.description)
                file.write("\n---\n\n")
                print("\n---\n")

    file_path = os.path.abspath(output_file)
    print(f"RSS feed saved to: {file_path}")
    another_feed = input("Another feed? (y/n): ")
    if another_feed.lower() != 'y':
        break
