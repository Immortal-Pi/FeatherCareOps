
# FeatherCareOps: Poultry Chick Disease Classification

This repository demonstrates the implementation of MLOps principles in the development, deployment, and monitoring of a machine learning application. The project integrates automation, continuous integration/continuous deployment (CI/CD), and scalability to ensure efficient and reliable ML workflows.

##  Features:
- **Dataset**: 
    - dataset like :-  
- **Model**: ElasticNet
- **MLOps Integration**:
    - Config-driven pipeline setup with YAML.
    - Data versioning and workflow tracking using DVC.
    - Modular project structure with reusable components.
- **Deployment**: Dockerized Flask app for serving the model and deployed on AWS.
- **Utilities**: Common functions for reading YAML, saving JSON, and handling data.
- **Project Workflow**:
    - Data ingestion and preprocessing.
    - Model training and evaluation.
    - Deployment with Docker and AWS.

# How to run?

### STEPS:
Clone the repository
```bash
https://github.com/Immortal-Pi/ML-project-with-MLFlow
```

### STEP 01- Create a conda environment after opening the repository
```bash 
conda create -n mlopscnn python=3.9 -y
```
```bash 
conda activate mlopsML
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

# Finally run the following command
```bash
python app.py
```

Now,

open up you local host and port

# MLflow & pipeline tracking

dagshub repo : wait

```bash
import dagshub
dagshub.init(repo_owner='your-github-username', repo_name='your-repository-name', mlflow=True)
```


### mlflow experiments 
```bash 
- mlflow ui 
``` 

## AWS CICD Deployment with Github Actions

    1. Login to AWS console 
    2. Create IAM use for deployment 

```bash
# with specific access
    1. ECR access
    2. ECR Elastic Container 

# Description: About the deployment 
    1. Build docker image of the source code 
    2. Push the docker imange to ECR
    3. Launch your EC2 
    4. Pull your image from ECR in EC2 
    5. Launch your docker image in EC2 

# Policy 
    1. AmazonEC2ContainerRegistryFullAccess
    2. AmazonEC2FullAccess
```

## 3. Create ECR repo to store/save docker image 
    - save the URI: 'use the URI from AWS console' 

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and install docker in EC2 Machine 
```bash
# installation of docker on the virtual machine
    sudo apt-get update -y
    sudo apt-get upgrade
    #required
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker ubuntu
    newgrp docker
```

## Demo 



## Tech Stack 

- **Programming Language**: Python
- **Deep Learning Framework**: Keras with TensorFlow backend
- **MLOps Tools**:
    - Docker for containerization
    - Github actions CICD pipelines
- **Web Framework**: Flask for model deployment
- **Cloud Platform**: AWS for hosting the model
- **Version Control**: Git and GitHub
- **Data Utilities**: YAML, JSON handling, and custom preprocessing functions

## Conclusion
This project highlights the integration of MLOps principles in managing the entire machine learning lifecycle. While the focus was on building a wine quality prediction model using regression techniques, the core objective was to emphasize the importance of project structure, automation of workflows, and the use of tools like Docker for deployment. Additionally, a CI/CD pipeline was implemented to automate the testing, building, and deployment processes, ensuring consistent and reliable updates to the application. This project serves as a foundation for understanding how to design scalable, maintainable, and efficient ML pipelines, ensuring reproducibility and streamlined collaboration in real-world scenarios.
