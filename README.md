# httpstatus.vim

[![Build Status](https://travis-ci.org/zakuro9715/httpstatus.vim.svg?branch=master)](https://travis-ci.org/zakuro9715/httpstatus.vim)
[![Coverage Status](https://coveralls.io/repos/zakuro9715/httpstatus.vim/badge.svg?branch=master)](https://coveralls.io/r/zakuro9715/httpstatus.vim?branch=master)

httpstatus.vim is vim plugin to see description of http status(es)

# Usage

Install with NeoBundle

```
NeoBundle 'zakuro9715/httpstatus.vim'
```

See description of a http status:

```
:HttpStatus 200
200 OK | Request fulfilled, document follows 
```

And, you can ommit end of digits.
```
:HttpStatus 40
400 ...
401 ...
...
409

:Http 4
400 ...
401 ...
...
417 ...
```
