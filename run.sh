#!/bin/bash
# Script para executar o programa no ambiente virtual

# Ativar ambiente virtual
source venv/bin/activate

# Executar programa principal
python main.py "$@"

# Desativar ambiente virtual
deactivate
