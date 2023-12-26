import requests
import json
import pprint
import urllib3

class nxapi_json:
    def __init__(self):
        self.switchuser= input("Enter Username: ")
        self.switchpassword= input("Enter Password: ")
        self.ip = input("Enter IP of NX Device: ")
        self.url='https://{}/ins'.format(self.ip)
        self.myheaders={'content-type':'application/json'}
        self.payload={
          "ins_api": {
            "version": "1.0",
            "type": "cli_show",
            "chunk": "0",
            "sid": "sid",
            "input": "sh ip int br vrf all",
            "output_format": "json"
          }
        }

    def run_nxapi(self):
        urllib3.disable_warnings()
        response = requests.post(self.url,data=json.dumps(self.payload), headers=self.myheaders,auth=(self.switchuser,self.switchpassword),verify=False).json()
        #print(json.dumps(response, indent=4))
        row_intf = response["ins_api"]["outputs"]["output"]["body"]["TABLE_intf"]["ROW_intf"]
        #print(row_intf)
        for i in range(len(row_intf)):
            print(row_intf[i]['prefix'])

obj1 = nxapi_json()
obj1.run_nxapi()
