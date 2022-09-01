## VScode利用者と非利用者が共存できるやつ

vscode利用者は `devcontainer` を利用でき、
vscode使ってない人も普通にdocker-composeができるsandbox環境。

### in VScode
---

- requirement: vscode / docker / XQuartz

```
#clone code & cd
git clone this-repository

# open in the VScode
code this-repository

# in VScode

- open `Command palette` / cmd + shift + p
- search and execute  `Reopen in Container` 

# test command
bin/exec src/test.py
=> This is test message!!
```


### in Other
---
- requirement: docker / XQuartz

```
#clone code & cd
git clone this-repository

# build container
docker-compose build

# up container
docker-compose up

# test command
bin/exec src/test.py
=> This is test message!!
```