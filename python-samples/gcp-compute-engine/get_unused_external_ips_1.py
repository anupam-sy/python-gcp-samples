# from google.oauth2 import service_account
from google.cloud import compute_v1

# Use this, if authentication to be done via service account
# credentials = service_account.Credentials.from_service_account_file('sa-key.json')
# addresses_client = compute_v1.AddressesClient(credentials=credentials)

def get_reserved_ips(project_ids):
    addresses_client = compute_v1.AddressesClient()

    for project_id in project_ids:
        request = compute_v1.AggregatedListAddressesRequest()
        request.project = project_id

        for region, response in addresses_client.aggregated_list(request=request):
            if response.addresses:
                for address in response.addresses:
                    if(address.address_type == "EXTERNAL" and address.status == "RESERVED"):
                        print("External IP:", address.name, "Region:", region)

def main():
    project_ids = ["UPDATE_ME"]
    get_reserved_ips(project_ids)

if __name__ == "__main__":
    main()