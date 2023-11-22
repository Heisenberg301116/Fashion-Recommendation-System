from pinscrape import pinscrape
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory path
parent_path = os.path.dirname(script_directory)
os.chdir(parent_path)
print(os.getcwd())

title = input("Enter the title to scrap: ")
# title = 'Alia Bhatt'

details = pinscrape.scraper.scrape(title, "Trending fashion", {}, 10, 15)

if details["isDownloaded"]:
    print("\nDownloading completed !!")
    print("\n\n")
    print(f"\nTotal urls found: {len(details['extracted_urls'])}")
    print("\n\n")
    print(f"\nTotal images downloaded (including duplicate images): {len(details['url_list'])}")
    print("\n\n", details, "\n\n")
    
else:
    print("\nNothing to download !!")
    
    
"""
`scrape("messi", "output", {}, 10, 15)` <br/>
- `"messi"` is keyword
- `"output"` is path to a folder where you want to save images
- `{}` is proxy list if you want to add one (optional)
- `10` is a number of threads you want to use for downloading those images (optional)
- `15` is the maximum number of images you want to download (optional)
"""