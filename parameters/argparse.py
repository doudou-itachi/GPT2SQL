import argparse


def get_argparse():
    parser = argparse.ArgumentParser(description='get argparse')
    parser.add_argument('--api_keys', nargs='+', type=str, required=True,
                        help='api_key')

    parser.add_argument('--model_name', type=str, required=False, default="gpt-3.5-turbo-16k",
                        help='model_name')

    parser.add_argument('--temperature', type=int, required=False, default=0,
                        help='temperature')

    parser.add_argument('--database_name', type=str, required=True,
                        help='database_name')

    parser.add_argument('--database_type', type=str, required=False, default="mysql",
                        help='database_type')

    parser.add_argument('--name', type=str, required=False, default="root",
                        help='name')

    parser.add_argument('--password', type=str, required=False, default="123456",
                        help='password')

    parser.add_argument('--ipaddr', type=str, required=False, default="127.0.0.1",
                        help='ipaddr')

    parser.add_argument('--http_proxy', type=str, required=False, default="127.0.0.1:7890",
                        help='http_proxy')

    parser.add_argument('--https_proxy', type=str, required=False, default="127.0.0.1:7890",
                        help='https_proxy')

    args = parser.parse_args()

    return args
