// Executar quando o documento HTML for completamente carregado
document.addEventListener('DOMContentLoaded', function () {
    
    // Receber o SELETOR calendar do atributo id
    var calendarEl = document.getElementById('calendar');

    // Instanciar FullCalendar.Calendar e atribuir a variável calendar
    var calendar = new FullCalendar.Calendar(calendarEl, {
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,timeGridDay,listMonth'
        },
        locale: 'pt-br',
        initialDate: new Date(),
        navLinks: true, // can click day/week names to navigate views
        businessHours: true, // display business hours
        selectable: true,
        selectMirror: true,
        events: function(fetchInfo, successCallback, failureCallback) {
            // Buscar eventos de ambos os endpoints
            Promise.all([
                fetch('/api/reservas-produtos/'),  // Endpoint de reservas de produtos
                fetch('/api/reservas-servicos/')   // Endpoint de reservas de serviços
            ])
            .then(responses => Promise.all(responses.map(response => response.json())))
            .then(data => {
                // Combinar os dados dos dois endpoints
                let eventos = [];

                // Processar os dados de reservas-produtos
                data[0].forEach(reserva => {
                    eventos.push({
                        title: reserva.produto.nome,  // Ajuste conforme os campos da sua API
                        start: reserva.data_reservada,  // Exemplo: '2025-02-25T14:00:00'
                        display:'#background',
                        backgroundColor: '#20b2aa' ,
                        color: reserva.disponivel ? '#008000' : '#b81414',
                        extendedProps: { 
                            tipo: 'produto', 
                            quantidade_comprada: reserva.quantidade_comprada,  // Armazenando a quantidade
                            user: reserva.user.username // Armazenando o usuário
                        } // Adicionando um tipo para diferenciar
                    });
                });

                // Processar os dados de reservas-servicos
                data[1].forEach(reserva => {
                    eventos.push({
                        title: reserva.servico.nome,  // Ajuste conforme os campos da sua API
                        start: reserva.data_reservada,  // Exemplo: '2025-02-25T14:00:00'
                        display:'#background',
                        backgroundColor: '#f39c12' ,
                        color: reserva.disponivel ? '#008000' : '#b81414',
                        extendedProps: { 
                            tipo: 'serviço',
                            user: reserva.user.username
                        } // Adicionando um tipo para diferenciar
                    });
                });

                // Passar todos os eventos para o sucesso
                successCallback(eventos);
            })
            .catch(error => {
                console.error('Erro ao buscar reservas:', error);
                failureCallback(error);
            });
        },
        // Modificar título apenas na visão de lista
        eventDidMount: function(info) {
            if (info.view.type.startsWith('list')) {  // Se estiver na visão de lista
                let tipo = info.event.extendedProps.tipo;
                let user = info.event.extendedProps.user; // puxar da api
                let tituloOriginal = info.event.title;
                let novoTitulo = '';

            if (tipo === 'produto') {
                let quantidade = info.event.extendedProps.quantidade_comprada; //puxar da api
                novoTitulo = `Retirada do produto: '${tituloOriginal}' - Quantidade: ${quantidade} - user: ${user}`;
            } else if (tipo === 'serviço') {
                novoTitulo = `Serviço ${tituloOriginal} - user: ${user}`;
            }

            // Modificar o título apenas na lista
            let tituloElemento = info.el.querySelector('.fc-list-event-title');
            if (tituloElemento) {
                tituloElemento.innerText = novoTitulo;
            }
            }
        }
    });

    calendar.render();
});
