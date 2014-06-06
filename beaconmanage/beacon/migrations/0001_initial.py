# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'beacon_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'beacon', ['Location'])

        # Adding model 'Beacon'
        db.create_table(u'beacon_beacon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('major', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('minor', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['beacon.Location'], null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('metadata', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('last_checkin', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'beacon', ['Beacon'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'beacon_location')

        # Deleting model 'Beacon'
        db.delete_table(u'beacon_beacon')


    models = {
        u'beacon.beacon': {
            'Meta': {'object_name': 'Beacon'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_checkin': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['beacon.Location']", 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'metadata': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'minor': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'beacon.location': {
            'Meta': {'object_name': 'Location'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['beacon']