Instalando a 'venv'
sudo apt-get install python3-venv

Cria uma ambiente virtual para somente isolar as variaveis
no ambiente da aplicacao usando o 'venv'
-> python3 -m venv ./venv

Instalando o pip
-> python -m pip install --upgrade pip
-> python -m ensurepip

abrir o ambiente usando o venv
-> source /workspace/venv/bin/activate

o PIP deve ser instalado no venv

o terminal ficara desse jeito
(venv) root@b1785c37c80f:/workspace#

instalar o DJANGO (docker-compose.yml) já está instalando
-> pip install Django

atualizar o pip com:
-> /workspace/venv/bin/python3 -m pip install --upgrade pip

executando o help
-> django-admin help

para iniciar um projeto
-> django-admin startproject alurareceita .

para rodar a aplicacao
-> python manage.py runserver

para instalar os requirments
-> pip install setuptools

---

criando um APP de RECEITAS
--> python manage.py startapp receitas
(o app precisa ser registrado)

---

criar o arquivo urls.py


para fazer as migrations e migrate
-> python manage.py makemigrations
-> python manage.py migrate

