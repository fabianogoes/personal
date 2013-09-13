Arquivos e dicas para facilitar configurações de ambiente de desenvolvimento

===
### Virtualenv
>
* ``` $ sudo apt-get update ```
* ``` $ sudo apt-get install python-dev python-setuptools ```
* ``` $ sudo easy_install pip ```
* ``` $ sudo pip install virtualenv ```
### Virtualenvwrapper
* ``` $ sudo pip install virtualenvwrapper ```
* ``` $ mkdir ~/pywork ```    
> 
Depois basta editar seu “~/.bashrc” e colocar no final do mesmo:     
```
export WORKON_HOME=~/pywork
source /usr/local/bin/virtualenvwrapper.sh     
```   
> Criando Ambientes “–no-site-packages –distribute” por Padrão   
alterar o seu “~/.bashrc” e colocar no final(além do que tinha sido posto antes) o seguinte código:  
>
```
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages --distribute'
```

>
Para instalar pacotes na criação do virtualenv, alterar o arquivo: $WORKON_HOME/postmkvirtualenv
```
pip install yolk
pip install ipython
pip install freeze
pip install django
```

===

### Windows Hack para facilitar o uso do django-admin
> * Criar um arquivo django-admin.bat para chaamr o django-admin.py
> * Criar essa .bat dentro do diretório "%VIRTUAL_ENV%"\Scripts
```
@python "c:\Python27\path\venv\Scripts\django-admin.py" %* 
```   
exemplo:      
```
$ django-admin startproject project_name .
```

===

### Executar o manage.py de qualquer diretório dentro do virtualenv
> No Windows
* Crie o arquivo "%VIRTUAL_ENV%"\Scripts\manage.bat    
```
@python "c:\Python27\path_project\manage.py" %* 
```       
> exemplo:               
```
$ manage help
```      

---
> No Mac ou Linux
* Crie um alias no seu ~/.bashrc ou ~/.profile       
```
alias manage='python $VIRTUAL_ENV/manage.py'
```       
> exemplo:               
```
$ manage help
```


### Configuração do vim      
> 
* No Windows o arquivo fica em: "C:\Program Files (x86)\Vim\_vimrc" 
* No Linux o arquivo fica em: "/home/user/.vimrc"  
>>> para resolver o erro: "Unable to create Ubuntu Menu Proxy: Timeout was reached" <<<<      
add this to ~/.bashrc and restart the     
```     
function gvim () { (/usr/bin/gvim -f "$@" &) }
```     
