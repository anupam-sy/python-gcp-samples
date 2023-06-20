from google.cloud import compute_v1

def get_unused_compute_disks(project_id):
    """
    Prints the unused regional/zonal compute disks of a project.
    """
    
    addresses_client = compute_v1.DisksClient()
    for zone, response in addresses_client.aggregated_list(project=project_id):
        if response.disks:
            for disk in response.disks:
                if len(disk.users) == 0:
                    print(f"Disk Name: {disk.name}, Disk Size: {disk.size_gb}, Disk Location: {zone}")

def main(project_id):
    get_unused_compute_disks(project_id)

if __name__ == "__main__":
    project_id = "UPDATE_ME"
    main(project_id)