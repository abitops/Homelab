# Home Lab Checklist

## Phase 1: Build the Core Stack Manually

- [ ] Install Linux on host machine (or VMs)
- [ ] Create 2–3 VMs using KVM/VirtualBox or use K3s
- [ ] Install Docker and container runtime on each VM
- [ ] Deploy Kubernetes cluster manually using kubeadm or k3s
- [ ] Deploy a sample containerized app (e.g., Ghost blog)

## Phase 2: Add Config Management

- [ ] Write Ansible playbooks to install system packages (Docker, kubeadm)
- [ ] Configure firewalls, users, and SSH access via Ansible
- [ ] Automate Kubernetes setup using Ansible
- [ ] Optionally try Puppet to manage system state and packages

## Phase 3: Infrastructure as Code with Terraform

- [ ] Use Terraform to provision local VMs (libvirt/VirtualBox providers)
- [ ] Define network and storage resources
- [ ] Use Terraform provisioners to call Ansible for inside-VM configuration

## Phase 4: Monitoring + Observability Stack

- [ ] Deploy Prometheus (with node_exporter and kubelet scraping)
- [ ] Install Grafana and configure dashboards
- [ ] Set up Alertmanager for alerting
- [ ] Optionally deploy Zabbix for comparison

## Phase 5: Simulated Real Workloads

- [ ] Deploy a load generator like Locust, k6, or wrk
- [ ] Simulate CPU, memory, and I/O pressure
- [ ] Observe resource usage in Grafana
- [ ] Test autoscaling and resource limits in Kubernetes

## Optional Add-Ons

- [ ] Set up GitOps with ArgoCD or Flux
- [ ] Install Jenkins or run GitHub Actions inside the cluster
- [ ] Secure services with TLS using cert-manager
- [ ] Create and enforce Kubernetes network policies
