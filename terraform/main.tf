provider "azurerm" {
  version = "=1.30.1"
}
module "nginx" {
  source = "./modules/nginx"
  admin_user = "jenkins"
  resource_group = azurerm_resource_group.default
  virtual_network = azurerm_virtual_network.default
}
module "jenkins" {
  source = "./modules/jenkins"
  admin_user = "jenkins"
  resource_group = azurerm_resource_group.default
  virtual_network = azurerm_virtual_network.default
  subnet_cidr = "10.0.1.0/24"
}
module "master" {
  source = "./modules/master"
  admin_user = "jenkins"
  resource_group = azurerm_resource_group.default
  virtual_network = azurerm_virtual_network.default
}
module "worker" {
  source = "./modules/worker"
  admin_user = "jenkins"
  resource_group = azurerm_resource_group.default
  virtual_network = azurerm_virtual_network.default
}
