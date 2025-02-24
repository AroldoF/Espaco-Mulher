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
                        color: '#3788d8'  // Se tiver uma cor definida na API
                    });
                });

                // Processar os dados de reservas-servicos
                data[1].forEach(reserva => {
                    eventos.push({
                        title: reserva.servico.nome,  // Ajuste conforme os campos da sua API
                        start: reserva.data_reservada,  // Exemplo: '2025-02-25T14:00:00'
                        color: '#f39c12'  // Cor diferente para serviços
                    });
                });

                // Passar todos os eventos para o sucesso
                successCallback(eventos);
            })
            .catch(error => {
                console.error('Erro ao buscar reservas:', error);
                failureCallback(error);
            });
        }
    });

    calendar.render();
});
