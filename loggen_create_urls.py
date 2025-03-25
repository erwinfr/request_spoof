import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
import getopt
import argparse
import lxml
def main(argv):
   url = ''
   cmstype = ''
   inputfile = ''
   outputfile = ''
   try:
      parser = argparse.ArgumentParser(description="Helper function to create an input file for the url crawler")
      parser.add_argument("url")
      parser.add_argument("outputfile")
      parser.add_argument("cmstype")
      args=parser.parse_args()
      url=args.url
      outputfile=args.outputfile
      cmstype=args.cmstype
   except getopt.GetoptError:
      print ('loggen_create_urls.py <url> <outputfile> <basic>, <sitemapped> or <wordpress>')
      sys.exit(2)
   
   print ('Url to crawl is "', url)
   print ('Output file is "', outputfile)
   print ('cmstype file is "', cmstype)
   if cmstype != "basic":
      extract_links(url, outputfile,cmstype)
   
   else:
      extract_basic_links(url, outputfile)
     
   
links = []
#df = pd.DataFrame({"links":links})
def extract_links(url, outputfile, cmstype):
   print(url, cmstype)
   global links
   if cmstype == "wordpress":
      linkxml = url + "/wp-sitemap.xml"
   if cmstype == "sitemapped":
      linkxml = url + "/sitemap.xml"
      print(linkxml)
   """output_file = outputfile"""
   source_url = requests.get(linkxml)
        
      
   with open(outputfile, 'a+') as output_file:
      soup = BeautifulSoup(source_url.text, 'xml')
      for item in soup.find_all('loc'):
          try:
            if '.xml' in item.text:
               #Send another GET request to the .xml link
               r = requests.get(item.text)
               new_soup = BeautifulSoup(r.text, 'xml')
               for new_item in new_soup.findAll('loc', recursive=True):
                  output_file.write(new_item.text  + "\n")
                  print(new_item.text)
            #If the link doesn't have a .xml extension, add it to the list
            else:
                  output_file.write(item.text  + "\n")
                  print(item.text)
          except TypeError:
               pass

                
def extract_basic_links(url, outputfile):  
    global links
    source_url = requests.get(url)
    
    with open(outputfile, 'a+') as output_file:
         
         soup = BeautifulSoup(source_url.content,'html.parser')
         #print(soup)
         a_tags=soup.find_all('a',href=True, recursive=True)
         for a_tag in a_tags:
            if str(url) not in a_tags:
               output_file.write(a_tag.get('href') + "\n")
               print(a_tag.get('href'))
         output_file.close()


if __name__ == "__main__":
   main(sys.argv[1:])