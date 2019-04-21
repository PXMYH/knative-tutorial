# Installation

## Local Development

```bash
# install hyperkit driver
# https://github.com/kubernetes/minikube/blob/master/docs/drivers.md#hyperkit-driver
brew install hyperkit
curl -LO https://storage.googleapis.com/minikube/releases/latest/docker-machine-driver-hyperkit \
&& sudo install -o root -g wheel -m 4755 docker-machine-driver-hyperkit /usr/local/bin/

# install minikube
brew cask install minikube

# start minikube
minikube start --memory=8192 --cpus=2 \
  --vm-driver=hyperkit \
  --disk-size=20g \
  --extra-config=apiserver.enable-admission-plugins="LimitRanger,NamespaceExists,NamespaceLifecycle,ResourceQuota,ServiceAccount,DefaultStorageClass,MutatingAdmissionWebhook"
```

## Hosted Solutions

> Amazon Web Services

> Google Cloud Platform

> IBM Cloud

## Install Gloo

```bash
brew install glooctl
glooctl --version
glooctl install knative
kubectl apply --filename https://github.com/knative/build/releases/download/v0.5.0/build.yaml
```
