# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://blog.csdn.net/aiwandianao?type=blog'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''  
   <div align="center">
    <a href="https://blog.csdn.net/aiwandianao?type=blog">
      <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=435&lines=你好&center=true&size=27" alt="Typing SVG" />
    </a>
  </div>

  <img src="https://cdn.jsdelivr.net/gh/aiwandianao/aiwandianao/assets/images/coding.gif" /><br>

  <div align="center">
    <img src="https://komarev.com/ghpvc/?username=aiwandianao&label=Views&color=0e75b6&style=flat" alt="访问量统计" />
  </div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/aiwandianao/aiwandianao/tree/outputs/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://cdn.jsdelivr.net/gh/aiwandianao/aiwandianao/tree/outputs/github-contribution-grid-snake.svg" />
  <img alt="github-snake" src="https://cdn.jsdelivr.net/gh/aiwandianao/aiwandianao/tree/outputs/github-contribution-grid-snake-dark.svg" />
</picture>

</div>

<p align="center"> 5+年技术博主，CSDN笔耕不辍、云计算初级工程师…… </p>  
<p align="center"> Java开发，也掌握Python相关技术栈  </p>  
<p align="center"> 擅长Java、Lniux、Redis，对操作系统、网络......也有涉猎</p>  
<table align="center">
<td valign="top" width="33%">

### 工作经验  

<img align="right" width="88" src="https://cdn.jsdelivr.net/gh/aiwandianao/aiwandianao/assets/images/tuniu.png" />

- [途牛旅游网](https://www.tuniu.com/) &emsp; 📌 2023-07 —— 2023-09
  - 工作岗位：软件开发工程师（实习）

</td>


<td valign="top" width="33%">


### 开源项目  
- [my_github_profile](https://github.com/aiwandianao/aiwandianao)我github首页	
  

[查看更多](https://github.com/aiwandianao/)	 

</td>

''' 
	f.write(txt)

def addProjectInfo(f):
	txt ='''
### 开源项目  
- [my_github_profile](https://github.com/aiwandianao/aiwandianao)我github首页	
   
[查看更多](https://github.com/aiwandianao/)	 

	''' 
	f.write(txt) 

def addOthers(f):
	txt ='''
</td>
<td valign="top" width="33%">




</table>

<img width="200%" src="https://cdn.jsdelivr.net/gh/aiwandianao/aiwandianao/assets/images/hr.gif" />

<div align="center" >

```mermaid
mindmap
  root((60分))
    编程
      Java开发
      人工智能
    旅行
      北京
      莫斯科
      徐州
      南京
      苏州
      乌鲁木齐
      杭州
      上海
      丽水
      温州
      洛阳
      郑州    
    阅读
      计算机技术
      人物传记
      个人成长
      社会文化
      玄幻修真
      
```



<!-- programming tool icon 编程工具图标 -->
<img src="https://skillicons.dev/icons?i=idea,git,postman,maven,spring,redis,rabbitmq,mysql,mongodb,nginx,tensorflow,pytorch,python,matlab,cpp" /><br>



<!-- GitHub 数据统计 -->
<img align="" height="137px" src="https://github-readme-stats-git-masterrstaa-rickstaa.vercel.app/api?username=aiwandianao&hide_title=true&hide_border=true&show_icons=true&include_all_commits=true&line_height=21text_color=000&icon_color=000&bg_color=0,ea6161,ffc64d,fffc4d,52fa5a&theme=graywhite" />
<br>







<img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=aiwandianao&theme=dark&hide_border=true" />

	''' 
	f.write(txt) 


def addBlogInfo(f):  
	http = urllib3.PoolManager(num_pools=5, headers = headers)
	resp = http.request('GET', blogUrl)
	resp_tree = etree.HTML(resp.data.decode("utf-8"))
	# html_data = resp_tree.xpath(".//div[@class='article-item-box csdn-tracking-statistics']/h4") 
	html_data = resp_tree.xpath(".//article[@class='blog-list-box']")

 
	f.write("\n### 我的博客\n")
	cnt = 0
	for i in html_data: 
		if cnt >= 5:
			break
		# title = i.xpath('./a/text()')[1].strip()
		title = i.xpath("./a//h4/text()")[0].strip()
		url = i.xpath('./a/@href')[0] 
		item = '- [%s](%s)\n' % (title, url)
		f.write(item)
		cnt = cnt + 1
	f.write('\n[查看更多](https://aiwandianao.blog.csdn.net/)\n')


if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	f.write('<td valign="top" width="33%">\n')
	addBlogInfo(f)
	f.write('</table>\n')
	addOthers(f)
	f.close 

