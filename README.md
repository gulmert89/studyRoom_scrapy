## Notes
1) Example usage of `meta` flag to pass information:
```python
def parse(self, response):    
    my_item = response.xpath(...)
    for [...]:
        name = my_item.xpath(...)
        [...]
        
        yield response.follow(
            url=link,
            callback=self.parse_item,
            meta={"item_manufacturer": name})

def parse_item(self, response):
    name = response.request.meta["item_manufacturer"]
    [...]
```

2) **(Not read yet!)** [Passing additional data to callback functions](https://doc.scrapy.org/en/latest/topics/request-response.html#passing-additional-data-to-callback-functions)

3) For all **Requests** and to override them all:
```python
DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla..."
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # # 'Accept-Language': 'en',
}
``` 
Or we can change the `scrapy.Request` values in `yield` of the functions (`start_request`, `parse` etc.) and add `User-Agent` item to the `headers={"User_agent": "Mozilla..."}` dictionary. To observe the result, you can get the value under the `parse` function by assigning another `yield` item as ```"my_user_agent": response.request.headers["User-Agent"]```.

4) **(Not read yet!)** [Debugging Spiders](https://docs.scrapy.org/en/latest/topics/debug.html)<br>(Not tried yet!) [Udemy Video on Debugging](https://www.udemy.com/course/web-scraping-in-python-using-scrapy-and-splash/learn/lecture/16388482?start=57#notes)

5) (crawler_udmy) `Rule` class:<br>
    * There could be multiple rules (`Rule` objects) in `rules` tuple which follow certain links.
    * `callback` of this class is a `str` unlike `scrapy.Spider` class. Also, you shouldn't name it `parse` (whereas the default value is `parse_item`). 
    * `LinkExtractor` method has various link follow parameters like `allow`, `disallow`, `restrict_xpath` etc. to guide crawler while crawling links.

6) You can use `normalize-space()` function inside the `response.xpath('normalize-space(...)')` to get rid of unnecessary white spaces or new lines.

7)Let's say this returns 2 items: `'//*[@class="lister-page-next next-page"]'`. You can wrap it between paranthesis and take the desired item like: `(//*[@class="lister-page-next next-page"])[2]`

8) To specify a user agent for a specific request only (like `start_requests`), you need to use `headers` dictionary inside the function and feed the `User-Agent` key with the desired value.

9) `JS` web sites are executed in the client side. It requires a browser to be executed.

10) Browsers and their engines:<br>
    * **Chrome:** V8 Engine
    * **Firefox:** Spider Monkey
    * **Safari:** Apple Webkit (Also used by **Splash**)
    * **Edge:** Chakra

11) Optional: [Learn Lua in 15 Minutes
](http://tylerneylon.com/a/learn-lua/)

12) 