import csv
import requests
import json
import config

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

def modifytag(token, tag, parent):
    tagId=str(tag)
    ptagId=str(parent)
    params = ( ('access_token', token),)
    patchdata = '{"parentTagId":'+ptagId+'}'
    driver = requests.patch('https://api.samsara.com/v1/tags/'+tagId, 
           params=params, data=patchdata)
    print patchdata
    print driver.status_code

def updatestuff(token,group,alltags,item):
    tagId=alltags[item[2]]
    ptag1=alltags[item[1]]
    ptag2=alltags[item[0]]
    noparentId=0
    modifytag(token,tagId, noparentId)
    modifytag(token,ptag1, noparentId)

with open('tagload.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count=0
    apitoken=config.token
    apigroup=config.group
    for row in csv_reader:
        if row[0]=='org':
            alltags=gettags(apitoken,apigroup)
        else:
	    updatestuff(apitoken, apigroup, alltags, row)
        line_count+=1
