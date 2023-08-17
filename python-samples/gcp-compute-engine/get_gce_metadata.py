# Import the required python libraries
import requests

def get_instance_metadata(root_url, request_header, metadata_list):
    """
    This function returns the google compute instance metadata.
    
    Note: You can query the contents of the metadata server by making a request to the root URLs from within 
    a virtual machine instance. 
    Use the http://metadata.google.internal/computeMetadata/v1/ root URL to make requests to metadata server.

    Ref: https://cloud.google.com/compute/docs/metadata/overview#querying
    """

    for metadata in metadata_list:
        try:
            response = requests.get(root_url + metadata, headers=request_header)
            print(response.text)
        except Exception as error:
            print(f'Error occurred: {error}')

def main():
    """
    This main function calls the `get_instance_metadata` function to get google compute instance metadata.
    """
    
    root_url = "http://metadata.google.internal/computeMetadata/v1/"
    request_header = {"Metadata-Flavor": "Google"}
    metadata_list = ["instance/hostname", "instance/network-interfaces/0/ip"]

    get_instance_metadata(root_url, request_header, metadata_list)

if __name__ == "__main__":
    main()
