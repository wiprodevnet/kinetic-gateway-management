##################################################
'''
This Module written for GMM kinetic REST API
'''
##################################################
import getpass
import requests
from prettytable import PrettyTable
import urllib3

KINETIC_GATEWAYS = PrettyTable(['Name', 'Id', 'Organization ID', 'Model',
                                'Status', 'SW Version', 'Up Time'])
KINETIC_GATEWAYS.padding_width = 1

# Silence the insecure warning due to SSL Certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS = {'accept': "application/json", 'Authorization': "application/json",}

class CISCOKinetic:
    """
    This class return a kinetic getway base on originzation
    """
    def __init__(self, host, user, password):
        """
        """
        self.host = host
        self.user = user
        self.password = password

    def kinetic_login(self):
        """
        This method return login token number.
        """
        try:
            url = "https://"+self.host+"/api/v2/users/access_token"
            payload = {"otp":"string", "password":self.password,
                       "email":self.user}
            response = requests.post(url, headers=HEADERS, json=payload)
            login = ''
            if response.json():
                login = response.json()["access_token"]
        except Exception as error:
            print('Error: {}'.format(error.__str__()))
        return login

    def org_id(self, token):
        """
        This method return the organizations id based on login token
        """
        try:
            url = "https://"+self.host+"/api/v2/organizations?limit=1"
            token1 = "Token " + token
            HEADERS["Authorization"] = token1
            response = requests.get(url, headers=HEADERS, verify=False)
            data = response.json()
        except Exception as error:
            print('Error: {}'.format(error.__str__()))
        return data[0]['id']

    def gateway_list(self, orgid, token):
        """
        This method return the getway details
        """
        try:
            url = "https://"+self.host+"/api/v2/organizations/"\
                   +str(orgid)+"/gate_ways"
            token1 = "Token " + token
            HEADERS["Authorization"] = token1
            response = requests.get(url, headers=HEADERS, verify=False)
            data = response.json()
            # print data
            for each in range(0, len(data['gate_ways'])):
                KINETIC_GATEWAYS.add_row(
                    [data['gate_ways'][each]['name'],
                     data['gate_ways'][each]['id'],
                     data['gate_ways'][each]['organization_id'],
                     data['gate_ways'][each]['model'],
                     data['gate_ways'][each]['fog_director_state'],
                     data['gate_ways'][each]['sw_version'],
                     data['gate_ways'][each]['uptime']])
        except Exception as error:
            print('Error: {}'.format(error.__str__()))

if __name__ == '__main__':
    OBJ_KINETIC = CISCOKinetic(input('Host:'),
                               input('Email:'),
                               getpass.getpass('Password:'))
    LOGIN = OBJ_KINETIC.kinetic_login()
    ORGID = OBJ_KINETIC.org_id(LOGIN)
    OBJ_KINETIC.gateway_list(ORGID, LOGIN)
    print(KINETIC_GATEWAYS)
