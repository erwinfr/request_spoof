# request_spoof
Small Python file to sent website requests 

Python file to sent website requests with an different originating IP for each request without using a proxy. 
It takes an input file with URLs and requests the URLS and inserts a random IP as requestor.  Use the X-Forwarded-For header.
To capture the originating IP, your website or other tools need to be configured to read this header
