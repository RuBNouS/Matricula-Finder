Matrícula Finder para Portugal em Python

Um script em Python para gerar matrículas portuguesas aleatórias e reconstruir matrículas incompletas com base nos formatos existentes.

Funcionalidades:
O programa apresenta um menu no terminal com as seguintes opções:
1. Gerar matrícula aleatória: Cria uma matrícula válida escolhida à sorte entre os 4 formatos que existiram em Portugal.
2. Completar matrícula parcial: Recebe uma matrícula com espaços em falta (ex: `41-__-BG`) e verifica se pode existir. Gera as combinaçãoes possíveis em Portugal e guarda os resultados num ficheiro ".txt" organizado alfabeticamente.
3. Ajuda: Explicação de como o sistema funciona.

Os 4 formatos suportados em Portugal:
 - 1937 a 1992:      `AA-00-00` (Letras - Números - Números)
 - 1992 a 2005:      `00-00-AA` (Números - Números - Letras)
 - 2005 a 2020:      `00-AA-00` (Números - Letras - Números)
 - 2020 ao presente: `AA-00-AA` (Letras - Números - Letras)

(Nota: O programa sabe que blocos de letras e números nunca se misturam).

Como Executar:
Requer apenas o [Python](https://www.python.org/downloads/) instalado. No terminal da pasta do projeto, corre:
```bash
python "Matrícula Finder.py"
