# Filename : backup_ver3.py

import os
import time

# 1. The files and directories to be backed up are
# specified in a list.
source = ['/Users/garethryle/Documents/Testfolder']
# Remember to change this to which folder you will be using

# 2. The backup must be stored in a
# main backup directory
target_dir = '/Users/garethryle/Documents/backup'

# Create target directory if it is not present
if not os.path.exists(target_dir):
    os.mkdir(target_dir) # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.
today = target_dir + os.sep + time.strftime('%y%m%d')
# The current time is the name of the zip archive.
now = time.strftime('%H%M%S')

# Take a commend from the user to
# create the name of the zip file
comment = input('Enter a comment -->')
# Check if a comment was entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    comment.replace(' ', '_') + '.zip'

# Create the subdirectory if it isn't already there
if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# run the backup
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
