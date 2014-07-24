# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Events.desc'
        db.alter_column('home_events', 'desc', self.gf('django.db.models.fields.CharField')(max_length=1000))
        # Adding field 'Athlete.height'
        db.add_column('home_athlete', 'height',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Athlete.weight'
        db.add_column('home_athlete', 'weight',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Country.coody'
        db.delete_column('home_country', 'coody')

        # Deleting field 'Country.coodx'
        db.delete_column('home_country', 'coodx')

        # Deleting field 'Country.coodz'
        db.delete_column('home_country', 'coodz')

        # Adding field 'Country.coordx'
        db.add_column('home_country', 'coordx',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.coordy'
        db.add_column('home_country', 'coordy',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.coordz'
        db.add_column('home_country', 'coordz',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Events.desc'
        db.alter_column('home_events', 'desc', self.gf('django.db.models.fields.CharField')(max_length=500))
        # Deleting field 'Athlete.height'
        db.delete_column('home_athlete', 'height')

        # Deleting field 'Athlete.weight'
        db.delete_column('home_athlete', 'weight')

        # Adding field 'Country.coody'
        db.add_column('home_country', 'coody',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.coodx'
        db.add_column('home_country', 'coodx',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.coodz'
        db.add_column('home_country', 'coodz',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Country.coordx'
        db.delete_column('home_country', 'coordx')

        # Deleting field 'Country.coordy'
        db.delete_column('home_country', 'coordy')

        # Deleting field 'Country.coordz'
        db.delete_column('home_country', 'coordz')


    models = {
        'home.athlete': {
            'Meta': {'ordering': "['last_name']", 'object_name': 'Athlete'},
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'bronze_medals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Events']", 'symmetrical': 'False', 'related_name': "'athlete_bronze'", 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['home.Country']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'gold_medals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Events']", 'symmetrical': 'False', 'related_name': "'athlete_gold'", 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'silver_medals': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Events']", 'symmetrical': 'False', 'related_name': "'athlete_silver'", 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        'home.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'athletes': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Athlete']", 'symmetrical': 'False', 'null': 'True', 'related_name': "'country_athletes'", 'blank': 'True'}),
            'coordx': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coordy': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'coordz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'total_bronze_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_gold_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'total_silver_medals': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'home.events': {
            'Meta': {'ordering': "['sport', 'name']", 'object_name': 'Events'},
            'bronze_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Athlete']", 'symmetrical': 'False', 'related_name': "'events_bronze'", 'blank': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'gold_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Athlete']", 'symmetrical': 'False', 'related_name': "'events_gold'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'silver_medalists': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['home.Athlete']", 'symmetrical': 'False', 'related_name': "'events_silver'", 'blank': 'True'}),
            'sport': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['home']