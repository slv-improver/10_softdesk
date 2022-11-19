from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models


class Project(models.Model):

    class Type(models.TextChoices):
        BACK = 'BA'
        FRONT = 'FR'
        IOS = 'IOS', _('iOs')
        ANDROID = 'AN'

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=4096)
    type = models.fields.CharField(max_length=3, choices=Type.choices)


class Contributor(models.Model):

    class Meta:
        unique_together = ['user', 'project']

    READ = 'R'
    UPDATE_DELETE = 'UD'
    PERMISSIONS = [
        (READ, 'Read'),
        (UPDATE_DELETE, 'Update & Delete'),
    ]

    AUTHOR = 'AU'
    COLLABORATOR = 'CO'
    ROLES = [
        (AUTHOR, 'Author'),
        (COLLABORATOR, 'Collaborator'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    permission = models.fields.CharField(
        max_length=2,
        choices=PERMISSIONS,
        default=READ,
    )
    role = models.fields.CharField(max_length=3, choices=ROLES)


class Issue(models.Model):

    class Tag(models.TextChoices):
        BUG = 'BU'
        IMPROVEMENT = 'IM'
        TASK = 'TS'

    class Priority(models.TextChoices):
        LOW = 'LO'
        MEDIUM = 'ME'
        HIGH = 'HI'

    class Status(models.TextChoices):
        TODO = 'TD'
        IN_PROGRESS = 'IP'
        ENDED = 'ND'

    title = models.fields.CharField(max_length=128)
    description = models.fields.CharField(max_length=4096)
    tag = models.fields.CharField(max_length=3, choices=Tag.choices,)
    priority = models.fields.CharField(max_length=3, choices=Priority.choices)
    status = models.fields.CharField(max_length=3, choices=Status.choices)
    created_time = models.DateTimeField(auto_now_add=True)

    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='author_of_issues',
    )
    assignee_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='assignee_of_issues',
        default=author_user,
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        related_name='issues',
    )


class Comment(models.Model):
    description = models.fields.CharField(max_length=4096)
    created_time = models.DateTimeField(auto_now_add=True)

    author_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='author_of_comments',
    )
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE,
        related_name='comments',
    )
