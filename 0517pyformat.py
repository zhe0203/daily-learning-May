# 使用% and .format()
# basic formatting
>>> '%s %s' % ('one','two')
'one two'
>>> '{} {}'.format('one','two')
'one two'
>>> '%d %d' % (1,2)
'1 2'
>>> '{} {}'.format(1,2)
'1 2'
>>> '{1} {0}'.format('one','two')       // 使用索引来定位数据的位置
'two one'

# value conversion 变量转换
# 如果想产生str() repr() 可以使用!s !r来转换
# %s %r 也是可行的
>>> class Data(object):
	def __str__(self):
		return 'str'
	def __repr__(self):
		return 'repr'
>>> '%s %r' % (Data(),Data())
'str repr'
>>> '{0!s} {0!r}'.format(Data())
'str repr'

# 填充和对齐字符串
>>> '%10s' % ('test')              // 老版默认右对齐
'      test'
>>> '{:>10}'.format('test')        // 右对齐
'      test'

>>> '%-10s'%('test')               // 左对齐
'test      '
>>> '{:10}'.format('test')         // 左对齐
'test      '

>>> '%*s'%((-8),'test')            // 添加索引变量值
'test    '
>>> '{:<{}s}'.format('test',8)
'test    '

>>> '{:_<10}'.format('test')        // 添加空值填充格式
'test______'
>>> '{:^10}'.format('test')          // 居中对齐
'   test   '

# 截断长字符串
>>> '%.5s' % ('xylophone')
'xylop'
>>> '{:.5}'.format('xylophone')     // 使用小数点 . 表示截取数据
'xylop'
>>> '%.*s' % (7,'xylophone')         // 添加相应参数
'xylopho'
>>> '{:.{}}'.format('xylophone',7)
'xylopho'

>>> '%-10.5s' % ('xylophone')         // 修改截取后数据的长度
'xylop     '
>>> '{:10.5}'.format('xylophone')
'xylop   '
>>> '{:_<10.5}'.format('xylophone')    // 添加空值填充格式
'xylop_____'

# 数字变换
>>> '%d' % 32
'32'
>>> '{:d}'.format(32)
'32'
import math
>>> '%f' % (math.pi)                  // 浮点型
'3.141593'
>>> '{:f}'.format(math.pi)
'3.141593'
>>> '%4d' % (32,)
'  32'
>>> '{:4d}'.format(32)
'  32'
>>> '%06.2f' % (math.pi)
'003.14'
>>> '{:06.2f}'.format(math.pi)
'003.14'
>>> '%04d' % (32,)
'0032'
>>> '{:04d}'.format(32)
'0032'

# signed numbers
>>> '%+d' % (32,)
'+32'
>>> '{:+d}'.format(32)
'+32'
>>> '% d' % ((-23),)            // 使用空格来表示负值
'-23'
>>> '{: d}'.format((-23))
'-23'
>>> '{:=5d}'.format((-23))      // 使用 = 来空值负号的位置
'-  23'

# named placeholders
>>> '%(first)s %(last)s' % data
'hodor hodor!'
>>> '{first} {last}'.format(**data)
'hodor hodor!'
>>> '{first} {last}'.format(first='Hodor', last='Hodor!')  // 可修改变量值
'Hodor Hodor!'
>>> data=[12,312,123,34,12,79]
>>> '{d[3]} {d[2]}'.format(d=data)       // 索引值
'34 123'

>>> from datetime import datetime 
>>> '{:%Y-%m-%d %H:%M}'.format(datetime(2001,2,3,4,5))     // 时间格式
'2001-02-03 04:05'
