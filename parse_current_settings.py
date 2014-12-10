#!/usr/bin/python
import re
import sys
import os


def main(argv):
    config_name = argv[1]
    app_name = argv[2]

    current_dir = os.path.dirname(argv[0])
    pg_vars_file = os.path.join(current_dir, "includes", "pg_vars.yaml")

    root_dir = os.path.abspath(os.path.join(
        current_dir,
        os.pardir,
    ))

    config_file = os.path.abspath(os.path.join(
        root_dir,
        app_name,
        'settings',
        '%s.py' % config_name
    ))

    fh = open(config_file, 'r')
    lines = fh.read()

    pg_engine = re.search("'ENGINE'*\s*:\s*'([a-zA-Z._0-9]+)'\s*", lines)
    pg_engine = "" if pg_engine is None else pg_engine.group(1)
    print "Engine: %s" % pg_engine
    if pg_engine == "django.db.backends.postgresql_psycopg2":
        pg_host = re.search("'HOST'*\s*:\s*'([a-zA-Z0-9]+)'\s*", lines)
        pg_user = re.search("'USER'*\s*:\s*'([a-zA-Z0-9]+)'\s*", lines)
        pg_db = re.search("'NAME'*\s*:\s*'([a-zA-Z0-9]+)'\s*", lines)
        pg_passwd = re.search("'PASSWORD'*\s*:\s*'([a-zA-Z0-9]+)'\s*", lines)

        pg_host = "" if pg_host is None else pg_host.group(1)
        pg_user = "" if pg_user is None else pg_user.group(1)
        pg_db = "" if pg_db is None else pg_db.group(1)
        pg_passwd = "" if pg_passwd is None else pg_passwd.group(1)
    else:
        pg_host = ""
        pg_user = ""
        pg_db = ""
        pg_passwd = ""

    with open(pg_vars_file, 'w') as v_file:
        v_file.write("---\n")
        v_file.write("pg_host: \"%s\"\n" % pg_host)
        v_file.write("pg_user: \"%s\"\n" % pg_user)
        v_file.write("pg_db: \"%s\"\n" % pg_db)
        v_file.write("pg_passwd: \"%s\"\n" % pg_passwd)


if __name__ == "__main__":
   main(sys.argv)