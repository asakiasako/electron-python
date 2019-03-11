from paths import get_sub_dir

LOG_FILE_PATH = get_sub_dir('Logs')

LOG_FILE_BACKUP_COUNT = 30  # New log file is generated every day at midnight and old ones are backup. The oldest file will be removed if file count exceeds.
