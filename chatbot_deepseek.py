# 任务二：DeepSeek Chatbot 运行说明
## 一、核心信息
- 功能：调用DeepSeek R1模型实现交互式文本对话，流程为「输入问题→调用模型→返回回复」
- 调用平台：火山引擎（火山方舟）
- 调用方式：OpenAI兼容API
- 编程语言：Python 3.8+

## 二、运行前置条件
1. 安装Python 3.8及以上版本；
2. 拥有火山引擎方舟平台的API Key（已开通DeepSeek R1模型服务）；
3. 网络通畅（无需科学上网，关闭VPN）。

## 三、依赖安装步骤
1. 打开终端，进入本文件夹（hw02）：
   - Windows：`cd C:\Users\你的用户名\Desktop\hw02`
   - Mac/Linux：`cd /Users/你的用户名/Desktop/hw02`
2. 执行安装命令：`pip install -r requirements.txt`
3. 若提示“pip不是内部命令”，替换为：`python -m pip install -r requirements.txt`

## 四、API Key配置
1. 打开`.env`文件；
2. 将`VOLCENGINE_API_KEY`的值替换为自己的火山引擎API Key；
3. 保存文件（请勿泄露API Key，提交GitHub时可脱敏为`sk-xxxx`）。

## 五、启动Chatbot
终端执行命令：`python chatbot_deepseek.py`

## 六、使用方法
1. 启动后输入任意文本问题（如“什么是医学图像分割？”）；
2. 按回车键获取模型回复；
3. 输入`q`、`quit`或`退出`，结束程序。

## 七、示例输入/输出
