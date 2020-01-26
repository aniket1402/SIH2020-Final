from bs4 import BeautifulSoup
from mobile_extractor import *
import urllib
import csv
import urllib.request
from city_calc import *

def innerHTML(element):
    return element.decode_contents(formatter="html")

def get_name(body):
	return body.find('span', {'class':'jcn'}).a.string

def get_phone_number(body):
	try:
		score = str(body.find('p', {'class':'contact-info'}).span)
		# print(score)
		# print(type(score))
		ph_no = number_extract(score)
		# print(ph_no)
		# print(score)
		return ph_no
	except AttributeError:
		return ''

def get_address(body):
	return body.find('span', {'class':'mrehover'}).text.strip()

def get_location(body):
	text = body.find('a', {'class':'rsmap'})
	if text == None:
		return
	text_list = text['onclick'].split(",")
	
	latitutde = text_list[3].strip().replace("'", "")
	longitude = text_list[4].strip().replace("'", "")
	
	return latitutde + ", " + longitude

def contact_police(cityy):
	service_count = 1

	fields = ['Name', 'Phone', 'Address', 'Location']
	out_file = open('Contact_police.csv','w')
	csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)

	# Write fields first
	#csvwriter.writerow(dict((fn,fn) for fn in fields))

	url="https://www.justdial.com/"+cityy+"/Police"
	print(url)
	req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
	page = urllib.request.urlopen( req )
	# page=urllib2.urlopen(url)

	soup = BeautifulSoup(page.read(), "html.parser")
	services = soup.find_all('li', {'class': 'cntanr'})

	# Iterate through the 10 results in the page
	for service_html in services:

		# Parse HTML to fetch data
		dict_service = {}
		name = get_name(service_html)
		phone = get_phone_number(service_html)
		if len(phone) > 10 or '-' in phone:
			continue
		address = get_address(service_html)
		location = get_location(service_html)
		if name != None:
			dict_service['Name'] = name
		if phone != None:
			# print('getting phone number')
			dict_service['Phone'] = phone
		if address != None:
			dict_service['Address'] = address
		if location != None:
			dict_service['Address'] = location

		# Write row to CSV
		csvwriter.writerow(dict_service)

		print("#" + str(service_count) + " " , dict_service)
		service_count += 1


	out_file.close()








