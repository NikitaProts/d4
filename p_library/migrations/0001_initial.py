from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
                ('birth_year', models.SmallIntegerField()),
                ('country', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('year_release', models.SmallIntegerField()),
                ('copy_count', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Author')),
            ],
        ),
    ]
