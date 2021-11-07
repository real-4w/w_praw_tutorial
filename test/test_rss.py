import feedparser

#http://rss.nzherald.co.nz/rss/xml/nzhrsscid_000000002.xml

NewsFeed = feedparser.parse("http://rss.nzherald.co.nz/rss/xml/nzhrsscid_000000002.xml")

entry = NewsFeed.entries[1]

print (entry.published)
print ("******")
print (entry.summary)
print ("------News Link--------")
print (entry.link)