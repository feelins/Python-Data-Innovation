# Python_for_Data_Analysis
这本书。
> 欢迎关注公众号：极地语音工作室；
> CSDN博客：[https://blog.csdn.net/shaopengfei](https://blog.csdn.net/shaopengfei)  

![效果](res/IMG_0167.PNG)

说明：每一部分为一个主题，第一部分适合初学者练手；第二部分每一小部分为一个主题；第三部分为；  



## 第5章 pandas 入门
本部分的脚本多为10行以内的代码量，主要目的是针对一个小小的知识点，了解一个概念或者一个用法。更适合于学习者了解某一个点的语法知识。   


| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
|  [P02_5-1-1](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-1-1_series.py) | * Series的用法和dict有些相似，它到底有什么优点？; <br>* 可以指定索引，也有默认的索引;   <br>* 可以有丰富的计算、过滤功能; <br> | [阅读原文] | - |  
|  [P02_5-1-2](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-1-2_DataFrame.py) | * DataFrame表示的是矩阵的数据表，它包含已排序的列集合，每一列都可以是不同的值类型; <br>* DataFrame既有行索引也有列索引，可视为共享相同索引的Series的字典；  <br>* 尽管是二维的，但是通过分层索引可以展现更高维度的数据; <br> | [阅读原文] | - | 
|  [P02_5-1-3](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-1-3_index_object.py) | * pandas的索引对象是用于存储轴标签和其它元数据的，它的使用比较灵活，比如可以切片使用; <br>* 上述索引对象可以共享给其它数据结构使用；  | [阅读原文] | - |
|  [P02_5-2-1](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-1_rebuild_index.py) | * Series调用reindex方法时，会将数据按新的索引进行排列，不存在的索引值会引入缺失值; <br>* 顺序数据，比如时间序列等，需要插值或者填值，method允许我们使用如ffill，向前插值的方法填充； <br>* DataFrame中，reindex可以改变行索引、列索引；  | [阅读原文] | - |
|  [P02_5-2-2](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-2_drop_items.py) | * 轴向上删除数据；  | [阅读原文] | - |
|  [P02_5-2-3](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-3_index_select_filter.py) | * 索引、选择各种灵活的使用方式; <br>* 普通的Python切片是不包括尾巴的，但是请注意这里的切片！是包括的！！！； <br>* 根据一个布尔值数组切片或者选择数据；<br>* loc iloc灵活使用;  | [阅读原文] | - |
|  [P02_5-2-4](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-4_integer_index.py) | * 尽量使用loc, iloc;  | [阅读原文] | - |
|  [P02_007_6-1-2](Part-02/P02_007_Python_for_Data_Analysis/Chap06/p02_007_6-1-2_write_to_csv.py) | * 将数据导出为逗号分隔的文件;  <br>* 可以禁止写入索引，和表头; <br>* 缺失值替换为NULL; <br>* 只保存指定的两列;这里报错？？？| [阅读原文] | - |
|  [P02_007_6-1-3](Part-02/P02_007_Python_for_Data_Analysis/Chap06/p02_007_6-1-3_use_split_csv.py) | * 使用Python内置的csv模块读取CSV文件; | [阅读原文] | - |


## 第6章 数据载入、存储及文件格式

| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-------: | :------------- | :---------: | :------------- | 
|  [P02_6-1](Part-02/P02_007_Python_for_Data_Analysis/Chap06/p02_6-1-0_read_write_txt.py) | * read_csv, read_table用法; <br> | [阅读原文] | - |  