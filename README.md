基于lxml库的xml文件同步工具

github仓库地址

此工具使用了python的lxml库中对xml文件进行解析，并同步xml文件的格式，包括同步元素的数据、同步增删元素。

lxml库的安装

安装相关库（可选）

以下只适用于linux

libxml2库中包含了xmllint程序，用来格式化xml文件，对程序正确性无影响，以下安装内容可选。

lxml 5.0 及更高版本需要 Python 3.6+。lxml 5.0 之前的版本支持 Python 2.7 和 3.6+。

lxml 需要安装 libxml2 和 libxslt，特别是：
- libxml2版本 2.9.2 或更高版本。
- libxslt版本 1.1.27 或更高版本。
  - 我们推荐 libxslt 1.1.28 或更高版本。
要在 Linux 系统上安装这些依赖项所需的开发包，请使用特定于发行版的安装工具，例如 Debian/Ubuntu 上的 apt-get：
sudo apt-get install libxml2-dev libxslt-dev python-dev
对于基于 Debian 的系统，安装提供的 lxml 包的已知构建依赖项就足够了，例如：
sudo apt-get build-dep python3-lxml
安装lxml库
如果您的系统不提供二进制包或者您想要安装较新的版本，最好的方法是获取pip包管理工具（或使用virtualenv）并运行以下命令：
pip install lxml
如果你没有在虚拟环境中使用 pip 而是想要全局安装 lxml，那么你必须以管理员身份运行上述命令，例如在 Linux 上：
sudo pip install lxml
要安装特定版本，请手动下载发行版并让 pip 安装，或者将所需版本传递给 pip：
pip install lxml==5.0.0
为了加快测试环境中的构建速度（例如在持续集成服务器上），通过设置CFLAGS环境变量来禁用 C 编译器优化：
CFLAGS="-O0"  pip install lxml
（选项为“-O0”，即零优化。）

安装xmllint
sudo apt-get install libxml2-utils

使用方法

run.sh和run.bat分别为linux、windows下的运行脚本，source run.sh即可运行程序，也可以自己调用python命令
eg：
#!/usr/bin/zsh

# 运行格式：python ./src/main.py 保存着需要同步标签的文件 样本xml ……所有需要同步的目录路径
python ./src/main.py ./resource/sync_value.txt ./resource/cell1.xml ./resource/benchmark/NarrowBand/fdd6cell20mhz-am

- 注意相对路径是相对于工程根目录xml_synchronize_py/
- sync_value.txt中保存着指定要同步的标签的名称，每个名称一行；只有在sync_value.txt中指定的标签数据会同步，未指定的标签，即使其数据在样本xml中修改，也不会同步到目标xml文件中
- xml_synchronize_py/resource/cell1.xml：该位置的参数为样本xml文件，你需要在其中修改内容，包括修改标签的数据、增删标签节点，其他指定的与该xml文件同名的xml文件会据此同步；自动增删标签来使得目标xml文件的结构与样本xml文件相同
- 后续的可变长参数为指定的所有目录，这些目录下所有与样本xml文件同名的xml文件都会被同步
- 程序运行后会显示同步的文件数量，以及其中的成功数量与失败数量，类似于下图：
![image](https://github.com/user-attachments/assets/354ecaca-6191-4ff0-9288-4da93169c054)

![image](https://github.com/user-attachments/assets/d058e3e6-67ad-4c36-b54f-8d8b2379e999)

![image](https://github.com/user-attachments/assets/4b33723a-ab9b-4a4f-868c-86e821bfb4f7)

- 在succeed.txt中保存着成功同步的xml文件的信息，包括该xml文件做出的改动（更改了哪些标签的数据、增删了哪些标签）
- 在fail.txt中保存着同步失败的xml文件的报错信息，错误原因可能为xml格式错误、存在重复名称标签、根节点标签名称与样本xml不匹配等原因，方便使用者在同步失败时快速定位、排查问题

