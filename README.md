# request_spoof
Small Python file to sent website requests 

Python file to sent website requests with an different originating IP for each request without using a proxy. 
It takes an input file with URLs and requests the URLS and inserts a random IP as requestor.  Use the X-Forwarded-For header.
To capture the originating IP, your website or other tools need to be configured to read this header

#loggen_create_urls
The loggen_create_urls.py program takes an URL, output filename and site type as input.
usage: loggen_create_urls.py [-h] url outputfile cmstype

cmstype could be basic, wordpress or sitemapped:
  - basic will try to find url using hrefs on the page
  - wordpress will try to retrieve the wp-sitemap.xml file and recursively walk through it and store all links in the output file
  - sitemapped will try to retrieve the sitemap.xml file and store all links in the output file

  example python loggen_create_urls.py https://www.nasa.gov/ nasa wordpress will lookup the wp-sitemap.xml and walk through links in that sitemap.  
    - Currently this seems only to work with some Wordpress sites that use another sitemap file than wp-sitemap.xml.  Just test and see if it works
    - large CMS sytems seems also limited
    
