# Generated by Django 3.1.14 on 2023-12-03 11:48

from django.db import migrations
import edc_base.sites.managers
import flourish_caregiver.models.antenatal_enrollment
import flourish_caregiver.models.caregiver_child_consent
import flourish_caregiver.models.maternal_delivery
import flourish_caregiver.models.maternal_visit
import flourish_caregiver.models.model_mixins.crf_model_mixin
import flourish_caregiver.models.onschedule


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('flourish_caregiver', '0041_auto_20240530_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalantenatalenrollment',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Maternal Antenatal Enrollment'},
        ),
        migrations.AlterModelOptions(
            name='historicalcaregivercontact',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Caregiver Contact'},
        ),
        migrations.AlterModelOptions(
            name='historicalcaregiverlocator',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Caregiver Locator'},
        ),
        migrations.AlterModelOptions(
            name='historicalcaregiveroffschedule',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical caregiver off schedule'},
        ),
        migrations.AlterModelOptions(
            name='historicalcaregiverrequisition',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical caregiver requisition'},
        ),
        migrations.AlterModelOptions(
            name='historicalcaregiverrequisitionresult',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Sample Result'},
        ),
        migrations.AlterModelOptions(
            name='historicalcaregiverresultvalue',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Analysis Result Value'},
        ),
        migrations.AlterModelOptions(
            name='historicalcohort',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Cohort'},
        ),
        migrations.AlterModelOptions(
            name='historicalcohortschedules',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Cohort Schedule'},
        ),
        migrations.AlterModelOptions(
            name='historicalenrollment',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Enrollment'},
        ),
        migrations.AlterModelOptions(
            name='historicallocatorlog',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical locator log'},
        ),
        migrations.AlterModelOptions(
            name='historicallocatorlogentry',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical locator log entry'},
        ),
        migrations.AlterModelOptions(
            name='historicalmaternaldelivery',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Birth Form'},
        ),
        migrations.AlterModelOptions(
            name='historicalmaternalvisit',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Maternal Visit'},
        ),
        migrations.AlterModelOptions(
            name='historicalscreeningpregwomen',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Screening for Newly Enrolled Pregnant Women'},
        ),
        migrations.AlterModelOptions(
            name='historicalscreeningpriorbhpparticipants',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Screening Prior BHP Participants'},
        ),
        migrations.AlterModelOptions(
            name='historicalsubjectconsent',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Adult Participation Consent'},
        ),
        migrations.AlterModelOptions(
            name='historicaltbadolconsent',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical TB Adolescent Caregiver Consent'},
        ),
        migrations.AlterModelOptions(
            name='historicaltbinformedconsent',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical TB Informed Consent'},
        ),
        migrations.AlterModelOptions(
            name='historicaltboffstudy',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical TB Off Study'},
        ),
        migrations.AlterModelManagers(
            name='antenatalenrollment',
            managers=[
                ('objects', flourish_caregiver.models.antenatal_enrollment.AntenatalModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='arvsprepregnancy',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='breastfeedingquestionnaire',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiverchildconsent',
            managers=[
                ('objects', flourish_caregiver.models.caregiver_child_consent.ChildConsentModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiverclinicalmeasurements',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiverclinicalmeasurementsfu',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiveredinburghdeprscreening',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregivergadanxietyscreening',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiverhamddeprscreening',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiverphqdeprscreening',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='caregiversocialworkreferral',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='cliniciannotes',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='covid19',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='foodsecurityquestionnaire',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='hivdisclosurestatusa',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='hivdisclosurestatusb',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='hivdisclosurestatusc',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='hivrapidtestcounseling',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='hivviralloadandcd4',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='interviewfocusgroupinterest',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='interviewfocusgroupinterestv2',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalarvadherence',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalarvatdelivery',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalarvduringpreg',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalarvpostadherence',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternaldelivery',
            managers=[
                ('objects', flourish_caregiver.models.maternal_delivery.MaternalDeliveryManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternaldiagnoses',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalhivinterimhx',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalinterimidcc',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalinterimidccversion2',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='maternalvisit',
            managers=[
                ('on_site', flourish_caregiver.models.maternal_visit.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.maternal_visit.VisitModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='medicalhistory',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='obstericalhistory',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortaantenatal',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortabirth',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortaenrollment',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortafu',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortafuquarterly',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortaquarterly',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortasec',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortasecquart',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortatb2months',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortatb6months',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortbenrollment',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortbfu',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortbfuquarterly',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortbquarterly',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortbsec',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortbsecquart',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcenrollment',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcfu',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcfuquarterly',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcpool',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcquarterly',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcsec',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='onschedulecohortcsecquart',
            managers=[
                ('on_site', edc_base.sites.managers.CurrentSiteManager()),
                ('objects', flourish_caregiver.models.onschedule.OnScheduleModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='posthivrapidtestandconseling',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='relationshipfatherinvolvement',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='sociodemographicdata',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='substanceuseduringpregnancy',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='substanceusepriorpregnancy',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbengagement',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbhistorypreg',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbinterview',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbinterviewtranscription',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbinterviewtranslation',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbknowledge',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbpresencehouseholdmembers',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbreferral',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbreferraloutcomes',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbroutinehealthscreen',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbroutinehealthscreenv2',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbscreenpreg',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbstudyeligibility',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='tbvisitscreeningwomen',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='ultrasound',
            managers=[
                ('objects', flourish_caregiver.models.model_mixins.crf_model_mixin.CrfModelManager()),
            ],
        ),
    ]
