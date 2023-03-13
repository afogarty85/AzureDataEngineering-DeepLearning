import adal
import pandas as pd
import requests

# sample get request
# GET https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}?api-version=2021-06-01

uri = 'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Synapse/workspaces/{workspaceName}/sqlPools/{sqlPoolName}?api-version=2021-06-01'

# parameters
CLIENTID = 'client_id'
CLIENTSECRET = 'client_secret'
TENANT = 'tenant_id'
authority_url = 'https://login.microsoftonline.com/' + TENANT

# get context
context = adal.AuthenticationContext(authority_url)

# get token
token = context.acquire_token_with_client_credentials(
    resource='https://management.azure.com/',
    client_id=CLIENTID,
    client_secret=CLIENTSECRET
)

# REST headers; use token
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + token['accessToken']
}

# get response
resp = requests.get(url=uri, headers=headers)

# convert
resp.json()
pd.json_normalize(resp.json())



# for Synapse; Pipelines API
uri = 'https://synapse_workspace_name.dev.azuresynapse.net/pipelines?api-version=2020-12-01'
authority_url = 'https://login.microsoftonline.com/' + TENANT
context = adal.AuthenticationContext(authority_url)
token = context.acquire_token_with_client_credentials(
    resource='https://dev.azuresynapse.net/',  # data plane
    client_id=CLIENTID,
    client_secret=CLIENTSECRET
)

# REST headers
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + token['accessToken']
}
resp = requests.get(url=uri, headers=headers)

resp.json()
