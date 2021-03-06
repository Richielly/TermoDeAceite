import streamlit as st
from arquivo import Arquivo

st.set_page_config(layout="wide")

documento = st.radio("Tipo",['Conversão', 'Treinamento'])

if documento == 'Conversão' :
    st.title("**Termo Aceite Conversão**")
    with st.form("form"):
        st.write("**Informações da entidade**")
        container_1 = st.container()
        st.write("**Informações no corpo do termo**")
        container_2 = st.container()
        st.write("**Informações assinaturas responsável conversão/treinamento**")
        container_3 = st.container()
        st.write("**Informações assinaturas cliente**")
        container_4 = st.container()

        with container_1:
            col1, col2 = st.columns(2)
            with col1:
                cliente = st.text_input("Nome Cliente")
                tipoProcesso = st.text_input("Modalidade")
            with col2:
                nrProcesso = st.text_input("Número Processo")
            with col2:
                anoProcesso = st.text_input("Ano Processo")
            with col2:
                contrato  = st.text_input("Número Contrato")
        with container_2:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                dia = st.text_input("Dia")
                rua = st.text_input("Rua")
                rua = rua.upper().replace('RUA','').capitalize()
            with col2:
                mes = st.text_input("Mês (Ex.: 'Janeiro')")
                numero = st.text_input("Número")
            with col3:
                ano = st.text_input("Ano")
                sistema = st.text_input("Sistema")

            with col4:
                cidade = st.text_input("Cidade")
                responsavel = st.text_input("Responsável")

        with container_3:
            col1, col2= st.columns([3,1])
            responsavelImplantacao = st.text_input("Responsável Implantação campo assinatura")
        with container_4:
            col1, col2 = st.columns([3,1])
            with col1:
                responsavelAssinatura = st.text_input("Cliente responsável")
            with col1:
                responsavelCargo = st.text_input("Cargo responsável")
                responsavelNrDocumento = st.text_input("Documento responsável")

        submitted = st.form_submit_button("Enviar")
        if submitted:
            arq = Arquivo()
            nome_doc = arq.alterar_doc(cliente, nrProcesso, tipoProcesso, anoProcesso, contrato, dia, mes, ano, cidade, rua, numero, sistema, responsavel, responsavelImplantacao, responsavelAssinatura,responsavelCargo, responsavelNrDocumento)

            with open(nome_doc, 'rb') as f:
                doc = f.read()

    if submitted:
        st.download_button(f'Download doc {nome_doc}', data=doc, file_name=nome_doc, mime='text/plain')
        # st.download_button('Download pdf', data=PDFbyte, file_name=nome_pdf + '.docx', mime='application/octet-stream')


if documento == 'Treinamento' :
    st.title("**Termo Aceite Treinamento**")
    with st.form("form"):
        st.write("**Informações no corpo do termo**")
        container_2 = st.container()
        st.write("**Informações assinaturas responsável conversão/treinamento**")
        container_3 = st.container()
        st.write("**Informações assinaturas cliente**")
        container_4 = st.container()

        with container_2:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                dia = st.text_input("Dia")
                rua = st.text_input("Rua")
                rua = rua.upper().replace('RUA','').capitalize()
            with col2:
                mes = st.text_input("Mês (Ex.: 'Janeiro')")
                numero = st.text_input("Número")
            with col3:
                ano = st.text_input("Ano")
                sistema = st.text_input("Sistema")

            with col4:
                cidade = st.text_input("Cidade")
                responsavel = st.text_input("Responsável")

        with container_3:
            col1, col2= st.columns([3,1])
            responsavelImplantacao = st.text_input("Responsável Implantação campo assinatura")
        with container_4:
            col1, col2 = st.columns([3,1])
            with col1:
                responsavelAssinatura = st.text_input("Cliente responsável")
            with col1:
                responsavelCargo = st.text_input("Cargo responsável")
                responsavelNrDocumento = st.text_input("Documento responsável")

        submitted = st.form_submit_button("Enviar")
        if submitted:
            arq = Arquivo()
            nome_doc = arq.alterar_doc_treinamento(dia, mes, ano, cidade, rua, numero, sistema, responsavel, responsavelImplantacao, responsavelAssinatura,responsavelCargo, responsavelNrDocumento)

            with open(nome_doc, 'rb') as f:
                doc = f.read()

    if submitted:
        st.download_button(f'Download doc {nome_doc}', data=doc, file_name=nome_doc, mime='text/plain')
        # st.download_button('Download pdf', data=PDFbyte, file_name=nome_pdf + '.docx', mime='application/octet-stream')