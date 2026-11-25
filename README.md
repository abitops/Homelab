#### VM Layout

|VM|Purpose|
|---|---|
|bastion|SSH jump host|
|k8s-control|Control plane|
|worker-1|Kubernetes|
|worker-2|Kubernetes|
|ci-server|CI/CD|

#### Applications

Jenkins or GitLab
Harbor
Argo CD
SonarQube
Keycloak

#### Demo workflow

Push code.
Jenkins builds image.
Harbor stores image.
ArgoCD deploys to Kubernetes.
Grafana monitors app.
