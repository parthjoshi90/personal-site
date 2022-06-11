from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import(
    CharField,
    TextField,
    SlugField,
    IntegerField,
    ManyToManyField
)
from django.utils.text import slugify
from src.apps.core.models import TimestampedModel


class PostCategory(TimestampedModel):
    name = CharField(max_length=255)
    description = TextField(max_length=500, null=True, blank=True)
    slug = SlugField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Post(TimestampedModel):
    DRAFT = "D"
    HIDDEN = "H"
    PUBLISHED = "P"
    STATUS = (
        (DRAFT, _("Draft")),
        (HIDDEN, _("Hidden")),
        (PUBLISHED, _("Published")),
    )

    title = CharField(max_length=255)
    slug = SlugField(blank=True)
    categories = ManyToManyField('PostCategory', related_name='posts')
    status = CharField(max_length=10, choices=STATUS)
    content = models.TextField(null=True, blank=True)
    summary = models.TextField(max_length=255, null=True, blank=True)
    start_publication = models.DateTimeField()

    class Meta:
        verbose_name = _("post")
        verbose_name_plural = _("posts")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("blog:post", args=(self.slug,))
