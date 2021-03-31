from discord_webhooks import DiscordWebhooks

#Put your discord webhook url here.

webhook_url = 'https://discord.com/api/webhooks/826712492427313182/s2XXTKT2RPTECeEC9Xdh0JrTRlZK71gcPERju_iL76Lss4l0sbUDARvBqYCBty5Sg9b5'


def send_msg(class_name,status,start_time,end_time):

    WEBHOOK_URL = webhook_url 

    webhook = DiscordWebhooks(WEBHOOK_URL)
    # Attaches a footer
    webhook.set_footer(text='-- NaniJpr')

    #if(status=="joined"):

    webhook.set_content(title='Your Class Timings......',description="Here's your report with :heart:")

      # Appends a field
    webhook.add_field(name='Class', value=class_name)
    webhook.add_field(name='Status', value=status)
    webhook.add_field(name='Started at', value=start_time)
    webhook.add_field(name='Ends at', value=end_time)

    #webhook.set_content(title='Class left Succesfully',
                         #description="Here's your report with :heart:")

      # Appends a field
      #webhook.add_field(name='Class', value=class_name)
      #webhook.add_field(name='Status', value=status)
      #webhook.add_field(name='Joined at', value=start_time)
      #webhook.add_field(name='Left at', value=end_time)



    webhook.send()

    print("Sent message to discord")
