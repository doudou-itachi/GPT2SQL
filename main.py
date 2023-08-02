import os

from database.connect_database import DataBaseConnect
from openaichat.generate_model import LLMInterface
from parameters.argparse import get_argparse


def main():
    arg = get_argparse()
    os.environ['http_proxy'] = arg.http_proxy
    os.environ['https_proxy'] = arg.https_proxy
    while True:
        prompt = input("prompt:")
        if prompt.lower() == "exit" or not prompt:
            break
        llm = LLMInterface(api_keys=arg.api_keys, model_name=arg.model_name,
                           temperature=arg.temperature).create_llm_instance

        output = DataBaseConnect(database_name=arg.database_name, database_type=arg.database_type, name=arg.name,
                                 password=arg.password, ipaddr=arg.ipaddr).get_result(prompt=prompt, llm=llm)


if __name__ == '__main__':
    main()
