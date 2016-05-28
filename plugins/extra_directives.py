from __future__ import unicode_literals

from docutils import nodes
from docutils.parsers.rst import Directive, directives


class ImageLinkBlock(Directive):
    """
    Usage:
    .. image-link:: <link_to_image>
        :link-attr: <attributes for the link>
        :img-attr: <attributes for the image>
    """
    required_arguments = 1
    optional_arguments = 2
    has_content = False
    CODE = '\
    <a href="{0}" {1}><img src="{0}" {2} /></a>\
    '

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        url = ' '.join(self.arguments)

        return [nodes.raw('', self.CODE.format(
            url,
            self.options.get('link-attr', ''),
            self.options.get('img-attr', ''),
        ), format='html')]


class PostImageBlock(Directive):
    """
    Usage:
    .. post-image:: <link_to_image>
    """
    required_arguments = 1
    has_content = False
    IMG_DEFAULT_ATTRIBUTES = {
        'max-width': '250px',
        'class': 'align-center'
    }

    LINK_DEFAULT_ATTRIBUTES = {
        'class': 'colorbox',
        'align': 'center',
    }

    CODE = '\
    <a href="{0}" {1}><img src="{0}" {2} /></a>\
    '

    @classmethod
    def build_attributes(cls, attrs):
        ''' makes a string out of a dictionary of attributes '''
        return ' '.join(('{}="{}"'.format(k, v) for k, v in attrs.iteritems()))

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        url = ' '.join(self.arguments)

        return [nodes.raw('', self.CODE.format(
            url,
            self.build_attributes(self.LINK_DEFAULT_ATTRIBUTES),
            self.build_attributes(self.IMG_DEFAULT_ATTRIBUTES),
        ), format='html')]


class HtmlTag(Directive):
    optional_arguments = 10
    has_content = True
    tag = 'div'

    CODE = '\
    <{0} {1}>{2}</{0}>'

    @classmethod
    def build_attributes(cls, attrs):
        ''' makes a string out of a dictionary of attributes '''
        return ' '.join(('{}="{}"'.format(k, v) for k, v in attrs.iteritems()))

    def run(self):
        return [nodes.raw('', self.CODE.format(
            self.tag,
            self.build_attributes(self.options),
            '\n'.join(self.content),
        ), format='html')]


class SectionTag(HtmlTag):
    tag = 'section'

# Copyright (c) 2012 Roberto Alsina y otros.

# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of
# the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
# OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

CODE = """\
<iframe src="http://www.youtube.com/embed/{yid}?rel=0&amp;hd=1&amp;wmode=transparent"
style="border: 0;"></iframe>"""


class Youtube(Directive):
    """ Restructured text extension for inserting youtube embedded videos

    Usage:
        .. youtube:: lyViVmaBQDg
    """
    has_content = True
    required_arguments = 1

    def run(self):
        self.check_content()
        options = {
            'yid': self.arguments[0],
        }
        options.update(self.options)
        return [nodes.raw('', CODE.format(**options), format='html')]

    def check_content(self):
        if self.content:
            raise self.warning("This directive does not accept content. The "
                               "'key=value' format for options is deprecated, "
                               "use ':key: value' instead")


directives.register_directive('youtube', Youtube)
directives.register_directive('image-link', ImageLinkBlock)
directives.register_directive('post-image', PostImageBlock)
directives.register_directive('section', SectionTag)
