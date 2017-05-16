# 第八章 异常
# raise 语句
>>> raise Exception
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise Exception
Exception
>>> raise Exception('yichang')                                // 这里添加了错误信息
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    raise Exception('yichang')
Exception: yichang

>>> import math
>>> dir(math)                                                //可以使用 dir 函数列出模块的内容
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

class SomeCustomException(Exception):pass                   // 编写自定义异常类

try:
	x=input('enter the first number:')
	y=input('enter the second number:')
	print(x/y)
except ZeroDivisionError:
	print('the second number can not be zero!')

class muffledcalculator:
	muffled=False
	def calc(self,expr):
		try:
			return eval(expr)
		except ZeroDivisionError:
			if self.muffled:
				print('Division by zero is illegal!')
			else:
				raise

>>> calculator=muffledcalculator()
>>> calculator.calc('10/2')
5.0
>>> calculator.calc('10/0')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    calculator.calc('10/0')
  File "<pyshell#1>", line 5, in calc
    return eval(expr)
  File "<string>", line 1, in <module>
ZeroDivisionError: division by zero
>>> calculator.muffled=True                  // 屏蔽机制打开
>>> calculator.calc('10/0')
Division by zero is illegal!

# 多个except
try:
	x=input('enter the first number:')
	y=input('enter the second number:')
	print(x/y)
except ZeroDivisionError:
	print('the second number can not be zero!')
except TypeError:                                          // 加入 except 捕捉其他异常
	print('that was not a number,was it?')

# 用一个块捕捉两个异常
try:
	x=input('enter the first number:')
	y=input('enter the second number:')
	print(x/y)
except (ZeroDivisionError,TypeError,NameError):           // 这里使用 () 将多个异常信息放在一起
	print('your numbers were bogus...')

# except 访问对象本身
try:
	x=input('enter the first number:')
	y=input('enter the second number:')
	print(x/y)
except (ZeroDivisionError,TypeError) as e:                // 访问对象本身返回的异常信息
	print(e)

# 捕捉所有的异常
try:
	x=input('enter the first number:')
	y=input('enter the second number:')
	print(x/y)
except Exception as e:                                   // except 后面不加，返回异常本身，可以捕捉所有的异常
	print(e)

# 加入 else 子句
while True:
    try:
        x=input('enter the first number:')
        y=input('enter the second number:')
        value=x/y
        print('x/y is ',value)
    except:
        print('Invalid input.please try again.')
    else:                                                // 这里 else 循环只有在没有异常引发的情况下才会发生
        break
enter the first number:1
enter the second number:0
Invalid input.please try again.
enter the first number:1
enter the second number:'z'
Invalid input.please try again.
enter the first number:1
enter the second number:2
('x/y is ', 0)

while True:
    try:
        x=input('enter the first number:')
        y=input('enter the second number:')
        value=x/y
        print('x/y is ',value)
    except Exception as e:
        print('Invalid input:',e)                        // 打印出更加有用的错误信息
        print('please try again')
    else:                                                // 这里 else 循环只有在没有异常引发的情况下才会发生
        break

def describePerson(person):
	print('Description',person['name'])
	print('Age:',person['age'])
	try：                                                // 这里使用 try except 来查询字典中是否包含另一个字段
		print('Occupation:'+person['occupation'])
	except KeyError:
		pass
