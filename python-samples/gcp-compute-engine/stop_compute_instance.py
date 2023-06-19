from google.cloud import compute_v1

def get_compute_instances(project_id):
    """
    Gets the details list of targetted Google Compute Engine instances.
    """

    instance_list = [] # Initialize an empty list to store instance details

    instance_client = compute_v1.InstancesClient()
    agg_list = instance_client.aggregated_list(project=project_id)

    for zone, response in agg_list:
        if response.instances:
            for instance in response.instances:
                if ("purpose", "test") in instance.labels.items():
                    temp_instance_dict = {} # Initialize a dictionary to temporary hold and dump values in a dict
                    temp_instance_dict.update({"instance_name" : instance.name})
                    temp_instance_dict.update({"instance_zone" : zone.split("/")[1]})
                    temp_instance_dict.update({"instance_project" : project_id})
                    instance_list.append(temp_instance_dict)
    return instance_list

def stop_compute_instances(instance_list):
    """
    Stops running Google Compute Engine instances.
    """
    instance_client = compute_v1.InstancesClient()

    for instance in instance_list:
        operation = instance_client.stop(
            project=instance["instance_project"], zone=instance["instance_zone"], instance=instance["instance_name"]
        )
        result = operation.result(timeout=300)

    print("Stop operation completed for targetted compute instances.")

def main(project_id):
    instance_list = get_compute_instances(project_id)
    stop_compute_instances(instance_list)

if __name__ == "__main__":
    project_id = "UPDATE_ME"
    main(project_id)