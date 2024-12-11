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

- **Models**
  - AppUser, Profile, Budget, FinancialGoal, InvestmentPortfolio, Transaction, EqualInstallmentPlan, EqualPrincipalPortionPlan, EqualInstallmentChangeableIPPlan
- **Forms**
  -  Forms for user creation and actions create, update, delete
- **Mixins**
  - OperationNameContextMixin, DisabledReadonlyMixin, PlaceholderMixin, CreateActionFormValidMixin, AdminAddFieldSetMixin, RepaymentJSONContextToTableMixin
- **Helpers**
  - Every calculation related app has a **helpers.py** with complex formulas used in the views to calculate the result
- **Admin**
    - All the models are registered in the admin pannel
    - There are three levels of administration: superuser, staff, moderator 

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




