# Permissions and Groups Configuration

## Overview
This Django application implements role-based access control using custom permissions and user groups to manage book operations.

## Custom Permissions

The `Book` model defines four custom permissions:

```python
class Meta:
    permissions = [
        ("can_view", "Can View book"),
        ("can_create", "Can create a book"),
        ("can_edit", "Can edit a book"),
        ("can_delete", "Can delete a book")
    ]
```

## Group Setup

Create the following groups in Django Admin (`/admin/auth/group/`):

| Group Name | Assigned Permissions |
|------------|---------------------|
| **Viewers** | `can_view` |
| **Editors** | `can_view`, `can_create`, `can_edit` |
| **Admins** | `can_view`, `can_create`, `can_edit`, `can_delete` |

### Steps to Configure Groups:

1. Navigate to Django Admin
2. Go to **Authentication and Authorization > Groups**
3. Click **Add Group**
4. Enter group name (e.g., "Viewers")
5. Select appropriate permissions from the "Available permissions" list
6. Click **Save**
7. Repeat for Editors and Admins groups

## Assigning Users to Groups

1. Go to **Users** in Django Admin
2. Select a user
3. Scroll to **Permissions** section
4. Add user to desired group(s) under **Groups**
5. Click **Save**

## Permission Enforcement

All views are protected with the `@permission_required` decorator:

```python
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # View implementation

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    # Create implementation

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    # Edit implementation

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    # Delete implementation
```

## Testing Permissions

1. Create test users in Django Admin
2. Assign each user to different groups
3. Log in as each user
4. Verify access controls:
   - **Viewers**: Can only view book list
   - **Editors**: Can view, create, and edit books
   - **Admins**: Full CRUD access

Unauthorized access attempts will return a **403 Forbidden** error.

## Running Migrations

After adding custom permissions, run:

```bash
python manage.py makemigrations
python manage.py migrate
```
