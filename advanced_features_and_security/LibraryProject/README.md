# Permissions & Groups – Blog App

## Custom Permissions (codenames)
| Codename     | Meaning                |
|--------------|------------------------|
| `can_view`   | View article list/detail |
| `can_create` | Create new articles    |
| `can_edit`   | Edit existing articles |
| `can_delete` | Delete articles        |

## Groups
| Group    | Permissions                     |
|----------|---------------------------------|
| **Viewers** | `can_view`                     |
| **Editors** | `can_create`, `can_edit`       |
| **Admins**  | `can_view`, `can_create`, `can_edit`, `can_delete` |

## How to assign a user
```python
user.groups.add(Group.objects.get(name='Editors'))

