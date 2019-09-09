from flask import Flask, render_template, jsonify, redirect, request
from flask_pymongo import PyMongo

from splinter import Browser
from bs4 import BeautifulSoup

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    mars = mongo.db.mars

    # Put everything from Jupyter Notebook Here
    # Set the executable path and initialize the chrome browser in splinter
   
    executable_path = {'executable_path': 'C:\\Users\\enere\\Desktop\chromedriver'}
    browser = Browser('chrome', **executable_path)

    ##### MARS NEWS Scrape #####
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_scraper = BeautifulSoup(html, 'html.parser')

    # Use the parent element to find the first a tag and save it as `news_title`
    title_element = news_scraper.find('div', {'class': 'content_title'})
    news_title = title_element.get_text()

    # Use the parent element to find the paragraph text
    teaser_element = news_scraper.find('div', {'class': 'article_teaser_body'})
    teaser_text = teaser_element.get_text()

    ##### JPL Space Images Featured Image #####
    # Visit URL
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    full_image_elem = browser.find_by_id('full_image')
    full_image_elem.click()

    # Find the more info button and click that
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_elem = browser.find_link_by_partial_text('more info')
    more_info_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_scraper = BeautifulSoup(html, 'html.parser')

    # find the relative image url
    img_element = img_scraper.find('img', {'class': 'main_image'})

    # find the relative image url
    img_src = img_element.get('src')

    # Use the base url to create an absolute url
    img_url = f'https://www.jpl.nasa.gov{img_src}'

    ##### Mars Weather Scrape
    # Visit URL
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    weather_soup = BeautifulSoup(html, 'html.parser')

    # First, find a tweet with the data-name `Mars Weather`
    mars_weather_tweet = weather_soup.find('div', attrs={"class": "tweet", "data-name": "Mars Weather"})

    # Next, search within the tweet for the p tag containing the tweet text
    mars_weather = mars_weather_tweet.find('p', 'tweet-text').get_text()
    mars_weather

        ##### Mars Facts Scrape

    # Visit URL
    url = 'https://space-facts.com/mars/'
    browser.visit(url)

    tables = pd.read_html(url)
    
    html_table = df.to_html()
    
    df.to_html('table.html')

    type(tables)

    df = tables[0]
    df.columns = ['Mars - Earth Comparison', 'Mars', 'Earth']
   
    # Set the index to Mars - Earth Comparison column
    df.set_index('Mars - Earth Comparison', inplace=True)

    #convert DataFrames back to HTML tables using the to_html function
    html_table = df.to_html()


    ##### Mars Hemisphere Scrape
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    hemisphere_image_urls = []

    # First, get a list of all of the hemispheres
    links = browser.find_by_css("a.product-item h3")

    # Next, loop through those links, click the link, find the sample anchor, return the href
    for i in range(len(links)):
        hemisphere = {}
    
    # We have to find the elements on each loop to avoid a stale element exception
        browser.find_by_css("a.product-item h3")[i].click()
    
    # Next, we find the Sample image anchor tag and extract the href
        sample_elem = browser.find_link_by_text('Sample').first
        hemisphere['img_url'] = sample_elem['href']
    
    # Get Hemisphere title
        hemisphere['title'] = browser.find_by_css("h2.title").text
    
    # Append hemisphere object to list
        hemisphere_image_urls.append(hemisphere)
    
        hemisphere_image_urls
    # Finally, we navigate backwards
        browser.back()  
       

    browser.quit()
    ##### Create a dictionary to store our scraped data
    scraped_data = {
        'News Title': news_title,
        'Teaser Text': teaser_text,
        'Image URL': img_url,
        'Mars Weather': mars_weather,
        'Mars Hemisphere': hemisphere_image_urls,
        'Mars Facts': html_table
    }

    ##### Put into MongoDB
    mars.update({}, scraped_data, upsert=True)

    return jsonify(scraped_data)


if __name__ == "__main__":
    app.run()
