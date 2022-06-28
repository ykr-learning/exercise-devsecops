output "public_dns" {
  description = "The public DNS name assigned to the instance. For EC2-VPC, this is only available if you've enabled DNS hostnames for your VPC"
  value       = aws_instance.webserver.public_dns
}

output "Webserver-Public-IP" {
  value = aws_instance.webserver.public_ip
}

output "ssh-command" {
  value = "ssh -i webserver-devsecops-key.pem  ubuntu@${aws_instance.webserver.public_ip}"
}