\# Unit 3 – Enterprise Smart Library Management Platform



\## 1. Project Overview



The \*\*Enterprise Smart Library Management Platform\*\* is a DevOps mini-project that demonstrates how to develop, test, build, containerize, and deploy a Python-based library management application using modern DevOps tools.



The project implements an automated CI/CD pipeline using Jenkins, packages the application with Docker, and deploys it on Kubernetes with three replicas to demonstrate scalability, health monitoring, and self-healing.



\## 2. Objectives



\- Set up and manage an AWS EC2 Linux instance.

\- Connect to the remote server using MobaXterm and SSH.

\- Develop and test a Python Flask application.

\- Perform code-quality checks and automated testing.

\- Configure a Jenkins CI/CD pipeline.

\- Build and run a Docker container.

\- Deploy the application on Kubernetes using Minikube.

\- Configure health checks and verify Kubernetes self-healing.

\- Document the implementation with screenshots and command explanations.



\## 3. Technologies Used



| Technology | Purpose |

|---|---|

| AWS EC2 | Cloud-based Linux server |

| Ubuntu Linux | Server operating system |

| MobaXterm | Remote SSH access and terminal |

| Python | Application development |

| Flask | Web application and REST API |

| pytest | Automated testing |

| flake8 | Python code-quality checks |

| Jenkins | CI/CD automation |

| Git and GitHub | Source-code management and version control |

| Docker | Container image creation and execution |

| Kubernetes | Container orchestration |

| Minikube | Local Kubernetes cluster |

| kubectl | Kubernetes resource management |



\## 4. Project Structure



```text

unit-3/

├── README.md

├── .gitkeep

├── DevOps\_Report\_with\_Screenshots.docx

└── library-management-platform/

&#x20;   ├── app/

&#x20;   ├── database/

&#x20;   ├── tests/

&#x20;   ├── k8s/

&#x20;   ├── Dockerfile

&#x20;   ├── Jenkinsfile

&#x20;   ├── requirements.txt

&#x20;   └── run.py

```



\*Note: The Word report and project files should be present at the paths shown above for this structure to match the repository.\*



\## 5. Application Features



\- Python Flask application with a health-check endpoint.

\- In-memory data storage for the application.

\- Automated unit tests using pytest.

\- Code-quality validation using flake8.

\- Docker image built through the Jenkins pipeline.

\- Kubernetes deployment configured with three application replicas.

\- Readiness and liveness probes for health monitoring.

\- NodePort service for application access.

\- Automatic replacement of a deleted pod by Kubernetes.



\## 6. DevOps Workflow



The project follows this workflow:



1\. \*\*Source code:\*\* Store the application and configuration files in GitHub.

2\. \*\*Cloud environment:\*\* Use an Ubuntu EC2 instance accessed through MobaXterm.

3\. \*\*Code quality:\*\* Run flake8 to identify Python code-quality issues.

4\. \*\*Automated testing:\*\* Execute pytest and publish the JUnit test report in Jenkins.

5\. \*\*Continuous integration:\*\* Use Jenkins to automate the validation and Docker image build.

6\. \*\*Containerization:\*\* Package the application as `library-management-platform:1.0`.

7\. \*\*Orchestration:\*\* Load the image into Minikube and deploy three replicas.

8\. \*\*Health verification:\*\* Check the application health endpoint and Kubernetes pod status.

9\. \*\*Self-healing:\*\* Delete a running pod and verify that Kubernetes creates a replacement.



\## 7. Jenkins CI/CD Pipeline



The Jenkins job used for this project is named \*\*Library-Management-CI\*\*.



The pipeline contains the following stages:



\- Setup Python environment

\- Code Quality

\- Run Tests

\- Build Docker Image



The pipeline executes code-quality checks and automated tests before building the Docker image. Test results are published in Jenkins so that the build outcome can be reviewed.



\*\*Expected result:\*\* A successful Jenkins build with passing tests and a completed Docker image build.



\## 8. Docker Implementation



The application is packaged into a Docker image:



```bash

sudo docker build -t library-management-platform:1.0 .

```



Run the application container:



```bash

sudo docker run -d \\

&#x20; --name library-app \\

&#x20; -p 5000:5000 \\

&#x20; library-management-platform:1.0

```



Verify the running container:



```bash

sudo docker ps

sudo docker images

```



Check the application health endpoint:



```bash

curl http://localhost:5000/health

```



Expected response:



```json

{"status":"healthy"}

```



\## 9. Kubernetes Deployment



The application is deployed on Minikube using a Kubernetes Deployment and NodePort Service.



The deployment is configured for three replicas, with readiness and liveness probes to monitor application health.



Useful verification commands:



```bash

kubectl get pods

kubectl get deployments

kubectl get services

```



The desired deployment status is \*\*3/3 available replicas\*\*, with all three application pods in the Running and Ready state.



\### Access the Application



Forward the Kubernetes Service to a local port:



```bash

kubectl port-forward svc/library-app-service 8081:5000

```



In another terminal, test the application:



```bash

curl http://localhost:8081/health

```



Expected response:



```json

{"status":"healthy"}

```



\## 10. Kubernetes Self-Healing Test



To demonstrate self-healing, a running application pod was deleted intentionally.



```bash

kubectl get pods

kubectl delete pod <pod-name>

kubectl get pods -w

```



Replace `<pod-name>` with the name of an existing application pod.



\*\*Observed result:\*\* Kubernetes created a replacement pod, which subsequently reached the Running and Ready state. This demonstrated that the Deployment controller maintained the desired replica count.



\## 11. Testing and Validation



The project was validated through the following checks:



\- \*\*Automated tests:\*\* 15 pytest tests passed.

\- \*\*Code quality:\*\* flake8 checks completed successfully.

\- \*\*Jenkins:\*\* CI/CD pipeline completed successfully.

\- \*\*Docker:\*\* Application image built and container ran successfully.

\- \*\*Health endpoint:\*\* Returned `{"status":"healthy"}`.

\- \*\*Kubernetes:\*\* Three application replicas were running and ready.

\- \*\*Self-healing:\*\* A deleted pod was automatically replaced.



\## 12. Learning Outcomes



Through this project, the following practical skills were developed:



\- Connecting to and managing a Linux cloud server.

\- Using terminal commands to install and verify software.

\- Understanding Git branches, commits, and remote repositories.

\- Automating software validation through Jenkins.

\- Running Python tests and code-quality checks.

\- Building and managing Docker containers.

\- Deploying applications with Kubernetes.

\- Configuring service access and health probes.

\- Observing Kubernetes self-healing behavior.

\- Preparing technical documentation with command explanations and screenshots.



\## 13. Project Evidence



The detailed implementation report is available here:



\*\*\[DevOps AWS Implementation Report with Screenshots](DevOps\_Report\_with\_Screenshots.docx)\*\*



The report documents the AWS instance setup, terminal commands, Jenkins pipeline, Docker implementation, Kubernetes deployment, and verification results.



\## 14. Conclusion



The Enterprise Smart Library Management Platform demonstrates an end-to-end DevOps workflow, from source-code management and automated testing to containerization and Kubernetes orchestration.



The successful CI/CD pipeline, healthy application endpoint, three ready Kubernetes replicas, and verified pod replacement demonstrate practical understanding of essential DevOps concepts.



\---



\*\*Project:\*\* Unit 3 – Enterprise Smart Library Management Platform  

\*\*Repository:\*\* \[DevOps-mini-projects](https://github.com/surajsase08/DevOps-mini-projects)  

\*\*Branch used during implementation:\*\* `staged/foundation`

