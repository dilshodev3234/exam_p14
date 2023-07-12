# import requests
# import os
# from multiprocessing import Pool
#
#
# def download_image(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         filename = url.split('/')[-1]
#         with open("images.png", 'wb') as file:
#             file.write(response.content)
#             print(f"Downloaded {filename}")
#
#
# if __name__ == '__main__':
#     image_urls = [
#         'https://us.123rf.com/450wm/santiaga22/santiaga222112/santiaga22211200200/179912563-man-hikes-mountains-with-travel-backpack-wandering-lifestyle-adventure-concept-autumn-vacation.jpg?ver=6',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcS6k9RY3Lo5uQk3Fh8b8_JEGXE_Ir6zCayqQLJ7vnVtmQoGedmo_ppRrLedvFiBp-sFCMg&usqp=CAU',
#         'https://media.istockphoto.com/id/618060058/photo/dzhuma-mosque-in-tashkent-uzbekistan.jpg?s=612x612&w=0&k=20&c=5G_H4dlQv-NJRAEQkm3MrNHa3771t-Jbnh8ngKXXF_Q=',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcRZZcQqcBc_n2e9mN_yKj_SVie5BJ2XeHxN_ViO93FY6B_Ww9s_faILWFw9-_SfX9c5jAM&usqp=CAU',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcQ-dLkG1h5RI7nuqGFllw-aw5Br3qsTpz7J5gf2YgcK8ILIugtkH7762QWAPSeetF3DyL4&usqp=CAU',
#         'https://media.istockphoto.com/id/1034587098/photo/tashkent-tv-tower-aerial-shot-during-sunset-in-uzbekistan.jpg?s=612x612&w=0&k=20&c=vos2bfAhLB8HuKgh91KnMkllxkZC6RYoXNt-F8Tz6Os=',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcQmttfF6jNR2phUQlq_t0-lbABzWs0twMVWEMzMdEusdCj7c_7F0qA8ALRiTbvGMzHLBOw&usqp=CAU',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcRU28gkuEbkv72fw46OT65N1BPaDEHRRG5d0qMx40D2hZXyZCytpc9U5EU7mlZZ4cSy3QU&usqp=CAU',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcQb2vLWISECiWGTjuuOPOGmvbC89t03pqtt4Iy3KGxrrFo3Pba5HNxFfPoEaz8tP1BOKp4&usqp=CAU',
#         'https://encrypted-tbn0.gstatic.com/filename?q=tbn:ANd9GcSdBMcoGO4Ug_RwJHjPWw95qP5cbXY4bI7iPTW6-Mu-4oiLlD_tfCMEfWAG_4GycDr2I6w&usqp=CAU'
#     ]
#
#     pool = Pool()
#
#     pool.map(download_image, image_urls)
#
#     pool.close()
#     pool.join()
#
#     destination_directory = 'filename'
#     os.makedirs(destination_directory, exist_ok=True)
#     for filename in os.listdir('.'):
#         if filename.endswith('.jpg'):
#             os.rename(filename, os.path.join(destination_directory, filename))
#
#
# import httpx
# response = httpx.get("https://directline.digital/media/page_photos/0000/photo_14.normal.png")
# d = response.content
# with open("img.png" , "wb") as f:
#     f.write(d)


# import smtplib
# import threading
# from asyncio import threads
# from email.message import EmailMessage
# import time
#
# email_address = "ahmatovdilshodbek@gmail.com"
# email_password = "xnogjpmascurfkks"
#
# email_ = [
#
# ]
#
#
# def send_email(recipient):
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         msg = EmailMessage()
#         msg['Subject'] = "Hello Hi"
#         msg['From'] = email_address
#         msg['To'] = recipient
#         msg.set_content (Ahmatov_Dilshodbek_Python3.txt)
#         smtp.login(email_address, email_password)
#         smtp.send_message(msg)
#     print(f"Email sent to {recipient}!")
#
#
# for email in email_:
#     thread = threading.Thread(target=send_email, args=(email,))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()

# email_address = "ahmatovdilshodbek@gmail.com"
# email_password = "lrtigfroqxwqulrk"
#
# mail_list = ["absaitovdev@gmail.com"]
#
#
# def send_mail(mail):
#     msg = EmailMessage()
#     msg['Subject'] = f'The contents of {Ahmatov Dilshodbek Python3}'
#     msg['From'] = email_address
#     msg['To'] = mail
#     msg.set_content("This is eamil message")
#
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(email_address, email_password)
#         smtp.send_message(msg)
#         print("send mail !")
#
#
# l = []
# for i in mail_list:
#     t = threading.Thread(target=send_mail, args=(i,))
#     l.append(t)
#
# for i in l:
#     i.join()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


sender_email = "ahmatovdilshodbek@gmail.com"
recipient_email = "Adilshod3234@gmail.com"
subject = "Code File Attachment"
body = "Please find attached the code file."
code_file_path = "Ahmatov_Dilshodbek_Python3.txt"
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = recipient_email
message["Subject"] = subject
message.attach(MIMEText(body, "plain"))
with open('Ahmatov_Dilshodbek_Python3.txt.txt', "rb") as file:
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(file.read())
    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {code_file_path.split('/')[-1]}",
    )
    message.attach(attachment)

smtp_host = "smtp.gmail.com"
smtp_port = 587
smtp_username = "ahmatovdilshodbek@gmail.com"
smtp_password = "????"

with smtplib.SMTP(smtp_host, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(message)
    print("Email sent successfully!")