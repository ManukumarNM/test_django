# Generated by Django 2.0.2 on 2018-02-26 12:01

#import swapper
#from django.db import migrations


#class Migration(migrations.Migration):

    #initial = True

    #dependencies = [
       # ('contenttypes', '0002_remove_content_type_name'),
       # swapper.dependency('config', 'Device', '0004_add_device_model'),
    #]

    #operations = [
        #migrations.CreateModel(
           # name='DeviceData',
           # fields=[],
           # options={
                #'indexes': [],
                #'proxy': True,
                #'swappable': swapper.swappable_setting(
                   # 'device_monitoring', 'DeviceData'
              #  ),
            },
            bases=(swapper.get_model_name('config', 'Device'),),
        )
    ]
