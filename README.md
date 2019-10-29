# kinetic-gateway-management
Sample gateway management sample code using kinetic APIs

## Sample Code Description:
GMM - Retrieve list of Gateways deployed in specific Organization - based on org id

## Description:
1. Gateways will be claimed in a specific GMM instance, the location details (address with zipcode) must be available.
2. Input to the script will be GMM instance,  organization ID.
3. Gateways matching the requirements will be displayed in tabular format

## Refer below link for more details:
  1. https://developer.cisco.com/docs/kinetic/#!gmm-overview/gmm-overview
  2. https://developer.cisco.com/docs/kinetic-api/
  3. https://github.com/CiscoDevNet/iox-app-template
  
## GMM Kinetic REST API:
1. Generate a user token or API key to authenticate the API methods
2. Generate a user token for your Cisco Kinetic user account using the POST /v2/users/access_token v2 API.
3. Enter the email and password and host(us.ciscokinetic.io) for your Cisco Kinetic account.
4. Get the user organization id using GET /api/v2/organizations  v2 API.
5. Get the user organization Gatway details using GET v2/organizations/{organizationID}/gate_ways v2 API.

## Technologis:
Python3
requests

## How to Get Started:
1. Clone this repo
2. Install all the necessary packages (Python3,requests)
3. Run the app(python3 kinetic.py)
4. Enter host address and Email, Password

## kinetic-gateway-management Output:
![kinetic-gateway-management](https://github.com/wiprodevnet/kinetic-gateway-management/blob/master/images/kineticGMM.PNG)
   
  

