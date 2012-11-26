# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('product_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('product', ['Category'])

        # Adding model 'Product'
        db.create_table('product_product', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['product.Category'], null=True, blank=True)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('kdv', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('total_price', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('product', ['Product'])

        # Adding model 'ProductSettings'
        db.create_table('product_productsettings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('order_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('site_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('kdv_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('product', ['ProductSettings'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('product_category')

        # Deleting model 'Product'
        db.delete_table('product_product')

        # Deleting model 'ProductSettings'
        db.delete_table('product_productsettings')


    models = {
        'product.category': {
            'Meta': {'object_name': 'Category'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'product.product': {
            'Meta': {'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Category']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kdv': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'total_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        'product.productsettings': {
            'Meta': {'object_name': 'ProductSettings'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kdv_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'order_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'site_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['product']