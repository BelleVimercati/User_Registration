# como está funcionando a arquitetura do projeto
projeto_cad_usuarios:
    pasta que contem todos os arquivos padrões de execução do vs code para a parte de "background" do djando

app_cad_usuarios:
    pasta de funcionalidades do projeto

url -> view -> html

projeto_cad_usuarios/urls.py:
    #rota, view responsavel e nome de referência
    Aqui criamos as rotas de url do navegador

app_cad_usuarios/view.py:
    renderiza as paginas htmls criadas

app_cad_usuarios/models.py:
Configuração do banco de dados a partir de classes python

## Dicas
É necessario se atentar as palavras chaves que o Django usa para que o sistema seja capaz de reconhecer o que está sendo feito, como a pasta ***Templates*** que precisa estar no plural!

## como executar o projeto
Na pasta com o arquivo ***manage.py***: \
<code>python manage.py runserver</code>

Para refazer o banco de dados\
`python ./manage.py makemigrations`\
`python ./manage.py migrate`

