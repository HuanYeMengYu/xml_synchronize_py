# 基于lxml库的xml文件同步工具

[github仓库地址](https://github.com/HuanYeMengYu/xml_synchronize_py)

此工具使用了python的lxml库中对xml文件进行解析，并同步xml文件的格式，包括同步元素的数据、同步增删元素。

# [lxml库的安装](https://lxml.de/installation.html)

## 安装相关库（可选）

> 以下只适用于linux

libxml2库中包含了xmllint程序，用来格式化xml文件，对程序正确性无影响，以下安装内容可选。

lxml 5.0 及更高版本需要 Python 3.6+。lxml 5.0 之前的版本支持 Python 2.7 和 3.6+。

lxml 需要安装 libxml2 和 libxslt，特别是：

- **[libxml2](http://xmlsoft.org/)**版本 2.9.2 或更高版本。
- **[libxslt](http://xmlsoft.org/XSLT/)**版本 1.1.27 或更高版本。
  - 我们推荐 libxslt 1.1.28 或更高版本。

要在 Linux 系统上安装这些依赖项所需的开发包，请使用特定于发行版的安装工具，例如 Debian/Ubuntu 上的 apt-get：

```
sudo apt-get install libxml2-dev libxslt-dev python-dev
```

对于基于 Debian 的系统，安装提供的 lxml 包的已知构建依赖项就足够了，例如：

```
sudo apt-get build-dep python3-lxml
```

## **安装lxml库**

如果您的系统不提供二进制包或者您想要安装较新的版本，最好的方法是获取**[pip](http://pypi.python.org/pypi/pip)**包管理工具（或使用**[virtualenv](https://pypi.python.org/pypi/virtualenv)**）并运行以下命令：

```
pip install lxml
```

如果你没有在虚拟环境中使用 pip 而是想要全局安装 lxml，那么你必须以管理员身份运行上述命令，例如在 Linux 上：

```
sudo pip install lxml
```

要安装特定版本，请手动下载发行版并让 pip 安装，或者将所需版本传递给 pip：

```
pip install lxml==5.0.0
```

为了加快测试环境中的构建速度（例如在持续集成服务器上），通过设置CFLAGS环境变量来禁用 C 编译器优化：

```
CFLAGS="-O0"  pip install lxml
```

（选项为“-O0”，即零优化。）

## 安装xmllint

```SQL
sudo apt-get install libxml2-utils
```

# 使用方法

run.sh和run.bat分别为linux、windows下的运行脚本，`source run.sh`即可运行程序，也可以自己调用python命令

eg：

```Shell
#!/usr/bin/zsh

# 运行格式：python ./src/main.py 保存着需要同步标签的文件 样本xml ……所有需要同步的目录路径
python ./src/main.py ./resource/sync_value.txt ./resource/cell1.xml ./resource/benchmark/NarrowBand/fdd6cell20mhz-am
```

- 注意相对路径是相对于工程根目录xml_synchronize_py/
- sync_value.txt中保存着指定要同步的标签的名称，每个名称一行；**只有在sync_value.txt中指定的标签数据会同步**，未指定的标签，即使其数据在样本xml中修改，也不会同步到目标xml文件中
- xml_synchronize_py/resource/cell1.xml：该位置的参数为样本xml文件，你需要在其中修改内容，包括修改标签的数据、增删标签节点，其他指定的与该xml文件同名的xml文件会据此同步；**自动增删标签**来使得目标xml文件的结构与样本xml文件相同
- 后续的可变长参数为指定的所有目录，这些目录下所有与样本xml文件同名的xml文件都会被同步
- 程序运行后会显示同步的文件数量，以及其中的成功数量与失败数量，类似于下图：

![img](https://diangroup.feishu.cn/space/api/box/stream/download/asynccode/?code=ODE1YWVjNjI1NzdhZDE2NTFmYjZkY2QyOGE0N2QwNmFfdUJIbTVaTlRnb0x0VWphbUFJVXRFWUxIblNoWU5pSzVfVG9rZW46TGU1RmJvZXp3b0VoZm14ODl6aWM2WUUxbjhBXzE3MjMxMDQ2NTA6MTcyMzEwODI1MF9WNA)

![img](https://diangroup.feishu.cn/space/api/box/stream/download/asynccode/?code=ODM0NDAxZDMyYzkyYmE3YjM2NDkyYmYwMWZkNDZlMWJfYWU0dVVpS3ZscFJRWWUxTEowMEoxbldlSUlKcElsdU1fVG9rZW46SHVZT2I5ekF1bzl0Y1R4c1Y2VmNyZ29UbnRmXzE3MjMxMDQ2NTA6MTcyMzEwODI1MF9WNA)

![img](https://diangroup.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWQ1N2NhOTVhMTAyOTRkZjZmMjFiMmU3ZWE5NzNkMjdfekVzdE5qUXVhcDdTZ1k5TTh2c3RheXhmUDZtRFRJbEJfVG9rZW46UnU4ZWJRb0lBb0czdmt4T3ZSaGM2WHNnbkpjXzE3MjMxMDQ2NTA6MTcyMzEwODI1MF9WNA)

- 在succeed.txt中保存着成功同步的xml文件的信息，包括该xml文件做出的改动（更改了哪些标签的数据、增删了哪些标签）

Eg：

> This is the information of successful synchronization of XML files.
>
> ------
>
> ------
>
> Successfully synchronized file:'./resource/project/config/benchmark/HTOFF_todo/PacketHTOFF/UMHTOFF/cell1.xml'
>
> Added tag '/CellConfig/Russia'
>
> Added tag '/CellConfig/new1'
>
> Deleted tag '/CellConfig/nULBandwidth'
>
> Synchronized tag data '/CellConfig/nDMRSTypeAPos' = 777
>
> ------
>
> Successfully synchronized file:'./resource/project/config/benchmark/HTOFF_todo/PacketHTOFF/AMHTOFF/cell1.xml'
>
> Added tag '/CellConfig/Russia'
>
> Added tag '/CellConfig/new1'
>
> Deleted tag '/CellConfig/nULBandwidth'
>
> Synchronized tag data '/CellConfig/nDMRSTypeAPos' = 777

- 在fail.txt中保存着同步失败的xml文件的报错信息，错误原因可能为xml格式错误、存在重复名称标签、根节点标签名称与样本xml不匹配等原因，方便使用者在同步失败时快速定位、排查问题

Eg:第一个xml文件存在同名节点，第二个xml文件格式不正确，解析错误

> This is the information of unsuccessful synchronization of XML files.
>
> ------
>
> ------
>
> Failed synchronizing xml file './resource/project/config/benchmark/NarrowBand/fdd6cell20mhz-um/cell1.xml'
>
> The target xml file './resource/project/config/benchmark/NarrowBand/fdd6cell20mhz-um/cell1.xml' has tags with same name {'cellId'} .
>
> Skip synchronizing this target file.
>
> ------
>
> Failed synchronizing xml file './resource/project/build/nr5g/cell1.xml'
>
> The format of XML file './resource/project/build/nr5g/cell1.xml' doesn't meet the specifications!
>
> The following is the parsing error output:
>
> ./resource/project/build/nr5g/cell1.xml:270: parser error : Opening and ending tag mismatch: cellId line 10 and CellConfig
>
> </CellConfig>
>
> ​             ^
>
> ./resource/project/build/nr5g/cell1.xml:271: parser error : Premature end of data in tag cellId line 10
>
> 
>
> ^
