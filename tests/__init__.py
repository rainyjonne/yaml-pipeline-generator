from yaml_pipeline_generator.db.sql_db_handler import sql_db 
from yaml_pipeline_generator.task_bypass.tasktypes.transform import *
from yaml_pipeline_generator.task_bypass.tasktypes.merge import *


def configure():
    # Create your db connection.
    db = sql_db(f'yaml_pipeline_generator/db/outputs/test.db')
    # Drop tables inside test db
    db.dropAllTables()
    table_structure = """
            'level' TEXT NOT NULL,
            'stage_name' TEXT NOT NULL,
            'task_name' TEXT NOT NULL,
            'date_time' TEXT NOT NULL,
            'error_message' TEXT,
            'other_info' TEXT
            """

    # Create logging table
    db.createTable('_log', table_structure)
    return db


DB = configure() 
