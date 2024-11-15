# SaaS-Based Utility Booking Application

This repository contains the code for a SaaS-based utility booking application with a microservices architecture. The application is designed to handle user login, travel booking, stay booking, and local conveyance booking. The microservices are deployed on Google Kubernetes Engine (GKE) with Docker.

## Table of Contents
- [Project Structure](#project-structure)
- [Setup and Deployment](#setup-and-deployment)
- [Recreating the Kubernetes Cluster](#recreating-the-kubernetes-cluster)
- [Running Services](#running-services)
- [Scaling and Performance Testing with JMeter](#scaling-and-performance-testing-with-jmeter)
- [Contact](#contact)

## Project Structure
booking-app/
├── UserLogin/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── Travel/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── Stay/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
├── LocalConveyance/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
└── k8s-manifests/
    ├── userlogin-deployment.yaml
    ├── travel-deployment.yaml
    ├── stay-deployment.yaml
    ├── localconveyance-deployment.yaml
    ├── services.yaml



## Setup and Deployment

### Prerequisites
- Docker
- Google Cloud SDK
- kubectl
- Apache JMeter

### Building and Pushing Docker Images
Navigate to each service directory and build the Docker images:

```bash
cd UserLogin
docker build -t gcr.io/sde-major-g39-booking-app/userlogin:latest .
docker push gcr.io/sde-major-g39-booking-app/userlogin:latest

cd ../Travel
docker build -t gcr.io/sde-major-g39-booking-app/travel:latest .
docker push gcr.io/sde-major-g39-booking-app/travel:latest

cd ../Stay
docker build -t gcr.io/sde-major-g39-booking-app/stay:latest .
docker push gcr.io/sde-major-g39-booking-app/stay:latest

cd ../Localconveyance
docker build -t gcr.io/sde-major-g39-booking-app/localconveyance:latest .
docker push gcr.io/sde-major-g39-booking-app/localconveyance:latest

Applying Kubernetes Manifests
Deploy the services to GKE:

kubectl apply -f k8s-manifests/userlogin-deployment.yaml
kubectl apply -f k8s-manifests/userlogin-service.yaml

kubectl apply -f k8s-manifests/travel-deployment.yaml
kubectl apply -f k8s-manifests/travel-service.yaml

kubectl apply -f k8s-manifests/stay-deployment.yaml
kubectl apply -f k8s-manifests/stay-service.yaml

kubectl apply -f k8s-manifests/localconveyance-deployment.yaml
kubectl apply -f k8s-manifests/localconveyance-service.yaml


Running Services
Access Services via curl

curl http://35.239.67.194/login
curl -v -X POST http://35.239.67.194/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "password"}'
curl -v -X POST http://35.239.67.194/login -H "Content-Type: application/json" -d '{"username": "admina", "password": "password"}'

curl http://35.226.229.49/travel
curl -X POST http://35.226.229.49/travel -H "Content-Type: application/json" -d '{"destination": "New York", "travel_type": "Flight"}'


curl http://35.224.120.4/stay
curl -X POST http://35.224.120.4/stay -H "Content-Type: application/json" -d '{"stay_options": "Hotel A", "check_in": "2024-12-01", "check_out": "2024-12-05"}'

curl http://34.29.168.239/localconveyance
curl -X POST http://34.29.168.239/localconveyance -H "Content-Type: application/json" -d '{"conveyance_type": "Taxi", "destination": "Hotel A"}'

Scaling and Performance Testing with JMeter
Install Apache JMeter
Download and install JMeter from the official website.

Create JMeter Test Plan
Create a Thread Group: Add a Thread Group to the Test Plan and configure the number of threads, ramp-up period, and loop count.
Add HTTP Request Defaults: Set the Server Name or IP to the external IP of your service.
Add HTTP Requests: Configure GET and POST requests for each service.
Add Listener: Add a Listener to view results, such as "View Results in Table".
Running JMeter Test Plan
Save the test plan.
Click the green start button to run the test.
Monitor the results in the listener.
Example: Setting Up HPA for UserLogin Service
Create an HPA configuration file (userlogin-hpa.yaml):
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: userlogin-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: userlogin
  minReplicas: 1
  maxReplicas: 10
  targetCPUUtilizationPercentage: 50

Apply the HPA configuration:
kubectl apply -f userlogin-hpa.yaml

Monitor scaling with:
kubectl get hpa
kubectl get pods

