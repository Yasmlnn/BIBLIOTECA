import streamlit as st
import pandas as pd

#criar titulo do aplicativo
st.title("BIBLIOTECA DE LIVROS")


livros = pd.DataFrame(columns=['ISBN', 'TITULO', 'AUTOR', 'ANO_PUBLICACAO', 'GENERO'])
estudantes = pd.DataFrame(columns=['nome', 'matricula', 'email', 'telefone', 'curso'])
emprestimos =pd.DataFrame(columns=['id_emprestimo', 'matricula_estudante', 'ISBN_livro', 'data_emprestimo', 'data_devolucao'
])
#adicionar alguns livros ao dataframe
novos_livros = pd.DataFrame([
    {'ISBN': '123-456', 'TITULO': 'AULA DE IC', 'AUTOR': 'VAHID', 'ANO_PUBLICACAO': 2026, 'GENERO': 'FICCAO'},
    {'ISBN': '789-101', 'TITULO': 'MECANICA ESTATICA', 'AUTOR': 'CM COSSU', 'ANO_PUBLICACAO': 2006, 'GENERO': 'TERROR'}
])

livros = pd.concat([livros, novos_livros], ignore_index=True)

#adicionar os estudantes
novos_estudantes = pd.DataFrame([
    {'nome': 'yasmin dos anjos', 'matricula': 202120435911, 'email': 'y.dosanjos08@gmail.com', 'telefone': 21989608757, 'curso': 'eng. mecanica'},
    {'nome': 'luiza dos anjos', 'matricula': 202120469811, 'email': 'luiza@gmail.com', 'telefone': 21986152882, 'curso': 'eng. quimica'}
])

estudantes = pd.concat([estudantes, novos_estudantes], ignore_index=True)

#adicionar os emprestimos
novos_emprestimos = pd.DataFrame([
    {'id_emprestimo': 1, 'matricula_estudante':202120435911, 'ISBN_livro': '123-456', 'data_emprestimo': '21/02/2026', 'data_devolucao': '21/03/2026'}
])

emprestimos = pd.concat([emprestimos, novos_emprestimos], ignore_index=True)

#quero ter um sidebar com as opçoes de menu para o usuario escolher entre "livros", "estudantes" e "emprestimo"
menu = st.sidebar.selectbox("Selecione uma opção", ["Livros", "Estudantes", "Emprestimos"])
if menu == "Livros":
    st.subheader("Lista de livros")
    st.dataframe(livros)
elif menu == "Estudantes":
    st.subheader("Lista de estudantes")
    st.dataframe(estudantes)
elif menu == "Emprestimos":
    st.subheader("Lista de emprestimos")
    st.dataframe(emprestimos)