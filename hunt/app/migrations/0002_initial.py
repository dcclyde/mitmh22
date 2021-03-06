# Generated by Django 3.2.8 on 2022-03-08 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hunt_app', '0001_initial'),
        ('spoilr_core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamsession',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.team'),
        ),
        migrations.AddField(
            model_name='teamdata',
            name='team',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.team'),
        ),
        migrations.AddField(
            model_name='rounddata',
            name='round',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.round'),
        ),
        migrations.AddField(
            model_name='puzzledata',
            name='interaction_to_unlock',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_core.interaction'),
        ),
        migrations.AddField(
            model_name='puzzledata',
            name='puzzle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.puzzle'),
        ),
        migrations.AddField(
            model_name='puzzledata',
            name='solves_to_unlock',
            field=models.ManyToManyField(related_name='_hunt_app_puzzledata_solves_to_unlock_+', to='spoilr_core.Puzzle'),
        ),
        migrations.AddField(
            model_name='interactiondata',
            name='interaction',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.interaction'),
        ),
        migrations.AddField(
            model_name='interactiondata',
            name='puzzle_trigger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='spoilr_core.puzzle'),
        ),
        migrations.AddField(
            model_name='freeunlockrequest',
            name='puzzle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spoilr_core.puzzle'),
        ),
        migrations.AddField(
            model_name='freeunlockrequest',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='free_unlocks', to='spoilr_core.team'),
        ),
        migrations.AlterUniqueTogether(
            name='teamsession',
            unique_together={('team', 'group_type')},
        ),
        migrations.AddConstraint(
            model_name='interactiondata',
            constraint=models.CheckConstraint(check=models.Q(('type__in', ['submission', 'story', 'unlock', 'answer'])), name='hunt_app_interactiondata_type_valid'),
        ),
        migrations.AlterUniqueTogether(
            name='freeunlockrequest',
            unique_together={('team', 'puzzle')},
        ),
    ]
