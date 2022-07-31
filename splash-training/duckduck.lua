function main(splash, args)

    --------------------------------------------
    --------- Spoofing request headers ---------
    custom_headers = [[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
    Other HTTP headers
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    Accept-Encoding: gzip, deflate, br
    Accept-Language: en-GB,en;q=0.9,el-GR;q=0.8,el;q=0.7,en-US;q=0.6
    Host: duckduckgo.com
    Referer: https://duckduckgo.com/
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36
    SEC-CH-UA: ".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"
    SEC-CH-UA-MOBILE: ?0
    SEC-CH-UA-PLATFORM: "macOS"
    SEC-FETCH-DEST: document
    SEC-FETCH-MODE: navigate
    SEC-FETCH-SITE: same-origin
    SEC-FETCH-USER: ?1
    SSL-JA3-HASH: a872603c2b12dab865af3f7ee9bc4ef0
    UPGRADE-INSECURE-REQUESTS: 1]]
    -- splash:set_user_agent(custom_headers)
    -- headers = {['User-Agent'] = custom_headers}
    -- splash:set_custom_headers(headers)
    splash:on_request(function(request)
        request:set_header('User-Agent',custom_headers)
    end)
    --------------------------------------------
    --------------------------------------------

    url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))

    input_box = assert(splash:select("#search_form_input_homepage"))
    input_box:focus()
    input_box:send_text("my user agent")
    assert(splash:wait(0.5))
    input_box:send_keys("<Enter>")
    --[[
    button = assert(splash:select("#search_button_homepage"))
    button:mouse_click()
    --]]
    assert(splash:wait(5))

    splash:set_viewport_full()
    return {
        image = splash:png(),
        html = splash:html()
    }
end