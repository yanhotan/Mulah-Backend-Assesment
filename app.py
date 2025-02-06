import streamlit as st
import json
from datetime import datetime
from scraper.scrape_verge import scrape_the_verge
from utils.helpers import load_articles, save_articles

st.set_page_config(page_title="The Verge Title Aggregator", layout="wide")

def load_articles():
    with open("data/articles.json", "r") as file:
        return [(datetime.fromisoformat(article["date"]), article["title"], article["link"]) for article in json.load(file)]

articles = load_articles()

with open('static/styles.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📰 The Verge Title Aggregator")
st.write("Displaying article headlines from January 1, 2022 onwards.")

articles.sort(reverse=True, key=lambda x: x[0])
if articles:
    for article_date, title, link in articles:
        st.write(f"🕒 **{article_date.strftime('%B %d, %Y')}**")
        st.markdown(f"[{title}]({link})", unsafe_allow_html=True)
        st.write("---")

if st.button('Refresh Scrape'):
    with st.spinner('Scraping articles from The Verge...'):
        articles_scraped = scrape_the_verge()

    if articles_scraped:
        articles_scraped.sort(reverse=True, key=lambda x: x[0])  # Sort anti-chronologically
        save_articles(articles_scraped) 
        st.write(f"Found {len(articles_scraped)} articles.")
        for article_date, title, link in articles_scraped:
            st.write(f"🕒 **{article_date.strftime('%B %d, %Y')}**")
            st.markdown(f"[{title}]({link})", unsafe_allow_html=True)
            st.write("---")
    else:
        st.write("No new articles found or failed to scrape.")
