terraform {
  required_providers {
    local = {
      source = "hashicorp/local"
    }
  }
}

provider "local" {}

resource "local_file" "devops_test" {
  content  = "CI/CD Terraform is working!"
  filename = "devops.txt"
}
