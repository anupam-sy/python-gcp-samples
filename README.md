# python-gcp-samples
This repository contains python samples intended to use in day to day operational activities on google cloud platform.
Usecases for which the python scripts are written can be found [here](./usecases.md).

## Prerequisites
Below prerequisites must be fulfilled for the successful execution of code.

### Software Requirement
Resources in this repository are meant for use with Python 3.x (check the version using `python3 --version`) and pip3 (check the version using `pip3 --version`). If you don't have the compatible version, download it from official python repository.

- [python3](https://www.python.org/downloads/) >= 3.9.2
- [pip3](https://pypi.org/project/pip/) >= 20.3.4

### Bootstrap Virtual Environment
[venv](https://docs.python.org/3/library/venv.html) is a tool that creates isolated Python environments. These isolated environments can have separate versions of Python packages, which allows you to isolate one project's dependencies from the dependencies of other projects.

**Linux**
```
    cd your-project
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt

  * If you want to stop using the virtual environment and go back to your global Python, you can deactivate it:
    deactivate
```

**Note:** Follow the [google article](https://cloud.google.com/python/docs/setup) to setup your Python development environment.

## Quick Start
If you want to quickly run and test Python samples without installing python, the recommended approach is to use Cloud Shell.

Cloud Shell is a Compute Engine virtual machine. The service credentials associated with this virtual machine are automatic, so there is no need to set up or download a service account key.

Cloud shell terminal is preloaded with softwares and utilities such as Python, gcloud command-line tool, kubectl, and more. letting you get started with less setup.
- **Step-01:** Activate Cloud Shell at the top of the Google Cloud Console.
- **Step-02:** Clone this repository: `git clone https://github.com/anupam-sy/python-gcp-samples.git`
- **Step-03:** Setup the python virtual environment using [Bootstrap Virtual Environment](#bootstrap-virtual-environment).

### Authentication and Authorization
This client library used in the python script supports authentication via Google Application Default Credentials, or by providing a JSON key file for a Service Account. Google Application Default Credentials (ADC) is the recommended way to authorize and authenticate clients.

## Accessing Cloud APIs
You can access Cloud APIs using client libraries available for many popular programming languages While you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

1. Cloud Client Libraries are the recommended option for accessing Cloud APIs programmatically, where available. Cloud Client Libraries use the latest client library model. 
[NEW - Recommended Way] https://github.com/googleapis/google-cloud-python

2. A few Google Cloud APIs don't have Cloud Client Libraries available in all languages. If you want to use one of these APIs and there is no Cloud Client Library for your preferred language, you can still use the previous style of client library, called Google API Client Libraries. 
[OLD - Not Recommended] https://github.com/googleapis/google-api-python-client

**Note:** It is recommended to use Cloud Client Libraries for Python, where possible, for new code development due to the following reasons:

With Cloud Client Libraries for Python:
- There is a separate client library for each API, so you can choose which client libraries to download. Whereas, google-api-python-client is a single client library for all APIs. As a result, the total package size for google-api-python-client exceeds 50MB.
- There are stricter controls for breaking changes to the underlying APIs as each client library is focused on a specific API.
- There are more features in these Cloud Client Libraries as each library is focused on a specific API, and in some cases, the libraries are owned by team who specialized in that API.

## References
- https://cloud.google.com/python/docs/setup
- https://cloud.google.com/apis/docs/overview
- https://cloud.google.com/apis/docs/client-libraries-explained
- https://cloud.google.com/apis/docs/cloud-client-libraries
- https://cloud.google.com/python/docs/reference
- [OLD] https://developers.google.com/api-client-library/
- https://cloud.google.com/docs/samples
- https://cloud.google.com/compute/docs/samples
- https://github.com/googleapis/google-cloud-python
- https://github.com/googleapis/python-compute
- https://github.com/GoogleCloudPlatform/python-docs-samples

## License
This repository is under MIT License.

## Providing feedback
Open an issue in this GitHub repository.