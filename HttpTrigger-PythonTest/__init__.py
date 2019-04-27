import logging
import os
import azure.functions as func
#import json
#from msrestazure.azure_active_directory import MSIAuthentication
#from azure.mgmt.resource import ResourceManagementClient, SubscriptionClient
from azure.common.credentials import ServicePrincipalCredentials
#from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.keyvault import KeyVaultClient
#from azure.mgmt.resource.resources import ResourceManagementClient
#from haikunator import Haikunator


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    servicePrincipalClientId = os.environ.get('servicePrincipalClientId')
    servicePrincipalSecret = os.environ.get('servicePrincipalSecret')
    servicePrincipalTenant = os.environ.get('servicePrincipalTenant')
    credentials = ServicePrincipalCredentials(
        client_id= servicePrincipalClientId,
        secret=servicePrincipalSecret,
        tenant=servicePrincipalTenant
    )
   
    # credentials = MSIAuthentication()
    #kv_client = KeyVaultManagementClient(credentials,'subscriptionKeyHere')
    kv_client = KeyVaultClient(credentials)
    kvUrl = os.environ.get('kvUrl')
    kvSecretName = os.environ.get('kvSecretName')
    kvSecretVersion = os.environ.get('kvSecretVersion')
    kvSecret = kv_client.get_secret(kvUrl,kvSecretName,kvSecretVersion)
    kvSecretValue = kvSecret.value
    logging.info(f"Value from keyVault {kvSecretValue}")
    
    return func.HttpResponse(f"Don't tell anyone about {kvSecretValue}")
    