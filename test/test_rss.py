import feedparser

#http://rss.nzherald.co.nz/rss/xml/nzhrsscid_000000002.xml

NewsFeed = feedparser.parse("http://rss.nzherald.co.nz/rss/xml/nzhrsscid_000000002.xml")
print(len(NewsFeed['entries']))

for entry in NewsFeed['entries']:
    print(f"Date: {entry.published}, Title {entry.title}, Link: {entry.link}")

#entry = NewsFeed.entries[1]
#print(len(entry))
#print (entry.published)
#print ("******")
#print (entry.title)
#print ("------News Link--------")
#print (entry.link)