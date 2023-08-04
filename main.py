import logging
import os
import sys

from langchain import SQLDatabase, OpenAI
from langchain.agents import create_sql_agent, AgentType
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

from database.connect_database import DataBaseConnect
from openaichat.generate_model import LLMInterface
from parameters.argparse import get_argparse


def get_logger(name: str) -> logging.Logger:
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S"
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger


logger = get_logger(__name__)


def main():
    arg = get_argparse()
    os.environ['http_proxy'] = arg.http_proxy
    os.environ['https_proxy'] = arg.https_proxy
    if not arg.use_other:
        while True:
            prompt = input("prompt:")
            if prompt.lower() == "exit" or not prompt:
                break
            llm = LLMInterface(api_keys=arg.api_keys, model_name=arg.model_name,
                               temperature=arg.temperature).create_llm_instance

            output = DataBaseConnect(database_name=arg.database_name, database_type=arg.database_type, name=arg.name,
                                     password=arg.password, ipaddr=arg.ipaddr).get_result(prompt=prompt, llm=llm)

    # 该代理基于
    # SQLDatabaseChain
    # 构建，旨在回答有关数据库的更多常见问题，以及从错误中恢复。
    #
    # 请注意，由于此代理处于积极开发阶段，因此所有答案可能都不正确。此外，对于某些问题，不能保证代理不会对您的数据库执行
    # DML
    # 语句。小心在敏感数据上运行它！
    else:
        while True:
            prompt = input("prompt:")
            if prompt.lower() == "exit" or not prompt:
                break
            llm = LLMInterface(api_keys=arg.api_keys, model_name=arg.model_name,
                               temperature=arg.temperature).create_llm_instance

            db = DataBaseConnect(database_name=arg.database_name, database_type=arg.database_type, name=arg.name,
                                 password=arg.password, ipaddr=arg.ipaddr).get_connect

            toolkit = SQLDatabaseToolkit(db=db, llm=llm)

            agent_executor = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                verbose=True,
                agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
            )
            # 设为True 获取中间步骤生成的SQL语句
            agent_executor.return_intermediate_steps = True
            output = agent_executor(prompt)
            # GET SQL
            logger.info(output['intermediate_steps'][-1][0].tool_input)


if __name__ == '__main__':
    main()
