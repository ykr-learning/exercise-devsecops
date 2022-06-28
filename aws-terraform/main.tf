#Create and bootstrap webserver
resource "aws_instance" "webserver" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t3.medium"
  key_name                    = aws_key_pair.webserver-key.key_name
  associate_public_ip_address = true
  vpc_security_group_ids      = [aws_security_group.sg.id]
  subnet_id                   = aws_subnet.subnet.id
  user_data                   = file("install_vm.sh")

  provisioner "file" {
    source      = "install_vm.sh"
    destination = "/tmp/install_vm.sh"
  }

  provisioner "file" {
    source      = "docker-compose.yml"
    destination = "/tmp/docker-compose.yml"
  }

  provisioner "remote-exec" {
    # https://www.terraform.io/language/resources/provisioners/remote-exec
    inline = [
      "set -o errexit",
      "chmod +x /tmp/install_vm.sh",
      "/tmp/install_vm.sh args",
    ]
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("./webserver-devsecops-key.pem")
    host        = self.public_ip
    # timeout     = "1m"
  }

  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = 15
  }

  tags = {
    Name = "${var.default_tag}"
  }
}
