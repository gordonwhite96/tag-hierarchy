import csv
import requests
import json

def gettags(token, group):
    d={}
    params = ( ('access_token', token),)
    groupId = group
    getdata = '{"groupId":'+group+'}'
    tag = requests.get('https://api.samsara.com/v1/tags', 
           params=params, data=getdata)
    data = json.loads(tag.text)
    for tag in data['tags']:
        name = tag['name']
        tagid=tag['id']
        d[name] = tag['id']
    return d

def getdrivers(token, group):
    d={}
    params = ( ('access_token', token),)
    groupId = group
    postdata = '{"groupId":'+group+'}'
    driver = requests.post('https://api.samsara.com/v1/fleet/drivers', 
           params=params, data=postdata)
    data = json.loads(driver.text)
    for driver in data['drivers']:
        name = driver['name']
        #driverid=driver['id']
        d[name] = driver['id']
    return d

def modifytag(token, tag, driver):
    driverId=str(driver)
    tagId=str(tag)
    params = ( ('access_token', token),)
    patchdata = '{"add":{"drivers":[{"id":'+driverId+'}]}}'
    driver = requests.patch('https://api.samsara.com/v1/tags/'+tagId, 
           params=params, data=patchdata)
    print patchdata
    print driver.status_code

def updatestuff(token,group,alltags,item):
    tagId=alltags[item[2]]
    driverId1=alldrivers[item[3]]
    driverId2=alldrivers[item[4]]
    print "Tag name: %s ID: %d" % (item[2], tagId)
    print "Driver name: %s ID: %d" % (item[3], driverId1)
    print "Driver name: %s ID: %d" % (item[4], driverId2)
    modifytag(token,tagId, driverId1)
    modifytag(token,tagId, driverId2)
    #driverId(token,group,item[3])
    #modifytag(token,group,tagId, driverId)


with open('tagload.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if row[0]=='token':
            apitoken=row[1]
        elif row[0]=='group':
            apigroup=row[1]
        elif row[0]=='org':
            alltags=gettags(apitoken,apigroup)
            alldrivers=getdrivers(apitoken,apigroup)
        else:
	    updatestuff(apitoken, apigroup, alltags, row)
        line_count+=1
