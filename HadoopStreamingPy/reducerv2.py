# -*- coding: utf-8 -*-

import sys

desc_list = []
job_desc_dict = {
    "title": '',
    "desc_list": desc_list
}

for line in sys.stdin:
    job, descorid = line.split('\t', 1)
    if job_desc_dict["title"] == job:
        desc_list.append(descorid)
    else:
        jobid = None
        if desc_list:
            for index, desc in enumerate(desc_list):
                if desc[0] == '!':
                    jobid = desc
                    del desc_list[index]
            if jobid:
                if len(desc_list) <= 3:
                    for desc in desc_list:
                        print "%s\t%s" % (jobid[1:], desc)
                else:
                    for x in range(3):
                        print "%s\t%s" % (jobid[1:], desc_list[x])
        job_desc_dict["title"] = job
        desc_list = []
        desc_list.append(descorid)

# get the last output
jobid = None
if desc_list:
    for index, desc in enumerate(desc_list):
        if desc[0] == '!':
            jobid = desc
            del desc_list[index]
    if jobid:
        if len(desc_list) <= 3:
            for desc in desc_list:
                print "%s\t%s" % (jobid[1:], desc)
        else:
            for x in range(3):
                print "%s\t%s" % (jobid[1:], desc_list[x])
