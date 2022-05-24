## Detector de Fake News

Este projeto é resultado de um trabalho de conclusão de curso, da faculdade de Análise e Desenvolvimento de Sistemas realizado no IFRS - Câmpus Sertão - RS.

O projeto é composto por três aplicações web. Um bot que realiza a raspagem de dados em 3 sites de noticias, coletando as seguintes informações: **titulo, dominio, data, autor, url, status e texto**, após possuir os dados é  realizado um request para a API.

A API foi desenvolvido com framework **FastAPI**, banco de dados utilizado é o **Firestore Database**.
Recursos da api:

 - Listar todas as noticias cadastradas 
 - Cadastrar noticias novas
 - Checar se noticia é fake ou verdadeira

Neste projeto para classificar as noticias, fake ou verdadeiras, foi utilizado o algotirimo **TfidfVectorizer**, que funciona aumentando proporcionalmente o número de vezes que uma palavra aparece no documento, mas é contrabalançado pelo número de documentos em que está presente.  
E para classificar as noticias, foi utilizado o algoritimo de machine learning  **Random Forest Classifier**.

O frontend, foi desenvolvido com framework **Nuxt.js** aproveitando ao máximos os recursos do Vue.js e Vuetify.


## Os Dados
O Dataset utilizado foi o Fake.Br Corpus. Gostaria de agradecer ao Roney Santos e a todos os envolvidos no desenvolvimento deste conjunto de dados, que foi incrivelmente bem feito e me economizou muito tempo e trabalho. Este projeto não teria sido possível com tais resultados sem dados bem coletados e limpos, como o do Fake.Br Corpus.

``Monteiro R.A., Santos R.L.S., Pardo T.A.S., de Almeida T.A., Ruiz E.E.S., Vale O.A. (2018) Contributions to the Study of Fake News in Portuguese: New Corpus and Automatic Detection Results. In: Villavicencio A. et al. (eds) Computational Processing of the Portuguese Language. PROPOR 2018. Lecture Notes in Computer Science, vol 11122. Springer, Cham``