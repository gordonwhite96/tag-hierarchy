#Tool for demo-ing tag hierarchy.

## Steps
1.  Org structure in tagload.csv.  The last column is a driver.  Preceding columns are tags.
2.  Build a config.py with token='abc123' and group=1234
3.  Run load.py to build the drivers and tags
4.  Run org-tags.py to set the driver to their base tag
5.  Run hierarchy.py to build the tag relationship
6.  Run undo-hierarchy.py to remove the tag relationship

**Contact gordon@samsara.com for more info**
