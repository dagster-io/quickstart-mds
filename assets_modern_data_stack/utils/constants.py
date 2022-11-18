import os

from dagster_postgres.utils import get_conn_string

from dagster._utils import file_relative_path

# =========================================================================
# To get this value, run `python -m assets_modern_data_stack.setup_airbyte`
# and grab the connection id that it prints at the end
AIRBYTE_CONNECTION_ID = os.environ.get("AIRBYTE_CONNECTION_ID", "your_airbyte_connection_id")
# =========================================================================


PG_SOURCE_CONFIG = {
    "username": os.environ.get("PG_USERNAME", "postgres"),
    "password": os.environ.get("PG_PASSWORD", "password"),
    "host": os.environ.get("PG_HOST", "localhost"),
    "port": os.environ.get("PG_PORT", 5432),
    "database": os.environ.get("PG_SOURCE_DATABASE", "postgres"),
}
PG_DESTINATION_CONFIG = {
    "username": os.environ.get("PG_USERNAME", "postgres"),
    "password": os.environ.get("PG_PASSWORD", "password"),
    "host": os.environ.get("PG_HOST", "localhost"),
    "port": os.environ.get("PG_PORT", 5432),
    "database": os.environ.get("PG_DESTINATION_DATABASE", "postgres_replica"),
}

AIRBYTE_CONFIG = {
    "host": os.environ.get("AIRBYTE_HOST", "localhost"),
    "port": os.environ.get("AIRBYTE_PORT", "8000"),
}

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt_project")
DBT_PROFILES_DIR = file_relative_path(__file__, "../../dbt_project/config")
DBT_CONFIG = {"project_dir": DBT_PROJECT_DIR, "profiles_dir": DBT_PROFILES_DIR}

POSTGRES_CONFIG = {
    "con_string": get_conn_string(
        username=PG_DESTINATION_CONFIG["username"],
        password=PG_DESTINATION_CONFIG["password"],
        hostname=PG_DESTINATION_CONFIG["host"],
        port=str(PG_DESTINATION_CONFIG["port"]),
        db_name=PG_DESTINATION_CONFIG["database"],
    )
}
