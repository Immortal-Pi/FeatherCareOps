
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
    - Deployment with Docker and AWS/Azure

# How to run?

### STEPS:
Clone the repository
```bash
https://github.com/Immortal-Pi/FeatherCareOps
```

### STEP 01- Create a conda environment after opening the repository
```bash 
conda create -n mlopscnn python=3.10 -y
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

### tensorboard 
```bash
tensorboard --logdir artifacts/prepare_callbacks/tensorboard_log_dir/
```

## AZURE-CICD-Deployment-with-Github-Actions

### Save pass: 
```bash

```

### Run from terminal 
```bash 
docker build -t chickenapp.azurecr.io/chicken:latest.
```
```bash 
docker login chickenapp.azurecr.io
```
```bash 
docker push chickenapp.azurecr.io/chicken:latest
```

###  Deployment Steps:
1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run


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
This project highlights the integration of MLOps principles in managing the entire machine learning lifecycle. While the focus was on building a disease classification prediction model using regression techniques, the core objective was to emphasize the importance of project structure, automation of workflows, and the use of tools like Docker for deployment. Additionally, a CI/CD pipeline was implemented to automate the testing, building, and deployment processes, ensuring consistent and reliable updates to the application. This project serves as a foundation for understanding how to design scalable, maintainable, and efficient ML pipelines, ensuring reproducibility and streamlined collaboration in real-world scenarios.
