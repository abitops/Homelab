#!/usr/bin/env python3

import subprocess
import json

HOME_DIR = "/Users/abiskup/HomeLab"

def run(cmd, capture=False):
    if capture:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    subprocess.run(cmd, shell=True, check=True)


#bastion = {
#    "name": "bastion",
#    "cpu": "2",
#    "memory": "4G",
#    "disk" : "20G"
#}

k8s_control = {
    "name": "k8s-control",
    "cpu": "2",
    "memory": "4G",
    "disk": "20G"
}

worker_1 = {
    "name": "worker-1",
    "cpu": "4",
    "memory": "8G",
    "disk": "40G"
}

worker_2 = {
    "name": "worker-2",
    "cpu": "4",
    "memory": "8G",
    "disk": "40G"
}

worker_3 = {
    "name": "worker-3",
    "cpu": "4",
    "memory": "8G",
    "disk": "40G"
}
#ci_server = {
#    "name": "ci-server",
#    "cpu": "4",
#    "memory": "8G",
#    "disk": "40G"
#}

vm_ips = {}

#for vm in bastion, k8s_control, worker_1, worker_2, ci_server:
for vm in k8s_control, worker_1, worker_2, worker_3:
    print(f"[+] Creating vm --> {vm['name']}")
    run(
        f"multipass launch noble -n {vm['name']} -c {vm['cpu']} -m {vm['memory']} -d {vm['disk']}",
        capture = True
    )

#for vm in bastion, k8s_control, worker_1, worker_2, ci_server:
for vm in k8s_control, worker_1, worker_2, worker_3:
    print(f"[+] Adding ssh key --> {vm['name']}")
    run(
        f"multipass exec {vm['name']} -- bash -c 'echo \"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAINdduPKiHNXQTKNMPpu8hJ98x0s/xkxPLiloLrD+w/fJ abiskup@BishopsNexus\" > .ssh/authorized_keys'"
    )

print("[I] VM IPs")
#for vm in bastion, k8s_control, worker_1, worker_2, ci_server:
for vm in k8s_control, worker_1, worker_2, worker_3:
    output = run(
        f"multipass info {vm['name']} --format json",
        capture = True
    )
    vm_output = json.loads(output)
    vm_ips.update({vm['name']: vm_output['info'][f"{vm['name']}"]['ipv4'][0]})
    print(f"{vm['name']:12}: {vm_output['info'][f"{vm['name']}"]['ipv4'][0]}")


print("[+] Creating inventory file")
file_path = f"../inventory/inventory.ini"

with open(file_path, "w") as file:
    cp_header = "[controlplane]"
    work_header = "[workers]"
    file.write(cp_header + "\n")
    file.write(vm_ips["k8s-control"] + "\n")
    file.write(work_header + "\n")
    for vm in worker_1, worker_2, worker_3:
        file.write(vm_ips[vm['name']] + "\n")


print("[+] Setting up environment")
run(
    f'ansible-playbook -i ../inventory/inventory.ini ../yamls/playbook.yaml --key-file ~/.ssh/abitops --ssh-extra-args="-oStrictHostKeyChecking=no"'
)
