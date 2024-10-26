# Sistema de Gerenciamento de Inventário de Bicicletas

## Descrição

Este é um sistema web desenvolvido com Flask para gerenciar o estoque de bicicletas de uma loja fictícia. O sistema permite adicionar novas bicicletas, visualizar bicicletas cadastradas, marcar bicicletas como vendidas e remover bicicletas do inventário.

## Funcionalidades

- **Adicionar nova bicicleta**: Permite adicionar bicicletas com detalhes como modelo, categoria, preço e status.
- **Listar bicicletas**: Exibe uma lista de todas as bicicletas no estoque, mostrando modelo, categoria, preço e status.
- **Marcar bicicleta como vendida**: Permite marcar uma bicicleta como "Vendida".
- **Remover bicicleta do estoque**: Permite remover uma bicicleta do inventário.

## Requisitos

- Python 3.x
- Flask
- SQLAlchemy
- PostgreSQL (usando Supabase para este projeto)

## Estrutura do Projeto

```bash
bike_inventory/
│
├── app.py                    # Ponto de entrada da aplicação Flask
├── controllers/
│   └── bike_controller.py    # Controlador de bicicletas usando Blueprint
├── services/
│   └── bike_service.py       # Regras de negócio
├── models/
│   └── bike_model.py         # Estrutura de dados de cada bicicleta
├── templates/
│   └── index.html            # Página HTML para exibição do inventário
└── static/
    └── styles.css            # Arquivo CSS para estilizar a aplicação