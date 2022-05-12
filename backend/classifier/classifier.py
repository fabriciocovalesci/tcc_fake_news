import os
import pandas as pd
import numpy as np
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer, CountVectorizer
import string
import time

import warnings 
warnings.filterwarnings("ignore")

CLASSIFIER_NEWS_PATH = "classifier_news.pkl"

fileDir = os.path.dirname(os.path.realpath('__file__'))

joblib_vect = pickle.load(open(os.path.join(fileDir, "../model_data/tfidfvect.pkl"), 'rb'))

joblib_model = pickle.load(open(os.path.join(fileDir, "model.pkl"), 'rb'))

with open(os.path.join(fileDir, "classifier_news.pkl") , 'rb') as model_pkl:
    classifier_news = pickle.load(model_pkl)

cv = CountVectorizer()
tf_vectorizer = TfidfVectorizer(
                    stop_words=stopwords.words('portuguese'), analyzer='word',
                    ngram_range=(1, 1), lowercase=True, use_idf=True)


# load modelo

def process_text(text):
    not_punc = [char for char in text if char not in  string.punctuation]
    not_punc = "".join(not_punc)
    clean_words = [word.lower() for word in not_punc.split() if word.lower() not in stopwords.words('portuguese') ]
    return clean_words



def predict(new_text):    
    TXT = """O governo federal anunciou nesta quarta-feira (4) um conjunto de medidas para impulsionar a empregabilidade de mulheres e permitir a flexibilização da jornada de trabalho após o fim da licença maternidade. Elas constam em uma Medida Provisória assinada pelo presidente Jair Bolsonaro e fazem parte do Programa de Renda e Oportunidade, do Ministério do Trabalho e Previdência, criado para alavancar a geração de empregos no país.Entre as novidades, apresentadas durante cerimônia no Palácio do Planalto, estão duas novas modalidades de saque do Fundo de Garantia do Tempo de Serviço (FGTS), exclusivamente voltada às mulheres.A primeira modalidade prevê a liberação de recursos do fundo para auxiliar no pagamento de creche. A outra possibilidade de liberação será o custeio de cursos de qualificação profissional em áreas específicas, como inovação, tecnologia e engenharia, consideradas as que oferecem melhores oportunidades profissionais atualmente, mas que ainda são dominadas por homens no mercado de trabalho.Os valores, limites e tempo de uso dessas duas novas modalidades de saque do FGTS ainda precisarão ser regulamentados pelo Conselho Curador do fundo, em resolução própria. Não há prazo para que essa análise ocorra e as novas modalidades entrem em vigor.Ainda em relação à creche, a MP regulamenta o auxílio-creche, ou reembolso creche, que é um valor repassado pelas empresas que possuem mais de 30 empregadas mulheres (a partir dos 16 anos), definido por meio de convenções coletivas ou acordos individuais entre funcionários e empregadores. Atualmente, esse benefício consta apenas em Portaria do Ministério do Trabalho e Previdência, mas passará a constar em lei federal.A Medida Provisória também passa a prever a possibilidade de flexibilização do regime de trabalho dos homens que são pais, após o término da licença maternidade, para dar mais tempo às mulheres no retorno ao trabalho nesse período. Isso inclui a redução proporcional de jornada e salário, regime especial de 36 horas de descanso por 12 horas trabalhadas, quando a ocupação permitir, banco de horas e antecipação de férias."A mulher vai ficar mais livre pra exercer suas atividades laborais e o homem vai exercer, de forma mais flexível, suas atividades de pai. Vai poder cuidar mais do filho e estar mais presente em casa, para que ela [mãe] possa de dedicar, estar mais disponível no trabalho e fique menos tempo desconectada", afirmou a secretária-adjunta do Trabalho, Tatiana Severino, em coletiva de imprensa para explicar a medida.Outra alternativa incluída na MP é a possibilidade de implementação do lay-off, que é a suspensão temporária do contrato de trabalho para qualificação profissional. Voltada para os pais, essa nova modalidade de play-off permite o afastamento do empregado para cursos de qualificação profissional, desde que sejam no formato Educação à Distância (EaD), para que ele permaneça em casa e possa colaborar com os cuidados do filho.O governo também instituiu na MP uma mudança na lei que criou o programa Empresa Cidadã, que prevê a extensão por até 60 dias da licença-maternidade de mulheres empregadas. Na prática, as empresas que fazem parte do programa recebem incentivos para estender o afastamento de mães por mais dois meses além dos quatro previstos pela legislação trabalhista (CLT). A ideia é que a extensão da licença-maternidade possa ser usada também pelo pai, no lugar da mãe, desde que seja de comum acordo entre as partes. Assim, a mãe retorna ao mercado de trabalho antes, mas o pai ganha licença para cuidar da criança.Também foi anunciada, nesta quarta-feira, a criação de 100 mil novas vagas no programa Jovem Aprendiz e a instituição do Projeto Nacional de Incentivo à Contratação de Aprendizes, por meio do qual as empresas participantes terão benefícios para regularizarem o cumprimento da cota de aprendizagem, com uma estimativa de contratação de 250 mil adolescentes e jovens ainda este ano.Uma das mudanças é a ampliação também do prazo máximo da aprendizagem de dois para três anos e a criação de incentivos para que as empresas efetivem os aprendizes em contratos de trabalho por tempo indeterminado após a conclusão do programa de aprendizagem.Ainda segundo o governo, foram estabelecidas medidas para incluir mais adolescentes e jovens vulneráveis na aprendizagem, com prioridade para o público do Auxílio Brasil, adolescentes em acolhimento institucional, aqueles provenientes do trabalho infantil, entre outros."""
    clean_text = process_text(new_text)    
    vectorized_text = joblib_vect.transform(clean_text).toarray()
    model = joblib_model.predict(vectorized_text)
    probabilidade = joblib_model.predict_proba(vectorized_text)
    
    print(round(probabilidade.mean()*100, 3))
    print(f"Probabilidade: {probabilidade[:,1].mean()}%")
    print(f"-> {round(probabilidade[::,1].mean()*100, 2)}")
    print(f"Fake ou Não: {model[0]}")
    return { "modelo": model[0].item() }