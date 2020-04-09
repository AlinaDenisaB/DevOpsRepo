resource "azurerm_network_interface" "worker" {
  name = "${terraform.workspace}-master-nic"
  location  = var.resource_group.location
  resource_group_name = var.resource_group.name
  network_security_group_id = azurerm_network_security_group.master.id
  ip_configuration {
    name = "${terraform.workspace}-worker"
    subnet_id = azurerm_subnet.default.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id = azurerm_public_ip.worker.id
  }

}
