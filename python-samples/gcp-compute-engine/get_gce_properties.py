# Import the required python libraries
from google.cloud import compute_v1

def get_instance_properties(project_id, zone, instance_name):
    """
    This function returns the google compute instance properties.
    """

    instances_client = compute_v1.InstancesClient()

    try:
        instance_properties = instances_client.get(project=project_id, zone=zone, instance=instance_name)
        if instance_properties:
            print(f"Instance Name: {instance_properties.name}")
            print(f"Instance ID: {instance_properties.id}")
            print(f"Instance Status: {instance_properties.status}")
            print(f"Instance Machine Type: {instance_properties.machine_type}")
            print(f"Instance Creation Time: {instance_properties.creation_timestamp}")
    except Exception as error:
        print(f"Error retrieving instance properties: {error}")

def main():
    """
    This main function calls the `get_instance_properties` function to get google compute instance properties.
    """

    project_id = "UPDATE_ME"
    zone = "UPDATE_ME"
    instance_name = "UPDATE_ME"

    get_instance_properties(project_id, zone, instance_name)

if __name__ == "__main__":
    main()
