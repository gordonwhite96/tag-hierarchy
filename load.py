import csv
import requests
import config

def createtag(token, group, tagname):
    params = ( ('access_token', token),)
    groupId = group
    postdata = '{"name":"'+tagname+'"}'
    tag = requests.post('https://api.samsara.com/v1/tags', 
           params=params, data=postdata)
    return tag.status_code

def createdriver(token, group, drivername):
    params = ( ('access_token', token),)
    groupId = group
    postdata = '{"name":"'+drivername+'"}'
    driver = requests.post('https://api.samsara.com/v1/fleet/drivers/create', 
           params=params, data=postdata)
    return driver.status_code

def loadrow(token,group,item):
    createtag(token,group,item[0])
    createtag(token,group,item[1])
    createtag(token,group,item[2])
    createdriver(token,group,item[3])
    createdriver(token,group,item[4])


with open('tagload.csv') as csv_file:
    apitoken=config.token
    apigroup=config.group
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if row[0]=='org':
            print "skip headers"
        else:
	    loadrow(apitoken, apigroup, row)
        line_count+=1
