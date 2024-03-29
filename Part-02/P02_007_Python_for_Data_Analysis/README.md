# Python_for_Data_Analysis
这本书。
> 欢迎关注公众号：极地语音工作室；
> CSDN博客：[https://blog.csdn.net/shaopengfei](https://blog.csdn.net/shaopengfei)  

![效果](../../res/IMG_0167.PNG)

说明：每一部分为一个主题，第一部分适合初学者练手；第二部分每一小部分为一个主题；第三部分为；  

## 第4章 NumPy基础
| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :----------: | :------------- | :---------: | :------------- | 
|  [P02_4-0-0](Chap04/p02_007_4-0-0_numpy_more_fast.py) | * numpy更高效; <br> | [阅读原文] | - |  

## 第5章 pandas 入门
本部分的脚本多为10行以内的代码量，主要目的是针对一个小小的知识点，了解一个概念或者一个用法。更适合于学习者了解某一个点的语法知识。   


| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :----------: | :------------- | :---------: | :------------- | 
|  [P02_5-1-1](Chap05/p02_5-1-1_series.py) | * Series的用法和dict有些相似，它到底有什么优点？; <br>* 可以指定索引，也有默认的索引;   <br>* 可以有丰富的计算、过滤功能; <br> | [阅读原文] | - |  
|  [P02_5-1-2](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-1-2_DataFrame.py) | * DataFrame表示的是矩阵的数据表，它包含已排序的列集合，每一列都可以是不同的值类型; <br>* DataFrame既有行索引也有列索引，可视为共享相同索引的Series的字典；  <br>* 尽管是二维的，但是通过分层索引可以展现更高维度的数据; <br> | [阅读原文] | - | 
|  [P02_5-1-3](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-1-3_index_object.py) | * pandas的索引对象是用于存储轴标签和其它元数据的，它的使用比较灵活，比如可以切片使用; <br>* 上述索引对象可以共享给其它数据结构使用；  | [阅读原文] | - |
|  [P02_5-2-1](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-1_rebuild_index.py) | * Series调用reindex方法时，会将数据按新的索引进行排列，不存在的索引值会引入缺失值; <br>* 顺序数据，比如时间序列等，需要插值或者填值，method允许我们使用如ffill，向前插值的方法填充； <br>* DataFrame中，reindex可以改变行索引、列索引；  | [阅读原文] | - |
|  [P02_5-2-2](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-2_drop_items.py) | * 轴向上删除数据；  | [阅读原文] | - |
|  [P02_5-2-3](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-3_index_select_filter.py) | * 索引、选择各种灵活的使用方式; <br>* 普通的Python切片是不包括尾巴的，但是请注意这里的切片！是包括的！！！； <br>* 根据一个布尔值数组切片或者选择数据；<br>* loc iloc灵活使用;  | [阅读原文] | - |
|  [P02_5-2-4](Part-02/P02_007_Python_for_Data_Analysis/Chap05/p02_5-2-4_integer_index.py) | * 尽量使用loc, iloc;  | [阅读原文] | - |



## 第6章 数据载入、存储及文件格式

| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :----------: | :------------- | :---------: | :------------- | 
|  [P02_6-1](Part-02/P02_007_Python_for_Data_Analysis/Chap06/p02_6-1-0_read_write_txt.py) | * read_csv, read_table用法; <br> | [阅读原文] | - |  
|  [P02_007_6-1-2](Part-02/P02_007_Python_for_Data_Analysis/Chap06/p02_007_6-1-2_write_to_csv.py) | * 将数据导出为逗号分隔的文件;  <br>* 可以禁止写入索引，和表头; <br>* 缺失值替换为NULL; <br>* 只保存指定的两列;这里报错？？？| [阅读原文] | - |
|  [P02_007_6-1-3](Part-02/P02_007_Python_for_Data_Analysis/Chap06/p02_007_6-1-3_use_split_csv.py) | * 使用Python内置的csv模块读取CSV文件; | [阅读原文] | - |
|  [P02_007_6-4](Chap06/p02_007_6-4_query_database.py) | * 与数据库交互；<br>* 安装sqllite插件，打开ctrl+shift+p，输入sqllite，选择Open Database，选择新建的数据库，在左下方，会出现sqllite explorer，可以显示数据表格； | [阅读原文] | - |


## 第7章 数据清洗与准备
| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-----------: | :------------- | :---------: | :------------- | 
|  [7.1 处理缺失值](Chap07/p02_007_7-1-0_about_null_value.py) | * NaN表示空值，数组中的None也会被表示为空值；<br> * 除了isnull判断空值，还有一个反函数，notnull; | [阅读原文] | - |
|  [7.1.1 过滤缺失值](Chap07/p02_007_7-1-1_filter_null_values.py) | * 在Series上使用dropna会返回非空的数据和索引值；<br> * 引入how='all'参数， 将会只删除这一行里的元素全部为NA的行; <br> * 以上两个操作删除列，则加一个axis=1; <br> * 使用thresh=2过滤每一行中，至少有3个非空值，不满足的过滤掉，还可以使用0.7*len()的形式代表百分比； | [阅读原文] | - |
|  [7.1.2 补全缺失值](Chap07/p02_007_7-1-2_complete_null_values.py) | * 赋值一个常数；<br> * 可以分别对不同的列赋值不同的常数; <br> * fillna是生成一个新的对象，但是也可以通过inplace=True修改本身，同样适用于Series; <br> * 也可以使用一些插值方法； | [阅读原文] | - |
|  [7.2.1 删除重复值](Chap07/p02_007_7-2-1_drop_duplicate_values.py) | * 返回一个布尔值，Series，每一行是否存在重复值（与之前出现的行重复）；<br> * 返回的是DataFrame，将上面为False的部分保留下来; <br> * 根据name这一列去除重复的部分; <br> * 根据name这一列，去除重复，而且是保留最后一个出现的； | [阅读原文] | - |
|  [7.2.2 使用映射数据转换](Chap07/p02_007_7-2-2_trans_data_with_map_dict_or_function.py) | * 也可以通过映射函数实现，对数据转换；<br> | [阅读原文] | - |
|  [7.2.3 替代值](Chap07/p02_007_7-2-3_replace_values.py) | * 相对于fillna，是通用的值替换的方法；<br> | [阅读原文] | - |
|  [7.2.4 重命名轴索引](Chap07/p02_007_7-2-4_rename_column_index.py) | * 重命名；<br> | [阅读原文] | - |
|  [7.2.5 离散化和分箱](Chap07/p02_007_7-2-5_discrete_cut_bins.py) | * 可以根据最大值，最小值，计算出平均出来的箱区间；<br> | [阅读原文] | - |
|  [7.2.6 检测和过滤异常值](Chap07/p02_007_7-2-6_detect_filter_unusual_values.py) | * 检测和过滤异常值；<br> | [阅读原文] | - |
|  [7.3.3 pandas中的向量化字符串函数](Chap07/p02_007_7-3-3_vectorized_string_function.py) | * pandas中的向量化字符串函数；<br> | [阅读原文] | - |

## 第8章 数据规整：连接、联合与重塑
| 分类目录  | 知识点 | 详情阅读 | 应用举例 |  
| :-----------: | :------------- | :---------: | :------------- | 
|  [8.1 分层索引](Chap08/p02_007_8-1-0_multi_index.py) | * 使用MultiIndex作为索引的美化视图；<br> | [阅读原文] | - |
|  [8.1.1 重排序和层级排序](Chap08/p02_007_8-1-1_swap_level_re_sort.py) | * swaplevel接收两个层级的序号，或者层级名称，顺序变化了之后，数据不变；<br> * sort_index在单一层级上对数据！！！进行排序；<br> | [阅读原文] | - |
|  [8.1.2 按层级进行汇总统计](Chap08/p02_007_8-1-2_sumup_by_levels.py) | * 这部分不成功；<br> | [阅读原文] | - |
|  [8.2.1 数据库风格的DataFrame连接](Chap08/p02_007_8-2-1_merge_concat_dataset_style.py) | * merge默认情况下做的是inner，内连接，按交集；<br> | [阅读原文] | - |
