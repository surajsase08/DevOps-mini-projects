<div align="center">

# 📚 Enterprise Smart Library Management Platform

### A DevOps Mini Project | Unit 3

**Build · Test · Containerize · Deploy · Monitor**

A Python Flask application deployed through Jenkins CI/CD, packaged with Docker, and orchestrated using Kubernetes on Minikube.

<img src="https://img.shields.io/badge/Project-Unit%203-2563EB?style=for-the-badge" alt="Unit 3">
<img src="https://img.shields.io/badge/CI%2FCD-Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white" alt="Jenkins">
<img src="https://img.shields.io/badge/Container-Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/Orchestration-Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes">

</div>

---

## 📌 Overview

The **Enterprise Smart Library Management Platform** demonstrates an end-to-end DevOps workflow for a Python Flask application. It combines source-code management, code-quality checks, automated testing, continuous integration, containerization, and Kubernetes deployment.

The application and its supporting tools were configured and tested using an Ubuntu-based AWS EC2 environment accessed through **MobaXterm/SSH**.

## 🎯 Objectives

- Provision and prepare a Linux environment on AWS EC2.
- Manage source code with Git and GitHub.
- Validate Python code with **Flake8** and automated tests with **pytest**.
- Automate validation and Docker image creation through **Jenkins**.
- Package the application as a Docker image.
- Deploy three application replicas on Kubernetes using Minikube.
- Verify application health and demonstrate Kubernetes self-healing.
- Document the implementation with screenshots and command explanations.

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| ☁️ AWS EC2 | Cloud-hosted Linux environment |
| 🐧 Ubuntu | Server operating system |
| 🖥️ MobaXterm / SSH | Remote terminal access |
| 🐍 Python + Flask | Application and health endpoint |
| 🧪 pytest | Automated testing |
| 🔎 Flake8 | Code-quality checks |
| 🔁 Jenkins | CI/CD pipeline |
| 🌿 Git + GitHub | Version control and source hosting |
| 🐳 Docker | Application containerization |
| ☸️ Kubernetes + Minikube | Deployment and orchestration |
| ⌨️ kubectl | Kubernetes resource management |

## 🔄 DevOps Workflow

```text
GitHub Repository
        │
        ▼
 AWS EC2 (Ubuntu)
  MobaXterm / SSH
        │
        ▼
 Jenkins CI/CD Pipeline
 ┌──────────────────────┐
 │ Setup Python         │
 │ Code Quality         │
 │ Automated Tests      │
 │ Build Docker Image   │
 └──────────────────────┘
        │
        ▼
 Docker Image
 library-management-platform:1.0
        │
        ▼
 Kubernetes (Minikube)
 ┌──────────┬──────────┬──────────┐
 │  Pod 1   │  Pod 2   │  Pod 3   │
 └──────────┴──────────┴──────────┘
        │
        ▼
 Service + Health Checks
```

## 📁 Project Structure

```text
unit-3/
├── README.md
├── DevOps_Report_with_Screenshots.docx
└── library-management-platform/
    ├── app/             # Flask application
    ├── database/        # Data/storage components
    ├── tests/           # Automated tests
    ├── k8s/             # Kubernetes manifests
    ├── Dockerfile       # Docker image instructions
    ├── Jenkinsfile      # Jenkins pipeline definition
    ├── requirements.txt # Python dependencies
    └── run.py           # Application entry point
```

> This documents the intended layout; check the repository to confirm the current contents of each directory.

## ⚙️ CI/CD with Jenkins

**Jenkins job:** `Library-Management-CI`

The pipeline automates the main validation and image-build steps:

1. **Setup Python** — prepare the Python environment.
2. **Code Quality** — run Flake8 checks.
3. **Run Tests** — execute pytest and publish test results in Jenkins.
4. **Build Docker Image** — create the application image after validation.

The implementation was verified with a successful Jenkins build and passing tests.

## 🧪 Testing and Code Quality

Run these commands from the `library-management-platform` directory, where dependencies are installed:

```bash
python -m pytest tests/ -v
python -m flake8 app database tests run.py
```

**Recorded result:** 15 tests passed, and the Flake8 check completed successfully.

## 🐳 Docker

Image used in this project:

```text
library-management-platform:1.0
```

Build the image from the directory containing the `Dockerfile`:

```bash
sudo docker build -t library-management-platform:1.0 .
```

Run the container:

```bash
sudo docker run -d \
  --name library-app \
  -p 5000:5000 \
  library-management-platform:1.0
```

Inspect images and running containers:

```bash
sudo docker images
sudo docker ps
```

### Health Check

```bash
curl http://localhost:5000/health
```

Expected response:

```json
{"status":"healthy"}
```

## ☸️ Kubernetes with Minikube

The application was deployed with **three replicas**, readiness/liveness probes, and a NodePort service.

```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

**Verified target state:** `3/3` deployment replicas available, with all three application pods Running and Ready.

### Access the Service

Start port forwarding:

```bash
kubectl port-forward svc/library-app-service 8081:5000
```

In another terminal:

```bash
curl http://localhost:8081/health
```

Expected response:

```json
{"status":"healthy"}
```

### ♻️ Self-Healing Verification

A running pod was intentionally deleted to verify that Kubernetes replaced it:

```bash
kubectl get pods
kubectl delete pod <pod-name>
kubectl get pods -w
```

Replace `<pod-name>` with the actual name of an application pod. The replacement pod was observed progressing to **Running** and **Ready**, demonstrating the Deployment controller's self-healing behavior.

## ✅ Validation Summary

| Validation | Recorded outcome |
|---|---|
| pytest automated tests | ✅ 15 tests passed |
| Flake8 code-quality check | ✅ Passed |
| Jenkins CI/CD build | ✅ Successful |
| Docker image and container | ✅ Built and run |
| Flask health endpoint | ✅ Healthy response |
| Kubernetes replicas | ✅ 3/3 ready |
| Pod self-healing | ✅ Replacement pod became ready |

## 📄 Detailed Implementation Report

For screenshots, terminal commands, setup steps, and implementation evidence, see:

**[📥 DevOps AWS Implementation Report with Screenshots](DevOps_Report_with_Screenshots.docx)**

## 🧠 Learning Outcomes

- Linux server setup and remote administration using SSH.
- Git branching, commits, and pushing changes to GitHub.
- CI/CD concepts and automated validation with Jenkins.
- Python testing and code-quality analysis.
- Docker image creation and container execution.
- Kubernetes Deployments, Services, replicas, and health probes.
- Application health verification and pod self-healing.
- Technical documentation and evidence collection.

## 🏁 Conclusion

This project demonstrates a practical DevOps workflow—from version-controlled source code and automated testing to Docker packaging and Kubernetes orchestration. Successful pipeline execution, passing tests, a healthy application endpoint, three ready replicas, and a verified replacement pod provide evidence of the implemented workflow.

---

<div align="center">

**Unit 3 · DevOps Mini Project**

[Repository Home](https://github.com/surajsase08/DevOps-mini-projects) · [Unit 3 on `staged/foundation`](https://github.com/surajsase08/DevOps-mini-projects/tree/staged/foundation/unit-3)

</div>
