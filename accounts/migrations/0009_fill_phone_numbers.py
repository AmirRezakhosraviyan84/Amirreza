from django.db import migrations

def fill_phone_numbers(apps, schema_editor):
    CustomUser = apps.get_model('accounts', 'CustomUser')
    for i, user in enumerate(CustomUser.objects.filter(phone_number__isnull=True) | CustomUser.objects.filter(phone_number='')):
        # هر رکورد NULL یا خالی یه مقدار یکتا می‌گیره
        user.phone_number = f'000000000{i+1}'
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_customuser_options_alter_customuser_managers_and_more'),  # <- اینو با آخرین migration قبلی عوض کن
    ]

    operations = [
        migrations.RunPython(fill_phone_numbers),
    ]
