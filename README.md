
Bootstrapping a node:

```
dnf install install https://repo.saltstack.com/py3/redhat/salt-py3-repo-3002.el8.noarch.rpm
dnf install salt-minion
echo "master: control" >/etc/salt/minion.d/minion.conf
salt-call state.highstate
```


