#imports
from selenium import webdriver
import html
import csv

#each email is on its own page, the differentiated by the email id (1 through 44503)
#goes to the page of the email you are scraping
def gotoemailpage(driver,i):
	url="https://www.wikileaks.org/dnc-emails/emailid/"+i
	driver.get(url)
    
#returns the email content
def getcontent(driver):
	try:
		content = driver.find_element_by_css_selector("#content")
        	the_text = content.text
        	the_text=html.unescape(the_text)
        	return the_text
    	except:
        	return
        
#format the content to fit into the spreadsheet's row as I desired. See README for column specs.
def formatcontent(text,i):
	try:
		complete=[]
        	splitted=text.split("\n")
        	complete.append(i)
        	complete.append(splitted[1])
        	complete.append(splitted[2])
        	complete.append(splitted[3])
        	complete.append(splitted[4])
        
		#some emails have a CC: row, others don't. So sometimes length of splitted array is 5, others 4
		if("CC: " in splitted[3]):
			complete.append(splitted[5])
			#format the content after the subject
			aftersub=text.split(splitted[5])
			betterHTML = aftersub[1]
			b=html.unescape(betterHTML)
			b=b.replace("\n"," ")
		else:
			aftersub=text.split(splitted[4])
			betterHTML = aftersub[1]
			b=html.unescape(betterHTML)

		complete.append(b)
		return complete
	except:
		return
				
#given the path to the csv file and the content for the row, print the content
#use append mode to write a new row each time, instead of overwriting in the same row
def writeincsv(path,line):
	try:
		with open(path, mode='a') as dnc_file:
			dnc_writer = csv.writer(dnc_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
			dnc_writer.writerow(line)
	except:
        	return
				
def run():
	#THIS IS THE PART WHERE YOU DEFINE THE PATHS TO THE CSVs YOU'RE WRITING IN. 
	path1='/Users/YOU/DIRECTORY/FILENAME1.csv'
	#etc
	path20='/Users/YOU/DIRECTORY/FILENAME20.csv'
	
	#usual path to chromedriver (i think): /usr/local/bin/chromedriver
	driver=webdriver.Chrome('/PATH/TO/YOUR/chromedriver')
    
	#number of these loops depends on how many csv's you're writing to/whether you're running multiple processes at once
	#this is just the basic premise of the loop to read and write the page content to your csv
	for i in range(START,FINISH+1):
		j=str(i)
		try:
			gotoemailpage(driver,j)
			writeincsv(path1,formatcontent(getcontent(driver),i))
		except:
			#whatever you want here, just want it to keep going
			print(i)

	driver.quit()    

#run the damn thing!
run()
