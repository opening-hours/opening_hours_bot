#!/usr/bin/env python
# encoding: utf-8

# modules {{{
import logging, sys
import xml.etree.ElementTree as ET

logging.basicConfig(
    format='%(levelname)s: %(message)s',
    # level=logging.DEBUG,
    level=logging.INFO,
    )
# }}}


# Called for each object (node, way).
def for_object(object_root):
    for tag in object_root.findall('tag'):
        if tag.attrib['k'] == 'opening_hours':
            # tag.set('v', 'yes')
            print tag.attrib['v']

# main {{{
def main(osm_file):
    osm_xml_root = ET.parse(osm_file)
    osm_xml = osm_xml_root.getroot()

    logging.info(u'Parsing OSM file version "%s" generated by %s …' % (osm_xml.attrib['version'], osm_xml.attrib['generator']))
    for node in osm_xml_root.findall('node'):
        for_object(node)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        osm_file = sys.argv[1]
    else:
        logging.error('Not enough parameters.'
                + ' 1. File path OSM file.'
                )
        sys.exit(1)
    main(osm_file)
# }}}