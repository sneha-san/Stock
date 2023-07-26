import streamlit as st
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
load_dotenv(".env")

api_key = os.getenv("NEWS_API_KEY")


newsapi = NewsApiClient(api_key=api_key)


# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                           category='business',
#                                           language='en',
#                                           country='us')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2023-07-01',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=1)
#
# # /v2/top-headlines/sources
# print(top_headlines)
# print(all_articles)


def show_top_headlines():
    top_headlines = newsapi.get_top_headlines(
        q='bitcoin',
        category='business',
        language='en',
        country='us'
    )

    if top_headlines['status'] == 'ok':
        articles = top_headlines['articles']
        for article in articles:
            title = article['title']
            url = article['url']
            st.write(f"Title: {title}")
            st.write(f"URL: {url}")
            st.write('---')

def show_all_articles():
    all_articles = newsapi.get_everything(
        q='bitcoin',
        domains='bbc.co.uk,techcrunch.com',
        from_param='2023-07-25',
        to='2023-07-26',
        language='en',
        sort_by='relevancy',
        page=2
    )

    if all_articles['status'] == 'ok':
        articles = all_articles['articles']
        for article in articles:
            title = article['title']
            url = article['url']
            st.write(f"Title: {title}")
            st.write(f"URL: {url}")
            st.write('---')

def main():
    st.title('News API App')

    st.subheader('Top Headlines')
    show_top_headlines()

    st.subheader('All Articles')
    show_all_articles()

if __name__ == '__main__':
    main()
