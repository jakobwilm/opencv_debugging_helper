#

import dumper
import numpy

def qform__cv__Mat():
	return 'Normal,Displayed'
	#return 'Normal'

def qdump__cv__Mat(d, value):
	#ptrSize = d.ptrSize()

	flags = value['flags']
	channels = 1 + (flags >> 3) & 63;
	rows = int(value['rows'])
	cols = int(value['cols'])
	d.putValue('(%dx%dx%d)' % (rows, cols, channels))

	depth = flags & 7
	if depth == 0:
		cvTypeName = 'CV_8U'
	elif depth == 1:
		cvTypeName = 'CV_8S'
	elif depth == 2:
		cvTypeName = 'CV_16U'
	elif depth == 3:
		cvTypeName = 'CV_16S'
	elif depth == 4:
		cvTypeName = 'CV_32S'
	elif depth == 5:
		cvTypeName = 'CV_32F'
	elif depth == 6:
		cvTypeName = 'CV_64F'

	#data = v['data'].cast(gdb.lookup_type("char").pointer())
	d.putNumChild(1)
	if d.isExpanded():
		with dumper.Children(d):
			#d.putIntItem('width', width)
			d.putIntItem('cols', cols)
			d.putIntItem('channels', channels)
			#d.putIntItem('data', value['data'])
			d.putIntItem('dims', value['dims'])
			d.putIntItem('rows', rows)
			d.putIntItem('size', value['size']['p'].dereference())
			d.putIntItem('step', value['step']['p'].dereference())
			with dumper.SubItem(d, 'type'):
				d.putValue(cvTypeName)
				d.putNumChild(0)
			d.putIntItem('flags', flags)
			d.putIntItem('refcount', value['u']['refcount'])

			with dumper.SubItem(d, "data"):
				d.putNumChild(rows)
				base = value["data"].dereference()
				#elemSize = base.type.size()
				elemSize = 1
				with dumper.Children(d):
					for i in range(cols):
						d.putArrayItem('[%d]' %i, value["data"] + elemSize*i*cols, rows, base.type.name)
		
	format = d.currentItemFormat()
	if format == 1:
		d.putDisplay(StopDisplay)
	#elif format == 2:
		#if dims == 2:
			#img = cv2.cv.CreateImageHeader((cols,rows), depth, channels)
			#bytes = value['step'] * value['rows']
			#cv2.cv.SetData(img, d.readMemory(value['data'], bytes))
			#if channels == 1:
				#cv2.cv.CvtColor(img, img, cv2.cv.CV_GRAY2RGB)
			#d.putField("editformat", DisplayImageData)
			#d.put('editvalue="')
			#d.put('%08x%08x%08x%08x' % (cols, rows, byteSize, 13))
			#d.put(img.data)
			#d.put('",')

def qdump__cv__Size_(d, value):
	height = value['height']
	width = value['width']
	d.putNumChild(0)
	d.putValue('(%dx%d)' % (width, height))
	d.putType('cv::Size_')



