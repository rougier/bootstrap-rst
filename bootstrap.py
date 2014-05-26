#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Bootstrap RST
# Copyright (c) 2014, Nicolas P. Rougier
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import sys, os, re

from docutils import nodes, utils
from docutils.parsers.rst.directives import images
from docutils.transforms import TransformError, Transform, parts
from docutils.parsers.rst import Directive, directives, states, roles
from docutils.nodes import fully_normalize_name, whitespace_normalize_name
from docutils.parsers.rst.roles import set_classes
from docutils.writers import html4css1


from roles import *
from directives import *

class HTMLWriter(html4css1.Writer):
    """ This docutils writer will use the MyHTMLTranslator class below. """

    def __init__(self):
        html4css1.Writer.__init__(self)
        self.translator_class = HTMLTranslator


class HTMLTranslator(html4css1.HTMLTranslator):
    """
    This is a translator class for the docutils system.
    """

    def visit_h1(self, node):
        self.body.append('<h1>%s</h1>' % node.children[0])
        raise nodes.SkipNode

    def visit_h2(self, node):
        self.body.append('<h2>%s</h2>' % node.children[0])
        raise nodes.SkipNode

    def visit_h3(self, node):
        self.body.append('<h3>%s</h3>' % node.children[0])
        raise nodes.SkipNode

    def visit_h4(self, node):
        self.body.append('<h4>%s</h4>' % node.children[0])
        raise nodes.SkipNode

    def visit_h5(self, node):
        self.body.append('<h5>%s</h5>' % node.children[0])
        raise nodes.SkipNode

    def visit_h6(self, node):
        self.body.append('<h6>%s</h6>' % node.children[0])
        raise nodes.SkipNode


    def visit_label_default(self, node):
        self.body.append(
            '<span class="label label-default">%s</span>' % node.children[0])
        raise nodes.SkipNode

    def visit_label_primary(self, node):
        self.body.append(
            '<span class="label label-primary">%s</span>' % node.children[0])
        raise nodes.SkipNode

    def visit_label_success(self, node):
        self.body.append(
            '<span class="label label-success">%s</span>' % node.children[0])
        raise nodes.SkipNode

    def visit_label_info(self, node):
        self.body.append(
            '<span class="label label-info">%s</span>' % node.children[0])
        raise nodes.SkipNode

    def visit_label_warning(self, node):
        self.body.append(
            '<span class="label label-warning">%s</span>' % node.children[0])
        raise nodes.SkipNode

    def visit_label_danger(self, node):
        self.body.append(
            '<span class="label label-danger">%s</span>' % node.children[0])
        raise nodes.SkipNode

    def visit_page_row(self, node):
        self.body.append(self.starttag(node,'div'))

    def depart_page_row(self, node):
        self.body.append('</div>\n')

    def visit_page_column(self, node):
        self.body.append(self.starttag(node,'div'))

    def depart_page_column(self, node):
        self.body.append('</div>\n')



    def visit_panel(self, node):

        # self.body.append(self.starttag(node, 'div', CLASS='panel'))
        # if node['header']:
        #     self.body.append('<div class = "panel-heading">\n')
        #     self.body.append(node['header'] + '\n')
        #     self.body.append('</div>\n')
        # self.body.append('<div class="panel-body">')
        pass

    def depart_panel(self, node):
        # self.body.append('</div>\n')
        # if node['footer']:
        #     self.body.append('<div class = "panel-footer">\n')
        #     self.body.append(node['footer'] + '\n')
        #     self.body.append('</div>\n')
        # self.body.append('</div>\n')
        pass


    def visit_button(self, node):
        types = { 'default' : 'btn-default',  'primary' : 'btn-primary',
                  'success' : 'btn-success',  'info'    : 'btn-info',
                  'warning' : 'btn-warning',  'danger'  : 'btn-danger',
                  'link'    : 'btn-link',      'outline' : 'btn-outline' }
        sizes = { 'tiny'    : 'btn-xs',        'small'   : 'btn-sm',
                  'default' : '',              'large'   : 'btn-lg' }

        target = node['target']
        classes = 'btn'
        properties = ''

        # Type
        classes += ' ' + types[node['type']]

        # Size
        classes += ' ' + sizes[node['size']]

        # Active
        if node['active']:
            classes += ' active'

        # Disabled
        if node['disabled']:
            if target:
                properties += ' disabled="disabled"'
            else:
                classes += ' disabled'

        # Active
        if node['block']:
            classes += ' btn-block'

        # Data toggle
        if node['toggle']:
            classes += ' dropdown-toggle '
            properties += ' data-toggle="dropdown"'

        if target:
            properties += ' role="button"'
            anchor = '<a href="%s" class="%s" %s>' % (target,classes,properties)
            self.body.append(anchor)
        else:
            properties += ' type="button"'
            button = '<button class="%s" %s>' % (classes,properties)
            self.body.append(button)

        #type = type_to_class.get(node['type'], 'btn-default')
        #size = size_to_class.get(node['size'], 'default')
        #active = 'active ' if node['active'] else ''
        #block = 'btn-block' if node['block'] else ''
        # toggle = 'data-toggle="dropdown"' if node['toggle'] else ''
        #target = node.get('target', '')
        # if len(target):
        #     anchor = '<a href="%s" class="btn %s %s %s %s" role="button">'
        #     if node['disabled']:
        #         anchor = '<a href="%s" type="button" class="btn %s %s %s %s disabled">'
        #     ref = '#'
        #     self.body.append(anchor % (ref, type, size, active, block))
        # else:
        #     button = '<button type="button" class="btn %s %s %s %s">'
        #     if node['disabled']:
        #         button = '<button type="button" class="btn %s %s %s %s" disabled="disabled">'
        #     self.body.append(button % (type, size, active, block))

    def depart_button(self, node):
        if node['target']:
            self.body.append('</a>\n')
        else:
            self.body.append('</button>\n')

    def visit_progress(self, node):

        label = node['label']
        classes = 'progress-bar '
        classes += 'progress-bar-%s' %  node['type']
        properties = 'role="progress-bar"'
        properties += ' aria-valuenow="%d"' % node['value']
        properties += ' aria-valuemin="%d"' % node['value_min']
        properties += ' aria-valuemax="%d"' % node['value_max']
        properties += ' style="width: %d%%";' % node['value']
        if node['animated']:
            self.body.append('<div class="progress progress-striped active">')
        elif node['striped']:
            self.body.append('<div class="progress progress-striped">')
        else:
            self.body.append('<div class="progress">')
        self.body.append(
            '<div class="%s" %s>%s</div>' % (classes,properties,label))
        self.body.append('</div>')
        raise nodes.SkipNode

    def visit_alert(self, node):
        self.body.append(self.starttag(node, 'div', CLASS='alert'))
        if node.dismissable:
            self.body.append(
                u"""<button type="button" class="close" data-dismiss="alert" """
                u"""aria-hidden="true">×</button>""")

    def depart_alert(self, node):
        self.body.append('</div>\n')

    def visit_callout(self, node):
        self.body.append(self.starttag(node, 'div', CLASS='bs-callout'))

    def depart_callout(self, node):
        self.body.append('</div>\n')


    # def visit_mute(self, node):
    #     pass

    # def depart_mute(self, node):
    #     pass

    # overwritten
    def visit_definition_list(self, node):
        list_class = node.parent.get('list-class', [])
        list_class.append('docutils')
        list_class = ' '.join(list_class)
        self.body.append(self.starttag(node, 'dl', CLASS=list_class))

    # overwritten
    def visit_sidebar(self, node):
        self.body.append(self.starttag(node, 'div', CLASS='col-md-3 col-md-push-9'))
        self.body.append(self.starttag(node, 'div', CLASS='bs-docs-sidebar hidden-print affix-top'))
        self.body.append(self.starttag(node, 'div', CLASS='sidebar'))
        self.set_first_last(node)
        self.in_sidebar = True

    # overwritten
    def depart_sidebar(self, node):
        self.body.append('</div>\n')
        self.body.append('</div>\n')
        self.body.append('</div>\n')
        #  Opening tag for body
        self.body.append(self.starttag(node, 'div', CLASS='col-md-9 col-md-pull-3'))
        self.in_sidebar = False

    # overwritten : removed compact paragraph
    # def visit_paragraph(self, node):
    #     if self.should_be_compact_paragraph(node):
    #         self.context.append('')
    #     else:
    #         self.body.append(self.starttag(node, 'p', ''))
    #     self.context.append('</p>\n')

    # overwritten: remove border=1, replace docutils/table class
    def visit_table(self, node):
        self.context.append(self.compact_p)
        self.compact_p = True
        #classes = ' '.join(['docutils', self.settings.table_style]).strip()
        classes = ' '.join(['table', self.settings.table_style]).strip()
        self.body.append(self.starttag(node, 'table', CLASS=classes))

    # overwritten : removed 'container' class
    def visit_container(self, node):
        self.body.append(self.starttag(node, 'div', CLASS=''))

    # def visit_header(self, node):
    #     self.context.append(len(self.body))

    # overwritten: get rid of <hr> tag
    def depart_header(self, node):
        start = self.context.pop()
        header = [self.starttag(node, 'div', CLASS='header')]
        header.extend(self.body[start:])
        header.append('\n</div>\n')
        self.body_prefix.extend(header)
        self.header.extend(header)
        del self.body[start:]

    # overwritten: get rid of <hr> tag
    def depart_footer(self, node):
        start = self.context.pop()
        footer = [self.starttag(node, 'div', CLASS='footer')]
        footer.extend(self.body[start:])
        footer.append('\n</div>\n')
        self.footer.extend(footer)
        self.body_suffix[:0] = footer
        del self.body[start:]

    # overwritten
    def depart_document(self, node):
        self.head_prefix.extend([self.doctype,
                                 self.head_prefix_template %
                                 {'lang': self.settings.language_code}])
        self.html_prolog.append(self.doctype)
        self.meta.insert(0, self.content_type % self.settings.output_encoding)
        self.head.insert(0, self.content_type % self.settings.output_encoding)
        if self.math_header:
            self.head.append(self.math_header)
        # skip content-type meta tag with interpolated charset value:
        self.html_head.extend(self.head[1:])
        # self.body_prefix.append(self.starttag(node, 'div', CLASS='document'))
        self.body_prefix.append(self.starttag(node, 'div', CLASS='container'))
        # self.body_suffix.insert(0, '</div>\n')
        self.fragment.extend(self.body) # self.fragment is the "naked" body
        self.html_body.extend(self.body_prefix[1:] + self.body_pre_docinfo
                              + self.docinfo + self.body
                              + self.body_suffix[:-1])
        assert not self.context, 'len(context) = %s' % len(self.context)




# -----------------------------------------------------------------------------
from docutils.core import publish_cmdline, publish_parts, default_description
description = ('Generates (X)HTML bootstrap-ready documents from standalone reStructuredText '
               'sources.  ' + default_description)
publish_cmdline(writer=HTMLWriter(),
                writer_name='bootstrap',
                description=description)
