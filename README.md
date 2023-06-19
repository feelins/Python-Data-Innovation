# Python-linguistics
这个项目主要和语言学专业的数据处理，包括但不限于语音、文本等方面，使用Python的一些脚本和技巧，同时也面向初学者，提供短小精悍的一些练手学习的脚本。
> 欢迎关注公众号：极地语音工作室；
> CSDN博客：[https://blog.csdn.net/shaopengfei](https://blog.csdn.net/shaopengfei)  

![效果](res/IMG_0167.PNG)

说明：每一部分为一个主题，第一部分适合初学者练手；第二部分每一小部分为一个主题；第三部分为；  


## 第〇部分 相关文档

* [Ubuntu 20.04.3 Anaconda安装及Python多版本虚拟环境配置](https://blog.csdn.net/shaopengfei/article/details/123440125)
* [VS Code中使用Python相对路径问题](https://blog.csdn.net/shaopengfei/article/details/123454659)
* [更优雅熟练的使用git-学习记录](https://blog.csdn.net/shaopengfei/article/details/123955385)
## 第一部分 入门脚本
本部分的脚本多为10行以内的代码量，主要目的是针对一个小小的知识点，了解一个概念或者一个用法。更适合于学习者了解某一个点的语法知识。   


| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
|  [P01-001](Part-01/src/p01_001_hello_world.py) | * 学习编程语言第一步，学会打印hello, world!; <br>* Python可以使用单引号，也可以使用双引号;   <br>* 如果在引号内部有引号，注意使用不同的就可以了; <br>* 如果必须使用相同的符号，那么需要加转义符号，斜杠; <br>* 笔者习惯于所有引号位置都使用单引号，内部使用双引号； | [阅读原文] | - |  
|  [P01-002](Part-01/src/p01_002_read_simple.py)  | * 读文本内容，并打印在屏幕上 | [阅读原文] | - | 
|  [P01-003](Part-01/src/p01_003_internal_function_of_dict.py) | * 字典的内置函数; <br>* dict.clear()清除字典; <br>* dict.get()搜索字典，如果发现返回关联的值。如果未找到，则返回None; <br>* dict.items(), 返回字典中的键值对列表; <br>* dict.keys(), dict.values(), 返回字典的键和值的列表; <br>* dict.pop(), 从字典中删除一个键; <br>* dict.popitem(), 从字典删除键值对，删除最后一个; <br>* dict.update(), 将字典与另一个字典或可迭代的键值对合并; <br>| [阅读原文] | - | 
| [P01-004](Part-01/src/p01_004_merge_two_list_to_dict.py)  | * 用三种方法将两个列表，转化为字典， 使用zip函数 | [阅读原文] | - | 
| [P01-005](Part-01/src/p01_005_dict_orderby.py)  | * 对字典列表，根据键，值进行排序 | [阅读原文] | - | 
| [P01-006](Part-01/src/p01_006_string_list_orderby.py) | * 对字符串列表进行排序 <br> * sort 与 sorted 区别 | [阅读原文] | - | 
| [P01-007](Part-01/src/p01_007_string_orderby_byte.py) | * 以字节为单位获取字符串大小<br> * 如何获取字符串的字节数 | [阅读原文] | - | 
| [P01-008](Part-01/src/p01_008_vscode_path_problem.py) | * VS Code中使用Python相对路径问题 | [阅读原文] | - | 
| [P01-009](Part-01/src/p01_009_swap.py)| python是如何实现两个变量交换的？ | [阅读原文] | - | 
| [P01-010](Part-01/src/p01_010_how_to_use_at.py) | * python修饰符@的使用 | [阅读原文] | - | 
| [P01-011](Part-01/src/p01_011_better_code_style.py) | * 几个例子，代码的一些更好的形式 | [阅读原文] | - | 
| [P01-012](Part-01/src/p01_012_string_upper_lower_title.py) | * 字符串的大写，小写，第一个字母大写用法 | [阅读原文] | - | 
| [P01-013](Part-01/src/p01_013_something_about_function.py) | 理解一些关于函数的概念<br>* 函数的对象特性，也可以赋值，也可以当作参数，返回值也可以是函数<br>* 函数也可以在字典里当参数使用 | [阅读原文] | - | 
| [P01-014](Part-01/src/p01_014_join_string.py) | 字符串连接，加号和join的区别<br>* 在连接字符串数组的时候，我们应考虑优先使用join | [阅读原文] | - | 

## 第二部分 简单功能脚本
* 本部分的代码多为能实现一个简单的小功能。 


| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
| [P02-001](Part-02/P02_001_ProgressBar) | <font color=orange>进度条的一些实现形式</font><br>* p02_001_alive_progress_bar.py, 有一些动画效果的进度条<br>* p02_001_normal_progress_bar.py, 普通进度条<br>* p02_001_progress_bar_iterations.py, 用于定义迭代次数的进度条<br>* p02_001_progress_bar_with_time.py, 带时间进度条<br>* p02_001_tqdm_progress_bar.py, tqdm进度条<br>  | [阅读原文] | - | 
| [P02-002](Part-02/P02_002_Numpy) | <font color=orange>Numpy的一些学习知识点</font> | [阅读原文] | - | 
| [P02-003](Part-02/P02_003_FileNameOrder/p02_003_001_file_name_order.py) | <font color=orange>文件名排序问题</font><br> * 文件名可以按包含的数字排序，而不是按整个文件名字符串排序 | [阅读原文](https://blog.csdn.net/shaopengfei/article/details/123455273) | - | 
| [P02-004](Part-02/P02_004_Deep_Learning_from_Scratch) | <font color=orange>《深度学习入门-基于Python的理论与实现》学习记录</font> | [阅读原文] | - | 
| [P02-005](Part-02/P02_005_Pandas)  | <font color=orange>Pandas的一些学习知识点</font> | [阅读原文] | - | 
| [P02-006](Part-02/P02_006_Head_First_Python)  | <font color=orange>《Head First Python》学习记录</font> | [阅读原文] | - | 


## 第三部分 音频处理

| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
| [P03-001](Part-03/P03_001_read_wav/p03_001_read_wavform.py) | * 基本的读取wav的操作 |  [阅读原文] | - | 
| [P03-002](Part-03/P03_002_wav_duration/p03_002_compute_wav_duration.py) |* 计算一个音频目录里的wav文件的总时长和每个文件的时长。 | * 基本的读取wav的操作 |  [阅读原文] | - | 

## 第四部分 文本处理

| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
| [P04-001](Part-04/P04_001_WordSegment)  | 前后项分词|  [阅读原文] | - | 
| [P04-002](Part-04/P04_002_Split_Text)| 对一个有几列的文本，通过某种分割符分别保存|  [阅读原文] | - | 


## 第五部分 Praat标注相关

| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
| [P05-001](Part-05/P05_001_check_file_numbers/p05_001_check_file_numbers.py)  |* 检查两个目录里文件对应情况，分别保存两个目录都有的文件，<br>每个目录独有的文件，以及上述文件的log|  [阅读原文](https://blog.csdn.net/shaopengfei/article/details/123554296) | - | 
| [P05-002](Part-05/P05_002_pitch_distance)  |* 通过基频曲线的距离做一个声调判别器|  [阅读原文](https://blog.csdn.net/shaopengfei/article/details/124058801) | - | 

## 第六部分 数据相关

| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
| [P06-001](Part-06\P06_001_download_douban_info\p06_001_download_douban_book_movie_list.py)  |* 获取豆瓣的读书和影视列表|  [阅读原文]() | - | 

## 参考文档
* [Python - 100天从新手到大师](https://github.com/jackfrued/Python-100-Days)

## 索引此项目请参考