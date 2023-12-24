from pyzabbix import ZabbixAPI, ZabbixAPIException

# Zabbix API information
zabbix_url = "http://your-zabbix-server/zabbix"
zabbix_user = "your-username"
zabbix_password = "your-password"

# Host name filter
host_name_filter = '-SW'

def get_zabbix_hosts(zabbix_url, zabbix_user, zabbix_password, host_name_filter):
    # Connect to Zabbix server
    try:
        zabbix = ZabbixAPI(zabbix_url)
        zabbix.login(zabbix_user, zabbix_password)
        print(f"Connected to Zabbix API Version {zabbix.api_version()}")

        # Get all hosts with the specified name filter
        hosts = zabbix.host.get(filter={'host': host_name_filter}, output=['hostid', 'host', 'status', 'ip'])
        
        # Filter active hosts
        active_hosts = [host for host in hosts if host['status'] == '0']

        # Get the list of IP addresses
        ip_addresses = [host['ip'] for host in active_hosts]

        return ip_addresses

    except ZabbixAPIException as e:
        print(f"Error: {e}")
    finally:
        if 'zabbix' in locals():
            zabbix.logout()

if __name__ == "__main__":
    # Get the list of IP addresses from Zabbix
    ip_addresses_list = get_zabbix_hosts(zabbix_url, zabbix_user, zabbix_password, host_name_filter)

    # Print the list of IP addresses
    print("List of IP addresses for active hosts with '-SW' in their names:")
    for ip_address in ip_addresses_list:
        print(ip_address)




		