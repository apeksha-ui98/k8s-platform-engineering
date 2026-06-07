module "ecr" {
  source = "../../modules/ecr"

  repository_name = "k8s-platform-app"
}
output "repository_url" {
  value = module.ecr.repository_url
}
module "vpc" {
  source = "../../modules/vpc"

  environment = "dev"
}

module "eks" {
  source = "../../modules/eks"

  cluster_name = "platform-eks"

  subnet_ids = module.vpc.public_subnet_ids
}
