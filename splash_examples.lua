-- Also see: Learn Lua in 15 Minutes - http://tylerneylon.com/a/learn-lua

--duckduckgo.com example:
--Subject: type and go!
function main(splash, args)
    --To change user-agent request header:
    user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    splash:set_user_agent(user_agent)
    
    --Alternatively, we can create an object for other request headers:
    --[[ --commented out
    headers = {
      ["User-Agent"] = user_agent
    }
    splash:set_custom_headers(headers)
    ]]
  
    --Or, it will be called on each request sent we use:
    splash:on_request(
    function(request)
        request:set_header("User-Agent", user_agent)
      end
    )
    
    url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))
    
    --Selecting the "id" of the search box
    input_box = assert(splash:select("#search_form_input_homepage"))
    input_box:focus() --need to focus to type things
    input_box:send_text("what is my user agent")
    assert(splash:wait(0.5))
    
    --1st way: click the search button
    --Selecting the "id" of the search button:
    --[[ --commented out--
    button = assert(splash:select("#search_button_homepage"))
    button:mouse_click()
    ]]
  
    --2nd way: press enter
    input_box:send_keys("<Enter>")
    
    assert(splash:wait(3))
    
    --to get the preview of the whole page
    -- splash:set_viewport_full()
    
    return {
      html = splash:html(),
      png = splash:png(),
      -- har = splash:har(),
    }
end