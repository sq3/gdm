#! /usr/bin/env python

import sys
import socket
from settings import *
from gapis import *
from commons import *
import syslog

# email_list = [{'src': 'genius@olddomain.com', 'dest': 'genius@newdomain.com'}]
def google_drive_migrate(csv_file, condition_number):
    email_map_list =  get_dict_data_from_csv_file(csv_file)

#########################################################################


if __name__ == "__main__":

    src_csv = sys.argv[1]

    google_drive_migrate(src_csv, condition_number)

class Migrator():

    def __init__(user_data):
        self.user_data = user_data

    def migrate():
        for email in email_map_list:
          num = str_to_num(email['src']) % 10

          src_service = create_drive_service_2_steps(
                  CLIENT_ID_SRC,
                  CLIENT_SECRET_SRC,
                  OAUTH_SCOPE,
                  REDIRECT_URI
                  )

          if src_service:
              syslog.syslog("Processing %s" % (email['src']))
              # rename duplicate files/folders before migrating
              syslog.syslog("Renaming duplicate files and folders of user %s" % (email['src']))
              rename_all_dup_files(src_service)
              syslog.syslog("Finish renaming files and folders of user %s" % (email['src']))

              dest_service = create_drive_service(
                      SERVICE_ACCOUNT_PRIVATE_KEY_DST,
                      SERVICE_ACCOUNT_DST, OAUTH_SCOPE,
                      email['dest']
                      )

              if dest_service:

                  files = get_own_files(src_service)

                  if files:
                      files_map = [{'src': email['src'], 'dest': email['dest'], 'files': files}]

                      # Step 1. share files with new account
                syslog.syslog("Share permissions to destionation account %s" % email['dest'])
                      perms, shared_files = share_files(src_service, files_map)

                syslog.syslog("Share %s files" % len(shared_files))

                      # Step 2. make a copy of shared files in new account
                    syslog.syslog("Make a copy of shared files of user %s" % email['dest'])
                      new_files_map = make_a_copy(dest_service, shared_files)

                      # Step 3. disable sharing on source account
                    syslog.syslog("Disable sharing on source account %s" % email['src'])
                      disable_sharing(src_service, perms)

                      # Step 4. copy permissions
                      if new_files_map:
                        syslog.syslog("Copy permissions of all files of %s" % email['src'])
                          copy_perms(src_service, dest_service, email['src'], email['dest'], new_files_map)
                  else:
                    syslog.syslog("User %s has no file" % email['dest'])
              else:
                syslog.syslog("Canot initiate drive service of user %s. Skipped!" % (email['dest']))
          else:
            syslog.syslog("Skip processing user %s" % (email['src']))
        syslog.syslog("\nFinish migrating user %s\n" % (email['src']))
