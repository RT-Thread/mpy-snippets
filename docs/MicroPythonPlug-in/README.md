# VSCode 最好用的 MicroPython 插件 

## 介绍 ([Drop down to view the English introduction document](#Introduction))

VSCode 最好用的 MicroPython 插件，为 MicroPython 开发提供了强大的开发环境，主要特性如下：

- 便捷的开发板连接方式（串口、网络、USB）
- 支持基于 MicroPython 的代码智能补全与语法检查
- 支持 MicroPython REPL 交互环境
- 提供丰富的代码示例与 demo 程序
- 提供工程同步功能
- 支持下载单个文件或文件夹至开发板
- 支持在内存中快速运行代码文件功能
- 支持运行代码片段功能
- 支持多款主流 MicroPython 开发板
- 支持 windows 及 ubuntu 操作系统

## 开发板支持列表

| 编号 | 开发板名称                                                   | 固件获取方式                                                 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [潘多拉 IoT Board 物联网开发板 STM32L475](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.12.2ba47ea5PzJxZx&id=583843059625) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 2    | [正点原子 W601 WIFI 物联网开发板](https://item.taobao.com/item.htm?spm=a230r.1.14.13.7c5b4a9bS2LYUD&id=602233847745&ns=1&abbucket=17#detail) | [RT-Thread 论坛固件汇总贴 ](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 3    | [正点原子探索者 STM32F407 开发板](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.18.569779dc0A3gkT&id=41855882779) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 4    | [RT-Thread 麻雀一号音视频开发板](https://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.42d74829w5rUfo&id=606684373403&_u=t2dmg8j26111) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 5    | [ESP8266](http://docs.micropython.org/en/latest/esp8266/quickref.html) | [官方下载链接](https://micropython.org/download#esp8266)     |
| 6    | [ESP32](http://docs.micropython.org/en/latest/esp32/quickref.html) | [官方下载链接](https://micropython.org/download#esp32)       |
| 7    | [PYboard](http://docs.micropython.org/en/latest/pyboard/quickref.html) | [官方下载链接](https://micropython.org/download#pyboard)     |
| 8    | [others](https://micropython.org/download#other)             | [官方下载链接](https://micropython.org/download#other)       |

编号为 1 - 4 的开发板的固件由 RT-Thread 官方提供，同时针对 MicroPython 插件开发环境进行 **深度优化** ，提供强大的工程同步功能以及更加丰富的固件功能。

欢迎加入`RT-Thread MicroPython` 交流 QQ 群 **703840633** 交流 MicroPython 技术。

您还可以登陆 [RT-Thread 官方论坛 Micropython 专区](https://www.rt-thread.org/qa/forum.php?mod=forumdisplay&fid=2&filter=typeid&typeid=20) 或者向 email : SummerGift@qq.com 发送邮件反馈宝贵的使用意见和建议，我们会第一时间根据您的反馈改进插件的使用体验。

## 准备工作

1. 在 windows 操作系统下使用插件需要将 vscode 的默认终端修改为 powershell，如下图所示：

   ![01_select_powershell](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095612g1fkz5fkr7fff177.gif)

如果想要使用 MicroPython 自动补全功能（如果暂时不需要自动补全功能，可以跳过后续步骤），还需要进行如下操作：

2. 安装 Python 插件

3. 按照 Python 插件的提示在 PC 上安装 Python3 并加入到系统环境变量中

   ![02_Python plug](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095612sku6jdblbtu3jpb6.png)

如果在 PC 上已经安装过上述插件和程序，可以跳过此准备步骤。

### ubuntu 支持

本插件支持在 **ubuntu 18.04** 版本下运行，为了避免在 ubuntu 系统下频繁获取串口权限，需要将当前用户加入到 `dialout` 用户组中，手动输入如下命令即可，`$USERNAME` 是系统当前用户名：

`sudo usermod -aG dialout $USERNAME`

注意：配置修改后需要 **重启一下操作系统** 使配置生效。

## 快速上手

###  创建 MicroPython 工程

MicroPython 开发的第一步是创建 MicroPython 工程，后续所有操作都必须在工程内才能运行。创建一个新的 MicroPython 工程有两种方式，分别是创建一个空白工程和基于 Demo 创建工程，下面展示这两种方式。

#### 创建一个空白 MicroPython 工程

![03_create_blank_dir](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095613f5oshzvj2og32gio.gif)

#### 创建一个基于 Demo 的 MicroPython 工程

通过该功能可以创建一个基于 demo 的 MicroPython 工程，开发者可以直接运行该 Demo 工程或者在该 Demo 的基础上实现自己想要的功能。

![04_create_demo_dir](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095613zsspdy1cywjiyhcb.gif)

#### Weather Show Demo 在开发板上的运行效果

![05_demo_express](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095613vjarrl8nflyfzoya.png)

该 Demo 全部代码使用 MicroPython 编写，可以在 [潘多拉 IoT Board 开发板](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.12.2ba47ea5PzJxZx&id=583843059625) 和 [正点原子 W601 WIFI 物联网开发板](https://item.taobao.com/item.htm?spm=a230r.1.14.13.7c5b4a9bS2LYUD&id=602233847745&ns=1&abbucket=17#detail) 上直接下载运行。

### 连接开发板

点击左下角的连接按钮，然后在弹出的设备列表中选择想要连接的设备，即可连接 MicroPython 开发板。

![06_uart_connect](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095613vpb82unp0n9m8lf2.gif)

### 查看示例代码文件

MicroPython 插件提供丰富的示例代码，可在左侧活动栏中查看示例代码和库文件。右键点击示例文件，在下拉菜单中可以将示例文件添加到工程中。

![07_check_example](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095613szp10s0ouaulrxpq.png)

### 直接在开发板上运行 MicroPython 文件（调试神器）

该功能用于快速调试单个文件，频繁应用在调试代码的过程中。当我们在一个单独的文件中编写测试程序时，使用该功能可以将当前 python 文件下载到开发板的内存中运行，达到快速调试的效果，还可以使用快捷键 `alt + q` 来触发该功能。

![08_direct_run_files](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095614s0rbxgxrle0bjjix.gif)

### 在开发板上运行 MicroPython 代码片段

如果只是想进行代码量不大的代码调试，而不想将文件下载到开发板上，那么可以使用 **代码片段** 功能。在编辑器中选中想要运行的代码片段，然后在右键下拉菜单中选择 `在设备上执行选中的 MicroPython 代码` 选项，即可在 REPL 环境中运行所选代码。

![09_run_code_snippet](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095614buewlgkp2mml2wca.gif)

### 下载文件/文件夹到开发板

如果想要下载单个文件/文件夹到开发板，此时可以使用 **下载单个文件/文件夹到开发板** 的功能。在工程中选中想要下载到开发板上的文件/文件夹，在下拉菜单中使用该功能即可。这里需要注意的是，如果开发板上有同名的文件/文件夹，下载操作将会覆盖这些已有的文件/文件夹。

通过在 `repl` 中输入 `os.listdir()` 命令可以查看相应的文件/文件夹是否下载成功，同样在 `repl` 中还可以使用相应的命令 **删除文件或文件夹**，命令列表如下所示：

| 功能       | 命令                       |
| ---------- | -------------------------- |
| 删除文件   | `os.remove("file_to_del")` |
| 删除文件夹 | `os.rmdir("dir_to_del")`   |

![10_download_file_floder](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095614nbjb8bqzz48f8tl6.gif)

### 工程同步功能

点击左下角的同步按钮可以启动工程同步功能。通过该功能可将本地工程中所有目录文件，同步到开发板的文件系统中。该功能推荐在代码调试完成后使用，在调试过程中不必频繁同步工程。

工程同步完成后，可以在 `DEVICE FILES LIST` 栏目中看到 **设备中的文件列表**。

![11_sync_files](https://www.rt-thread.org/qa/data/attachment/forum/201910/22/095614jaitcbhh1ge30h1e.gif)

### 基于 MicroPython 的代码智能补全

本插件支持基于 MicroPython 语法的代码智能补全和语法检查，这一强大功能对于开发 MicroPython 代码十分实用。它可以让开发者在编写函数的同时查看 API 参数提示，同时它给出的醒目提示也让开发者更易于查找代码中的错误。

![12_auto_complete](https://i1.fuimg.com/702031/3145644b4275bce5.gif)

## 开发资源

- [RT-Thread MicroPython 开发用户手册](https://www.rt-thread.org/document/site/submodules/micropython/docs/)
- [RT-Thread MicroPython 软件包](https://github.com/RT-Thread-packages/micropython)
- [RT-Thread MicroPython 示例程序及库](https://github.com/RT-Thread/mpy-snippets)
- [RT-Thread MicroPython 论坛](https://www.rt-thread.org/qa/forum.php?mod=forumdisplay&fid=2&filter=typeid&typeid=20)
- [MicroPython IDE 用户指南](https://www.rt-thread.org/document/site/submodules/micropython/docs/MicroPythonPlug-in/MicroPython_IDE_User_Manual/)
- [MicroPython 固件开发指南](https://www.rt-thread.org/document/site/submodules/micropython/docs/MicroPythonPlug-in/MicroPython_Firmware_Development_Guide/)

## 注意事项

- 不要删除工程目录下的 `.mpyproject.json` 文件，该文件是 MicroPython 工程的配置文件，删除后将无法正常运行 MicroPython 代码程序。

---

# The best MicroPython plug-in of vscode

## Introduction

RT-Thread MicroPython is the best micropython plug-in in VScode, which provides a powerful development environment for MicroPython development. The main features are as follows:

- Convenient connection mode of development board (serial port, network, USB)
- Support MicroPython-based code intelligent completion and syntax check
- Support MicroPython REPL interactive environment
- Provides many code samples and demo program
- Support full project synchronization function
- Support to download files or folders to the development board
- Supports fast running code files in memory
- Supports code snippets to run functions
- Supports several major MicroPython development boards
- Support Windows and ubuntu operating systems

## Development board support list

| number | Name of development board                                    | Firmware acquisition                                         |
| ------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1      | [潘多拉 IoT Board 物联网开发板 STM32L475](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.12.2ba47ea5PzJxZx&id=583843059625) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 2      | [正点原子 W601 WIFI 物联网开发板](https://item.taobao.com/item.htm?spm=a230r.1.14.13.7c5b4a9bS2LYUD&id=602233847745&ns=1&abbucket=17#detail) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 3      | [正点原子探索者 STM32F407 开发板](https://item.taobao.com/item.htm?spm=a1z10.5-c-s.w4002-18400369818.18.569779dc0A3gkT&id=41855882779) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 4      | [RT-Thread 麻雀一号音视频开发板](https://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.42d74829w5rUfo&id=606684373403&_u=t2dmg8j26111) | [RT-Thread 论坛固件汇总贴](https://www.rt-thread.org/qa/forum.php?mod=viewthread&tid=12305&page=1&extra=#pid52954) |
| 5      | [ESP8266](http://docs.micropython.org/en/latest/esp8266/quickref.html) | [Official download link](https://micropython.org/download#esp8266) |
| 6      | [ESP32](http://docs.micropython.org/en/latest/esp32/quickref.html) | [Official download link](https://micropython.org/download#esp32) |
| 7      | [PYboard](http://docs.micropython.org/en/latest/pyboard/quickref.html) | [Official download link](https://micropython.org/download#pyboard) |
| 8      | [others](https://micropython.org/download#other)             | [Official download link](https://micropython.org/download#other) |

The firmware for the development boards numbered 1, 2, and 3 is provided by rt-thread, and is also optimized for the MicroPython plug-in development environment to provide powerful engineering synchronization and richer firmware features. 

## Preparation

1. Using plug-in under the Windows operating system requires changing the default terminal of vscode to powershell, as shown below:

   ![select_powershell](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/en_select_powershell.gif)

If you want to use the MicroPython autocompletion feature (you can skip the next step if you don't need autocompletion for now), you need to do the following:

2. Install the Python plug-in

3. Install Python3 on your PC and add it to the system environment variables as instructed by the Python plug-in

   ![Python plug](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/install_python_plug_en.png)

If you already have the above plug-ins and programs installed on your PC, you can skip this preparation step.

### Ubuntu support

This plug-in supports running under **ubuntu 18.04**. In order to avoid frequent access to serial port permissions under ubuntu system, the current user needs to be added to the user group `dialout`. Manually enter the following command: `$USERNAME` is the current USERNAME of the system:

`sudo usermod -ag dialout $USERNAME`

Note: the configuration change requires **to restart the operating system** for the configuration to take effect.

## Quick Start

### Create a MicroPython project

The first step in MicroPython development is to create a MicroPython project within which all subsequent operations must run. There are two ways to create a new MicroPython project, a blank project and a demo-based project, which are shown below.

![create_blank_dir](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/en_create_blank_project.gif)

### Connecting development board

You can connect to the MicroPython development board by clicking the connection button in the lower left corner and then selecting the device you want to connect to in the pop-up list of devices.

![uart_connect](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/en_connect_board.gif)

### View the sample code file

The MicroPython plug-in provides a wealth of sample code and library files to view in the left active bar. Right-click on the sample file to add the sample file to the project from the drop-down menu.

![example_code](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/check_example_en.png)

### Run MicroPython files directly on the development board (kind for debug)

This feature is used to `quickly debug a single file` and is frequently used in debugging code. When we write the test program in a separate file, we can use this function to download the current python file to the memory of the development board to run, achieving the effect of rapid debugging. We can also use the shortcut key `Alt + q` to trigger this function.

![run_example](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/direct_run_files_en.gif)

### Run MicroPython code snippets on the development board

If you just want to debug a small amount of code without downloading files to the development board, you can use the **code snippet** function. You can run the selected code in the REPL environment by selecting the snippet you want to run in the editor, and then selecting the `execute the selected MicroPython code` option on the device from the right-click menu.

![run_code_snippet](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/en_run_snippets.gif)

### Download files/folders to the development board

If you want to download individual files/folders to the development board, you can use the function of to **download individual files/folders to the development board**. Select the file/folder in the project that you want to download to the development board and use this feature in the drop-down menu. 

Note that if there are files/folders with the `same name` on the development board, the download will `overwrite` the existing files/folders.

By entering the command `os.listdir()` in `repl`, you can check whether the corresponding file/folder has been `downloaded` successfully. Similarly, you can also use the corresponding command **to delete the file or folder** in `repl`. The command list is as follows:

| function       | command                       |
| ---------- | -------------------------- |
| remove file   | `os.remove("file_to_del")` |
| remove folder | `os.rmdir("folder_to_del")`   |

![auto_complete](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/download_file_floder_en.gif)

### project synchronization

Click the synchronization button `in the lower left corner` to start the project synchronization function. This feature synchronizes `all directory files` in the local project to the development board's file system. This feature is recommended to be used `after the code is debugged`, without the need to synchronize the project frequently during debugging.

After the project synchronization is completed, `the list of files` in the DEVICE can be seen in the `DEVICE FILES LIST column`.

![run_code_snippet](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/sync_files_en.gif)

### Intelligent code completion based on MicroPython

This plug-in supports `intelligent code completion` and syntax checking `based on MicroPython syntax`, which is a powerful tool for developing MicroPython code. It allows developers to write functions while looking at API parameter hints, and it gives them a visual reminder that makes it easier to find errors in code.

![auto_complete](https://raw.githubusercontent.com/RT-Thread-packages/micropython/master/docs/MicroPythonPlug-in/assets/auto_complete.gif)

## Matters needing attention

- Do not delete the `.mpyproject.json` file in the project directory. This file is the configuration file of the MicroPython project.

## Contact & Supports

- [Github](https://github.com/SummerGGift/ampy)
- Support Email : SummerGift@qq.com
