from django.core.management import call_command

def my_backup():
    try:
        call_command('dbbackup')
    except Exception as e:
        print(f"Error during database backup: {e}")