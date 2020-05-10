### sleep and say

sleep 600 && say '10 minuts is over'

### Change the sound

use tab after

> say -v

> say -v ting-ting hello world!

### calendar and date

> cal

> cal 2020

> date

### ip

> ifconfig

> archey???

### files content check

1. check how many lines of a file: 
> wc -l out.txt
2. first 10 lines:
> head -10 out.txt
3. last 10 lines:
> tail -10 out.txt

## OH MY ZSH

### change bash to zsh

chsh -s /bin/zsh

### change the theme of zsh

```
vi ~/.zshrc
ZSH_THEME = ''ys''
source ~/.zshrc
```

The theme files are in: ~/.oh-my-zsh/themes
ls ~/.oh-my-zsh/themes

### git commands shortcuts

1. gco = 'git check out'
2. gd = 'git diff'
3. gst = 'git status'
4. g = 'git'
The rest commands are in ~/.oh-my-zsh/plugins/git/git.plugin.zsh

### autojump

1. brew install autojump
2. nvim ~/.zshrc
3. add autojump to the plugin()
4. add the codes below: [[ -s $(brew --prefix)/etc/profile.d/autojump.sh ]] && . $(brew --prefix)/etc/profile.d/autojump.sh
5. wq and then restart your terminal
6. j onedrive (j + folder name, this folder shoul be opened by cd command before)
7. j --stat (this will show all your history visiting record)

### enter d

then choose the number to jump into a folder