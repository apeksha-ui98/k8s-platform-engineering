module "ecr" {
  source = "../../modules/ecr"

  repository_name = "k8s-platform-app"
}
output "repository_url" {
  value = module.ecr.repository_url
}
