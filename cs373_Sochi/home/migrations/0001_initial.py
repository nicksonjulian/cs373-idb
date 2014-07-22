# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Athlete'
        db.create_table('home_athlete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['home.Country'])),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1, default='')),
            ('birthdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('home', ['Athlete'])

        # Adding M2M table for field gold_medals on 'Athlete'
        m2m_table_name = db.shorten_name('home_athlete_gold_medals')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False)),
            ('events', models.ForeignKey(orm['home.events'], null=False))
        ))
        db.create_unique(m2m_table_name, ['athlete_id', 'events_id'])

        # Adding M2M table for field silver_medals on 'Athlete'
        m2m_table_name = db.shorten_name('home_athlete_silver_medals')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False)),
            ('events', models.ForeignKey(orm['home.events'], null=False))
        ))
        db.create_unique(m2m_table_name, ['athlete_id', 'events_id'])

        # Adding M2M table for field bronze_medals on 'Athlete'
        m2m_table_name = db.shorten_name('home_athlete_bronze_medals')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False)),
            ('events', models.ForeignKey(orm['home.events'], null=False))
        ))
        db.create_unique(m2m_table_name, ['athlete_id', 'events_id'])

        # Adding model 'Events'
        db.create_table('home_events', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sport', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal('home', ['Events'])

        # Adding M2M table for field gold_medalists on 'Events'
        m2m_table_name = db.shorten_name('home_events_gold_medalists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('events', models.ForeignKey(orm['home.events'], null=False)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False))
        ))
        db.create_unique(m2m_table_name, ['events_id', 'athlete_id'])

        # Adding M2M table for field silver_medalists on 'Events'
        m2m_table_name = db.shorten_name('home_events_silver_medalists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('events', models.ForeignKey(orm['home.events'], null=False)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False))
        ))
        db.create_unique(m2m_table_name, ['events_id', 'athlete_id'])

        # Adding M2M table for field bronze_medalists on 'Events'
        m2m_table_name = db.shorten_name('home_events_bronze_medalists')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('events', models.ForeignKey(orm['home.events'], null=False)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False))
        ))
        db.create_unique(m2m_table_name, ['events_id', 'athlete_id'])

        # Adding model 'Country'
        db.create_table('home_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('total_gold_medals', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_silver_medals', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('total_bronze_medals', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('home', ['Country'])

        # Adding M2M table for field athletes on 'Country'
        m2m_table_name = db.shorten_name('home_country_athletes')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('country', models.ForeignKey(orm['home.country'], null=False)),
            ('athlete', models.ForeignKey(orm['home.athlete'], null=False))
        ))
        db.create_unique(m2m_table_name, ['country_id', 'athlete_id'])


    def backwards(self, orm):
        # Deleting model 'Athlete'
        db.delete_table('home_athlete')

        # Removing M2M table for field gold_medals on 'Athlete'
        db.delete_table(db.shorten_name('home_athlete_gold_medals'))

        # Removing M2M table for field silver_medals on 'Athlete'
        db.delete_table(db.shorten_name('home_athlete_silver_medals'))

        # Removing M2M table for field bronze_medals on 'Athlete'
        db.delete_table(db.shorten_name('home_athlete_bronze_medals'))

        # Deleting model 'Events'
        db.delete_table('home_events')

        # Removing M2M table for field gold_medalists on 'Events'
        db.delete_table(db.shorten_name('home_events_gold_medalists'))

        # Removing M2M table for field silver_medalists on 'Events'
        db.delete_table(db.shorten_name('home_events_silver_medalists'))

        # Removing M2M table for field bronze_medalists on 'Events'
        db.delete_table(db.shorten_name('home_events_bronze_medalists'))

        # Deleting model 'Country'
        db.delete_table('home_country')

        # Removing M2M table for field athletes on 'Country'
        db.delete_table(db.shorten_name('home_country_athletes'))


    models = {
        'home.athlete': {
            'Meta': {'object_name': 'Athlete'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bronze_medals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'athlete_bronze'", 'to': "orm['home.Events']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Country']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "''"}),
            'gold_medals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'athlete_gold'", 'to': "orm['home.Events']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'silver_medals': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'athlete_silver'", 'to': "orm['home.Events']"})
        },
        'home.country': {
            'Meta': {'object_name': 'Country'},
            'athletes': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'symmetrical': 'False', 'blank': 'True', 'related_name': "'country_athletes'", 'to': "orm['home.Athlete']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'total_bronze_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_gold_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_silver_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'home.events': {
            'Meta': {'object_name': 'Events'},
            'bronze_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'events_bronze'", 'to': "orm['home.Athlete']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'gold_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'events_gold'", 'to': "orm['home.Athlete']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'silver_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'blank': 'True', 'related_name': "'events_silver'", 'to': "orm['home.Athlete']"}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']