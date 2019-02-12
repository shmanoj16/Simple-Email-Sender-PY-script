#!C:/Users/support/AppData/Local/Programs/Python/Python37-32/python.exe
print("Content-Type: text/html\n")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import cgi



#getting form datas

form = cgi.FieldStorage()
sel_dept_for_new_tic =  form.getvalue('sel_dept_for_new_tic')
location =  form.getvalue('location')
type_sel =  form.getvalue('type_sel')
cat_sel =  form.getvalue('cat_sel')
pri_sel =  form.getvalue('pri_sel')
project =  form.getvalue('project')
nomini =  form.getvalue('nomini')
desc =  form.getvalue('desc')
tic_id =  form.getvalue('tic_id')
us =  form.getvalue('us')
dt =  form.getvalue('dt')
non_arr = nomini.split('-')

def py_mail(SUBJECT, BODY, TO, FROM):
    """With this function we send out our html email"""

    # Create message container - the correct MIME type is multipart/alternative here!
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = "ID38751 : IT Helpdesk Service Request "
    MESSAGE['To'] = "manoj.sh@prodapt.com"
    MESSAGE['From'] = "iprodapt@gmail.com"
    MESSAGE.preamble = """
Your mail reader does not support the report format.
Please visit us <a href="http://www.prodapt.com">online</a>!"""

    # Record the MIME type text/html.
    HTML_BODY = MIMEText(BODY, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    MESSAGE.attach(HTML_BODY)

    # The actual sending of the e-mail
    server = smtplib.SMTP('smtp.gmail.com:587')

    # Print debugging output when testing
    if __name__ == "__main__":
        server.set_debuglevel(1)

    # Credentials (if needed) for sending the mail
    password = "Hellowor!d"

    server.starttls()
    server.login(FROM,password)
    server.sendmail(FROM, [TO], MESSAGE.as_string())
    server.quit()

if __name__ == "__main__":
    """Executes if the script is run as main script (for testing purposes)"""

    email_content = """
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">

  </style>
</head>
<body>
  <tr>
<td valign="top">Dear """+str(non_arr)+""",<br>
<br>
IT Ticket – """+str(tic_id)+"""   has been Submited By """+str(us)+"""<br>
<br>
<table width="800" cellpadding="0" cellspacing="0" style="border:1px solid #cccccc; font-family:Arial,sans-serif; font-size:11px; margin-bottom:8px">
<tbody>
<tr>
<td valign="top" width="300" style="border:0px; border-right:1px solid #cccccc; background:#dceff8">
<table align="center" cellpadding="0" cellspacing="0" width="280">
<tbody>
<tr>
<td colspan="2" valign="middle" height="25" style="font-weight:bold; color:#4982b3">
<span style="font-family:Arial,sans-serif; font-size:12px">Ticket Details</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Ticket ID</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(tic_id)+"""</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Status</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">NEW</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Location</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(location)+"""</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Type</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(type_sel)+"""</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Priority</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(pri_sel)+"""</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Category</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(cat_sel)+"""</span></td>
</tr>

<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Project</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(project)+"""</span></td>
</tr>

<tr>
<td colspan="2" valign="middle" height="25" style="font-weight:bold; color:#4982b3">
<span style="font-family:Arial,sans-serif; font-size:12px">Requestor Details</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Requested by</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(us)+"""h&nbsp;&nbsp;|&nbsp;&nbsp;2628</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px"></span></td>
<td valign="mi
ddle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">"""+str(tic_id)+"""</span></td>
</tr>
</tbody>
</table>
</td>
<td valign="top" width="500" style="border:0px; background:#ffffff">


</td>
</tr>
</tbody>
</table>
<table width="800" cellpadding="0" cellspacing="0" style="border:1px solid #cccccc; font-family:Arial,sans-serif; font-size:11px; margin-bottom:8px">
<tbody>
<tr>
<td valign="top" width="300" style="border:0px; border-right:1px solid #cccccc; background:#dceff8">
<span style="font-family:Arial,sans-serif; font-size:12px"></span>
<table align="center" cellpadding="0" cellspacing="0" width="280">
<tbody>
<tr>
<td colspan="2" valign="middle" height="25" style="font-weight:bold; color:#4982b3">
<span style="font-family:Arial,sans-serif; font-size:12px">SLA Details</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Identified On</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">2019-01-17 12:34:32</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Approved On</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">2019-01-23 06:38:08</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Response Due</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">2019-01-23 10:00:00</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Actual Response</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">2019-01-23 07:17:49</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Completion Due</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">---</span></td>
</tr>
<tr>
<td valign="middle" width="120" height="22" style=""><span style="font-family:Arial,sans-serif; font-size:12px">Actual Completion</span></td>
<td valign="middle" width="180" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px">---</span></td>
</tr>
</tbody>
</table>
</td>
<td valign="top" width="500" style="border:0px; background:#ffffff">
<table align="center" cellpadding="0" cellspacing="0" width="480" style="margin-bottom:10px">
<tbody>
<tr>
<td valign="middle" height="25" style="font-weight:bold; color:#4982b3; word-break:break-all">
<span style="font-family:Arial,sans-serif; font-size:12px">Resolution</span></td>
</tr>
<tr>
<td valign="middle" width="480" style="font-weight:bold"><span style="font-family:Arial,sans-serif; font-size:12px"></span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<table cellpadding="0" cellspacing="0" style="border:0px; background-color:#fff; font-family:Tahoma,Geneva,sans-serif; font-size:12px; width:800px; vertical-align:top">
<tbody>
<tr>
<td style="height:20px; border:0px"><br>
<table width="800" cellpadding="0" cellspacing="0">
<tbody>
<tr>

</tr>
</tbody>
</table>
<br>
</td>
</tr>
</tbody>
</table>
</td>
</tr>
</body>
"""

    TO = 'manoj.sh@domain.com'
    FROM ='test@gmail.com'

    py_mail("Test email subject", email_content, TO, FROM)
print('-----')
