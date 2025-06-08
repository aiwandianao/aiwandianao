# -*- coding: utf-8 -*-
import urllib3
from lxml import etree
import html
import re

blogUrl = 'https://blog.csdn.net/aiwandianao?type=blog'

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'} 

def addIntro(f):
	txt = '''  
<p align="center">
  资深Java开发工程师 | 技术博主
</p>
<p align="center">
  专注于后端开发与AI应用领域
</p>
''' 
	f.write(txt)

def addProfessionalAndAcademicInfo(f):
    txt = '''
<p align="center">
  🎓 <b>学历背景</b>: 东南大学 & Monash University | 电子信息硕士
</p>
<p align="center">
  💻 <b>职业经历</b>: 具备扎实的后端开发经验，专注于构建高并发、高可用系统。
  在公司内部及网络上多次进行 AI 编码、AI 提示工程、AI Agent 工作流相关培训，目前主导部门 AI 应用相关工作。
</p>
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
	f.write('\n[查看更多](https://blog.csdn.net/aiwandianao?type=blog)\n')

def addOpenSourceContribution(f):
	txt = '''
### 🔧 开源贡献
#### 1. [agentUniverse](https://github.com/agentuniverse-ai/agentUniverse)
- \**贡献内容\**：
为 doc_processor 模块及相关文件补充方法注释，明确参数说明和功能逻辑。（PR #340）  
- \**技术价值\**：完善基础文档。
	'''
	f.write(txt)

def addOthers(f):
	txt ='''
<div align="center" >

<!-- programming tool icon 编程工具图标 -->
<img src="https://skillicons.dev/icons?i=python,tensorflow,pytorch,openai,langchain,jupyter,docker,git,idea" /><br>

</div>
''' 
	f.write(txt) 


if __name__=='__main__':
	f = open('README.md', 'w+')
	addIntro(f)
	addProfessionalAndAcademicInfo(f)
	addBlogInfo(f)
	addOpenSourceContribution(f)
	addOthers(f)
	f.close 

