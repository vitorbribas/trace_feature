# Trace Feature

![PyPI - Python Version](https://img.shields.io/badge/python-3-blue.svg?longCache=true&style=flat-square)
![License](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)


<!---Neste repositório se encontra a ferramenta de geração de _traces_ a partir da execução de cada feature BDD. 
O link para acesso das documetações se encontra *[aqui](https://trace-features-bdd.github.io/trace_feature_docs/)*. --->

## Instalação

### Virtualenv

##### **1. Instale o Pip**
Para visualizar se você possui o pip instalado, use:
```shell
pip --version
```

Caso não tenha o pip instalado, use:
```shell
sudo apt-get install python3-pip
```


##### **2. Instale o Virtualenv**
Para visualizar se você possui o virtualenv instalado, use:
```shell
virtualenv --version
```

Caso não tenha o pip instalado, use:
```shell
sudo pip3 install virtualenv
```


##### **3. Crie um Virtualenv com Python3**
```shell
virtualenv -p python3 env
```


##### **4. Entre no Virtualenv**
Entre na pasta que contém seu virtualenv e use:

```shell
source env/bin/activate
```

##### **5. Instalação da ferramenta**

Temos duas formas de executar o trace feature: **utilizando o pacote trace-feature** ou **clonando o repositório**.

---

**Utilizando o pacote trace-feature:**

Após criar um _virtualenv_ execute o seguinte comando:

```shell
$ pip install trace-feature
```

---

**Utilizando o projeto clonado localmente:**

Após criar um _virtualenv_, navegue até o diretório `trace_feature` e execute o seguinte comando:

```shell
$ pip install .
```

Instale outras dependências do projeto:

```shell
$ pip install -r requirements.txt
```
 ---

### Execução do projeto:
Para executar o projeto, use o comando:

```shell
trace-feature -f [feature] -s [linha do cenário] -u [url do servidor]
```

Os argumentos são opcionais e não precisam ser especificados depois do comando. Vale lembrar também que para que o comando seja executado sem parâmetros, é necessário navegar até a pasta do projeto onde se deseja executar a ferramenta.

Para obter ajuda sobre o comando e os argumentos, basta usar

```shell
trace-feature --help
```

Para execução completa da análise de features e métodos, devemos subir o servidor de análise de dados, com código fonte disponível *[aqui](https://github.com/BDD-OperationalProfile/server_op)*. Então, devemos executar esta ferramenta na seguinte ordem:

Primeiramente instalar Excellent:


```shell
gem install excellent
```

Então devemos incluir um arquivo de configuração onde vamos definir os dados que deverão ser obtidos pela gema Excellent. Para isso, crie um arquivo chamado .excellent.yml na pasta raíz do projeto analisado. Então inclua as seguintes linhas no arquivo:

```c
AbcMetricMethodCheck: True
CyclomaticComplexityMethodCheck:
      threshold: 0
MethodLineCountCheck:
      threshold: 0
```

Feito isso, execute:

```shell
trace-feature -m
```
Aguardar a conclusão da análise de todos os métodos do projeto e executar:


```shell
trace-feature
```

### Testes:
Para executar os testes em conjunto com o output de cobertura, use o comando:
```shell
pytest -v --cov
```

Para visualizar a cobertura dos testes em uma página HTML, execute:
```shell
pytest -v --cov --cov-report=html
```
E abra o arquivo index.html do diretório `htmlcov`
