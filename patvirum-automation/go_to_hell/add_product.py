curl 'http://127.0.0.1:8000/dashboard/products/add/select-type/' \
     -H 'Connection: keep-alive' \
        -H 'sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"' \
           -H 'Accept: */*' \
              -H 'X-Requested-With: XMLHttpRequest' \
                 -H 'sec-ch-ua-mobile: ?0' \
                    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36' \
                       -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
                          -H 'Origin: http://127.0.0.1:8000' \
                             -H 'Sec-Fetch-Site: same-origin' \
                                -H 'Sec-Fetch-Mode: cors' \
                                   -H 'Sec-Fetch-Dest: empty' \
                                      -H 'Referer: http://127.0.0.1:8000/dashboard/products/' \
                                         -H 'Accept-Language: en-US,en;q=0.9' \
                                            -H 'Cookie: csrftoken=8fAAVIJsTbETXGqyxVwd69F55M3Q5wWQ1XhY04h3oMVZd7yIibKk0YoL5z8nc20l; sessionid=k27cizih92yh70yk1v18v4rw3fmml6yc' \
                                               --data-raw 'csrfmiddlewaretoken=ak4VLerMmigZOJAKRAU2CoJU5vDsSBKC32LjQAZnRTx54aIUCQ89wdsA5iIZZ7O7&product_type=1' \
                                                          --compressed