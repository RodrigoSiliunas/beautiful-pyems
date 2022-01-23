# Beautiful Pyems

### Sobre o projeto

Beautiful Pyems tem a pretenção de ser uma APIRest, foi construida com o microframework python Flask. Seu principal propósito é retornas poemas de maneira simples para que esses dados sejam consumidos por outra aplicação.

Beautiful Pyems faz uso dos dados obtidos através de um ETL, o repositório usado para obtenção desses dados é o [ETL Pyem](https://github.com/RodrigoSiliunas/etl-pyems), também de minha autoria.

### Tecnologias Utilizadas

O projeto utiliza várias tecnologias por de baixo dos panos, eu listarei **apenas** as principais, incluindo bibliotecas.

>   1. Python
>   2. Flask
>   3. Flask RestX (Que é um fork do Flask RESTPlus)
>   4. Regex
>   5. Swagger
>   6. MongoDB

### Rodando o Projeto

O código principal fica na pasta raiz desse repositório, `run.py`. Antes de executar o código você deve se certificar que tem o Python em sua versão minima `3.10.1` instalada em sua máquina. Você também deverá possuir os dados fornecidos pela [ETL Pyem](https://github.com/RodrigoSiliunas/etl-pyems).

Se estiver cumprindo os requisitos basta abrir o terminal/powershell na pasta raiz do projeto e ativar a venv com o comando:

    enviroment/Scripts/activate

As bibliotecas seram carregadas e você pode simplesmente executar o comando:

    python run.py

A sua aplicação vai estar disponivel em `http://127.0.0.1:5000/`. Depois disso é só fazer requisições do tipo ***GET*** nas rotas e apreciar uma boa poesia.
<br/>

### Observações Importantes! ⚠️

O projeto possui documentação. Para acessar a documentação é muito simples. Assim que a API estiver online, basta abrir o seu navegador e digitar o endereço da aplicação seguido de barra docs.

##### Exemplo:

`http://127.0.0.1/docs`

Você vai acessar um site onde as requisições e modelos são apresentados, depois de entender a documentação é só sair fazendo requisição. (Se rimou é verdade 😂)

![Swagger Example](/static/swagger_example.png)

### Considerações Finais

Eu sempre gostei de literatura e de maneira recente eu entrei em uma vibe onde eu gosto de aproveitar meu café da manhã e meu break time lendo alguma poesia. Meu poéta favorito é Fernando Pessoa, e vindo dele as coisas sempre são intensas de alguma forma, quase sempre saio reflexivo (principalmente com os poemas de Alvaro Campos). Eu queria mostrar para as pessoas os poemas de Fernando Pessoa e de outros poetas mas não tenho nenhum contato com pessoas que se interessam por literatura ou poesia.

Fui inspirado de maneira quase sobrenatural pelo repositório de uma dev e tive um insight onde eu imaginei uma aplicação que enviava poemas diariamente para o Twitter, Telegram e WhatsApp. Para construir essa aplicação inteira eu resolvi separar o problema em partes menores (dividir para conquistar) e construir aos poucos.

Durante essa caminhada espero que eu inspire outros desenvolvedores, enriqueça ao menos um pouco meu porfólio e consiga fazer chegar um pouco de cultura(?) através de poemas ao máximo de pessoas possiveis.
Conceitos importantes estão sendo aprendidos e relembrados ao decorrer da minha jornada para a criação dessa aplicação.

De qualquer tempoespaço em que você leitor estiver, desejo profundo sucesso e boa sorte na vida. Obrigado por ler até aqui e se eu puder ajudar em alguma coisa me procure nas minhas [redes sociais](https://www.instagram.com/rosiliunas/). ✨🎉  🖖😉✌  ✨🎉

### API Online

Caso você queira fazer requisições nessa API você é livre para isso. A API está atualmente online em `http://beautiful-pyems.herokuapp.com`. ✌ 😍 ❤
