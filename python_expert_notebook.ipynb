{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# What Does It Take to Be An Expert At Python"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Notebook based off James Powell's talk at PyData 2017'\n",
    "https://www.youtube.com/watch?v=7lmCu8wz8ro\n",
    "\n",
    "If you want to become an expert in Python, you should definitely watch this PyData talk from James Powell."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Video Index\n",
    "* metaclasses: 18:50\n",
    "* metaclasses(explained): 40:40\n",
    "* decorator: 45:20\n",
    "* generator: 1:04:30\n",
    "* context manager: 1:22:37\n",
    "* summary: 1:40:00"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Definitions**\n",
    "    Python is a language orientated around protocols - Some behavior or syntax or bytecode or some top level function and there is a way to tell python how to implement that on an arbitrary object via underscore methods. The exact correspondance is usually guessable, but if you can't guess it you can it... google python data model\n",
    "\n",
    "**Metaclass**\n",
    "    Mechanism: Some hook into the class construction process. Questions: Do you have these methods implemented.\n",
    "    Meaning: Library code & User code? How do you enforce a constraint? \n",
    "    \n",
    "**Decorator**\n",
    "    Hooks into idea that everything creates a structure at run time. Wrap sets of functions with a before and after behavior. \n",
    "\n",
    "**Generators** \n",
    "    Take a single computation that would otherwise run eagerly from the injection of its parameters to the final computation and interleaving with other code by adding yield points where you can yield the intermediate result values or one small piece of the computation and also yield back to the caller. Think of a generator of a way to take one long piece of computation and break it up into small parts.\n",
    "    \n",
    "**Context managers**\n",
    "    Two structures that allow you to tie two actions together. A setup action and a teardown action and make sure they always happen in concordance with each other."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# some behavior that I want to implement -> write some __ function __\n",
    "# top-level function or top-level syntax -> corresponding __\n",
    "# x + y -> __add__\n",
    "# init x -> __init__\n",
    "# repr(x) --> __repr__\n",
    "# x() -> __call__\n",
    "\n",
    "class Polynomial:\n",
    "    def __init__(self, *coeffs):\n",
    "        self.coeffs = coeffs\n",
    "        \n",
    "    def __repr__(self):\n",
    "        return 'Polynomial(*{!r})'.format(self.coeffs)\n",
    "    \n",
    "    def __add__(self, other):\n",
    "        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))\n",
    "    \n",
    "    def __len__(self):\n",
    "        return len(self.coeffs)\n",
    "    \n",
    "    def __call__(self):\n",
    "        pass\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3 Core Patterns to understand object orientation\n",
    "* Protocol view of python\n",
    "* Built-in inheritance protocol (where to go)\n",
    "* Caveats around how object orientation in python works"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "p1 = Polynomial(1, 2, 3)\n",
    "p2 = Polynomial(3, 4, 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Polynomial(*(5, 7, 7))"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "p1 + p2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(p1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Metaclasses"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# File 1 - library.py\n",
    "\n",
    "class Base:\n",
    "    def food(self):\n",
    "        return 'foo'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "you broke it, you fool!",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-27-08fa6af0fb76>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# File2 - user.py\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32massert\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBase\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'foo'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"you broke it, you fool!\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0;32mclass\u001b[0m \u001b[0mDerived\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mBase\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAssertionError\u001b[0m: you broke it, you fool!"
     ]
    }
   ],
   "source": [
    "# File2 - user.py\n",
    "\n",
    "assert hasattr(Base, 'foo'), \"you broke it, you fool!\"\n",
    "\n",
    "class Derived(Base):\n",
    "    def bar(self):\n",
    "        return self.foo"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "# File 1 - library.py\n",
    "\n",
    "class Base:\n",
    "    def foo(self):\n",
    "        return self.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "# File2 - user.py\n",
    "\n",
    "assert hasattr(Base, 'foo'), \"you broke it, you fool!\"\n",
    "\n",
    "class Derived(Base):\n",
    "    def bar(self):\n",
    "        return 'bar'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.Derived.bar>"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Derived.bar"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def _():\n",
    "    class Base:\n",
    "        pass\n",
    "\n",
    "from dis import dis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  2           0 LOAD_BUILD_CLASS\n",
      "              2 LOAD_CONST               1 (<code object Base at 0x10f2daed0, file \"<ipython-input-18-a194b247271c>\", line 2>)\n",
      "              4 LOAD_CONST               2 ('Base')\n",
      "              6 MAKE_FUNCTION            0\n",
      "              8 LOAD_CONST               2 ('Base')\n",
      "             10 CALL_FUNCTION            2\n",
      "             12 STORE_FAST               0 (Base)\n",
      "             14 LOAD_CONST               0 (None)\n",
      "             16 RETURN_VALUE\n"
     ]
    }
   ],
   "source": [
    "\n",
    "dis(_) # LOAD_BUILD_CLASS"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Catch Building of Classes\n",
    "\n",
    "class Base:\n",
    "    def foo(self):\n",
    "        return self.bar()\n",
    "\n",
    "old_bc = __build_class__\n",
    "def my_bc(*a, **kw):\n",
    "    print('my buildclass ->', a, kw)\n",
    "    return old_bc(*a, **kw)\n",
    "import builtins\n",
    "builtins.__build_class__ = my_bc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Catch Building of Classes\n",
    "\n",
    "class Base:\n",
    "    def foo(self):\n",
    "        return self.bar()\n",
    "\n",
    "old_bc = __build_class__\n",
    "def my_bc(fun, name, base=None, **kw):\n",
    "    if base is Base:\n",
    "                print('Check if bar method defined')\n",
    "    if base is not None:\n",
    "        return old_bc(fun, name, base, **kw)\n",
    "    return old_bc(fun, name, **kw)\n",
    "\n",
    "import builtins\n",
    "builtins.__build_class__ = my_bc"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import builtins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<module 'builtins' (built-in)>"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import importlib\n",
    "importlib.reload(builtins)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BaseMeta.__new__ <class '__main__.BaseMeta'> Base () {'__module__': '__main__', '__qualname__': 'Base', 'foo': <function Base.foo at 0x107378048>}\n"
     ]
    }
   ],
   "source": [
    "class BaseMeta(type):\n",
    "    def __new__(cls, name, bases, body):\n",
    "        print('BaseMeta.__new__', cls, name, bases, body)\n",
    "        return super().__new__(cls, name, bases, body)\n",
    "\n",
    "class Base(metaclass=BaseMeta):\n",
    "    def foo(self):\n",
    "        return self.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my buildclass -> (<function BaseMeta at 0x10749cf28>, 'BaseMeta', <class 'type'>) {}\n"
     ]
    },
    {
     "ename": "RecursionError",
     "evalue": "maximum recursion depth exceeded",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRecursionError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-167-f2133308a9ce>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mclass\u001b[0m \u001b[0mBaseMeta\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtype\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__new__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbases\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;34m'bar'\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m             \u001b[0;32mraise\u001b[0m \u001b[0mTypeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'bad user class'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0msuper\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__new__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcls\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbases\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbody\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-165-f7e591caa0e8>\u001b[0m in \u001b[0;36mmy_bc\u001b[0;34m(*a, **kw)\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0;32mdef\u001b[0m \u001b[0mmy_bc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'my buildclass ->'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mold_bc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mbuiltins\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0mbuiltins\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__build_class__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mmy_bc\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-1-8d1486f0ff44>\u001b[0m in \u001b[0;36mmy_bc\u001b[0;34m(fun, name, base, **kw)\u001b[0m\n\u001b[1;32m     10\u001b[0m                 \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Check if bar method defined'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mbase\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mold_bc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfun\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbase\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mold_bc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfun\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "... last 1 frames repeated, from the frame below ...\n",
      "\u001b[0;32m<ipython-input-1-8d1486f0ff44>\u001b[0m in \u001b[0;36mmy_bc\u001b[0;34m(fun, name, base, **kw)\u001b[0m\n\u001b[1;32m     10\u001b[0m                 \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Check if bar method defined'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mbase\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 12\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mold_bc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfun\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mbase\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     13\u001b[0m     \u001b[0;32mreturn\u001b[0m \u001b[0mold_bc\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfun\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkw\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     14\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mRecursionError\u001b[0m: maximum recursion depth exceeded"
     ]
    }
   ],
   "source": [
    "class BaseMeta(type):\n",
    "    def __new__(cls, name, bases, body):\n",
    "        if not 'bar' in body:\n",
    "            raise TypeError('bad user class')\n",
    "        return super().__new__(cls, name, bases, body)\n",
    "\n",
    "class Base(metaclass=BaseMeta):\n",
    "    def foo(self):\n",
    "        return self.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "class BaseMeta(type):\n",
    "    def __new__(cls, name, bases, body):\n",
    "        if name != 'Base' and not 'bar' in body:\n",
    "            raise TypeError('bad user class')\n",
    "        return super().__new__(cls, name, bases, body)\n",
    "\n",
    "class Base(metaclass=BaseMeta):\n",
    "    def foo(self):\n",
    "        return self.bar()\n",
    "    \n",
    "    def __init_subclass__(*a, **kw):\n",
    "        print('init_subclass', a, kw)\n",
    "        return super().__init_subclass__(*a, **kw)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on method __init_subclass__ in module __main__:\n",
      "\n",
      "__init_subclass__(*a, **kw) method of __main__.BaseMeta instance\n",
      "    This method is called when a class is subclassed.\n",
      "    \n",
      "    The default implementation does nothing. It may be\n",
      "    overridden to extend subclasses.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(Base.__init_subclass__)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Decorators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# dec.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def add(x, y=10):\n",
    "    return x + y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add(10, 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.add>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'add'"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Name of function\n",
    "add.__name__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'__main__'"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# What module function is assigned to\n",
    "add.__module__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10,)"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Default values\n",
    "add.__defaults__"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "b'|\\x00|\\x01\\x17\\x00S\\x00'"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Byte code for function\n",
    "add.__code__.co_code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('x', 'y')"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Variable names function interacts with\n",
    "add.__code__.co_varnames"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What's your source code?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "from inspect import getsource"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'def add(x, y=10):\\n    return x + y\\n'"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "getsource(add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "def add(x, y=10):\n",
      "    return x + y\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(getsource(add))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<ipython-input-19-3cec442ba064>'"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# What file are you in? \n",
    "from inspect import getfile\n",
    "getfile(add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<module '__main__'>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from inspect import getmodule\n",
    "getmodule(add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "add(10) 20\n",
      "add(20, 30) 50\n",
      "add(\"a\", \"b\") ab\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', add(10))\n",
    "print('add(20, 30)', add(20, 30))\n",
    "print('add(\"a\", \"b\")', add(\"a\", \"b\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#Count how long it took to run"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def add_timer(x, y=10):\n",
    "    before = time()\n",
    "    rv = x + y\n",
    "    after = time()\n",
    "    print('elapsed:', after - before)\n",
    "    return rv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "elapsed: 0.0\n",
      "add(10) 20\n",
      "elapsed: 9.5367431640625e-07\n",
      "add(20, 30) 50\n",
      "elapsed: 9.5367431640625e-07\n",
      "add(\"a\", \"b\") ab\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', add_timer(10))\n",
    "print('add(20, 30)', add_timer(20, 30))\n",
    "print('add(\"a\", \"b\")', add_timer(\"a\", \"b\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### But what if we have multiple functions that require timing?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sub(x, y=10):\n",
    "    return x - y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sub(10) 0\n",
      "sub(20, 30) -10\n"
     ]
    }
   ],
   "source": [
    "print('sub(10)', sub(10))\n",
    "print('sub(20, 30)', sub(20, 30))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def timer(func, x, y=10):\n",
    "    before = time()\n",
    "    rv = func(x, y)\n",
    "    after = time()\n",
    "    print('elapsed', after - before)\n",
    "    return rv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "elapsed 9.5367431640625e-07\n",
      "add(10) 20\n",
      "elapsed 9.5367431640625e-07\n",
      "add(20, 30) 50\n",
      "elapsed 9.5367431640625e-07\n",
      "add(\"a\", \"b\") ab\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', timer(add, 10))\n",
    "print('add(20, 30)', timer(add, 20, 30))\n",
    "print('add(\"a\", \"b\")', timer(add, \"a\", \"b\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def timer(func):\n",
    "    def f(x, y=10):\n",
    "        before = time()\n",
    "        rv = func(x, y)\n",
    "        after = time()\n",
    "        print('elapsed', after - before)\n",
    "        return rv\n",
    "    return f"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "add = timer(add)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "elapsed 9.5367431640625e-07\n",
      "add(10) 20\n",
      "elapsed 9.5367431640625e-07\n",
      "add(20, 30) 50\n",
      "elapsed 9.5367431640625e-07\n",
      "add(\"a\", \"b\") ab\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', add(10))\n",
    "print('add(20, 30)', add(20, 30))\n",
    "print('add(\"a\", \"b\")', add(\"a\", \"b\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Don't need to do add = timer(add) with decorators..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "@timer\n",
    "def add_dec(x, y=10):\n",
    "    return x + y\n",
    "\n",
    "@timer\n",
    "def sub_dec(x, y=10):\n",
    "    return x - y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "elapsed 9.5367431640625e-07\n",
      "add(10) 20\n",
      "elapsed 1.1920928955078125e-06\n",
      "add(20, 30) 50\n",
      "elapsed 1.1920928955078125e-06\n",
      "add(\"a\", \"b\") ab\n",
      "elapsed 9.5367431640625e-07\n",
      "sub(10) 0\n",
      "elapsed 0.0\n",
      "sub(20, 30) -10\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', add_dec(10))\n",
    "print('add(20, 30)', add_dec(20, 30))\n",
    "print('add(\"a\", \"b\")', add_dec(\"a\", \"b\"))\n",
    "print('sub(10)', sub_dec(10))\n",
    "print('sub(20, 30)', sub_dec(20, 30))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Don't hardcode parameters in decorator functions\n",
    "def timer_k(func):\n",
    "    def f(*args, **kwargs):\n",
    "        before = time()\n",
    "        rv = func(*args, **kwargs)\n",
    "        after = time()\n",
    "        print('elapsed', after - before)\n",
    "        return rv\n",
    "    return f"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "elapsed 9.5367431640625e-07\n",
      "add(10) 20\n",
      "elapsed 9.5367431640625e-07\n",
      "add(20, 30) 50\n",
      "elapsed 9.5367431640625e-07\n",
      "add(\"a\", \"b\") ab\n",
      "elapsed 0.0\n",
      "sub(10) 0\n",
      "elapsed 9.5367431640625e-07\n",
      "sub(20, 30) -10\n"
     ]
    }
   ],
   "source": [
    "@timer_k\n",
    "def add_dec(x, y=10):\n",
    "    return x + y\n",
    "\n",
    "@timer_k\n",
    "def sub_dec(x, y=10):\n",
    "    return x - y\n",
    "\n",
    "print('add(10)', add_dec(10))\n",
    "print('add(20, 30)', add_dec(20, 30))\n",
    "print('add(\"a\", \"b\")', add_dec(\"a\", \"b\"))\n",
    "print('sub(10)', sub_dec(10))\n",
    "print('sub(20, 30)', sub_dec(20, 30))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# What if I want to run a function n number of times"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Let's have add run 3 times in a row and sub run twice in a row"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 97,
   "metadata": {},
   "outputs": [],
   "source": [
    "n = 2\n",
    "\n",
    "def ntimes(f):\n",
    "    def wrapper(*args, **kwargs):\n",
    "        for _ in range(n):\n",
    "            print('running {.__name__}'.format(f))\n",
    "            rv = f(*args, **kwargs)\n",
    "        return rv\n",
    "    return wrapper\n",
    "    \n",
    "        \n",
    "@ntimes\n",
    "def add_dec(x, y=10):\n",
    "    return x + y\n",
    "\n",
    "@ntimes\n",
    "def sub_dec(x, y=10):\n",
    "    return x - y\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "running add_dec\n",
      "running add_dec\n",
      "add(10) 20\n",
      "running add_dec\n",
      "running add_dec\n",
      "add(20, 30) 50\n",
      "running add_dec\n",
      "running add_dec\n",
      "add(\"a\", \"b\") ab\n",
      "running sub_dec\n",
      "running sub_dec\n",
      "sub(10) 0\n",
      "running sub_dec\n",
      "running sub_dec\n",
      "sub(20, 30) -10\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', add_dec(10))\n",
    "print('add(20, 30)', add_dec(20, 30))\n",
    "print('add(\"a\", \"b\")', add_dec(\"a\", \"b\"))\n",
    "print('sub(10)', sub_dec(10))\n",
    "print('sub(20, 30)', sub_dec(20, 30))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Higher Order Decorators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def ntimes(n):\n",
    "    def inner(f):\n",
    "        def wrapper(*args, **kwargs):\n",
    "            for _ in range(n):\n",
    "                print('running {.__name__}'.format(f))\n",
    "                rv = f(*args, **kwargs)\n",
    "            return rv\n",
    "        return wrapper\n",
    "    return inner\n",
    "    \n",
    "        \n",
    "@ntimes(2)\n",
    "def add_hdec(x, y=10):\n",
    "    return x + y\n",
    "\n",
    "@ntimes(4)\n",
    "def sub_hdec(x, y=10):\n",
    "    return x - y\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "running add_hdec\n",
      "running add_hdec\n",
      "add(10) 20\n",
      "running add_hdec\n",
      "running add_hdec\n",
      "add(20, 30) 50\n",
      "running add_hdec\n",
      "running add_hdec\n",
      "add(\"a\", \"b\") ab\n",
      "running sub_hdec\n",
      "running sub_hdec\n",
      "running sub_hdec\n",
      "running sub_hdec\n",
      "sub(10) 0\n",
      "running sub_hdec\n",
      "running sub_hdec\n",
      "running sub_hdec\n",
      "running sub_hdec\n",
      "sub(20, 30) -10\n"
     ]
    }
   ],
   "source": [
    "print('add(10)', add_hdec(10))\n",
    "print('add(20, 30)', add_hdec(20, 30))\n",
    "print('add(\"a\", \"b\")', add_hdec(\"a\", \"b\"))\n",
    "print('sub(10)', sub_hdec(10))\n",
    "print('sub(20, 30)', sub_hdec(20, 30))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Generators"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# gen.py - use whenever sequencing is needd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# top-level syntax, function -> underscore method\n",
    "# x()               __call__\n",
    "\n",
    "def add1(x, y):\n",
    "    return x + y\n",
    "\n",
    "class Adder:\n",
    "    def __call__(self, x, y):\n",
    "        return x + y\n",
    "add2 = Adder()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add1(10, 20)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 111,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "add2(10, 20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "# top-level syntax, function -> underscore method\n",
    "# x()               __call__\n",
    "\n",
    "def add1(x, y):\n",
    "    return x + y\n",
    "\n",
    "class Adder:\n",
    "    def __init__(self):\n",
    "        self.z = 0\n",
    "        \n",
    "    def __call__(self, x, y):\n",
    "        self.z += 1\n",
    "        return x + y + self.z\n",
    "\n",
    "add2 = Adder()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from time import sleep\n",
    "# This example has storage... and has eager return of the result sets\n",
    "def compute():\n",
    "    rv = []\n",
    "    for i in range(10):\n",
    "        sleep(.5)\n",
    "        rv.append(i)\n",
    "    return rv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "compute()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Wasteful because we have to wait for the entire action to complete and be read into memory, when we really just care about each number (one by one)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Compute:\n",
    "    def __call__(self):\n",
    "        rv = []\n",
    "        for i in range(100000):\n",
    "            sleep(5)\n",
    "            rv.append(i)\n",
    "        return rv\n",
    "    \n",
    "    def __iter__(self):\n",
    "        self.last = 0\n",
    "        return self\n",
    "    \n",
    "    def __next__(self):\n",
    "        rv = self.last\n",
    "        self.last += 1\n",
    "        if self.last > 10:\n",
    "            raise StopIteration()\n",
    "        sleep(.5)\n",
    "        return self.last\n",
    "        \n",
    "compute = Compute()\n",
    "\n",
    "# THIS IS UGLY... now let's make a generator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#This is a generator... don't eagerly compute. Return to user as they ask for it...\n",
    "\n",
    "def compute():\n",
    "    for i in range(10):\n",
    "        sleep(.5)\n",
    "        yield i"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [],
   "source": [
    "# for x in xs:\n",
    "#    pass\n",
    "\n",
    "# xi = iter(xs)    -> __iter__\n",
    "# while True:\n",
    "#   x = next(xi)   -> __next__\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "for val in compute():\n",
    "    print(val)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "class Api:\n",
    "    def run_this_first(self):\n",
    "        first()\n",
    "    def run_this_second(self):\n",
    "        second()\n",
    "    def run_this_last(self):\n",
    "        last()    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {},
   "outputs": [],
   "source": [
    "def api():\n",
    "    first()\n",
    "    yield\n",
    "    second()\n",
    "    yield\n",
    "    last()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Context Manager"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# cty.py\n",
    "\n",
    "from sqlite3 import connect"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "__enter__\n",
      "(1, 1)\n",
      "(1, 2)\n",
      "(2, 1)\n",
      "(2, 2)\n",
      "(9,)\n",
      "__exit__\n"
     ]
    }
   ],
   "source": [
    "# with ctx() as x:\n",
    "#   pass\n",
    "\n",
    "# x = ctx().__enter__\n",
    "# try:\n",
    "#   pass\n",
    "# finally:\n",
    "#    x.__exit__\n",
    "\n",
    "class temptable:\n",
    "    def __init__(self, cur):\n",
    "        self.cur = cur\n",
    "    def __enter__(self):\n",
    "        print('__enter__')\n",
    "        self.cur.execute('create table points(x int, y int)')\n",
    "    def __exit__(self, *args):\n",
    "        print('__exit__')\n",
    "        self.cur.execute('drop table points')\n",
    "\n",
    "with connect('test.db') as conn:\n",
    "    cur = conn.cursor()\n",
    "    with temptable(cur):\n",
    "        cur.execute('insert into points (x, y) values(1, 1)')\n",
    "        cur.execute('insert into points (x, y) values(1, 2)')\n",
    "        cur.execute('insert into points (x, y) values(2, 1)')\n",
    "        cur.execute('insert into points (x, y) values(2, 2)')\n",
    "        for row in cur.execute(\"select x, y from points\"):\n",
    "            print(row)\n",
    "        for row in cur.execute('select sum(x * y) from points'):\n",
    "            print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "rm test.db"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "created table\n",
      "(1, 1)\n",
      "(1, 2)\n",
      "(2, 1)\n",
      "(2, 2)\n",
      "(9,)\n",
      "dropped table\n"
     ]
    }
   ],
   "source": [
    "def temptable(cur):\n",
    "    cur.execute('create table points(x int, y int)')\n",
    "    print('created table')\n",
    "    yield\n",
    "    cur.execute('drop table points')\n",
    "    print('dropped table')\n",
    "    \n",
    "class contextmanager:\n",
    "    def __init__(self, cur):\n",
    "        self.cur = cur\n",
    "    def __enter__(self):\n",
    "        self.gen = temptable(self.cur)\n",
    "        next(self.gen)\n",
    "    def __exit__(self, *args):\n",
    "        next(self.gen, None)\n",
    "        \n",
    "with connect('test.db') as conn:\n",
    "    cur = conn.cursor()\n",
    "    with contextmanager(cur):\n",
    "        cur.execute('insert into points (x, y) values(1, 1)')\n",
    "        cur.execute('insert into points (x, y) values(1, 2)')\n",
    "        cur.execute('insert into points (x, y) values(2, 1)')\n",
    "        cur.execute('insert into points (x, y) values(2, 2)')\n",
    "        for row in cur.execute(\"select x, y from points\"):\n",
    "            print(row)\n",
    "        for row in cur.execute('select sum(x * y) from points'):\n",
    "            print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "created table\n",
      "(1, 1)\n",
      "(1, 2)\n",
      "(2, 1)\n",
      "(2, 2)\n",
      "dropped table\n"
     ]
    }
   ],
   "source": [
    "class contextmanager:\n",
    "    def __init__(self, gen):\n",
    "        self.gen = gen\n",
    "    def __call__(self, *args, **kwargs):\n",
    "        self.args, self.kwargs = args, kwargs\n",
    "        return self\n",
    "    def __enter__(self):\n",
    "        self.gen_inst = self.gen(*self.args, **self.kwargs)\n",
    "        next(self.gen_inst)\n",
    "    def __exit__(self, *args):\n",
    "        next(self.gen_inst, None)\n",
    "\n",
    "def temptable(cur):\n",
    "    cur.execute('create table points(x int, y int)')\n",
    "    print('created table')\n",
    "    yield\n",
    "    cur.execute('drop table points')\n",
    "    print('dropped table')\n",
    "temptable = contextmanager(temptable)\n",
    "            \n",
    "with connect('test.db') as conn:\n",
    "    cur = conn.cursor()\n",
    "    with temptable(cur):\n",
    "        cur.execute('insert into points (x, y) values(1, 1)')\n",
    "        cur.execute('insert into points (x, y) values(1, 2)')\n",
    "        cur.execute('insert into points (x, y) values(2, 1)')\n",
    "        cur.execute('insert into points (x, y) values(2, 2)')\n",
    "        for row in cur.execute(\"select x, y from points\"):\n",
    "            print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "created table\n",
      "(1, 1)\n",
      "(1, 2)\n",
      "(2, 1)\n",
      "(2, 2)\n",
      "dropped table\n"
     ]
    }
   ],
   "source": [
    "class contextmanager:\n",
    "    def __init__(self, gen):\n",
    "        self.gen = gen\n",
    "    def __call__(self, *args, **kwargs):\n",
    "        self.args, self.kwargs = args, kwargs\n",
    "        return self\n",
    "    def __enter__(self):\n",
    "        self.gen_inst = self.gen(*self.args, **self.kwargs)\n",
    "        next(self.gen_inst)\n",
    "    def __exit__(self, *args):\n",
    "        next(self.gen_inst, None)\n",
    "        \n",
    "@contextmanager\n",
    "def temptable(cur):\n",
    "    cur.execute('create table points(x int, y int)')\n",
    "    print('created table')\n",
    "    yield\n",
    "    cur.execute('drop table points')\n",
    "    print('dropped table')\n",
    "            \n",
    "with connect('test.db') as conn:\n",
    "    cur = conn.cursor()\n",
    "    with temptable(cur):\n",
    "        cur.execute('insert into points (x, y) values(1, 1)')\n",
    "        cur.execute('insert into points (x, y) values(1, 2)')\n",
    "        cur.execute('insert into points (x, y) values(2, 1)')\n",
    "        cur.execute('insert into points (x, y) values(2, 2)')\n",
    "        for row in cur.execute(\"select x, y from points\"):\n",
    "            print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "created table\n",
      "(1, 1)\n",
      "(1, 2)\n",
      "(2, 1)\n",
      "(2, 2)\n",
      "dropped table\n"
     ]
    }
   ],
   "source": [
    "from sqlite3 import connect\n",
    "from contextlib import contextmanager\n",
    "        \n",
    "@contextmanager\n",
    "def temptable(cur):\n",
    "    cur.execute('create table points(x int, y int)')\n",
    "    print('created table')\n",
    "    try:\n",
    "        yield\n",
    "    finally:\n",
    "        cur.execute('drop table points')\n",
    "        print('dropped table')\n",
    "            \n",
    "with connect('test.db') as conn:\n",
    "    cur = conn.cursor()\n",
    "    with temptable(cur):\n",
    "        cur.execute('insert into points (x, y) values(1, 1)')\n",
    "        cur.execute('insert into points (x, y) values(1, 2)')\n",
    "        cur.execute('insert into points (x, y) values(2, 1)')\n",
    "        cur.execute('insert into points (x, y) values(2, 2)')\n",
    "        for row in cur.execute(\"select x, y from points\"):\n",
    "            print(row)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
