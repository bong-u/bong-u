" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
filetype plugin indent on

"set showcmd        " Show (partial) command in status line.
"set showmatch      " Show matching brackets.
set ignorecase      " Do case insensitive matching
set smartcase       " Do smart case matching
"set incsearch      " Incremental search
"set autowrite      " Automatically save before commands like :next and :make
"set hidden         " Hide buffers when they are abandoned
"set mouse=a        " Enable mouse usage (all modes)
se number           " Show line number
set tabstop=4       " Set spacing of tab
set shiftwidth=4    " Set spacing of auto indentation
set smartindent     " Enable smart indentation

