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

def deletetag(token,group, tag):
    tagId=str(tag)
    params = ( ('access_token', token),)
    groupId = group
    getdata = '{"groupId":'+group+'}'
    deltagrequest = requests.delete('https://api.samsara.com/v1/tags/'+tagId, params=params, data=getdata)
    if deltagrequest.status_code==200:
        print "deleted ", tag
        return deltagrequest.status_code
    else:
        print "failed ", tag 

apitoken=config.token
apigroup=config.group
alltags=gettags(apitoken,apigroup)
for tag in alltags:
    deletetag(apitoken, apigroup, alltags[tag])
