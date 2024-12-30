import ast
import json

from financeDjango.annuity_factor_app.helpers import calculate_future_value_annuity_factor_end_year_payment


class OperationNameContextMixin:
    operation_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation_name'] = self.operation_name

        return context

class DisabledReadonlyMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values(): # ('name': object_field)
            field.widget.attrs['disabled'] = True
            field.widget.attrs['readonly'] = True

class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field.widget.attrs.get('placeholder') or field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()


class CreateActionFormValidMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AdminAddFieldSetMixin:
    def get_fieldsets(self, request, obj=None):

        if obj is None: # If object is not already created return add_fieldsets
            return self.add_fieldsets

        return super().get_fieldsets(request, obj)


class RepaymentJSONContextToTableMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        for plan in context['plans']:
            try:
                # Try to load the JSON with proper quotes
                plan.repayment_table = json.loads(plan.repayment)
            except json.JSONDecodeError:
                try:
                    # Handle pseudo-JSON with single quotes using ast.literal_eval
                    plan.repayment_table = ast.literal_eval(plan.repayment)
                except (ValueError, SyntaxError) as e:
                    print(f"Error parsing repayment data for plan {plan.id}: {e}")
                    # Default to an empty list if both methods fail
                    plan.repayment_table = []

        return context
