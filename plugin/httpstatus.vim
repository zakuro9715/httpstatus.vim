if exists("g:loaded_httpstatus")
  finish
endif
let g:loaded_vimtask = 1

let s:save_cpo = &cpo
set cpo&vim

command! -nargs=1 HttpStatus call httpstatus#print(<f-args>)

let &cpo = s:save_cpo
unlet s:save_cpo
