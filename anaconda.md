## Conda的Environment管理
### 创建一个新的environment
```bash
conda create --name python34 python=3.4
```

### 激活一个环境
```bash
# windows
activate python34

# linux&mac
source activate python34
```

### 退出一个环境
```bash
# windows
deactivate python34

# linux & mac
source deactivate python34
```

### 删除一个环境
```bash
conda remove --name python34 --all
```

### 查看已安装的python包
```bash
conda list
# 查看指定环境
conda list -n python34
# 删除一个python包
conda remove -n python34 package_nm
```

### 端口转发
```bash
ssh -N -f -L localhost:8888:localhost:8888 gitlab-demo-ci
```
