import smtplib
import smtplib
import ssl
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "spycropalerts@gmail.com"
receiver_email = 'value1'
password = "7ULJS7jp@17012004"

message = MIMEMultipart("alternative")
message["Subject"] = "Wear The Mask"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
            Please Up Your Mask while in Campus!"""
html = """\
            <!DOCTYPE html><html xmlns:v='urn:schemas-microsoft-com:vml' xmlns:o='urn:schemas-microsoft-com:office:office' lang='en'> <head> <title></title> <meta http-equiv='Content-Type' content='text/html; charset=utf-8'/> <meta name='viewport' content='width=device-width,initial-scale=1'/> <style>*{box-sizing: border-box;}body{margin: 0; padding: 0;}a[x-apple-data-detectors]{color: inherit !important; text-decoration: inherit !important;}#MessageViewBody a{color: inherit; text-decoration: none;}p{line-height: inherit;}@media (max-width: 520px){.icons-inner{text-align: center;}.icons-inner td{margin: 0 auto;}.row-content{width: 100% !important;}.column .border{display: none;}table{table-layout: fixed !important;}.stack .column{width: 100%; display: block;}}</style> </head> <body style='background-color: #fff; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;'> <table class='nl-container' width='100%' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0; background-color: #fff;'> <tbody> <tr> <td> <table class='row row-1' align='center' width='100%' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0;'> <tbody> <tr> <td> <table class='row-content stack' align='center' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0; color: #000; width: 500px;' width='500'> <tbody> <tr> <td class='column column-1' width='100%' style=' mso-table-lspace: 0; mso-table-rspace: 0; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0; border-right: 0; border-bottom: 0; border-left: 0; ' > <table class='image_block' width='100%' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0;'> <tr> <td style='width: 100%; padding-right: 0; padding-left: 0;'> <div align='center' style='line-height: 10px;'> <img src='https://d15k2d11r6t6rl.cloudfront.net/public/users/BeeFree/beefree-a8tlu86f8au/logo_black_trans.png' style='display: block; height: auto; border: 0; width: 225px; max-width: 100%;' width='225'/> </div></td></tr></table> <table class='heading_block' width='100%' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0;'> <tr> <td style='text-align: center; width: 100%;'> <h1 style=' margin: 0; color: #555; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 23px; font-weight: 700; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0; ' > PLEASE PUT ON YOUR MASK </h1> </td></tr></table> <table class='paragraph_block' width='100%' border='0' cellpadding='10' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0; word-break: break-word;'> <tr> <td> <div style=' color: red; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 14px; font-weight: 400; letter-spacing: 0; line-height: 120%; text-align: left; ' > <p style='margin: 0;'> Remember that the pandemic will not persist indefinitely. However, until then, continue to use masks as a critical precaution to minimise transmission and preserve lives. Please Up your mask and stand with the mask movement - Team SpyCrop </p></div></td></tr></table> </td></tr></tbody> </table> </td></tr></tbody> </table> <table class='row row-2' align='center' width='100%' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0;'> <tbody> <tr> <td> <table class='row-content stack' align='center' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0; color: #000; width: 500px;' width='500'> <tbody> <tr> <td class='column column-1' width='100%' style=' mso-table-lspace: 0; mso-table-rspace: 0; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0; border-right: 0; border-bottom: 0; border-left: 0; ' > <table class='icons_block' width='100%' border='0' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0;'> <tr> <td style='vertical-align: middle; color: #9d9d9d; font-family: inherit; font-size: 15px; padding-bottom: 5px; padding-top: 5px; text-align: center;'> <table width='100%' cellpadding='0' cellspacing='0' role='presentation' style='mso-table-lspace: 0; mso-table-rspace: 0;'> <tr> <td style='vertical-align: middle; text-align: center;'> <table class='icons-inner' style='mso-table-lspace: 0; mso-table-rspace: 0; display: inline-block; margin-right: -4px; padding-left: 0; padding-right: 0;' cellpadding='0' cellspacing='0' role='presentation' > </td></tr></table> </td></tr></table> </td></tr></table> </td></tr></tbody> </table> </td></tr></tbody> </table> </td></tr></tbody> </table> </body></html>
            """

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
