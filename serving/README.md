# Serving

Use Knative Serving to deploy code and deploy to Kubernetes

```bash
# install build template
kubens default
kubectl apply --filename https://raw.githubusercontent.com/knative/build-templates/master/kaniko/kaniko.yaml
kubectl apply --filename docker-secret.yaml
kubectl apply --filename service-account.yaml

# need to grant `cluster admin` permission to the user
kubectl create clusterrolebinding cluster-admin-binding   --clusterrole=cluster-admin   --user=system:serviceaccount:knative-serving:controller

kubectl apply --filename service.yaml
```
