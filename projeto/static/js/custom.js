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
                        title: reserva.produto.nome,
                        start: reserva.data_reservada,
                        backgroundColor: '#20b2aa',
                        color: reserva.disponivel ? '#008000' : '#b81414',
                        extendedProps: { 
                            tipo: 'produto',
                            quantidade_comprada: reserva.quantidade_comprada,
                            user: reserva.user.username
                        }
                    });
                });

                // Processar os dados de reservas-servicos
                data[1].forEach(reserva => {
                    eventos.push({
                        title: reserva.servico.nome,
                        start: reserva.data_reservada,
                        backgroundColor: '#f39c12',
                        color: reserva.disponivel ? '#008000' : '#b81414',
                        extendedProps: { 
                            tipo: 'serviço',
                            user: reserva.user.username
                        }
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
        eventDidMount: function(info) {
            if (info.view.type.startsWith('list')) {
                let tipo = info.event.extendedProps.tipo;
                let user = info.event.extendedProps.user;
                let tituloOriginal = info.event.title;
                let novoTitulo = '';

                if (tipo === 'produto') {
                    let quantidade = info.event.extendedProps.quantidade_comprada;
                    novoTitulo = `Retirada do produto: '${tituloOriginal}' - Quantidade: ${quantidade} - user: ${user}`;
                } else if (tipo === 'serviço') {
                    novoTitulo = `Serviço ${tituloOriginal} - user: ${user}`;
                }

                let tituloElemento = info.el.querySelector('.fc-list-event-title');
                if (tituloElemento) {
                    tituloElemento.innerText = novoTitulo;
                }
            }
        }
    });

    calendar.render();

    // Função para baixar o PDF
    function gerarPDF(periodo) {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();
        const eventos = calendar.getEvents();

        // Obter a data de início e fim com base na visualização atual
        let dataInicio = calendar.view.currentStart;
        let dataFim = calendar.view.currentEnd;

        // Filtrar eventos com base no período da visualização atual
        let eventosFiltrados = eventos.filter(evento => {
            const eventoData = new Date(evento.start);
            return eventoData >= dataInicio && eventoData <= dataFim;
        });

        // Adicionar eventos ao PDF
        doc.text(`Relatório de Reservas - Período: ${periodo}`, 10, 10);
        let y = 20;
        eventosFiltrados.forEach((evento, index) => {
            let titulo = evento.title;
            let tipo = evento.extendedProps.tipo;
            let user = evento.extendedProps.user;
            let quantidade = evento.extendedProps.quantidade_comprada || 'N/A';
            let descricao = tipo === 'produto' ? `Quantidade: ${quantidade}` : '';
            doc.text(`${index + 1}. ${titulo} - Tipo: ${tipo} - User: ${user} ${descricao}`, 10, y);
            y += 10;
        });

        // Gerar o arquivo PDF
        doc.save(`relatorio_${periodo}.pdf`);
    }

    // Funções de eventos para os botões
    document.querySelector('[onclick="baixarPDF(\'dia\')"]').addEventListener('click', () => gerarPDF('dia'));
    document.querySelector('[onclick="baixarPDF(\'semana\')"]').addEventListener('click', () => gerarPDF('semana'));
    document.querySelector('[onclick="baixarPDF(\'mes\')"]').addEventListener('click', () => gerarPDF('mes'));
});
