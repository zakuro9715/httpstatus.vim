let s:save_cpo = &cpo
set cpo&vim

pyfile <sfile>:h:h/httpstatus.py
python import vim

function! httpstatus#print(status)
  python print_httpstatuses(vim.eval('a:status'))
endfunction

let &cpo = s:save_cpo
unlet s:save_cpo
