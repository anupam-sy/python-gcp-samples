"""Get Unsed External IP Addresses

This script prints all the unused external IP addresses of all the projects
present under a parent(folder/organization) along with details like (region,
external IP name, project ID)

This script requires that Cloud Client Libraries of gcp services 
`google-cloud-compute` and `google-cloud-resource-manager` be installed 
within the Python environment you are running this script in.

This file can also be imported as a module and contains the following
functions:

    * get_gcp_projects - returns the list of projects under a parent
    * get_reserved_ips - prints the unused eips along with details
    * main - the main function of the script
"""

from google.cloud import compute_v1, resourcemanager_v3

def get_gcp_projects(parent):
    """Returns the list of projects under a parent (folder/org)

    Args:
        parent (str): the id of the parent whose projects to be returned

    Returns:
        list: a list of strings representing the projects under a parent
    """

    project_ids = []

    # Create a client
    client = resourcemanager_v3.ProjectsClient()
    # Initialize request argument(s)
    request = resourcemanager_v3.ListProjectsRequest(parent=parent)
    # Make the request
    page_result = client.list_projects(request=request)
    # Handle the response
    for response in page_result:
        project_ids.append(response.project_id)
    return project_ids

def get_reserved_ips(project_ids):
    """Prints the list of unused external IPs of a GCP Project

    Args:
        project_ids (list): the list of the projects whose unused external
        IP addresses to be printed

    Returns:
        it returns None as the function doesn't have any return statement
        but it prints the list of unused external IPs of a GCP Project
    """

    addresses_client = compute_v1.AddressesClient()

    for project_id in project_ids:
        request = compute_v1.AggregatedListAddressesRequest()
        request.project = project_id

        for region, response in addresses_client.aggregated_list(request=request):
            if response.addresses:
                for address in response.addresses:
                    if(address.address_type == "EXTERNAL" and address.status == "RESERVED"):
                        print(f"Project ID: {project_id} External IP: {address.name} Region: {region}")

def main():
    parent="organizations/UPDATE_ME" # For folder, use "folders/UPDATE_ME"
    project_ids = get_gcp_projects(parent)
    get_reserved_ips(project_ids)

if __name__ == "__main__":
    main()