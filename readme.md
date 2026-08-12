这是一个基于 LangGraph 的金融分析 Agent 系统，用于分析 A 股股票。参考了 GitHub 上的开源项目[ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)

系统包含五个 Agent：基本面分析 Agent、技术分析Agent、估值分析 Agent、新闻分析 Agent 和总结 Agent。前四个 Agent 通过 MCP 工具获取 A 股相关数据并与大语言模型（LLM）交互；总结 Agent 综合上游数据，提供最终投资建议。

![alt text](img/系统架构.png)

## 项目运行
1. 安装依赖
```bash
export PYTHONPATH=./                   #把当前目录加入 Python 的包搜索路径
pip install -r requirements.txt
```
2. 设置API
项目支持两种模式：API 调用大模型和本地FinR1模型。
目前只有Summary Agent可以使用本地 FinR1，其余4个Agent仍然依赖API调用大模型，所以无论哪种模式，都必须配置 API_KEY。

USE_LOCAL_MODEL=api表示使用api调用大模型，如果想使用FinR1，请设置为USE_LOCAL_MODEL=local，并自行下载https://huggingface.co/SUFE-AIFLM-Lab/Fin-R1模型（大小为7B）。