from Menu import Menu
from Option import Option
"""
This little file just has the menus declared.  Each variable (e.g. menu_main) has 
its own set of options and actions.  Although, you'll see that the "action" could
be something other than an operation to perform.

Doing the menu declarations here seemed like a cleaner way to define them.  When
this is imported in main.py, these assignment statements are executed and the 
variables are constructed.  To be honest, I'm not sure whether these are global
variables or not in Python.
"""

# The main options for operating on Departments and Courses.
menu_main = Menu('main', 'Please select one of the following options:', [
    Option("Add", "add(sess)"),
    Option("Report Data", "report_data(sess)"),
    Option("Required Reports", "reports(sess)"),
    Option("Delete", "delete(sess)"),
    Option("Update", "update(sess)"),
    Option("Commit", "sess.commit()"),
    Option("Rollback", "session_rollback(sess)"),
    Option("Exit this application", "pass")
])

add_menu = Menu('add', 'Please indicate what you want to add:', [
    Option("Piece Part", "add_piece_part(sess)"),
    Option("Assembly", "add_assembly(sess)"),
    Option("Assembly Part (AKA Usage)", "add_assembly_part(sess)"),
    Option("Vendor", "add_vendor(sess)"),
    Option("Exit", "pass")
])

report_data_menu = Menu('report data', 'Please indicate what kind of data you want to report:', [
    Option("Part", "report_data_part(sess)"),
    Option("Assembly Part (AKA Usage)", "report_data_assembly_part(sess)"),
    Option("Vendor", "report_data_vendor(sess)"),
    Option("Exit", "pass")
])

report_menu = Menu('reports', 'Please select a report:', [
    Option("Hierarchy Report", "hierarchy_report(sess)"),
    Option("Assemblies With Greatest Number of Components", "max_component_report(sess)"),
    Option("Exit", "pass")
])

delete_menu = Menu('delete', 'Please indicate what you want to delete:', [
    Option("Part", "delete_part(sess)"),
    Option("Assembly Part (AKA Usage)", "delete_assembly_part(sess)"),
    Option("Vendor", "delete_vendor(sess)"),
    Option("Exit", "pass")
])

update_menu = Menu('update', 'Please indicate what kind of data you want to update: ', [
    Option("Part", "update_part(sess)"),
    Option("Assembly Part (AKA Usage)", "update_assembly_part(sess)"),
    Option("Vendor", "update_vendor(sess)"),
    Option("Exit", "pass")
])

# A menu to prompt for the amount of logging information to go to the console.
debug_select = Menu('debug select', 'Please select a debug level:', [
    Option("Informational", "logging.INFO"),
    Option("Debug", "logging.DEBUG"),
    Option("Error", "logging.ERROR")
])
