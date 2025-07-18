# https://www.youtube.com/watch?v=945F3SxW7Tk
import trafilatura

# url = 'https://n.news.naver.com/article/003/0013072198?cds=news_media_pc&type=editn'

# html = trafilatura.fetch_url(url)

# # print(html)

# print(type(trafilatura.extract(html)))

# # text = trafilatura.extract(html)
# text = trafilatura.extract(html, 
#                            output_format='json',
#                            )

# text = trafilatura.extract(html, 
#                            output_format='xml',
#                            )


# print(text)



# RSS
from trafilatura import feeds, fetch_url, extract

# https://www.mk.co.kr/rss/
feed_url = 'https://www.mk.co.kr/rss/30000001/'
feed_list = feeds.find_feed_urls(feed_url)
print(len(feed_list))

# The 1 in enumerate(feed_list, 1) specifies the starting index for the enumeration.
for num, feed in enumerate(feed_list, 1):
    html = fetch_url(feed)
    text = extract(html)

    print(f"<<<<<{num}>>>>>")
    print(text)
    print(f"feed url:: {feed}")
    print()
