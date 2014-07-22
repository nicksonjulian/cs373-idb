# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Athlete.gender'
        db.alter_column('home_athlete', 'gender', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Athlete.gender'
        db.alter_column('home_athlete', 'gender', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        'home.athlete': {
            'Meta': {'object_name': 'Athlete', 'ordering': "['last_name']"},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bronze_medals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'athlete_bronze'", 'symmetrical': 'False', 'to': "orm['home.Events']", 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Country']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'gold_medals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'athlete_gold'", 'symmetrical': 'False', 'to': "orm['home.Events']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'silver_medals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'athlete_silver'", 'symmetrical': 'False', 'to': "orm['home.Events']", 'blank': 'True'})
        },
        'home.country': {
            'Meta': {'object_name': 'Country', 'ordering': "['name']"},
            'athletes': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'country_athletes'", 'null': 'True', 'to': "orm['home.Athlete']", 'symmetrical': 'False', 'blank': 'True'}),
            'coodx': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coody': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coodz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'total_bronze_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_gold_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_silver_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'home.events': {
            'Meta': {'object_name': 'Events', 'ordering': "['sport', 'name']"},
            'bronze_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events_bronze'", 'symmetrical': 'False', 'to': "orm['home.Athlete']", 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'gold_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events_gold'", 'symmetrical': 'False', 'to': "orm['home.Athlete']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'silver_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events_silver'", 'symmetrical': 'False', 'to': "orm['home.Athlete']", 'blank': 'True'}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']