class OperationNameContextMixin:
    operation_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation_name'] = self.operation_name
        return context


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