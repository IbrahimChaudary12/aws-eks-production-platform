# AWS EKS Production Platform

A production-style Kubernetes platform project designed to demonstrate DevOps, Kubernetes, GitOps, CI/CD, observability, security, and Infrastructure as Code practices.

The live lab currently runs locally on **RHEL 9 using Podman and kind** at zero cloud cost. AWS EKS infrastructure will later be designed using Terraform without deploying paid AWS resources.

## Architecture

```text
Client
  |
  v
localhost:8080
  |
  v
Traefik Ingress
  |
  v
Kubernetes Service
  |
  +------------------+------------------+
  |                  |                  |
  v                  v                  v
App Pod 1         App Pod 2         App Pod 3
  |
  v
Python / Flask API
```

The Kubernetes cluster consists of:

```text
RHEL 9 VM
|
+-- Podman
    |
    +-- kind Kubernetes Cluster
        |
        +-- Control Plane
        +-- Worker Node 1
        +-- Worker Node 2
```

## Current Features

* Three-node Kubernetes cluster using kind
* Podman container runtime
* Containerized Python Flask application
* Gunicorn application server
* Three application replicas
* Kubernetes Namespace isolation
* Kubernetes Deployment
* Kubernetes ClusterIP Service
* Traefik Ingress Controller
* External application access through port 8080
* Kubernetes load balancing across replicas
* Liveness probes
* Readiness probes
* CPU resource requests and limits
* Memory resource requests and limits
* `/health` endpoint
* `/ready` endpoint
* `/metrics` endpoint
* Prometheus-compatible application metrics
* Non-root application container

## Application Endpoints

| Endpoint   | Purpose                    |
| ---------- | -------------------------- |
| `/`        | Application information    |
| `/health`  | Kubernetes liveness check  |
| `/ready`   | Kubernetes readiness check |
| `/metrics` | Prometheus metrics         |

Example response:

```json
{
  "hostname": "devops-platform-app-xxxxxxxxxx-xxxxx",
  "message": "AWS EKS Production Platform",
  "status": "running"
}
```

The hostname changes between requests as Kubernetes distributes traffic across multiple application replicas.

## Repository Structure

```text
aws-eks-production-platform/
|
+-- app/
|   +-- app.py
|   +-- requirements.txt
|   +-- Dockerfile
|
+-- kubernetes/
|   +-- namespace.yaml
|   +-- deployment.yaml
|   +-- service.yaml
|   +-- ingress.yaml
|
+-- kind-config.yaml
+-- traefik-values.yaml
+-- README.md
+-- .gitignore
```

## Technology Stack

* Red Hat Enterprise Linux 9
* Kubernetes
* kind
* Podman
* Python
* Flask
* Gunicorn
* Traefik
* Helm
* kubectl
* Git
* GitHub

## Verified Load Balancing

Traffic entering through Traefik is routed through the Kubernetes Service and distributed across multiple application replicas.

```text
Request
   |
   v
Traefik
   |
   v
Service
   |
   +--------+--------+
   |        |        |
   v        v        v
 Pod 1    Pod 2    Pod 3
```

Repeated requests return different pod hostnames, demonstrating Kubernetes service discovery and load balancing.

## Roadmap

Planned additions:

* [ ] Metrics Server
* [ ] Horizontal Pod Autoscaler
* [ ] Prometheus
* [ ] Grafana dashboards
* [ ] Argo CD GitOps
* [ ] GitHub Actions CI pipeline
* [ ] Trivy container vulnerability scanning
* [ ] Kubernetes NetworkPolicies
* [ ] PodDisruptionBudget
* [ ] Secrets management
* [ ] Terraform AWS infrastructure
* [ ] Amazon EKS architecture
* [ ] Amazon ECR configuration
* [ ] VPC and subnet architecture
* [ ] IAM configuration
* [ ] Production architecture diagram
* [ ] Deployment and recovery documentation

## AWS Architecture Goal

Terraform will eventually define a production-style AWS architecture including:

```text
AWS
|
+-- VPC
|   +-- Public Subnets
|   +-- Private Subnets
|   +-- Route Tables
|
+-- Amazon EKS
|   +-- Managed Node Groups
|
+-- Amazon ECR
|
+-- IAM
|
+-- Load Balancing
|
+-- Monitoring
```

The AWS infrastructure will be written and validated as Infrastructure as Code without provisioning paid cloud resources during development.

## Project Goal

The goal of this project is to demonstrate practical experience across the full DevOps lifecycle:

```text
Code
  |
  v
Container Build
  |
  v
Security Scan
  |
  v
CI Pipeline
  |
  v
GitOps
  |
  v
Kubernetes
  |
  v
Monitoring
  |
  v
Autoscaling
```

This repository is actively being developed as a hands-on production-style DevOps and Kubernetes platform.
