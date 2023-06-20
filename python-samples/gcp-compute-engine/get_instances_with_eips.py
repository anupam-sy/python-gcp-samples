import argparse
from google.cloud import compute_v1

def get_gce_with_eips(project_id):
    """ Prints all the instances with external IP in any of its network interface """
    
    instance_client = compute_v1.InstancesClient()
    agg_list = instance_client.aggregated_list(project=project_id)

    for zone, response in agg_list:
        if response.instances:
            for instance in response.instances:
                for interface in instance.network_interfaces:
                    if interface.access_configs:
                        print(f"Instance Name: {instance.name}, Instance ID: {instance.id}, Instance Zone: {zone}")
                        break

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="Your Google Cloud project ID.")
    args = parser.parse_args()
    get_gce_with_eips(args.project_id)

if __name__ == "__main__":
    main()