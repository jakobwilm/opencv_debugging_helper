from dumper import Children, SubItem
from utils import TypeCode, DisplayFormat

def qform__cv__Mat():
    return [DisplayFormat.Simple, DisplayFormat.Separate]

def qdump__cv__Mat(d, value):
    # faster but potentially version-breaking
    # (flag, dims, rows, cols, data, refcount, datastart, dataend,
    #  datalimit, allocator, size, stepp) \
    #     = value.split('iiiipppppppp')
        
    dims = value['dims'].integer()
    if dims != 2:
        d.putEmptyValue()
        d.putPlainChildren(value)
        return

    rows = value['rows'].integer()
    cols = value['cols'].integer()

    flags = value['flags'].integer()
    channels = 1 + (flags >> 3) & 63
    depth = flags & 7

    cvTypeName = ['8U', '8S', '16U', '16S', '32S', '32F', '64F'][depth]

    d.putValue('%dx%d %sC%d' % (rows, cols, cvTypeName, channels))

    d.putNumChild(1)
    if d.isExpanded():
        address = value["data"].pointer()
        step = value['step']['p'].dereference().integer()
        typeName = ['uchar', 'char', 'ushort', 'short', 'int', 'float', 'double'][depth]
        elemSize = [1,1,2,2,4,4,8][depth]
        with Children(d):
            with SubItem(d, "elements"):
                s = "0x%x" % value["data"].pointer()
                d.putValue(d.hexencode(s), "utf8:1:1")
                d.putNumChild(rows)
                with Children(d):
                    for i in range(rows):
                        if channels == 1:
                            d.putArrayItem('[%d]' % i, address + i*step, cols, typeName)
                        else:
                            with SubItem(d, '[%d]' % i):
                                with Children(d):
                                    for j in range(cols):
                                        d.putArrayItem('[%d]' % j, address + i*step + j*channels*elemSize, channels, typeName)
            
            # put plain children
            d.putFields(value, True)

    # Note: displaying as image in a seperate window currently does not work on most platforms
    # https://bugreports.qt.io/browse/QTCREATORBUG-21233
    if d.currentItemFormat() == DisplayFormat.Separate:
        rs = steps[0] * innerSize
        cs = cols * innerSize
        dform = 'arraydata:separate:int:%d::2:%d:%d' % (innerSize, cols, rows)
        out = ''.join(d.readMemory(data + i * rs, cs) for i in range(rows))
        d.putDisplay(dform, out)


def qdump__cv__Size_(d, value):
    height = value['height']
    width = value['width']
    d.putNumChild(0)
    d.putValue('(%dx%d)' % (width, height))
    d.putType('cv::Size_')
