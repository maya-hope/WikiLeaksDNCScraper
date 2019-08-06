# WikiLeaks DNC Scraper

This python program employs a Selenium WebDriver to scrape the WikiLeaks archive of leaked DNC emails: https://www.wikileaks.org/dnc-emails/

"Starting on Friday 22 July 2016 at 10:30am EDT, WikiLeaks released over 2 publications 44,053 emails and 17,761 attachments from the top of the US Democratic National Committee -- part one of our new Hillary Leaks series. The leaks come from the accounts of seven key figures in the DNC: Communications Director Luis Miranda (10520 emails), National Finance Director Jordon Kaplan (3799 emails), Finance Chief of Staff Scott Comer (3095 emails), Finanace Director of Data & Strategic Initiatives Daniel Parrish (1742 emails), Finance Director Allen Zachary (1611 emails), Senior Advisor Andrew Wright (938 emails) and Northern California Finance Director Robert (Erik) Stowe (751 emails). The emails cover the period from January last year until 25 May this year."

The program was designed for my specific needs, which is why is splits the content into 20 csv's. The code is commented in areas where you can personalize it to your needs, as they may differ.

Each page is represented in one row of the sheet. Columns:
1 - id (which email out of the 44503 is it)
2 - From:
3 - To:
4 - CC (when available)
5- Date
6 - Subject
7 - Content


Notes: 
1. For my purposes, I wanted all of the raw data in my spreadsheet. I am manipulating the formatting and cleaning the data itself later. If you don't have a need for recording the raw data, it would be smart to incorporate methods for cleaning the content before you place it in your sheet.
2. It would be more efficient to run multiple scrapers on your computer in parallel, running on different ranges of id's. I needed to keep using my computer at work while this was running in the background, and running more than 1 scaper at a time slowed down my computer too much, so I ruled it out. 
To learn how to run multiple scrapers at a time, check out this site: 
https://saucelabs.com/blog/running-your-selenium-tests-in-parallel-python
3. I have a few exception catchers in my script to make sure it doesn't get stuck on the few "empty" emails in the DNC archive. These are essentially empty emails with no content. They are irrelevant to me, so I just skip past those with a simple try: except: in a couple of areas. 

