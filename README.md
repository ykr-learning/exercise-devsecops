# exercise-devsecops

#prepare
cd ./aws-terraform
ssh-keygen -f ./webserver-devsecops-key.pem -m PEM
mv webserver-devsecops-key.pem.pub webserver-devsecops-key.pub
chmod 700 webserver-devsecops-key.pem

#install with terraform

terraform fmt & terraform validate & terraform apply

ssh -i webserver-devsecops-key.pem  ubuntu@44.192.112.242

terraform destroy

### Portainer
curl http://44.192.112.242:9443/

admin
adminadmin


### Jenkins
curl http://44.192.112.242:8080/

sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

admin_user
admin_pwd
admin_user
mail-fake@gmail.com

http://44.192.112.242:8080/

install plugins:
github
Docker Pipeline Version 1.28 

new item: github-pipeline
type: Pipeline Multibranches

Add branch source:
https://github.com/ykr-learning/exercise-devsecops.git

Manage Jenkins > Manage credentials > globals > Add credential
type: username & password
id: dockerhub_id


check disk space:
df -h

git push all

