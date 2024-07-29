# Generated by Django 3.1.14 on 2024-05-30 10:48

from django.db import migrations, models
import edc_consent.validators


def move_data_to_tb_adol_child_model(apps, schema_editor):
    tb_adol_consent = apps.get_model('flourish_caregiver', 'tbadolconsent')
    tb_adol_child_consent = apps.get_model('flourish_caregiver', 'tbadolchildconsent')

    for consent in tb_adol_consent.objects.all():
        child_consents = tb_adol_child_consent.objects.filter(
            tb_adol_consent=consent)
        child_consents.update(tb_blood_test_consent=consent.tb_blood_test_consent,
                              samples_future_studies=consent.samples_future_studies)


class Migration(migrations.Migration):

    dependencies = [
        ('flourish_caregiver', '0076_auto_20231203_1348'),
        ]

    operations = [
        migrations.AddField(
            model_name='tbadolchildconsent',
            name='samples_future_studies',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=3, verbose_name="Use of Samples in Future Research: Do you give us permission to use your child's blood samples for future studies?"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbadolchildconsent',
            name='tb_blood_test_consent',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', help_text='Participant is not eligible if no', max_length=3, validators=[edc_consent.validators.eligible_if_yes], verbose_name='Will you allow for blood testing for TB for your adolescent? '),
            preserve_default=False,
        ),
        migrations.RunPython(move_data_to_tb_adol_child_model),
    ]
