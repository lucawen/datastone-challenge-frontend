# Challenge Frontend Datastone



## Introdução

A proposta do desafio é conseguir interpretar o código da api em django e implementar um frontend para criar uma votação de perguntas e votar nas respostas.


#### Antes de continuar
Estamos utilizando docker, então é necessário ter o mesmo instalado para rodar a api na sua maquina e conseguir acesso.


### Requisitos & Funcionalidades

- O consumo da API será feito via REST
- Criar rotas com VueRouter
- Não será necessário autenticação de usuário
- Deve-se possibilitar a criação, edição, visualização, remoção e votação de `polls`
- Deve-se possibilitar a edição e remoção das questões (`questions`) das `polls`
- Ao criar um `Poll` você envia todas as informações e a api faz o cadastro tudo de uma vez.
- Você pode atualizar todas as informações via POST ou PATCH incluindo os `choices` através da api do `poll`
- Para atualizar um choice específico, você tem a opção de usar uma api específica (`/api/choice/`) ou usar o método sugerido anteriormente.


### Tecnologias esperadas

- Vuejs
- VueRouter
- Vuetify


### Detalhes

Para rodar o projeto, basta executar:
```bash
$ make run
```

Para acessar o `/admin/` do django, já existe um usuário:
 Usuário: `admin`
 Senha: `admin123`


Já existe uma votação criada.


### Participe

Caso queira participar, faça um 'fork' do projeto, realize as alterações e faza um PR quando for finalizado.
