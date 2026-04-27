DevOps CI/CD Pipeline using Terraform & GitHub Actions

Project Overview

I built this project to automate infrastructure setup and application deployment on AWS using Terraform and GitHub Actions.

Instead of doing manual deployments, this pipeline automatically provisions infrastructure and deploys the application whenever code is pushed.

---

## Architecture

GitHub → GitHub Actions → Terraform → AWS → Application

---

## Tools Used

* AWS (EC2, S3, VPC, IAM)
* Terraform
* GitHub Actions
* Linux

---

## How it works

1. Code is pushed to GitHub
2. GitHub Actions workflow is triggered
3. Terraform runs and creates infrastructure on AWS
4. Application is deployed automatically

---

## Project Structure

* terraform/ → Terraform code
* .github/workflows/ → CI/CD pipeline
* app/ → Application code

---

## Steps to run

1. Clone the repository
2. Configure AWS credentials
3. Run:
   terraform init
   terraform apply
4. Push changes to trigger pipeline

---

## What I learned

* How CI/CD pipelines work in real scenarios
* How to provision infrastructure using Terraform
* How to automate deployments instead of manual work
* Understanding end-to-end DevOps workflow

---

## Next improvements

* Add Kubernetes deployment (EKS)
* Add monitoring setup
* Improve security configurations

---

## Author

BhanuShree
