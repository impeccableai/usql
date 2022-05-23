#!/usr/bin/env python3
import os
import sys


def main():
    args = sys.argv
    args[0] = "/usql"

    dsn = create_dsn()
    if dsn is not None:
        args = [args[0], dsn] + args[1:]

    os.execve(args[0], args, os.environ.copy())


def create_dsn():
    driver = os.environ.get("DRIVER")
    path = os.environ.get("DSN_PATH")
    if driver is not None:
        if path is not None:
            return f'{driver}:/{path}'
        user = os.environ.get("USER")
        password = os.environ.get("PASSWORD")
        host = os.environ.get("HOST")
        dbname = os.environ.get("DBNAME")
        transport = os.environ.get("TRANSPORT")
        options = os.environ.get("OPTIONS")

        dt = driver if transport is None else f'{driver}+{transport}'
        login = user if password is None else f'{user}:{password}'
        o = f'?{options}' if options is not None else ''

        return f'{dt}://{login}@{host}/{dbname}{o}'

    if path is not None:
        return path

    return None


if __name__ == "__main__":
    main()
