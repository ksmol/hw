list_of_all_sql_files = [files for files in
                         os.listdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Migrations')) if
                         '.sql' in files]