# collins_dict
Collins Dictionary in Terminal (Containing both Chinese and English explanation)  
终端下的柯林斯词典（包含中英双解）  

## Statement
It is just a web scraper, and the information is scraped from iciba.com.  
The reason to choose Collins Dictionary is that Collins Dictionary contains both Chinese and English exlanation and the English explanation is very easy to understand. Furthermore, it includes some good example sentences.  
The reason to write this script is that I often work in CLI mode or GUI mode with IDEs containing a Terminal tab. It's more convient to use the dictionary in your work window than to frequently switch windows to a browser or client.  
  
这只是一个网页爬虫而已，数据爬取自金山词霸的网站。  
之所以选择柯林斯，主要是因为柯林斯对单词的解释比较全面，既有中文释义，又有英文释义，而且英文释义还非常生动易懂。此外还有一些很好的例句。  
之所以写这个脚本，主要是因为我经常在纯文本模式下工作，或者使用的IDE有终端标签页。使用命令行下的词典，总比频繁地切窗口到浏览器或客户端方便。  

## How to Use
Please install Python3 first. If /usr/bin/python doesn't point to python3, you can switch the interpreter in the file dict by yourself. change "#！/usr/bin/python" to the path of the interpreter you want to use.  
  
After that, Add the directory containing the two files (dict and collins_scrap.py) to your Environment variable PATH.  
Edit ~/.bashrc file and add export PATH in the file then "source ~/.bashrc".  
  
The script has just one parameter, such as "dict word". If you want to search a phrase such as "pick up", just type "dict pick up".  
  
请先安装Python3。如果/usr/bin/python不是指向python3的，你可以在dict文件中自行切换解释器。修改"#!/usr/bin/python"到你想使用的解释器的路径便可。  
  
之后，将那两个文件（dict与collins_scrap.py）所在的目录添加到你的PATH环境变量中。  
编辑~/.bashrc文件，并将export PATH添加进去，然后执行“source ~/.bashrc”便可。  
  
本脚本只接受一个参数，例如“dict word”。如果你想查询一个短语，例如“pick up”，直接输入“dict pick up”就可以了。  
