#generate report for MSSQL_IFP
import os
from jinja2 import Template



#open template j2 file
with open('ifp\\ifp_report.html.jinja2') as file:
    template = Template(file.read())

output_html = template.render(
    BUILD_NEMBER_VAR=os.getenv('BUILD_NUMBER'),
    STATUS_VAR=os.getenv('STATUS'),
    START_JOB_VAR=os.getenv('STARTJOB'),
    END_JOB_VAR=os.getenv('ENDJOB'),
    CHECK_FILE_END_VAR=os.getenv('CHECK_FILE_END'),
    COPY_FILE_END_VAR=os.getenv('COPY_FILE_END'),
    IFP_PROCESS_END_VAR=os.getenv('IFP_PROCESS_END'),
)

out_report = open('ifp_report.html', 'w')
out_report.write(output_html)
out_report.close()
print (os.getenv('CHECK_FILE_END'))