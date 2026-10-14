# Enterprise Smart Library Management Platform

## 1. Project Overview

The Enterprise Smart Library Management Platform is a Python-based web application developed using Flask. It provides API endpoints for managing library books, users, and borrowing and returning operations.

This project demonstrates the practical implementation of DevOps practices, including Git version control, automated testing, code quality checks, Jenkins CI, Docker containerization, and Kubernetes orchestration.

## 2. Technologies Used

- **Python** — Application programming language
- **Flask** — Web application framework
- **Pytest** — Automated testing
- **Flake8** — Code quality and style checking
- **Git and GitHub** — Version control and source code management
- **Jenkins** — Continuous integration pipeline
- **Docker** — Application containerization
- **Kubernetes** — Container orchestration
- **Minikube** — Local Kubernetes cluster

## 3. Project Structure

```text
library-management-platform/
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── __init__.py
├── database/
│   ├── __init__.py
│   └── db.py
├── tests/
│   ├── test_api_endpoints.py
│   ├── test_book_service.py
│   ├── test_borrow_return.py
│   └── test_user_service.py
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
├── .dockerignore
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
└── run.py
```

## 4. Prerequisites

Install or configure the following tools according to your environment:

- Python 3
- Git
- Docker
- Jenkins
- kubectl
- Minikube

## 5. Run the Application Locally

Open a terminal in the `library-management-platform` directory.

### Step 1: Create a virtual environment

```bash
python -m venv .venv
```

### Step 2: Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux:

```bash
source .venv/bin/activate
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Start the application

```bash
python run.py
```

Use the application routes defined in the Flask code to access its functionality.

## 6. Automated Testing

Run the test suite:

```bash
python -m pytest tests/ -v
```

Generate a JUnit XML test report:

```bash
python -m pytest tests/ --junitxml=pytest-results.xml
```

Check code quality:

```bash
python -m flake8 app database tests run.py
```

## 7. Jenkins Continuous Integration

The `Jenkinsfile` defines the automated CI pipeline.

The pipeline performs these stages:

1. Set up the Python environment.
2. Install project dependencies.
3. Check code quality using Flake8.
4. Execute automated tests using Pytest.
5. Publish test results in Jenkins.
6. Build the Docker image.

The pipeline is configured to run from the project repository. The Jenkins job must use the repository's actual branch and Jenkinsfile path.

## 8. Docker Containerization

Build the Docker image from the project directory:

```bash
docker build -t library-management-platform:1.0 .
```

List available Docker images:

```bash
docker images
```

Run the application container:

```bash
docker run -d --name library-app -p 5000:5000 library-management-platform:1.0
```

Check running containers:

```bash
docker ps
```

Check the health endpoint:

```bash
curl http://localhost:5000/health
```

Stop the container when finished:

```bash
docker stop library-app
```

Remove the stopped container if required:

```bash
docker rm library-app
```

## 9. Kubernetes Orchestration

Ensure that Minikube is running and the Docker image is available to the cluster.

Load the image into Minikube:

```bash
minikube image load library-management-platform:1.0
```

Apply the Kubernetes manifests:

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Check the deployment:

```bash
kubectl get deployments
```

Check the pods:

```bash
kubectl get pods
```

Check the service:

```bash
kubectl get services
```

Inspect deployment details:

```bash
kubectl describe deployment
```

Kubernetes Deployment maintains the desired number of application replicas. If a pod fails or is deleted, Kubernetes can create a replacement pod to restore the desired state.

## 10. Project Workflow

The project is developed in stages:

1. **Foundation** — Application structure and initial configuration.
2. **Core application** — Models, services, and API routes.
3. **Automated tests** — Unit and API test cases.
4. **Jenkins CI** — Automated code quality checks and testing.
5. **Dockerization** — Container image configuration.
6. **Kubernetes orchestration** — Deployment and Service manifests.

Each stage is recorded through Git commits to maintain a clear development history.

## 11. Conclusion

This project demonstrates how a Python web application can be developed and managed using common DevOps tools. It combines source control, testing, continuous integration, containerization, and orchestration into a single practical workflow.

The project provides hands-on experience with application deployment, automated verification, and Kubernetes workload management.