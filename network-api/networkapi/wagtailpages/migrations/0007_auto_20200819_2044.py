# Generated by Django 2.2.14 on 2020-08-19 20:44

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailpages', '0006_publicationpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationpage',
            name='contents_title',
            field=models.CharField(blank=True, default='Table of Contents', max_length=250),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='publication_hero_image', to='wagtailimages.Image', verbose_name='Publication Hero Image'),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='notes',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='publication_date',
            field=models.DateField(blank=True, null=True, verbose_name='Publication date'),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='publication_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='secondary_subtitle',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='publicationpage',
            name='subtitle',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
