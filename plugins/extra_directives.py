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
        'width': '250px',
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
        return ' '.join(("{}={}".format(k, v) for k, v in attrs.iteritems()))

    def run(self):
        """ Required by the Directive interface. Create docutils nodes """
        url = ' '.join(self.arguments)

        return [nodes.raw('', self.CODE.format(
            url,
            self.build_attributes(self.LINK_DEFAULT_ATTRIBUTES),
            self.build_attributes(self.IMG_DEFAULT_ATTRIBUTES),
        ), format='html')]


directives.register_directive('image-link', ImageLinkBlock)
directives.register_directive('post-image', PostImageBlock)
