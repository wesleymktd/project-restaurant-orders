## 🧐 Sobre

Neste projeto, desenvolvi uma ferramenta para geração de cardápios, considerando possíveis restrições alimentares e disponibilidade de ingredientes em estoque. Ao longo deste projeto, construí testes para classes já implementadas. Também implementei uma nova classe para mapear pratos e suas respectivas receitas (ingredientes e quantidades), além de uma classe que gera os cardápios a serem exibidos para as pessoas que frequentam o estabelecimento, e outra classe que gerencia o estoque de ingredientes.

  🚵 Habilidades exercitadas:
  
- Aplicando o conceito de Hashmaps usando as estruturas de dados Dict e Set do Python.
- Aplicando conhecimentos de teste de software.
- Aplicação de conhecimentos de programação orientada a objetos.

</details>

## Rodar localmente:
- Primeiro clone o projeto para sua máquina;
```
git clone git@github.com:GabiNamu/Tryunfo.git
```
- Vá para a pasta do projeto:
```
cd restaurant-orders
```
 - Crie um amibiente virtual para o projeto:
```
python3 -m venv .venv && source .venv/bin/activate
```
- Instale as dependencias;
```
python3 -m pip install -r dev-requirements.txt
```
### Principais tecnologias utilizadas:
- Python;
- Pytest;
- Flake8;

## Contribuição:

Eu desenvolvi os arquivos:
 - src/menu_data.py;
 - src/menu_builder.py -> only the get_main_menu;
 - src/inventory_control.py -> only the check_recipe_availability and consume_recipe methods;

 - tests/ingredient/test_ingredient.py
 - tests/dish/test_dish.py
--------
Os demais arquivos forma feitos pela trybe.
