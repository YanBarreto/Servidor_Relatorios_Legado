from flask import render_template, request, redirect, session
from dbcm import BancoDeDados
from datetime import datetime

#Função principal - '/'
def index() -> 'html':
    return render_template('relatorio.html')
#Função de checagem - '/confirmacao'
def confirmacao() -> 'html':
    session['antigo'] = request.form['codigoantigo']
    session['novo'] = request.form['codigonovo']
    try:
        with BancoDeDados() as cursor:
            cursor.execute(f"select rls_titulo from rls where rls_cod in ({session['antigo']}, {session['novo']})")
            dados = cursor.fetchall()
    
    except Exception as err:
        return render_template('falha.html',
                                erro = err)
    #return redirect('/search')
    return render_template('confirmacao.html',
                            titulo_antigo = dados[0][0],
                            titulo_novo = dados[1][0])
        

# Função Resultado - '/search'
def resultado() -> 'html':
    codigo_antigo = session['antigo']
    codigo_novo = session['novo']
    
    try:
        with BancoDeDados() as cursor:
            cursor.execute(f"select rls_titulo from rls where rls_cod = {codigo_novo}")
            rls_titulo = cursor.fetchone()
            data_rls_titulo = (str(datetime.now().strftime(r'%Y.%m.%d_') + rls_titulo[0]))
            cursor.execute(f"UPDATE ars SET ars_rls_cod = {codigo_novo} WHERE ars_tipo = 'E' AND ars_rls_cod = {codigo_antigo}")
            cursor.execute(f"UPDATE rls SET rls_titulo = '{data_rls_titulo}' WHERE rls_cod = {codigo_antigo} ")
        
    except Exception as err:
        print('Erro -> ', err)
        return render_template('falha.html',
                                erro = err
                                )
    session.pop('antigo')
    session.pop('novo')
    return render_template('sucesso.html')

# Função Empresa Coligada '/empcolig'
def render_empresa_coligada() -> 'html':
    return render_template('empresa_coligada.html')

def changeEmpresa_coligada() -> 'html':
        os = request.form['os']
        cod = request.form['codigo']
        serie = os.split('.')
        numero = serie[1]
        serie = serie[0]
        return f'{serie} e {numero} com o código {cod}' #Retorno teste
