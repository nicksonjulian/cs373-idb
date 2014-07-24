# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.country_code'
        db.add_column('home_country', 'country_code',
                      self.gf('django.db.models.fields.CharField')(max_length=10, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Events.icon'
        db.add_column('home_events', 'icon',
                      self.gf('django.db.models.fields.CharField')(max_length=20, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Athlete.picture'
        db.add_column('home_athlete', 'picture',
                      self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True),
                      keep_default=False)

        # Adding field 'Athlete.video'
        db.add_column('home_athlete', 'video',
                      self.gf('django.db.models.fields.CharField')(max_length=50, blank=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.country_code'
        db.delete_column('home_country', 'country_code')

        # Deleting field 'Events.icon'
        db.delete_column('home_events', 'icon')

        # Deleting field 'Athlete.picture'
        db.delete_column('home_athlete', 'picture')

        # Deleting field 'Athlete.video'
        db.delete_column('home_athlete', 'video')


    models = {
        'home.athlete': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Athlete'},
            'birthdate': ('django.db.models.fields.DateField', [], {'blank': 'True', 'null': 'True'}),
            'bronze_medals': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'athlete_bronze'", 'symmetrical': 'False', 'to': "orm['home.Events']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Country']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'gold_medals': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'athlete_gold'", 'symmetrical': 'False', 'to': "orm['home.Events']"}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'silver_medals': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'athlete_silver'", 'symmetrical': 'False', 'to': "orm['home.Events']"}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True', 'null': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True', 'null': 'True'})
        },
        'home.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'athletes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Athlete']", 'blank': 'True', 'related_name': "'country_athletes'", 'symmetrical': 'False', 'null': 'True'}),
            'coordx': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'coordy': ('django.db.models.fields.FloatField', [], {'blank': 'True', 'null': 'True'}),
            'coordz': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True', 'null': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'total_bronze_medals': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'total_gold_medals': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'}),
            'total_silver_medals': ('django.db.models.fields.IntegerField', [], {'blank': 'True', 'null': 'True'})
        },
        'home.events': {
            'Meta': {'ordering': "['sport', 'name']", 'object_name': 'Events'},
            'bronze_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'events_bronze'", 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'gold_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'events_gold'", 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
            'icon': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'silver_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'events_silver'", 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']