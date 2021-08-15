from flask import Flask, request, abort
import views


app = Flask(__name__)
ips_permitidos_relatorio = ['10.100.6.1', '10.100.6.2','10.100.6.3','192.168.1.65','127.0.0.1']

@app.route('/')
def index() -> 'html':
    return views.index()

@app.route('/confirmacao', methods=['POST'])
def confirmacao() -> 'html':
    return views.confirmacao()


@app.route('/search', methods=['GET','POST'])
def resultado() -> 'html':
    return views.resultado()

@app.route('/empcolig')
def empcolig() -> 'html':
    return views.render_empresa_coligada()

@app.route('/empcolig/change',methods=['POST'])
def changeEmpresa() -> 'html':
    return views.changeEmpresa_coligada()


@app.before_request
def limit_remote_addr():
    if any( request.remote_addr == ip for ip in ips_permitidos_relatorio):
            # Limitações são colocadas aqui :D
            pass
    else:
        abort(403) #Acesso Negado

app.secret_key = '@#$%45K8lB93Af@62*5aT6'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)





    
    


    


