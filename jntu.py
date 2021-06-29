from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import os,time
rgno=input("Enter the full registration number to view your 3-1 cgpa and Percentage")






chrome_options=webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument('headless') #Set the parameters of the option
driver = webdriver.Chrome(chrome_options=chrome_options) # Open Google Chrome
#driver = webdriver.Chrome("chromedriver.exe", options=opt)
driver.get("https://jntukresults.edu.in/view-results-56736132.html")

sbox = driver.find_element_by_class_name("txt")
sbox.send_keys(rgno)

submit = driver.find_element_by_class_name("ci")
submit.click()
time.sleep(1)
rows = driver.find_elements_by_xpath("/html/body/div/div/div/div/center/div[1]/table/tbody/tr")
cols = driver.find_elements_by_xpath("//*[@id='rs']/table/tbody/tr[6]/td")

l=[]
k=[]
p=[]
for i in rows:
	l.append(i.text)
for i in cols:
	k.append(i.text)

v=len(l)
for i in range(1,v-1):
	p.append(list(l[i].split(" "))[-2:])
#print(p)

def grade(q):
	if(q=="COMPLETED"):
		return 0
	if(q=="O"):
		return 10
	elif(q=="S"):
		return 9
	elif(q=="A"):
		return 8
	elif(q=="B"):
		return 7
	elif(q=="C"):
		return 6
	elif(q=="D"):
		return 5

def percentage(p):
	a=0
	for i in p:
		a=a+grade(i[0])*int(i[1])
	return a
def total(p):
	a=0
	for i in p:
		a=a+int(i[1])
	return a
cgpa = round(percentage(p)/total(p),2)
percentage = round(((percentage(p)/total(p))-0.7)*10,2)
print("The Cgpa is:" + str(cgpa))
print("The Percentage is:" + str(percentage))
driver.close()

