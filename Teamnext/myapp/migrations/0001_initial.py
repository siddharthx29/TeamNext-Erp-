import django.db.models.deletion

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [

    ]

    operations = [

        migrations.CreateModel(

            name='Company',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=255)),

                ('email', models.EmailField(max_length=254, unique=True)),

                ('password', models.CharField(max_length=255)),

                ('address', models.TextField(blank=True, null=True)),

                ('phone', models.CharField(blank=True, max_length=20, null=True)),

                ('website', models.URLField(blank=True, null=True)),

                ('employees_count', models.CharField(blank=True, max_length=50, null=True)),

                ('industry', models.CharField(blank=True, max_length=100, null=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

            ],

        ),

        migrations.CreateModel(

            name='EmailMessage',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('sender_email', models.EmailField(max_length=254)),

                ('recipient_email', models.EmailField(max_length=254)),

                ('subject', models.CharField(max_length=255)),

                ('body', models.TextField()),

                ('is_draft', models.BooleanField(default=False)),

                ('is_sent', models.BooleanField(default=True)),

                ('timestamp', models.DateTimeField(auto_now_add=True)),

            ],

        ),

        migrations.CreateModel(

            name='Employee',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=255)),

                ('email', models.EmailField(max_length=254, unique=True)),

                ('password', models.CharField(max_length=255)),

                ('role', models.CharField(blank=True, max_length=100, null=True)),

                ('department', models.CharField(blank=True, max_length=100, null=True)),

                ('phone', models.CharField(blank=True, max_length=20, null=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='myapp.company')),

            ],

        ),

        migrations.CreateModel(

            name='LeaveRequest',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('reason', models.TextField()),

                ('start_date', models.DateField()),

                ('end_date', models.DateField()),

                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=10)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaves', to='myapp.employee')),

            ],

        ),

        migrations.CreateModel(

            name='Project',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('name', models.CharField(max_length=255)),

                ('description', models.TextField(blank=True, null=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='myapp.company')),

            ],

        ),

        migrations.CreateModel(

            name='ChatMessage',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('text', models.TextField()),

                ('timestamp', models.DateTimeField(auto_now_add=True)),

                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='myapp.employee')),

                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='myapp.project')),

            ],

        ),

        migrations.CreateModel(

            name='SocialItem',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('type', models.CharField(choices=[('birthday', 'Birthday'), ('topic', 'Hot Topic'), ('dare', 'Daily Dare')], max_length=10)),

                ('title', models.CharField(max_length=255)),

                ('content', models.TextField(blank=True, null=True)),

                ('meta_info', models.CharField(blank=True, max_length=255, null=True)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_items', to='myapp.company')),

            ],

        ),

        migrations.CreateModel(

            name='Ticket',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('title', models.CharField(max_length=255)),

                ('description', models.TextField()),

                ('priority', models.CharField(choices=[('high', 'High'), ('medium', 'Medium'), ('low', 'Low')], default='medium', max_length=10)),

                ('created_at', models.DateTimeField(auto_now_add=True)),

                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tickets', to='myapp.employee')),

                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='myapp.project')),

            ],

        ),

        migrations.CreateModel(

            name='ProjectMember',

            fields=[

                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('can_chat', models.BooleanField(default=True)),

                ('is_admin', models.BooleanField(default=False)),

                ('can_modify_settings', models.BooleanField(default=False)),

                ('can_approve_leaves', models.BooleanField(default=False)),

                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_memberships', to='myapp.employee')),

                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='myapp.project')),

            ],

            options={

                'unique_together': {('project', 'employee')},

            },

        ),

    ]
