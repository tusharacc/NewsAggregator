import feedparser,time
from flask import Flask, jsonify

app = Flask(__name__)

news = [{
'india_news':[r'http://indianexpress.com/section/india/feed/']
},{
'world_news':[r'http://indianexpress.com/section/world/feed/']
},{
'editorials':[r'http://indianexpress.com/section/opinion/editorials/feed/']
}]

articles = []
for n in news:
	for i in n.items():
		news_type, rss_links = i
		for rss in rss_links:
			feed = feedparser.parse(rss)
			for article in feed['items']:
				url = article['id']
				headline = article['title']
				pub_datetime = article.published_parsed
				published_on = str(pub_datetime[0]) + '-' + str(pub_datetime[1]) + '-'+str(pub_datetime[2]) 
				articles.append({'url':url,'headline':headline,'published_date':published_on})
				

@app.route('/news/all',methods=['get'])
def get_all_news():
	return jsonify({'articles':articles})

if __name__ == '__main__':
    app.run(debug=True)
