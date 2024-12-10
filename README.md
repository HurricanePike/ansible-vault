# _Ansible-Vault Tool_

Tool created for my hard skills upgrading and for my work tasks. You can use it for yourself(But idk why lmao)

## Installation
#### From repository

```sh
git clone git@github.com:HurricanePike/ansible-vault.git
cd ansible-vault
docker build -t ansible-vault-tool .
docker run -p 8080:8080 ansible-vault-tool
```

#### From docker registry

```sh
docker pull neptulonstep/ansible-vault-tool:latest
docker run -p 8080:8080 neptulonstep/ansible-vault-tool
```
