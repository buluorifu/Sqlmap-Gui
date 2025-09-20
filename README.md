# ✨ SQLMap GUI 工具使用指南
## 🔺 项目简介

SQLMap GUI 是一个基于 PyQt5 的图形用户界面工具，旨在简化 SQLMap 的使用。通过这个工具，用户可以轻松地配置和执行 SQLMap 的各种功能，而无需直接在命令行中输入复杂的参数。该工具支持读取和保存配置文件，方便用户快速启动测试，并提供了多种实用功能，如命令生成、日志记录、文件管理等。


## ➡️sqlmap下载地址

点击跳转 [sqlmap](https://github.com/sqlmapproject/sqlmap/releases/tag/1.8) 下载地址



## 🚀使用说明
```shell
选择 SQLMap 文件 ：点击此按钮可以选择 SQLMap 的 Python 脚本文件路径。选择后，路径会自动保存到 file_address.yaml 文件中。
启动 SQLMap ：点击此按钮启动 SQLMap 测试。工具会根据当前配置生成命令并执行。
启动 CMD ：点击此按钮在新的命令提示符窗口中启动 SQLMap 测试。
读取 Request 文件 ：点击此按钮选择一个请求文件（.txt），用于指定 HTTP 请求。
读取 URL 列表文件 ：点击此按钮选择一个包含多个 URL 的文件（.txt），用于批量测试。
打开日志文件夹：点击此按钮打开日志文件夹，查看 SQLMap 的输出日志。
清空命令行输出 ：点击此按钮清空当前的命令行输出内容。
更新 SQLMap ：点击此按钮更新 SQLMap 到最新版本。
显示帮助信息 ：点击此按钮显示 SQLMap 的帮助信息。
查看当前命令 ：点击此按钮查看当前配置生成的完整命令。
设置代理 ：勾选此按钮设置代理。
```

### 选择sqlmap.py文件

<img src="/PNG/1.png" alt="image" style="width:700px;height:700px;">

### 启动 SQLMap

<img src="/PNG/2.png" alt="image" style="width:700px;height:700px;">

### 启动 CMD

```shell
因为sqlmap在pyqt5界面内运行会自动交互，如需手动选择，请使用cmd命令执行。
```

<img src="/PNG/3.png" alt="image" style="width:700px;height:700px;">

### 读取 Request 文件

```shell
点击 读取 Request 文件 按钮后，工具会自动生成一个新的请求文件路径。同时，工具会打开一个编辑窗口，允许用户编辑该请求文件。文件名基于当前时间戳生成，确保唯一性。
```

<img src="/PNG/4.png" alt="image" style="width:700px;height:700px;">

### 读取 URL 列表文件 

```shell
点击 读取 URL 列表文件 按钮后，工具会自动生成一个新的 URL 列表文件路径。同时，工具会打开一个编辑窗口，允许用户编辑该文件。文件名基于当前时间戳生成，确保唯一性。
```

<img src="/PNG/5.png" alt="image" style="width:700px;height:700px;">

### 更新 SQLMap

```shell
点击 更新 SQLMap 按钮后，工具会在新的命令提示符窗口中执行 --update 命令，将 SQLMap 更新到最新版本。因为该操作在pyqt5界面内运行，可能会自动选择N，所有弹cmd运行窗口。
```

<img src="/PNG/6.png" alt="image" style="width:700px;height:700px;">

### 设置代理
```shell
勾选 设置代理 按钮后，工具会自动走代理文件路径。
```

<img src="/PNG/7.png" alt="image" style="width:700px;height:700px;">

### 命令行输出

```shell
命令行输出区域 ：显示 SQLMap 的实时输出，包括成功、警告、错误等信息。不同类型的输出会以不同的颜色显示，便于用户快速识别。

    绿色：表示 [INFO] 类型的输出。
    红色：表示 Type:、Title:、Payload: 类型的输出，以及 [ERROR] 类型的输出。
    橙色：表示 [WARNING] 类型的输出。
    白色：表示其他类型的输出。
```

<img src="/PNG/8.png" alt="image" style="width:700px;height:700px;">

## ⬆️更新日志
```
- 【2024.12.22】 发布
- 【2025.09.20】 优化UI界面
```



本项目遵循 MIT 许可证。详情请参阅 LICENSE 文件。