# exercise-devsecops

#prepare
cd ./aws-terraform
ssh-keygen -f ./webserver-devsecops-key.pem -m PEM
mv webserver-devsecops-key.pem.pub webserver-devsecops-key.pub
chmod 700 webserver-devsecops-key.pem

#install with terraform

terraform fmt & terraform validate & terraform apply

ssh -i webserver-devsecops-key.pem  ubuntu@{ip}

terraform destroy

### Portainer
curl https://{ip}:9443/

admin
adminadmin


### Jenkins
curl http://{ip}:8080/

sudo docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword

admin_user
admin_pwd
admin_user
mail-fake@gmail.com

install plugins:
* GitHub - Version 1.34.4 (to connect to github)
* Docker Pipeline - Version 1.28 (to build in docker containers, and build images)
* Warnings Next Generation - Version 9.13.0 (to publish hadolint reports)
* Official OWASP ZAP - Version 1.1.0

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

