# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Country.coodx'
        db.add_column('home_country', 'coodx',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.coody'
        db.add_column('home_country', 'coody',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.coodz'
        db.add_column('home_country', 'coodz',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Country.coodx'
        db.delete_column('home_country', 'coodx')

        # Deleting field 'Country.coody'
        db.delete_column('home_country', 'coody')

        # Deleting field 'Country.coodz'
        db.delete_column('home_country', 'coodz')


    models = {
        'home.athlete': {
            'Meta': {'object_name': 'Athlete'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bronze_medals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'athlete_bronze'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Events']"}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Country']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'default': "''"}),
            'gold_medals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'athlete_gold'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Events']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'silver_medals': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'athlete_silver'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Events']"})
        },
        'home.country': {
            'Meta': {'object_name': 'Country'},
            'athletes': ('django.db.models.fields.related.ManyToManyField', [], {'null': 'True', 'related_name': "'country_athletes'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
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
            'Meta': {'object_name': 'Events'},
            'bronze_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events_bronze'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'gold_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events_gold'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'silver_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'events_silver'", 'blank': 'True', 'symmetrical': 'False', 'to': "orm['home.Athlete']"}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']