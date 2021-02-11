# Projeto iClinic

O projeto foi criado com dois serviços em python utilizando django-rest. A comunicação entre eles foi utilizando o RabbitMQ e o banco de dados é o Postgresql. O docker-compose.yml está na raíz e pronto para subir todo o ambiente. A API opera na porta **8000**.

### Rotas
Foram definidas 3 rotas para a API, segue abaixo:

**GET http://localhost:8000/appointment/**
Lista todos os agendamentos.

*Response*
```json
[
    {
        "id": "8a53c78a-7e08-4fc6-a134-431d8468e86a",
        "start_date": "2021-02-20T13:00:00Z",
        "end_date": "2021-02-26T13:00:00Z",
        "price": "200.00",
        "patient": "1665ee98-a8e6-4f26-a7c9-c06f6dce3bc5",
        "physician": "dec81458-724a-4165-a40f-9398e3798a58"
    }
]
```

**POST http://localhost:8000/appointment/**
Realiza um novo agendamento.

*Request*
```json
{
	"start_date": "2021-2-20 13:00:00",
	"physician": "dec81458-724a-4165-a40f-9398e3798a58",
	"patient": "1665ee98-a8e6-4f26-a7c9-c06f6dce3bc5",
	"price": "100"
}
```

*Response*
```json
{
    "id": "8a53c78a-7e08-4fc6-a134-431d8468e86a",
    "start_date": "2021-02-20T13:00:00Z",
    "end_date": null,
    "price": "200.00",
    "patient": "1665ee98-a8e6-4f26-a7c9-c06f6dce3bc5",
    "physician": "dec81458-724a-4165-a40f-9398e3798a58"
}
```

**PUT http://localhost:8000/appointment/**
Realiza um novo agendamento.

*Request*
```json
{
	"id": "8a53c78a-7e08-4fc6-a134-431d8468e86a",
	"end_date": "2021-02-26 13:00:00"
}
```


### Dados

No banco estão cadastrados os seguintes dados para uso na API:

**Médicos**
| Id | Nome |
| ------ | ------ |
| 27406f80-42c6-48f4-9d1a-abb4d898f6c9 | Dr. John H. Watson |
| 796a25dd-06a7-48f7-870a-99c5ca564cd5 | Dr. Victor Frankenstein |
| 96aea2e4-d652-4c17-a36f-554740657ab6 | Dr. Abraham Van Helsing |
| b07f1d14-621f-404f-9d75-16f6118134f3 | Dr. Montgomery Montgomery |
| dec81458-724a-4165-a40f-9398e3798a58 | Dr. Henry Jekyll |

**Pacientes**
| Id | Nome |
| ------ | ------ |
| 1665ee98-a8e6-4f26-a7c9-c06f6dce3bc5 | Gabriel John Utterson |
| 2d3925e5-89da-4826-b0ec-c453bbc45fb0 | Elizabeth Lavenza |
| 53d65128-a361-4a47-973c-6ff7a27a859a | Baudelaires |
| 59149798-36b2-4c1d-b95e-92c47acf322c | Mina Murray |
| ddf76c8b-ff45-4d9a-87c8-f0a3521bb183 | Enoch Drebber |
