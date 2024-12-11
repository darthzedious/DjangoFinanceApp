# DjangoFinanceApp
### Project Overview
The Django Finance App is a powerful and user-friendly tool for managing personal finances, tracking budgets, and calculating complex financial formulas like ROE, CAPM, and dividend growth. It also includes features like calculating stocks prices and generate repayment plans. This app is designed for finance students/enthusiasts and professionals looking for a reliable and extendable solution.

## Contents
## Prerequisites
**To run this project, you will need:**

- Python 3.10+
- PostgreSQL for the database.

## Setup Guide

### Step 1: Clone the Repository
First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Environment Setup

**To set up the project, you'll need a virtual environment.**

**On Windows**

Open Command Prompt and create a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:
```bash
venv\Scripts\activate
```
**On macOS/Linux**

Open Terminal and create a virtual environment:
```bash
python3 -m venv venv
```
Activate the virtual environment:
```bash
source venv/bin/activate
```
### Step 3: Environment Setup
**Installing Requirements**

Once the virtual environment is activated, install the dependencies:

```bash
pip install -r requirements.txt
```

### Step 4: Set Up the Database
**Update Django settings.py**


Edit the DATABASES configuration in your Django project to use PostgreSQL:

```python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',  # Your Database name
        'USER': '',    # Your Database user
        'PASSWORD': '',  # Your User's password
        'HOST': 'localhost',  # Database host
        'PORT': '5432',     # Database port (default is 5432)
    }
}
```
https://docs.djangoproject.com/en/5.1/ref/settings/#databases

### Step 5: Apply Migrations

Run Django migrations to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser

To access the admin panel, create a superuser account:

```bash
  python manage.py createsuperuser
```
Follow the prompts to set up the superuser credentials.

### Step 6: Run the Server

Run the server with the following command:

```bash
python manage.py runserver
```
By default, the server runs on http://127.0.0.1:8000/.

## Key parts

- Models:
  - AppUser: Custom user model.
  - Profile: Contains user-specific details like budgets, financial goals, and income tracking.
  - Budget: Tracks individual user budgets.
  - FinancialGoal: Represents specific goals users set for financial planning.
  - InvestmentPortfolio: Tracks investments managed by the user.
  - Transaction: Logs financial transactions.
  - EqualInstallmentPlan, EqualPrincipalPortionPlan, EqualInstallmentChangeableIPPlan: Models for managing different types of repayment plans.
- **Forms**
  -  Includes forms for creating, updating, and deleting user data. 
- **Mixins**
  - OperationNameContextMixin: Adds dynamic context for operation-specific views.
    - Adds dynamic context for operation-specific views by injecting a predefined operation name into the template context.
      ```python
      class OperationNameContextMixin:
        operation_name = ''

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['operation_name'] = self.operation_name

            return context
      ```
  - DisabledReadonlyMixin: Used to make fields or forms read-only.
    - Dynamically disables all fields in a form by adding the disabled attribute, ensuring they are non-editable. Useful for rendering forms in a read-only state.
      ```python
      class DisabledReadonlyMixin:
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for field in self.fields.values(): # ('name': object_field)
                field.widget.attrs['disabled'] = True
                field.widget.attrs['readonly'] = True
      ```
  - PlaceholderMixin:
    -  Automatically assigns meaningful placeholders to form fields based on their labels or names, improving user experience.
    ```python
    class PlaceholderMixin:
    def add_placeholders(self):
        for field_name, field in self.fields.items():
            placeholder = field.widget.attrs.get('placeholder') or field.label or field_name.replace('_', ' ').capitalize()
            field.widget.attrs['placeholder'] = placeholder

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_placeholders()
      ```
  - CreateActionFormValidMixin:
    - Automatically associates the logged-in user with the form instance during creation, streamlining the connection between the user and the created object.
    ```python
    class CreateActionFormValidMixin:
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
      ```
  - AdminAddFieldSetMixin: Customizes field sets for the admin interface.
    - Customizes field sets in the admin interface to display a different layout when adding new objects versus editing existing ones.
    ```python
    class AdminAddFieldSetMixin:
        def get_fieldsets(self, request, obj=None):

            if obj is None: # If object is not already created return add_fieldsets
                return self.add_fieldsets

            return super().get_fieldsets(request, obj)
    ```
  - RepaymentJSONContextToTableMixin: Converts repayment JSON into a structured table format.
    - Converts repayment plan data stored as JSON or pseudo-JSON into structured Python objects (lists/dictionaries) for easier rendering in templates. It gracefully handles parsing errors.
    ```python
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
    ```
- **Helpers**
  - Each app includes a **helpers.py** file for complex financial formulas, encapsulating some of the the business logic used in views.
- **Admin**
    - All models are registered in the admin panel with three levels of administration:
      - Superuser
      - Staff
      -  Moderator 

## Concept

**User Registration**:
- Users must register to access features such as stock operations, repayment plan calculations, and financial formula evaluations (e.g., discount factors, future values).

**Repayment Plans**:

- After submitting the required details, the user receives a repayment plan in a structured table format, detailing installment amounts, interest portions, principal portions, and remaining principal for each period. Users can save these plans in their profiles for later review, editing, or deletion.

**Profile Features**:

Users can:

- Track personal spending, budgets, and income.
- Use all available financial calculations.
- Access only their own saved data, ensuring privacy. Attempts to access other users' data redirect them to their profile.




