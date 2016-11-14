import sys
import requests
from pprint import pprint
import http.client
import datetime
import json
import score
import weather
strcmd=sys.argv[1]
#number=sys.argv[2]

cmd=strcmd.split( )

if cmd[0]=="#weather" :
    weather.execute(cmd[1])
elif command=="Football":
    score.execute()
else:
    print("invalid command")
