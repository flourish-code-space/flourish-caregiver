from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from flourish_form_validations.form_validators import CaregiverPrevEnrolledFormValidator

from ..models import CaregiverPreviouslyEnrolled


class CaregiverPreviouslyEnrolledForm(
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = CaregiverPrevEnrolledFormValidator

    class Meta:
        model = CaregiverPreviouslyEnrolled
        fields = '__all__'
