resource "azurerm_virtual_machine" "worker" {
  name = "${terraform.workspace}-worker-vm"
  location = var.resource_group.location
  resource_group_name = var.resource_group.name
  network_interface_ids = [azurerm_network_interface.worker.id]
  vm_size = "Standard_DS1_v2"
  storage_image_reference {
    publisher = "credativ"
    offer = "Debian"
    sku = "9"
    version = "latest"
  }
  storage_os_disk {
    name = "${terraform.workspace}-worker-vm"
    caching = "ReadWrite"
    create_option = "FromImage"
    managed_disk_type = "Standard_LRS"
  }
  os_profile {
    computer_name  = "${terraform.workspace}-worker-vm"
    admin_username = var.admin_user
  }
  os_profile_linux_config {
    disable_password_authentication = true
    ssh_keys {
	  path = "/home/${var.admin_user}/.ssh/authorized_keys"
	  key_data = file(pathexpand("~/.ssh/id_rsa.pub"))
	}
  }
  tags = {
    environment = terraform.workspace
  }
  connection {
		type = "ssh"
		user = var.admin_user
		private_key = file(pathexpand("~/.ssh/id_rsa"))
		host = azurerm_public_ip.worker.DevOpsRepo
  }
}
