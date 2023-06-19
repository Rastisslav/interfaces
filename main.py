from modules.extract_json import extract_json, get_list_of_interfaces
from modules.managing_db import create_db_and_table, add_to_table, quit_db, show_history

if __name__ == "__main__":
    extract_json()
    create_db_and_table()
    add_to_table(get_list_of_interfaces())
    quit_db