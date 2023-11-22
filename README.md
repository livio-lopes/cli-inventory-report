## O que é projeto Inventory Report?
Esse projeto é um gerador de relatórios para dados de estoque, permitindo a importação de arquivos CSV ou JSON. Nele, manipulo dados, e implemento funções para gerar e exportar relatórios, enquanto também implemento de testes. 

## Quais desafios?
1. Testar o construtor do objeto  `Produto`
2. Testar o relatório individual gerador por `Produto`
3. Criar a interface `Importer`
4. Criar a classe `JsonImporter`
5. Criar a classe `Inventory`
6. Criar o protocolo `Report`
7. Criar o relatório `SimpleReport`
8. Criar a classe `CsvImporter`
9. Criar o relatório `CompleteReport`
10. Criar a função `process_report_request`

## Como iniciar?
1. Clonando o projeto `git clone https://github.com/livio-lopes/cli-inventory-report.git`
2. Criando e acesso seu ambiente virtual `python3 -m venv venv && source .venv/bin/activate`
3. Instalando dependencias `python3 -m pip install -r dev-requirements.txt`
4. Para visualizar o relatório no seu terminal `ir -p inventory_reṕort/data -t simple` ou `ir -p inventory_reṕort/data -t complete`
