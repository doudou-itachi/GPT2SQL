使用[langchain](https://github.com/langchain-ai/langchain) 和[OPENAI]([OpenAI](https://openai.com/)) ChatGPT实现了一个连接本地数据库做sql生成的demo

**前提**

确保你能访问chatgpt并且有可用的openai_api_key

**使用**

```shell
cd GPT2SQL
pip install -r requirements.txt
python main.py --api_keys
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
sk-UzT0rlqUgFqvSgmVdGskT3BlbkFcJaSPigmqXeNGPAaxvcqE
--database_name
xxxx
--password
xxxx
--ipaddr
xxx.xxx.x.x
```

##### 参数说明

```shell
api_keys:必填 允许多个
model_name:调用openai的模型名称,默认使用gpt-3.5-turbo-16k
temperature:温度 默认为0
database_name:必填 连接的数据库名称
database_type:数据库类型(PostgreSQL mysql SQLite....)默认 mysql
name:连接数据库的用户名 默认root
password:连接数据库的密码 默认123456
ipaddr:连接数据的地址 默认127.0.0.1
http_proxy:配置代理 默认 127.0.0.1:7890
https_proxy:配置代理 默认 127.0.0.1:7890

```



