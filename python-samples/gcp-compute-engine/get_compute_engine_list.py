import argparse
from google.cloud import compute_v1

def get_compute_instances(project_id):
    """ Prints all the google compute instances of a project """
    instance_client = compute_v1.InstancesClient()
    
    request = compute_v1.AggregatedListInstancesRequest()
    request.project = project_id
    request.max_results = 50

    agg_list = instance_client.aggregated_list(request=request)

    for zone, response in agg_list:
        if response.instances:
            for instance in response.instances:
                print(f"Instance Name: {instance.name}, Instance ID: {instance.id}, Instance Zone: {zone}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_id", help="Your Google Cloud project ID.")
    args = parser.parse_args()
    get_compute_instances(args.project_id)

if __name__ == "__main__":
    main()