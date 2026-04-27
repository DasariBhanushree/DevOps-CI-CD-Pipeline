# 🚀 DevOps CI/CD Pipeline using Terraform & GitHub Actions

## 📌 Project Overview

This project demonstrates a complete DevOps workflow by automating infrastructure provisioning and application deployment on AWS.

It simulates a real-world scenario where code changes trigger a CI/CD pipeline that provisions infrastructure and deploys an application automatically.

---

## 🏗️ Architecture

GitHub → GitHub Actions (CI/CD) → Terraform → AWS → Application Deployment

---

## 🛠️ Tech Stack

* AWS (EC2, S3, VPC, IAM)
* Terraform (Infrastructure as Code)
* GitHub Actions (CI/CD)
* Docker 
* Linux

---

## ⚙️ How It Works

1. Developer pushes code to GitHub
2. GitHub Actions pipeline is triggered
3. Terraform initializes and provisions infrastructure
4. Application is deployed on AWS
5. Pipeline ensures continuous integration and delivery

---

## 📂 Project Structure

* `/terraform` → Infrastructure code
* `/app` → Application code
* `.github/workflows` → CI/CD pipeline configuration

---

## 🚀 How to Run

1. Clone the repository
2. Configure AWS credentials
3. Run Terraform:

   ```
   terraform init
   terraform apply
   ```
4. Trigger GitHub Actions workflow

---

## 🎯 Key Learnings

* Automated infrastructure provisioning using Terraform
* CI/CD pipeline setup using GitHub Actions
* Understanding real-world DevOps workflow
* Hands-on experience with AWS services

---

## 📌 Future Improvements

* Add Kubernetes deployment (EKS)
* Implement monitoring (CloudWatch/Prometheus)
* Improve security using IAM best practices

---


