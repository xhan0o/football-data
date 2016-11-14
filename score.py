import requests
from pprint import pprint
import http.client
import datetime
import json
import score

def apicall(url,payload):
    headers = { 'X-Auth-Token': '040594424f1144b892cc2f93b91a503a', 'X-Response-Control': 'minified' }
    result=requests.get('http://api.football-data.org/v1/competitions/'+url, params=payload,headers=headers)
    response = result.json()
    return response

def apiteam(url,payload):
    headers = { 'X-Auth-Token': '040594424f1144b892cc2f93b91a503a', 'X-Response-Control': 'minified' }
    result=requests.get('http://api.football-data.org/v1/teams/'+url, params=payload,headers=headers)
    response = result.json()
    return response

payload= {}

def execute ():
    command=input("Enter:")
    if command=='league':
        season = input('Season: ')
        payload["season"]=season
        result=apicall("",payload)
        leaguedata=result
        print(">>> Leagure Name + Current Match Day + League ID")
        for i in leaguedata :
            print(i["caption"],i["currentMatchday"],i["id"])

    elif command=='table':
        matchid = input('League ID:')
        number = input('Match Day:')
        payload["matchday"]=number
        result=apicall(matchid+"/leagueTable/",payload)
        standing=result["standing"]
        print ("-->League Name:"+result['leagueCaption'])
        print ("-->Match day:"+str(result['matchday']))
        print (">>> Teams + Points")
        for i in standing :
            print (i["team"]+"\t",i["points"])

    elif command=='teams':
        leagueid=input('League ID:')
        result=apicall(leagueid+"/teams/",payload)
        print ("--> Total Teams:",result['count'])
        teams =result["teams"]
        for i in teams :
            print(i["name"]+"\t",i["id"])

    elif command=='fixtures':
        matchid = input('League ID:')
        np=input('Next(n)/Past(p):')
        number = input('Days:')
        payload["timeFrame"]=np+number
        result=apicall(matchid+"/fixtures/",payload)
        print("Total Fixtures",result["count"])
        fixtures =result["fixtures"]
        a=0
        for i in fixtures :
            a+=1
            print("Fixture",a)
            print(i["awayTeamName"],i["awayTeamId"])
            print(i["homeTeamName"],i["homeTeamId"])
            print("Date",i["date"][0:10]+"Time",i["date"][12:20],i["matchday"])
            print(i["result"],i["status"])

    elif command=='players' :
        number=input('Team ID:')
        #payload["id"]=number
        result=apiteam(number+"/players",payload)
        players =result["players"]
        for i in players :
            print(i["name"]+",",i["nationality"]+",\t",i["position"])

    elif command=='team' :

        number=input('Team ID:')
        result=apiteam(number,payload)
        print("-->Team Name  Team ID  Squad Value")
        print(result["name"],result["id"] ,result["squadMarketValue"])



    else:
        print("no valid response")

    #headers = { 'X-Auth-Token': '040594424f1144b892cc2f93b91a503a', 'X-Response-Control': 'minified' }

    #result=requests.get('http://api.football-data.org/v1/competitions/426/leagueTable/', params=payload,headers=headers)
    #response = result.json()

    #pprint.pprint (response)
