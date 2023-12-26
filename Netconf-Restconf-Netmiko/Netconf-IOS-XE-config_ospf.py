from ncclient import manager
import xmltodict
import pprint
import json

class config_ospf_iosxe:
    def __init__(self):
        self.username = input('Enter Username: ')
        self.password = input('Enter Pssword: ')
        self.IOSXEIPs = open('IOSXEIPs.txt', 'r')
        self.cmd = """
        <config>
            <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                <router>
                    <ospf xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf">
                        <id>16</id>
                        <network>
                            <ip>10.16.16.0</ip>
                            <mask>0.0.0.255</mask>
                            <area>0</area>
                        </network>
                    </ospf>
                </router>
            </native>
        </config>
        """

    def ios_xe_netconf(self):
        for ip in self.IOSXEIPs:
            print(ip)
            with manager.connect(host=ip, port="830", username=self.username, password=self.password, hostkey_verify=False) as csr:
                result = csr.edit_config(config=self.cmd, target="running")
                print(result)
                print(type(result))
                pp = pprint.PrettyPrinter(indent=4)
                pp.pprint(json.dumps(xmltodict.parse(str(result))))

        self.IOSXEIPs.close()

obj1 = config_ospf_iosxe()
obj1.ios_xe_netconf()
