resource "azurerm_public_ip" "worker" {
    name = "${terraform.workspace}-worker-pip"
    location = var.resource_group.location
    resource_group_name = var.resource_group.name
    allocation_method = "Dynamic"
    domain_name_label = "${terraform.workspace}-worker-alina"

}
