from google.cloud import resourcemanager_v3

def list_containers(parent):
    all_project_ids = []
    all_folder_ids = []
    folder_ids = []

    prj_client = resourcemanager_v3.ProjectsClient()
    prj_result = prj_client.list_projects(parent=parent)
    if prj_result:
        for prj_response in prj_result:
            all_project_ids.append(prj_response.project_id)
    
    fldr_client = resourcemanager_v3.FoldersClient()
    fldr_result = fldr_client.list_folders(parent=parent)
    if fldr_result:
        for fldr_response in fldr_result:
            all_folder_ids.append(fldr_response.name)
            folder_ids.append(fldr_response.name)

    while all_folder_ids:
        folder_id = all_folder_ids.pop()
        subfldr_result = fldr_client.list_folders(parent=folder_id)
        if subfldr_result:
            for subfldr_response in subfldr_result:
                all_folder_ids.append(subfldr_response.name)
                folder_ids.append(subfldr_response.name)

        project_under_folder_result = prj_client.list_projects(parent=folder_id)
        if project_under_folder_result:
            for prj_under_fldr_response in project_under_folder_result:
                all_project_ids.append(prj_under_fldr_response.project_id)
    return(f"Project IDs:{all_project_ids}, Folder IDs:{folder_ids}")

def main():
    parent="organizations/UPDATE_ME"
    print(list_containers(parent))

if __name__ == "__main__":
    main()